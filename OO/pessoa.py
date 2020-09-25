class Pessoa:                                            ### criação de class prinipal

    Estado = 'Recife-PE'                                 #### criação de atributo de class pode ser chamado em qual quer def

    def __init__(self,*filhos,nome=None,idade=18):       ###criando uma def de inicialização
        self.idade=idade
        self.nome=nome
        self.filhos=list (filhos)
    def cumprimentar(self):                             ###criando def com f estring   gerando o id
        return f'numero de protocolo {id(self)}'

if __name__ == "__main__":
        alikan = Pessoa(nome='alikan')
        felipe = Pessoa(alikan,nome='Felipe')
        rogerio =Pessoa(alikan,felipe,nome='Rogerio')
        print('testando:')
        print(Pessoa.cumprimentar(alikan))
        print(id (alikan))
        print(alikan.cumprimentar()),(alikan.nome)
        print(alikan.idade)
        print(alikan.Estado)
        print('lista de filhos  de rogerio:')
        for filho in rogerio.filhos:                                    ###pegando  objeto  anteriores
            if(rogerio.filhos):                                         ### para cada nome sera impresoo meu filhor
                print('meu filhor')
            print(filho.nome)
        print('alterando o estados:')
        alikan.estado = 'Sergipe'
        print ('Sergipe')
        rogerio.estado = 'São Paulo'
        print  ('São Paulo')
        felipe.estado = 'Rio de Janeiro'
        print  ('Rio de Janeiro')
        print ('liatade pessoal organizado:')
        print (rogerio.cumprimentar()),(rogerio.nome),(rogerio.idade),(rogerio.estado),()
        print (felipe.cumprimentar()),(felipe.nome),(felipe.idade),(felipe.estado),()
        print (alikan.cumprimentar()),(alikan.nome),(alikan.idade),(alikan.estado),()
        print ('os valores de  atributos intanciado/ligado  ao objeto ')
        print(alikan.__dict__)
        print(rogerio.__dict__)
        print(felipe.__dict__)