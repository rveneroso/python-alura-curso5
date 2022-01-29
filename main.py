#
# Formato de URL utilizado na aula que apresenta o método len()
#
url = "http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

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
    print(url_parametros)

    #
    # Procura pelo parâmetro moedaOrigem
    #
    parametro_busca = 'moedaOrigem'
    indice_moeda_origem = url.find(parametro_busca)
    if(indice_moeda_origem>0):
        #
        # Essa forma de busca só funciona com a URL estando no formato definido no início do programa.
        moeda_origem = url[indice_moeda_origem + len(parametro_busca) + 1:]
        print(f'A conversão será feita para a moeda {moeda_origem}')