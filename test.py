import re

def muito_forte(senha):
    return  re.search("[A-Z]", senha) and\
            re.search("[a-z]", senha) and\
            re.search("[0-9]", senha) and\
            len(re.findall("[^A-Za-z0-9]", senha)) >= 3 and\
            len(senha) >= 10 


def forte(senha):
        return re.search("[A-Z]", senha) and\
               re.search("[a-z]", senha) and\
               re.search("[0-9]", senha) and\
               re.search("[^A-Za-z0-9]", senha)  and\
               len(senha) >= 8 
    
def media(senha):
        return re.search("[A-Z]", senha) and\
               re.search("[a-z]", senha) and\
               re.search("[0-9]", senha) and\
               len(senha) >= 6
def fraca(senha):
        return len(senha) >= 6

def main():
    while True:
        senha = input("digite sua senha: ")
        if muito_forte(senha):
            print("Senha Forte!")
            break
        
        elif forte(senha):
            print("Senha Forte!")
        
        elif media(senha):
            print("Senha Moderada!")

        elif fraca(senha):
            print("Senha Fraca!")

        else:
            print("Senha Inválida!")



main()