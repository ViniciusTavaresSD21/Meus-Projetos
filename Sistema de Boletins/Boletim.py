class Aluno:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self._historico = Boletim()
        self._dados = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco' : endereco}
        
    @property
    def Historico(self):
        return self._historico


class Materias: 
    def __init__(self):
        self._matematica = []
        self._historia = []
        self._geografia = []
        self._português = []
        self._ingles = []
        self._artes = []
        self._quimica = []
        self._fisica = []
    
    @property
    def Matematica(self):
        return self._matematica
    
    @property
    def Historia(self):
        return self._historia
    
    @property
    def Geografia(self):
        return self._geografia
    
    @property
    def Portugues(self):
        return self._português
    
    @property
    def Inglês(self):
        return self._ingles
    
    @property
    def Artes(self):
        return self._artes
    
    @property
    def Quimica(self):
        return self._quimica
    
    @property
    def Fisica(self):
        return self._fisica


class Boletim(Materias):
    def __init__(self):
        super().__init__()
        self._boletim_notas = []
        self.juntar_materias()

    def juntar_materias(self):
        self._boletim_notas.append(Materias)


def validar_cpf(cpf):
    if len(cpf) != 11:
        print('CPF invalido.')
        return True
    elif '.' in cpf or ',' in cpf or ' ' in cpf or '-' in cpf:
        print('Digite somente os números do seu CPF.')
        return True

def validar_nota(nota):
    if 0 > nota > 10:
        print('Nota invalida.')
        return True

def filtrar_cpf(cpf, lista_de_alunos):
    for i in lista_de_alunos:
        if cpf == i.dados['nome']:
            print('CPF já cadastrado.')
            return True
Lista_alunos = []


def registrar_aluno(lista):
    cpf = input('CPF (somente números): ')
    validacao = validar_cpf(cpf)
    if validacao:
        return
    cpf_filtrado = filtrar_cpf(cpf, Lista_alunos)

    if cpf_filtrado:
        return
    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento: (dia/mês/ano): ')
    endereco = input('Endereço (Rua, bairro, cidade): ')

    aluno = Aluno(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    lista.append(aluno)


def registrar_nota(lista):
    cpf = input('CPF (somente números): ')
    validacao = validar_cpf(cpf)
    if validacao:
        return
    cpf_filtrado = filtrar_cpf(cpf, Lista_alunos)
    if cpf_filtrado:
        return
    