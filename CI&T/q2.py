'''
Você está trabalhando para uma empresa que fornece materiais escolares e precisa da sua ajuda para entrar no mundo digital. Como primeira atividade, você identificou que não existe uma funcionalidade que é muito importante para a empresa ter mais controle sobre os valores dos produtos vendidos. Esta funcionalidade consiste em descobrir o maior e o menor valor dos produtos vendidos em um período de tempo, para cada vendedor.

Os valores das vendas que devem ser consideradas podem variar entre 20 e 500 reais e estão agrupados por vendedores. Além disso, deve-se ignorar as devoluções, que estão indicadas com o valor 0.

A sua função/método deverá receber uma lista vendas agrupadas por vendedores, (e.g. [[200, 100], [300]]) e retornar um array onde a primeira posição contém o menor valor e a segunda posição o maior valor (e.g. [100, 300]).

Mas preste atenção! Algum vendedor pode não ter realizado vendas no período.
'''

def retorna_menor_e_maior_valor_de_vendas(tickets):
    aux = []
    menor_e_maior = []
    for i in tickets:
        aux = aux + i
    for i in aux:
        if i > 500:
            aux.remove(i)
    for i in aux:
        if i < 20:
            aux.remove(i)
    aux.sort() 
    menor_e_maior.append(aux[0])    
    menor_e_maior.append(aux[-1])
    return menor_e_maior


print(retorna_menor_e_maior_valor_de_vendas([[200, 100], [300, 700], [0, 501, 20, 19], [499, 500, 600]]))
print(retorna_menor_e_maior_valor_de_vendas([[200, 100], [300]]))
