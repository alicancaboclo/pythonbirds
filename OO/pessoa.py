class Pessoa:                                            ### criação de class prinipal

    Estado = 'Recife-PE'                                #### criação de atributo de class pode ser chamado em qual quer def
    olhos ='vermelhos'
    def __init__(self,*filhos,nome=None,idade=18):       ###criando uma def de inicialização
        self.idade=idade
        self.nome=nome
        self.filhos=list (filhos)

    @staticmethod
    def estatio ():
        return Pessoa.Estado
    @classmethod
    def acessa_das_class(cls):                          ###cria  def com palavra resevada (cls)
        return Pessoa.olhos                             ###criando atribudo aoto inserir no objeto
    def cumprimentar(self):                             ###criando def com f estring   gerando o id
        return f'numero de protocolo {id (self)}'          ###

if __name__ == "__main__":
        alikan = Pessoa(nome='alikan')                         ##objeto
        felipe = Pessoa(alikan,nome='Felipe')                  ##objeto
        rogerio =Pessoa(alikan,felipe,nome='Rogerio')          ##objeto ###passo todos objetos dentrodo atributo filho
        print('testando:>')
        print(Pessoa.cumprimentar(alikan))
        print(id (alikan))
        print(alikan.cumprimentar()),(alikan.nome)
        print(alikan.idade)                                    ##objeto passando atributo
        print(alikan.Estado)                                   ##objeto passando atributo
        print('lista de filhos  de rogerio:')
        for filho in rogerio.filhos:                           ###pegando  objeto  anteriores
            if(rogerio.filhos):                                ### para cada objeto sera impresoo meu filhor
                print('meu filho:>')
            print(filho.nome)
        print('alterando o estados:>')
        alikan.estado = 'Sergipe'                                 ##altrando  atributo do objeto
        print ('Sergipe')
        rogerio.estado = 'São Paulo'                              ##altrando  atributo do objeto
        print ('São Paulo')
        felipe.estado = 'Rio de Janeiro'                          ##altrando  atributo do objeto
        print  ('Rio de Janeiro')
        print ('listando Nº protocolo:>')
        print (rogerio.cumprimentar(),'Nome:>',(rogerio.nome),'Idade:>',(rogerio.idade),'Estado:>',(rogerio.estado))
        print (felipe.cumprimentar(),'Nome:>',(felipe.nome),'Idade:>',(felipe.idade),'Estado:>',(felipe.estado))
        print (alikan.cumprimentar(),'Nome:>',(alikan.nome),'Idade:>',(alikan.idade),'Estado:>',(alikan.estado))
        print ('os valores do  atributos intanciado e ligado  ao objeto:> ')
        print(alikan.__dict__)        ###  discrever o valor alocar em cada memonia do objeto
        print(rogerio.__dict__)
        print(felipe.__dict__)
        print('apricação de todos os item criado:>')
        print('os meu olhos  são:',alikan.olhos,'e',alikan.Estado,'é minha cidade e a meu nome é',alikan.nome,'tenho  idade',alikan.idade,
              'estou de mudança',alikan.estado,'e meus filhos',alikan.filhos,)
