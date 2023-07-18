import httpx


def load_data(
    account,
    offer_id,
    server_id,
    LVL,
    skin_count,
    summary_ru,
    summary_en,
    description_ru,
    description_en,
    price,
):
    default_data = {
        'csrf_token': account.csrf_token,
        'node_id': '85',
        'deleted': '',
        'fields[type]': 'Продажа',
        'fields[hero]': '',
        'fields[rank]': 'Нет ранга',
        'active': 'on',
        'deactivate_after_sale[]': ['', 'on'],
        'location': 'trade',
    }
    specific_data = {
        'offer_id': offer_id,
        'server_id': server_id,
        'fields[level]': LVL,
        'fields[skin]': skin_count,
        'fields[summary][ru]': summary_ru,
        'fields[summary][en]': summary_en,
        'fields[desc][ru]': description_ru,
        'fields[desc][en]': description_en,
        'price': price,
    }
    return {**default_data, **specific_data}


def load_headers(account):
    headers = {
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
    }
    return headers


def load_post(
    account,
    offer_id,
    server_id,
    LVL,
    skin_count,
    summary_ru,
    summary_en,
    description_ru,
    description_en,
    price,
):
    response = httpx.post(
        'https://funpay.com/lots/offerSave',
        cookies={
            'golden_key': account.golden_key,
            'PHPSESSID': account.phpsessid,
        },
        data=load_data(
            account,
            offer_id,
            server_id,
            LVL,
            skin_count,
            summary_ru,
            summary_en,
            description_ru,
            description_en,
            price,
        ),
        headers=load_headers(account),
    )
    return response.json()
