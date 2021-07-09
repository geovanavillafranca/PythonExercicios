import requests
try:
    site = requests.get('http://pudim.com.br')
except:
    print('\033[31mO site Pudim não está acessível no momento!')
else:
    print('\033[34mConsegui acessar o site Pudim com sucesso!\033[m')
    #print(site.content)

