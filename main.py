import unittest
import time
import requests
import json


class Ceps():
    def __init__(self, cep):
        self.cep = cep

    def pega_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        resposta = requests.get(url)
        return resposta.json()


class TestadorDeCep(unittest.TestCase):
    '''
    Verifica ser o cep buscado na API viacep corresponde
    ao logradouro desse lugar. Ex: se o cep buscado for 
    "01001-000", o logradouro tem que ser "Praça da Sé".
    '''

    def teste_cep_correto(self):
        comeco = time.time()
        cep = "01001-000" #Cep da praça da sé
        obj_cep = Ceps(cep)
        resultado = obj_cep.pega_cep()
        with open("cep_info.json", "w") as arquivo:
            arquivo.write(json.dumps(resultado))
        
        fim = time.time()
        tempo_total = fim - comeco
        print(f"Tempo total de execução {tempo_total:.2f} segundos")

        self.assertEqual("Praça da Sé", resultado["logradouro"]) 


if __name__ == "__main__":
    unittest.main()