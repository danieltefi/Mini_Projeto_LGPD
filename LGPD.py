from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime
import os
import pandas as pd
from decorador_tempo import medir_tempo

if not os.path.exists('data'): # cria a pasta data se n existir
    os.makedirs('data')

class Usuario: # cria a classe usuário para tratar os dados do banco (abstração)
    def __init__(self, row):
        self.id = row[0]
        self.nome = row[1]
        self.cpf = row[2]
        self.email = row[3]
        self.telefone = row[4]
        self.data_nascimento = row[5]

    def anonimizar(self): # encapsulamento para lógica de tratamento da atividade 1 (anonimização)
        partes = self.nome.split(' ') # nome (ex: O***** Araújo)
        primeiro = partes[0]
        self.nome = primeiro[0] + ('*' * (len(primeiro)-1)) + ' ' + ' '.join(partes[1:])
        
        self.cpf = f'{self.cpf[:3]}.***.***-**' # CPF (ex: 237.***.***-**)
        
        user, domain = self.email.split('@') # e-mail (ex: n*********@example.com)
        self.email = f'{user[0]}{'*' * 9}@{domain}'
        
        self.telefone = f'+** (***) *****-{self.telefone[-4:]}' # telefone (ex: +** (***) *****-6810)

engine = create_engine('postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2', echo=False)
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)

def LGPD(row): # transforma a row em um objeto e anonimiza para a atividade 1
    user_obj = Usuario(row) # instanciação
    user_obj.anonimizar()    # chamada do método
    return user_obj

@medir_tempo
def atividade_2(lista_usuarios): # atividade 2: exportar os dados anonimizados em arquivos XLS separados por ano
    grupos_por_ano = {} # cria um dicionário para agrupar por ano: { 1990: [dados], 1991: [dados] }

    for user in lista_usuarios:
        ano = user.data_nascimento.year
        
        dados = { # cria o dicionário com os dados que vão para a planilha
            'ID': user.id,
            'Nome': user.nome,
            'CPF': user.cpf,
            'Email': user.email,
            'Telefone': user.telefone,
            'Data de Nascimento': user.data_nascimento
        }

        if ano not in grupos_por_ano: # verifica se o grupo do ano já foi criado
            grupos_por_ano[ano] = [] # se o ano ainda não existia, cria ele
        
        grupos_por_ano[ano].append(dados) # localiza o grupo do ano correspondente e guarda na lista dele

    for ano, lista_dados in grupos_por_ano.items(): # gera um arquivo XLS para cada ano usando Pandas
        df = pd.DataFrame(lista_dados)
        caminho = f'data/{ano}.xlsx'
        df.to_excel(caminho, index=False)
    
    print(f'Atividade 2: {len(grupos_por_ano)} arquivos gerados na pasta data.')

@medir_tempo
def atividade_3(lista_originais): # atividade 3: exporta dados para relatório geral não anonimizados
    df = pd.DataFrame(lista_originais)
    caminho = 'data/todos.xlsx'
    df.to_excel(caminho, index=False)

    print(f'Atividade 3: Arquivo "{caminho}" gerado com sucesso.')

users = []
dados_originais = [] # lista atividade 3 (sem anonimização)
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM usuarios;'))
    for row in result:
        dados_originais.append({ # guarda os dados reais para a atividade 3 antes de anonimizar
            'Nome': row[1], 
            'CPF': row[2]
        })

        row = LGPD(row) # passa a ser anonimizada para as atividades 1 e 2
        users.append(row)

for user in users[:5]: # ver apenas os 5 primeiros dados anonimizados no terminal para conferência da atividade 1
    print(f'Nome: {user.nome} \nCPF: {user.cpf} \nEmail: {user.email} \nTel: {user.telefone}')

atividade_2(users) # chama a função para gerar os arquivos por ano
atividade_3(dados_originais) # chama a função para gerar o arquivo de relatório geral

if os.path.exists('data/execucao.log'): # verifica se o arquivo de log foi gerado para exibir no terminal
    print('Atividade 4: Log de tempo de execução "data/execucao.log" gerado com sucesso')
