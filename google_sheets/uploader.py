import os
import time

import httpx

from Utils.config_loader import load_main_config
from google_sheets.file_creator import create_cfg
from google_sheets.google.google_sheets import (
    read_from_google_sheets,
    update_format_google_sheets,
    write_to_google_sheets,
)
from google_sheets.srabber.lot_information import get_lot, get_name
from google_sheets.text_templates.make_text import (
    create_description_en,
    create_description_ru,
    create_summary_en,
    create_summary_ru,
    end_row,
    start_row,
)
from FunPayAPI.account import Account
import logging

logger = logging.getLogger(__name__)


def set_lot_status():
    logger.info('Start parsing statuses')
    end_column = 14  # replace with the actual number of columns in your sheet
    result = []
    for row in range(start_row, end_row + 1):
        try:
            offer_id = read_from_google_sheets(f'L{row}')[0][0]
            if get_lot(offer_id):
                update_format_google_sheets(
                    (row - 1, row, 0, end_column),
                    (182 / 255, 215 / 255, 168 / 255),
                )
                result.append(f'🟢Аккаунт №{row - 1} в продаже\n')
                name_info = get_name(offer_id)
                write_to_google_sheets(f'Q{row}', [[name_info]])
            else:
                update_format_google_sheets(
                    (row - 1, row, 0, end_column),
                    (255 / 255, 229 / 255, 153 / 255),
                )
                result.append(f'🟡Аккаунт №{row - 1} не в продаже\n')
                write_to_google_sheets(f'Q{row}', [['']])
        except IndexError:
            continue
    return result


def main_upload(upload=False, set_status=False, make_file=False):
    result = []
    if not upload and not set_status and not make_file:
        return 'Вы не указали задачу!'
    if upload is True:
        config_path = os.path.join('configs', '_main.cfg')
        config = load_main_config(config_path)
        golden_key = config['FunPay']['golden_key']
        user_agent = (
            config['FunPay']['user_agent']
            if config['FunPay']['user_agent'] != ''
            else None
        )

        account = Account(golden_key=golden_key, user_agent=user_agent)
        account.get()
        for row in range(start_row, end_row + 1):
            try:
                acc_number = read_from_google_sheets(f'A{row}')[0][0]
                offer_id = read_from_google_sheets(f'L{row}')[0][0]
                if get_lot(offer_id):
                    # str = f'🟠Аккаунт №{acc_number} уже в продаже'
                    # result.append(f'{str}\n')
                    continue
                # print(f'🔵Обрабатываю аккаунт №{acc_number}')
                login = (
                    read_from_google_sheets(f'C{row}')[0][0]
                    if read_from_google_sheets(f'C{row}')
                    else None
                )

                if login is None:
                    # str = f'⚪Аккаунт №{acc_number} не найден'
                    # result.append(f'{str}\n')
                    continue
                BE = read_from_google_sheets(f'E{row}')[0][0]
                LVL = read_from_google_sheets(f'F{row}')[0][0]
                skins = '\n'.join(
                    read_from_google_sheets(f'I{row}')[0][0].split(', ')
                )
                screenshot = read_from_google_sheets(f'J{row}')[0][0]
                RP = (
                    read_from_google_sheets(f'N{row}')[0][0]
                    if read_from_google_sheets(f'N{row}')
                    else None
                )
                price = read_from_google_sheets(f'K{row}')[0][0]

                server_id = read_from_google_sheets(f'M{row}')[0][0]
            except IndexError:
                continue

            skin_lines = skins.split('\n')
            skin_count = len(skin_lines)
            if skin_count > 7:
                skins = read_from_google_sheets(f'I{row}')[0][0]
            summary_ru = create_summary_ru(acc_number, BE, LVL, skins, RP)
            summary_en = create_summary_en(acc_number, BE, LVL, skins, RP)
            description_ru = create_description_ru(
                acc_number, skins, screenshot
            )
            description_en = create_description_en(
                acc_number, skins, screenshot
            )
            data = {
                'csrf_token': account.csrf_token,
                'offer_id': 0,
                'node_id': '85',
                'deleted': '',
                'server_id': server_id,
                'fields[type]': 'Продажа',
                'fields[level]': LVL,
                'fields[hero]': '',
                'fields[skin]': skin_count,
                'fields[rank]': 'Нет ранга',
                'fields[summary][ru]': summary_ru,
                'fields[summary][en]': summary_en,
                'fields[desc][ru]': description_ru,
                'fields[desc][en]': description_en,
                'price': price,
                'active': 'on',
                'deactivate_after_sale[]': [
                    '',
                    'on',
                ],
                'location': 'trade',
            }
            time.sleep(1)
            response = httpx.post(
                'https://funpay.com/lots/offerSave',
                cookies={
                    'golden_key': account.golden_key,
                    'PHPSESSID': account.phpsessid,
                },
                data=data,
                headers={
                    'User-Agent': account.user_agent,
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://funpay.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://funpay.com/lots/85/trade',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-GPC': '1',
                },
            )
            if response.json().get('done'):
                str = (
                    f'🟢Аккаунт №{acc_number} - {login} успешно выставлен на '
                    f'продажу'
                )
                result.append(f'{str}\n')
                logger.info(
                    f'Account number:{acc_number} is successfully on uploaded, waiting 15 '
                    f'sec'
                )
                time.sleep(15)

            else:
                error = response.json().get('errors')
                str = (
                    f'🚫Аккаунт №{acc_number} - {login} не выставлен на продажу, '
                    f'ошибка: {error}'
                )
                result.append(f'{str}\n')
                time.sleep(15)
    if set_status:
        result.append('\n'.join(set_lot_status()))


    return result