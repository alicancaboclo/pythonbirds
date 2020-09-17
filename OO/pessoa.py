class Pessoa:                           #atributo=metodo é função pertencer a# uma classer senpre esta conectada a um objeto
    def __init__(self, nota='9', idade='18', nome=None):       #atributo de dados(metodor(__init__)(defini um retorno vazio=None)
        self.nome = nome                          #nome do obejeto  #a tributo de metodp de intantência é criado cometodo __init__
        self.idade = idade
        self.nota = nota


    def cumplimentar(self):                       #criando o metodp comprimentar #lenbra uma execusao de uma função
        return f' ola {id(self)}'
if __name__ == '__name__':
    p = Pessoa('alikan')
    print(Pessoa.cumplimentar(p))
    print(id(p))
    print(p.cumplimentar())
    p.nome = 'alikan'
    print(p.nome)
    print(p.idade)

