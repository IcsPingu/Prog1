import funcoes as F 

cadastro = [
            {'Nome': 'Joelinton', 'Email': 'joelzinhodelas@gmail.com', 'Saldo': 25},
            {'Nome': 'Jose', 'Email': 'joseph@hotmail.com', 'Saldo': 32},
            {'Nome': 'Jair', 'Email': 'jairzinho@hotmail.com', 'Saldo': 500},
            {'Nome': 'Jude', 'Email': 'jdbel@gmail.com', 'Saldo': 75}
           ]

#saldo = F.calc_saldo_med(cadastro)
#print(saldo)

#filtro = F.mail_filter(cadastro,'@hotmail')
#print(filtro)

#saldo_filtro = F.saldo_filtro(cadastro,150,'MENOR')
#print(filtro)

#lista = [1,2,'A', 'B', 3, 'C']

#lista_filtrada=F.filtrar_por_tipo(lista, str)
#print(lista_filtrada)

#lista_nomes=F.filtro_nome(cadastro)
#print(lista_nomes)

#formatar_nomes=F.formatar_nome(lista_formatada)
#print(formatar_nomes)


#lista_tamanho_nomes = F.calcular_tamanho_nomes()
#print (lista_tamanho_nomes) 

import func as f
L1 = ['a', 'e', 'sal']
L2 = ['i', 'u', 've']

filtro = f.filter_concatenate(L1,L2)