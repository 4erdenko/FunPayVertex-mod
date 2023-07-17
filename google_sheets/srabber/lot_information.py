import httpx
from bs4 import BeautifulSoup

def get_name(offer_id):
    url = f'https://funpay.com/lots/offer?id={offer_id}'
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Определяем нужные нам ключевые слова
    keywords = [
        'Тип предложения',
        'Уровень',
        'Скины',
        'Ранг',
        'Краткое описание',
    ]

    # Находим все блоки с классом 'param-item'
    params = soup.find_all('div', class_='param-item')

    # Инициализируем словарь для хранения результатов
    result = {}

    # Проходим по всем блокам
    for param in params:
        # Извлекаем текст из блока
        key = param.h5.get_text(strip=True)
        value = param.div.get_text(strip=True)

        # Проверяем, содержит ли текст одно из ключевых слов
        if key in keywords:
            # Если содержит, сохраняем значение в словаре
            result[key] = value

    # Структурируем результат в требуемый формат
    formatted_result = (
        f"{result['Краткое описание']}, "
        f"{result['Тип предложения']}, уровень "
        f"{result['Уровень']}, скины {result['Скины']}, "
        f"{result['Ранг']}"
    )

    # Возвращаем результат
    return formatted_result


def get_lot(offer_id):
    url = f'https://funpay.com/lots/offer?id={offer_id}'
    response = httpx.get(url)
    if response.status_code == 200:
        return True
    return False
