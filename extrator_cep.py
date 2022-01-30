endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-129"
import re # Módulo do Python responsável por tratar Regular Expressions

#
# Para criar um padrão a ser usado em uma RE usa-se o método compile() do módulo re
# O argumento do método compile() é o padrão que se deseja criar. Para o CEP será criado o padrão 99999-999
# sendo que o hífen pode ou não aparecer no CEP ([-]?)
# Nessa nova versão, o padrão passado ao método compile foi simplificada.
# O {0,1} após o hífen indica que o hífen pode ocorrer zero ou, no máximo, uma vez.
padrao_cep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
#
# O método search retorna um objeto do tipo Match se o padrão for localizado na String ou None caso contrário.
#
busca = padrao_cep.search(endereco)

if busca: # Lembrando que None resulta em False
    # group() é o método de Match que retorna a String que confere com o padrão pesquisado.
    print(f'O CEP encontrado no endereço é {busca.group()}')