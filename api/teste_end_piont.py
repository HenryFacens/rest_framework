import requests
import json

end_point = 'http://localhost:8000/api/'

get_response = requests.get(end_point, headers={'testepara': '123'},json={'chave': 'valor'})

# print(get_response.json())
# print(get_response.status_code)