class Pessoa:                           #atributo=metodo é função pertencer a# uma classer senpre esta conectada a um objeto
    def __init__(self,*filhos, nota='9', idade='18', nome=None):       #atributo de dados(metodor(__init__)(defini um retorno vazio=None) #a tributo de metodp de intantência é criado cometodo __init__
        self.nome = nome                          #nome do obejeto
        self.idade = idade
        self.nota = nota
        self.filhos = list(filhos)               # criação de list para numero complexo

    def cumplimentar(self):                       #criando o metodp comprimentar #lenbra uma execusao de uma função
        return f' ola {id(self)}'
if __name__ == '__name__':
    alikan = Pessoa(nome='alikan')                  #obejeto do tipo complexo alikan
    caboclo = Pessoa(alikan,nome='silva')           #passando como atributo alikan
    print(Pessoa.cumplimentar(caboclo))
    print(id(caboclo))
    print(caboclo.cumplimentar())
    print(caboclo.nome)
    print(caboclo.idade)
    for filho in caboclo.filhos:           #
        print(filho.nome)
    print(caboclo.filho)                    #
