import re

def Q1(questions):
    padrao = re.compile(r"\b[aeiouAEIOU].*[aeiouAEIOU]\b")
    contador = 0
    while True:
        palavras = input('digite aqui a palavra a ser adicionada ao arquivo: ')
        print('digite, exit ,caso queira sair')
        if palavras.lower() == 'exit':
            print(f"O numero de palavras que cumprem os critérios adicionadas são: {contador}")
            with open("questions.txt", "r", encoding='utf-8') as f:
                texto = f.read()
                print(texto)
            break
        buscador = padrao.findall(palavras)
        if buscador: 
            with open("questions.txt", "a", encoding = 'utf-8') as f:
                for match in buscador:
                    f.write(match + "\n")
                    contador += 1

            print(f"O numero de palavras que cumprem os critérios adicionadas são: {contador}")    
        else:
             print("A palavra não atende aos critérios. Tente novamente.")
    
Q1("questions.txt")