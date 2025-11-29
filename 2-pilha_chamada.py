def saudacao(nome):
    print("Olá " + nome + "!")
    saudacao2(nome)
    tchau()

def saudacao2(nome):
    print("Como vai " + nome + "?")

def tchau():
    print("Ok, tchau!")

saudacao("Ana")