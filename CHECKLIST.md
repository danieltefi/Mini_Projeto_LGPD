# 🛡️ Mini Projeto LGPD - Checklist de Desenvolvimento

Este checklist detalha as etapas de construção do sistema de conformidade com a Lei nº 13.709/2018 (LGPD), utilizando os pilares de POO, SQLAlchemy e Decoradores.

## 🟢 1. Configuração e Infraestrutura
- [x] Inicializar repositório Git e configurar `.gitignore`.
- [x] Criar ambiente virtual Python (`python -m venv .venv`).
- [x] Ativar o ambiente virtual e instalar dependências (`SQLAlchemy`, `psycopg2`, `pandas`, `openpyxl`).
- [x] Criar arquivo `requirements.txt` com as bibliotecas utilizadas.
- [x] **Conexão:** Configurar `create_engine` para o banco PostgreSQL (Host: 200.19.224.150).

## 🔵 2. Modelo de Dados e POO
- [x] **Abstração:** Definir a classe `Usuario` mapeada para a tabela do banco de dados.
- [x] **Atributos:** Mapear `id`, `nome`, `cpf`, `email`, `telefone` e `data_nascimento`.
- [x] **Encapsulamento:** Implementar o método `anonimizar()` dentro da classe para proteger a lógica de tratamento.
- [x] **Atividade 1:** 
    - [x] Mascarar Nome (Ex: `O***** Sobrenome`).
    - [x] Mascarar CPF (Ex: `237.***.***-**`).
    - [x] Mascarar E-mail (Ex: `n*********@dominio.com`).
    - [x] Mascarar Telefone (Ex: manter apenas os 4 dígitos finais - `+** (***) *****-6810`).

## 🟡 3. Processamento e Exportação
- [ ] Criar diretório `data/` para armazenar os arquivos de saída.
- [ ] **Atividade 2:** Implementar lógica para filtrar usuários por ano e exportar arquivos `.xls` individuais com dados **anonimizados**.
- [ ] **Atividade 3:** Implementar lógica para exportar arquivo `todos.xls` contendo apenas Nome e CPF **(não anonimizados)**.
- [ ] **Polimorfismo:** Garantir que os métodos de exportação lidem corretamente com diferentes volumes de dados.

## 🟠 4. Performance e Monitoramento
- [ ] Criar o arquivo `decorator_tempo.py`.
- [ ] Implementar o decorador `@decorator_tempo` para capturar o tempo inicial e final da execução.
- [ ] **Logging:** Configurar o módulo `logging` para salvar o nome da função e o tempo gasto no arquivo `execucao.log`.
- [ ] **Atividade 4:** Aplicar o decorador nas funções das Atividades 2 e 3.

## 🔴 5. Finalização e Entrega
- [ ] Realizar teste de integração (Script lendo o banco e gerando arquivos na pasta `data/`).
- [ ] Comentar o código.
- [ ] Atualizar o `README.md`.
- [ ] Realizar o commit final e organizar a estrutura de pastas conforme o planejado.

---
*Status Atual: 🚧 Em desenvolvimento*