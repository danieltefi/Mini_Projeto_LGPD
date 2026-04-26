# Mini Projeto LGPD
> **Projeto FATEC LGPD**

## Sobre o Projeto
Este projeto tem como objetivo aplicar técnicas de anonimização de dados e manipulação de arquivos em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018). O sistema interage com um banco de dados PostgreSQL para extrair informações de usuários e realizar o tratamento de dados sensíveis (nome, CPF, e-mail e telefone) para depois exportá-los para formatos externos (XLSx).
- Atividade 1: Anonimação de campos, substituindo caracteres/letras por asteriscos (*).
- Atividade 2: Criar arquivos XLSx com dados (anonimizados) de pessoas divididos por ano.
- Atividade 3: Criar arquivo XLSx com todos os registros, contendo nome e CPF (não anonimizados).
- Atividade 4: Utilizar o decorator_tempo.py para gravar logs e tempo de exxecução das atividades 2 e 3.

## 🛠️ Tecnologias
- **Linguagem:** Python 3
- **Bibliotecas:** SQLAlchemy, psycopg2, pandas, openpyxl, logging
- **Arquitetura:** Orientação a Objetos (POO) com uso de Decoradores para medição de performance.
- **Saída:** Arquivo Exel (XLSx).

## ⚙️ Configuração do ambiente
O projeto utiliza **ambiente virtual (venv)** para isolamento de dependências.

### Instalação:
1. **Criar o Ambiente Virtual:**
   O ambiente virtual isola as bibliotecas do projeto:
   ```bash
   python -m venv .venv
2. **Ative o ambiente:**
   - Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
   - Windows (CMD): `.\.venv\Scripts\activate.bat`
   - Linux/macOS: `source .venv/bin/activate`
3. **Dependências:** `pip install -r requirements.txt`

### Execução:
- Com o venv ativo: `python LGPD.py`

## 📂 Estrutura de Arquivos

```text
├── .venv/               # Ambiente virtual isolado
├── data/                # Pasta de saída para os arquivos XLSx gerados
├── .gitattributes       # Configurações de atributos de caminho do Git
├── .gitignore           # Define arquivos que o Git deve ignorar
├── CHECKLIST.md         # Acompanhamento do progresso do projeto
├── decorator_tempo.py   # Módulo de monitoramento (Decorador e Logging)
├── LGPD.py              # Ponto de entrada e execução (com regras de anonimação)
├── LICENSE              # Termos de uso e licença do código
├── README.md            # Documentação do projeto
└── requirements.txt     # Lista de dependências (bibliotecas)
```

---

### 🚧 Status do Projeto:
*Concluído*