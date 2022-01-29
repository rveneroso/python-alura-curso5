class Util:
    def retorna_valor_parametro(nome_parametro, url_parametros):
        indice_parametro = url_parametros.find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
             valor = url_parametros[indice_valor:]
        else:
             valor = url_parametros[indice_valor:indice_e_comercial]
        return valor

from main import Util

def pesquisar():
    #
    # Formato de URL utilizado na aula que apresenta o método len()
    #
    url = "http://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"

    #
    # Usando o método find de str para identificar a posição onde determinado caracter se encontra
    #
    indice_interrogacao = url.find('?')

    #
    # Somente faz a extração das substrings caso a ? tenha sido encontrada na URL.
    #
    if(indice_interrogacao>0):
        #
        # No fatiamento de Strings, quando o primeiro argumento é omitido, a String retornada irá conter
        # a String original desde o início até a posição definida.
        #
        url_base = url[:indice_interrogacao] # Do início da String até a posição anterior à interrogação

        #
        # No fatiamento de Strings, quando o segundo argumento é omitido, a String retornada irá conter
        # a String original da posição definida até o seu fim.
        #
        url_parametros = url[indice_interrogacao+1:] # Da posição posterior à interroação até o fim.

        #
        # Busca o valor de um parâmetro
        #
        parametros = ['quantidade', 'moedaOrigem', 'moedaDestino']
        for parametro in parametros:
            valor_parametro = Util.retorna_valor_parametro(parametro, url_parametros)
            print(f'O valor do parâmetro {parametro} na URL é {valor_parametro}')


if(__name__ == "__main__"):
    pesquisar()