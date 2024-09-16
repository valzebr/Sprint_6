import requests

"""МЕТОД GET"""
# url =  'https://qa-mesto.praktikum-services.ru/api/users/me'
# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjhlODRiYWQ1NmMxNDAwM2Q0NzkxZTIiLCJpYXQiOjE3MjY0MjI1NjgsImV4cCI6MTcyNzAyNzM2OH0.2ogNAPdQ8mp1jRoseDwMzah7L_bdAm-JvoeJHNIZm7Y'
# headers =   {'Authorization': token}
# response = requests.get(url, headers=headers)
# assert 200 == response.status_code


# ===============================================================

"""Десериализация"""

# response = requests.get("https://jsonplaceholder.typicode.com/albums")
# r = response.json() # десериализация

# print(r)

# def test_email_name():
#     token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjhlODRiYWQ1NmMxNDAwM2Q0NzkxZTIiLCJpYXQiOjE3MjY0MjI1NjgsImV4cCI6MTcyNzAyNzM2OH0.2ogNAPdQ8mp1jRoseDwMzah7L_bdAm-JvoeJHNIZm7Y'
#     url = 'https://qa-mesto.praktikum-services.ru/api/users/me'
#     response = requests.get(url, headers ={'Authorization' : f'Bearer {token}'})
#     r = response.json()
#     email = r['data']['email']
#     correct_email = 'zacepin_11@gmail.com'
#     assert email == correct_email, f"Ожидался email: {correct_email}, но получен: {email}"


"""МЕТОД POST"""
"""task 1"""

# TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjhlODRiYWQ1NmMxNDAwM2Q0NzkxZTIiLCJpYXQiOjE3MjY0MjI1NjgsImV4cCI6MTcyNzAyNzM2OH0.2ogNAPdQ8mp1jRoseDwMzah7L_bdAm-JvoeJHNIZm7Y'
# BASE_URL = 'https://qa-mesto.praktikum-services.ru'
# API_ENDPOINT = '/api/signup'
# url = f'{BASE_URL}{API_ENDPOINT}'
# payload = {"email": "zacepin_11@gmail.com", 'password': "12345678aa"}
# response = requests.post(url, data=payload)  # Используем json вместо data
#
# print(response.status_code)
# print(response.json())

"""task 2"""

BASE_URL = 'https://qa-mesto.praktikum-services.ru'
API_ENDPOINT = '/api/signin'
url = f'{BASE_URL}{API_ENDPOINT}'
payload = {"email": "zacepin_11@gmail.com", 'password': "12345678aa"}
response = requests.post(url, data=payload)  # Используем json вместо data

print(response.status_code)
print(response.json()['data']['avatar'])