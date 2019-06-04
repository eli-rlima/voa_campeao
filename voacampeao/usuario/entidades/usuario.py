class Usuario():
    def __init__(self, cpf, nome, sexo, data_nascimento):
        self.__cpf = cpf
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento


        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
             self.__nome = nome

        @property
        def sexo(self):
            return self.__sexo

        @sexo.setter
        def sexo(self, sexo):
            self.__sexo = sexo

        @property
        def cpf(self):
            return self.__cpf

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf

        @property
        def data_nascimento(self):
            return self.__data_nascimento

        @data_nascimento.setter
        def data_nascimento(self, data_nascimento):
            self.__data_nascimento = data_nascimento