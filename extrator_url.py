import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        url = self.url
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        #
        # O método search não retorna uma String contida em outra como é o caso do método search(); ele
        # indica se uma String está dentro do pattern previamente compilado.
        #
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    #
    # Sobrescrita do método len()
    #
    def __len__(self):
        return len(self.url)

    #
    # Sobrescrita do método str
    #
    def __str__(self):
        return self.url + "\nParâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    #
    # Sobrescrita do método eq. Lembrando que igualdade é diferente de identidade. Igualdade é quando dois objetos
    # possuem o mesmo valor em atributos pré-definidos; identidade é quando dois objetos apontam para o mesmo
    # endereço de memória.
    #
    def __eq__(self, other):
        return self.url == other.url

url = "http://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(f'O tamanho da URL é {len(extrator_url)}')
print(extrator_url)
extrator_url2 = ExtratorURL(url)
print(f"Teste de igualdade de objetos retorna {extrator_url2 == extrator_url}")
print(f"Teste de identidade de objetos retorna {extrator_url2 is extrator_url}")

#
# Implementação do desafio - conversão de valores com base nas moedas de origem e destino
#
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
VALOR_REAL =  (1 / VALOR_DOLAR)
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = int(extrator_url.get_valor_parametro("quantidade"))
valor_convertido = 0
if(moeda_origem == "real"):
    valor_convertido = (quantidade * VALOR_REAL)
else:
    valor_convertido = (quantidade * VALOR_DOLAR)

print(f'O valor da conversão de {quantidade} unidades de {moeda_origem} para {moeda_destino} é {valor_convertido}')