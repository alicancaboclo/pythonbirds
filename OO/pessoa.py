class Pessoa:                                                          #atributo=metodo é função pertencer a# uma classer senpre esta conectada a um objeto
    olhos=2                                                            #criando atributo de class<> mas pode chamar na def sem locar memoria
                                                                       #os atributo de class (olhos0 pode chama dentro da def(objetos) sem declara (__init__)
    def __init__(self,*filhos, nota='9', idade='18', nome=None):       #atributo de dados(metodor(__init__)(defini um retorno vazio=None) #a tributo de metodp de intantência é criado cometodo __init__
        self.nome = nome                                               #nome do obejeto
        self.idade = idade
        self.nota = nota
        self.filhos = list(filhos)                                     # criação de list para numero complexo

    def cumplimentar(self):                                            #criando o metodp comprimentar #lenbra uma execusao de uma função
        return f' ola {id(self)}'
    @staticmethod                                                       #criando metodo estatio. não cria (self) poisnão depende do atribudo mas pode ser chamado
    def metodo_estatico():                                              # dando nome (metodo_estatico) a def (função atrelada a class)
        return 31
    @classmethod                                                       ###criando outra class (estatica)
    def nome_e_atributos_de_class(cls):                                ###criando um def do tipo >cls<(referente a class pessoa)
         return f'{cls}-olhos{cls.olhos}'                              #(cls)acessar dados da propria class  retorna def(função)com atribuindo a(olhos) por (cls) como estatico                     ###
if __name__ == '__name__':
    alikan = Pessoa(nome='alikan')                                      #obejeto do tipo complexo alikan
    caboclo = Pessoa(alikan,nome='silva')                               #passando como atributo alikan
    print(Pessoa.cumplimentar(caboclo))                                 ###chamando a class(pessoa) pelo metodo(def) mas tendo que passar o objeto(nome)
    print(id(caboclo))
    print(caboclo.cumplimentar())
    print(caboclo.nome)
    print(caboclo.idade)
    for filho in caboclo.filhos:                                       # FOR= para filho insira no objeto como atributo e passe filhos.nome(o atributo dentro da list)
        print(filho.nome)
    print(caboclo.filhos)
    del caboclo.filhos                                                  #deletando atributo dinâmico
    caboclo.sobrenome='kill'                                            #criando um atribudo dinâmico sem definir na def (o uso só onde foi criado)
    print(caboclo.sobrenome)                                            # o atribudo não modificar os objetos da mesma class
    caboclo.olhos= 1                                                    #mudando o valor do atributo do objeto sem autera a class
    print(caboclo.__dict__)                                             # discrição complete ou listando todos da objetos e atribudo da class
    print(caboclo.__dict__)
    Pessoa.olhos=3                                                      #auterandoo valor atributo de class
    print(Pessoa.olhos)                                                 #acessando atributo de class(olhos)
    print(caboclo.olhos)                                                ### se o atributo de class for ingual a para todos objetos nao cria objeto mas pode
    print(alikan.olhos)                                                 ###  ser auterado dentro do objeto
    print(id(Pessoa.olhos), id(caboclo.olhos),id(alikan.olhos))
    print(Pessoa.nome_e_atributos_de_class(),caboclo.nome_e_atributos_de_class()) ### acessando o metodo estatico por class ou objeto da class
    print(Pessoa.metodo_estatico()),(caboclo.metodo_estatico())         #chamando o metode_estatico pela claa ou objeto