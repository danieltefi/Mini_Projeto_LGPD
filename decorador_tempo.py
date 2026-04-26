import time
import logging
from functools import wraps

logging.basicConfig( # configuração do log atividade 4
    filename='data/execucao.log', # salva as mensagens noa arquivo log ao invés de exibir no terminal
    level=logging.INFO, # registra as mensagens informativas gerais
    format='%(asctime)s - %(message)s', # %(asctime)s insere data e hora que rodou, %(message)s texto do decorador
    encoding='utf-8' # padrão de escrita, garante que caracteres especiais e acentos sejam gravados corretamente sem gerar erros de leitura
)

def medir_tempo(func): # decorador atividade 4, mede o tempo de execução de uma função
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter() # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter() # tempo final
        duracao = fim - inicio
        
        mensagem = f'Função "{func.__name__}" executada em {duracao:.6f} segundos.'
        
        logging.info(mensagem) # grava no arquivo de log e mostra no terminal
        print(f'⏱ {mensagem}')
        
        return resultado
    return wrapper