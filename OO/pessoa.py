class Pessoa:                           #atributo=metodo é função pertencer a# uma classer senpre esta conectada a um objeto
    def cumplimentar(self):             #criando o metodp comprimentar #lenbra uma execusao de uma função
        return f' ola {id(self)}'
if __name__ == '__name__':
    p = Pessoa()
    print(Pessoa.cumplimentar())
    print(id(p))
    print(p.cumplimentar())


