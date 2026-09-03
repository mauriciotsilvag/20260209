# API Connect - Gerenciamento de Usuários

API RESTful desenvolvida em Python com o microframework Flask para o gerenciamento centralizado de usuários (CRUD). Este MVP foi construído focando nos padrões REST, arquitetura modular e tratamento rigoroso de dados em formato JSON.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework:** Flask
- **Gerenciador de Dependências:** Pip
- **Utilitários:** `python-dotenv` (gestão de variáveis de ambiente), `uuid` (geração de IDs únicos)

---

## 📂 Estrutura do Projeto

```text
api-connect-mvp/
├── src/
│   ├── controllers/
│   │   └── user_controller.py   # Validações e regras de negócio
│   ├── models/
│   │   └── user_model.py        # Camada de dados (em memória)
│   ├── routes/
│   │   └── userRoutes.py        # Definição e mapeamento dos endpoints HTTP
│   └── app.py                   # Instanciação do Flask e registro de rotas
├── .env.example                 # Modelo de variáveis de ambiente
├── .gitignore                   # Exclusão de venv e arquivos temporários
├── requirements.txt             # Lista de dependências do projeto
├── README.md                    # Documentação técnica
└── server.py                    # Ponto de entrada (entry point) da aplicação
```

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Git instalado.

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/api-connect-nome-sobrenome.git
   cd api-connect-nome-sobrenome
   ```

2. **Criar e Ativar o Ambiente Virtual:**
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Instalar as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:
   ```bash
   cp .env.example .env
   ```

5. **Iniciar o Servidor:**
   ```bash
   python server.py
   ```
   A aplicação estará disponível em: `http://localhost:5000`

---

## 📑 Tabela de Referência dos Endpoints (Documentação)

| Método | Endpoint | Descrição | Status Sucesso | Status Erro |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/users/` | Retorna a lista completa de usuários | `200 OK` | - |
| **GET** | `/api/users/<id>` | Busca um usuário específico por ID | `200 OK` | `404 Not Found` |
| **POST** | `/api/users/` | Cadastra um novo usuário | `201 Created` | `400 Bad Request` |
| **PUT/PATCH** | `/api/users/<id>` | Atualiza dados de um usuário existente | `200 OK` | `400 Bad Request` / `404 Not Found` |
| **DELETE** | `/api/users/<id>` | Remove um usuário por ID | `200 OK` | `404 Not Found` |

---

## 📋 Exemplos de Payload (JSON)

### Criar Usuário (`POST /api/users/`)
**Requisição:**
```json
{
  "nome": "Maria Silva",
  "email": "maria.silva@exemplo.com",
  "cargo": "Desenvolvedora"
}
```

**Resposta (`201 Created`):**
```json
{
  "status": "sucesso",
  "mensagem": "Usuário cadastrado com sucesso.",
  "dados": {
    "id": "e4a7b21a-8c3f-4f12-9b0d-1a2b3c4d5e6f",
    "nome": "Maria Silva",
    "email": "maria.silva@exemplo.com",
    "cargo": "Desenvolvedora"
  }
}
```
