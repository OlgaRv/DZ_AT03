# Функция get_random_cat_image:

# Делает GET-запрос к TheCatAPI.
# Использует заголовок x-api-key для передачи API ключа.
# Проверяет, успешен ли запрос (статус код 200).
# Возвращает URL изображения, если данные получены, иначе None.
# Тест test_get_random_cat_image_success:

# Использует mocker.patch для создания заглушки функции requests.get.
# Имитирует успешный ответ от API с кодом 200 и возвращаемыми данными.
# Проверяет, что функция возвращает правильный URL изображения.
# Тест test_get_random_cat_image_failure:

# Использует mocker.patch для создания заглушки функции requests.get.
# Имитирует неуспешный ответ от API с кодом 404.
# Проверяет, что функция возвращает None при неуспешном запросе.

import requests


def get_random_cat_image(api_key):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get("url")
    return None
