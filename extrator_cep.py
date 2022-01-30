endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Módulo do Python responsável por tratar Regular Expressions

#
# Para criar um padrão a ser usado em uma RE usa-se o método compile() do módulo re
# O argumento do método compile() é o padrão que se deseja criar. Para o CEP será criado o padrão 99999-999
# sendo que o hífen pode ou não aparecer no CEP ([-]?)
#
padrao_cep = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
#
# O método search retorna um objeto do tipo Match se o padrão for localizado na String ou None caso contrário.
#
busca = padrao_cep.search(endereco)

if busca: # Lembrando que None resulta em False
    # group() é o método de Match que retorna a String que confere com o padrão pesquisado.
    print(f'O CEP encontrado no endereço é {busca.group()}')