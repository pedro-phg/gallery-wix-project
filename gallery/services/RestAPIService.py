import requests

class RestAPIService:
    """
    Classe que fornece uma interface para realizar operações CRUD em uma API REST.
    Utiliza a biblioteca 'requests' para enviar requisições HTTP.
    """

    def __init__(self, base_url):
        """
        Inicializa a classe com a URL base da API.
        """
        self.base_url = base_url

    def get(self, endpoint):
        """
        Realiza uma requisição GET para o endpoint especificado.
        Retorna a resposta da requisição.
        """
        url = self.base_url + endpoint
        response = requests.get(url)
        return response

    def post(self, endpoint, data):
        """
        Realiza uma requisição POST para o endpoint especificado, com os dados fornecidos.
        Retorna a resposta da requisição.
        """
        url = self.base_url + endpoint
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data):
        """
        Realiza uma requisição PUT para o endpoint especificado, com os dados fornecidos.
        Retorna a resposta da requisição.
        """
        url = self.base_url + endpoint
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        """
        Realiza uma requisição DELETE para o endpoint especificado.
        Retorna a resposta da requisição.
        """
        url = self.base_url + endpoint
        response = requests.delete(url)
        return response
