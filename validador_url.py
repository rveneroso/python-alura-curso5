'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''
import re
'''
Construção de padrao_url

(http(s)?://)? -> indica que as Strings https:// e http:// podem ou não aparecer na String a ser pesquisada. 
O valor está entre parênteses para indicar que, se estiver presente da String, tem que ser exatamente naquele 
formato.

(www.)? -> ndica que a string www. pode ou não aparecer na String a ser pesquisada. O valor está entre
parênteses para indicar que, se estiver presente da String, tem que ser exatamente naquele formato.

bytebank.com(.br)? -> O valor bytebank.com é obrigatório ou seja, deve estar presente na URL para que ela
seja considerada válida. Por isso o valor não aparece entre parêntes. Já o (.br)? indica que a String .br
pode ou não estar presente na URL.

/cambio -> O valor /cambio deve estar obrigatoriamente presente na URL.

'''
url = "www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida")

print(f'A URL {url} é válida')