import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")

# Printa todos os dados dos produtos fornecidos pela API
print(response.json())

# Printa atributos da response
# print(response.headers)

'''
O método requests.get() usa um parâmetro chamado params, no qual podemos especificar nossos parâmetros de consulta na 
forma de um dicionário Python. Assim, criamos um dicionário chamado query_params e passamos limit como a chave e 3 como 
o valor. Em seguida, passamos esse query_params em requests.get().
'''
query_params = {
    "limit": 3
}
response2 = requests.get(f"{BASE_URL}/products", params=query_params)
# print(response2.json())

'''
Agora temos os dados da response limitados, vamos tentar pegar um produto pelo seu id.
Desde que haja um endpoint /products/<product_id>, nós podemos passar o id desejado na URL da API e fazer um GET request
'''
response3 = requests.get(f"{BASE_URL}/products/21")
print(response3)


'''
Agora vem o uso do método POST.
Os dados são enviados para o servidor em formato JSON. De acordo com a documentação da API, um produto tem os seguintes
atributos: title, price, description, image e category.
'''
new_product = {
    "title": 'test product',
    "price": '13.22',
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'eletronic',
}
#
# response4 = requests.post(f"{BASE_URL}/products", json=new_product)
# print(response4.status_code)


'''
Usando o método PUT
'''
updated_product = {
    "title": 'updated_product',
    "category": 'clothing'
}
# response5 = requests.put(f"{BASE_URL}/products/21", json=updated_product)
# print(response5.json())


'''
Quando for preciso alterar apenas partes de algum produto, usamos o método PATCH
'''

patched_product = {
    "category": 'eletronic'
}
# response6 = requests.patch(f"{BASE_URL}/products/21", json=patched_product)
# print(response6.json())



'''
Finalmente, se precisarmos deletar um recurso da API, podemos usar o método DELETE
'''
response7 = requests.delete(f"{BASE_URL}/products/21")
print(response7.json())