url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

#
# Usando o método find de str para identificar a posição onde determinado caracter se encontra
#
indice_interrogacao = url.find('?')

#
# No fatiamento de Strings, quando o primeiro argumento é omitido, a String retornada irá conter
# a String original desde o início até a posição definida.
#
url_base = url[:indice_interrogacao] # Do início da String até a posição anterior à interrogação
print(url_base)

#
# No fatiamento de Strings, quando o segundo argumento é omitido, a String retornada irá conter
# a String original da posição definida até o seu fim.
#
url_parametros = url[indice_interrogacao+1:] # Da posição posterior à interroação até o fim.
print(url_parametros)