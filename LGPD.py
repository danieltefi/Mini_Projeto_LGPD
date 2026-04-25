from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime

import time
from functools import wraps
def medir_tempo(func): # decorator que mede o tempo de execução de uma função.
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f'⏱ Função "{func.__name__}" executada em {duracao:.6f} segundos.')
        return resultado
    return wrapper

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

@medir_tempo
def LGPD(row): # transforma a row em um objeto e anonimiza para a atividade 1
    user_obj = Usuario(row) # instanciação
    user_obj.anonimizar()    # chamada do método
    return user_obj

users = []
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM usuarios LIMIT 5;'))
    for row in result:
        row = LGPD(row)
        users.append(row)

for user in users: # ver os dados anonimizados no terminal
    print(f'Nome: {user.nome} \nCPF: {user.cpf} \nEmail: {user.email} \nTel: {user.telefone}')