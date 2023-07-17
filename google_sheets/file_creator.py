import datetime
import os

from google_sheets.google.google_sheets import read_from_google_sheets


def write_vpn_info(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('[🅰️Автовыдача🅰️🛡️Надёжный 🌍VPN СЕРВИС от Proton, работает в России!🔥]\n')
        file.write('response : Спасибо за покупку, $username!\n\n')
        file.write('\tСсылка на инструкцию: https://telegra.ph/Kak-podklyuchitsya-k-VPN-ochen-prosto-06-29\n')
        file.write('\tСсылка на скачивание конфиг файла:\n\n')
        file.write('\t$product\n')
        file.write('productsFileName : vpn.txt\n')


def create_cfg(start_row, end_row):
    date = datetime.datetime.now().strftime('%d.%m.%Y')
    filename = f'accounts_{date}.cfg'
    # Обходим каждую строку в заданном диапазоне
    file_list = os.listdir()
    for file in file_list:
        if file.startswith('accounts_'):
            os.remove(file)
    for row in range(start_row, end_row + 1):
        # Считывание данных из ячейки Q
        name_info = read_from_google_sheets(f'Q{row}')
        if name_info:
            name_info = name_info[0][0]
        else:
            continue

        # Если ячейка Q не пустая, создаём файл .cfg
        if name_info:
            # Считывание логина и пароля из ячеек B и C
            login = read_from_google_sheets(f'C{row}')
            if login:
                login = login[0][0]
            else:
                continue

            password = read_from_google_sheets(f'D{row}')
            if password:
                password = password[0][0]
            else:
                continue

            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f'[{name_info}]\n')
                file.write(f'response : $username, cпасибо за покупку🥷\n\n')
                file.write(f'\tLogin:{login}\n')
                file.write(f'\tPass:{password}\n\n')
                file.write(
                    f'\tПосле смены почты, не забудьте подтвердить '
                    f'выполнение заказа и буду очень признателен за '
                    f'отзыв 🧙🏿‍♂️\n\n'
                )
    write_vpn_info(filename=filename)
    return filename
