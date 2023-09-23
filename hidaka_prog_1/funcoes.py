def calc_saldo_med(cadastro):
    media = 0
    for i in cadastro:
        media += i['Saldo']
    return media / len(cadastro)

def mail_filter(cadastro,provedor):
    cadastro2 = []
    for i in cadastro:
        if provedor not in i['Email']:
            cadastro2.append(i)
    return cadastro2

def saldo_filtro(cadastro,saldo,operador):
    filtrado = []
    for i in cadastro.copy():
        if operador == 'MAIOR' and i['Saldo'] > saldo or operador == 'MENOR' and i['Saldo'] < saldo:
            filtrado.append(i)
    return filtrado

def filtrar_por_tipo (lista, tipo): #no cabeçalho da funçao sao os parametros nesse cado 'lista'
    lista_filtrada = []
    for item in lista:
        if type(item)==tipo:
            lista_filtrada.append(item)
    return lista_filtrada 

def filtro_nome (cadastro):
    lista_nomes=[]
    for item in cadastro:
        lista_nomes.append(item['Nome']) 
    return lista_nomes 

def formatar_nome (lista, formatacao):
    """
    mapeia uma lista de str para uma lista de str em caixa alta
    Argumentos:
       lista : lista de str 
    retorno: lista de str em caixa alta 
    
    """
    lista_formatada = []
    for item in lista:
        lista_formatada.append(item.upper()) 
    return lista_formatada 
    
 #   if formatacao == 'CAIXA ALTA':
    

def calcular_tamanho_nomes (lista):
    lista_tamanho_nomes=[]
    for item in lista:
        lista_tamanho_nomes.append(len(item))
    return lista_tamanho_nomes

def filtro(elemento, saldo, operador):
    return operador == 'MAIOR' and \
        elemento['saldo'] > saldo or \
        operador == 'MENOR' and \
        elemento['saldo '] < saldo

def filtrar_por_saldo(cadastros,saldo,operador):
    return [elemento
            for elemento in cadastros 
            if filtro(elemento, saldo, operador)]

def extrair_nomes(cadastros):
    return[item ['nome'] for item in cadastros]


def filter_concatenate (L1, L2):
    Filtered = []
    for a, b in zip(L1,L2):
        Filtered.append(a + b)
    return  Filtered

def filter_concatenate_compreehense(L1,L2):
    return[(a + b) for a,b in zip(L1,L2)]

def prime_or_not(valor):
    if valor <= 1:
        return False
    
    for divisor in range(2, valor):
        if valor % divisor == 0:
            return False
    return True
def encontrar_primo(valor):
    valor += 1
    while not prime_or_not(valor):
        valor += 1
    return valor

def construir_lista_primo(lista):
    return[encontrar_primo(i) for i in lista]

def less_10(Lista):
    filtrado = []
    for i in Lista:
        if len(i) < 10:
            filtrado.append(i)
    filtrado.sort()
    return filtrado

def less_10_compressed(Lista):
    return sorted([elemento for elemento in Lista if len(elemento) < 10 ])

def sort_list_package(Lista):
    out_of_rules = 0
    for package in Lista:
        if package < 7 :
            out_of_rules += 1
    
    return out_of_rules

def task_completion_backlog(Lista, Speed):
    tasks = 0
    complexity = 0
    for i in Lista: 
        complexity += i
        if complexity <= Speed:
            tasks += 1
        else :
            break
    return tasks 