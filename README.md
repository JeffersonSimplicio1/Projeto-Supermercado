# 🛒 Sistema de Gerenciamento de Supermercado

Sistema Back-End desenvolvido em **Python e MySQL** com o objetivo de aplicar, na prática, conceitos de **Programação Orientada a Objetos, arquitetura em camadas, persistência de dados e testes unitários**.

O projeto simula operações de gerenciamento de um supermercado e está sendo desenvolvido de forma incremental, com novas entidades, regras de negócio e funcionalidades sendo adicionadas ao longo da evolução do sistema.

> 🚧 **Status:** Em desenvolvimento


## 🛠️ Tecnologias

<img src="https://skillicons.dev/icons?i=python,mysql,git,github" />

### Principais conceitos aplicados

- Programação Orientada a Objetos (POO)
- Separação de responsabilidades
- Camadas **Service** e **Repository**
- Persistência de dados com MySQL
- CRUD
- Validações e regras de negócio
- Tratamento de exceções
- Testes unitários com `unittest`
- Uso de mocks com `unittest.mock`
- Variáveis de ambiente com `python-dotenv`


## 🏗️ Arquitetura do Projeto

O projeto utiliza uma organização em camadas para separar as responsabilidades da aplicação.

```text
        Models
          │
          ▼
       Services
          │
          ▼
     Repositories
          │
          ▼
        MySQL
```

### 📦 Models

Representam as entidades do sistema e seus respectivos dados.

Atualmente o projeto possui modelos para:

- Produto
- Cliente
- Funcionário


### ⚙️ Services

Responsáveis pelas **regras de negócio e validações** antes das operações serem encaminhadas para a camada de persistência.

Entre as responsabilidades estão:

- Validação de dados
- Verificação da existência de registros
- Validação de valores
- Tratamento do resultado das operações
- Retorno de mensagens de acordo com cada situação


### 🗄️ Repositories

Responsáveis pela comunicação com o banco de dados e execução das operações de persistência.

Entre as operações implementadas estão:

- Cadastro
- Listagem
- Busca por ID
- Busca por nome
- Atualização
- Exclusão por ID
- Exclusão por nome


### 🛢️ Database

Responsável pela criação e gerenciamento da conexão com o **MySQL**.

Os dados de conexão são armazenados em variáveis de ambiente, evitando que informações sensíveis sejam inseridas diretamente no código.


## 🧪 Testes

O projeto utiliza o módulo `unittest` do Python para criação e execução dos testes.

Na camada de serviços também são utilizados **Mocks** através do `unittest.mock`, permitindo testar as regras de negócio de forma isolada da camada de Repository e do banco de dados.

### Estratégia utilizada

```text
        Teste
          │
          ▼
       Service
          │
          ▼
    Mock Repository
```

Dessa forma, é possível definir o comportamento esperado do Repository durante cada cenário de teste e verificar como o Service responde.

### Recursos utilizados nos testes

- `Mock()`
- `return_value`
- `assertEqual()`
- `assert_called_once_with()`
- `assert_not_called()`
- `setUp()`

Os testes contemplam cenários como:

- Operações realizadas com sucesso
- Registros inexistentes
- Dados inválidos
- Campos obrigatórios vazios
- Falhas simuladas no Repository
- Validações das regras de negócio


## 📂 Estrutura do Projeto

```text
Projeto-Supermercado/
│
├── database/
│   └── coneccao.py
│
├── models/
│   ├── produto.py
│   ├── cliente.py
│   └── funcionario.py
│
├── repositorios/
│   ├── produtos_repositorios.py
│   ├── cliente_repositorio.py
│   └── funcionario_repositorio.py
│
├── servicos/
│   ├── produto_servico.py
│   ├── cliente_servico.py
│   └── funcionario_servico.py
│
├── testes/
│   ├── TesteRepositorios/
│   └── TesteServicos/
│
├── .gitignore
├── requirements.txt
└── README.md
```


## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/JeffersonSimplicio1/Projeto-Supermercado.git
```

Entre no diretório:

```bash
cd Projeto-Supermercado
```


### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```


### 3. Instale as dependências

```bash
pip install -r requirements.txt
```


### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto contendo as informações necessárias para conexão com o MySQL.

> ⚠️ O arquivo `.env` contém informações locais/sensíveis e não deve ser enviado para o GitHub.


## 📦 Dependências

As principais dependências externas utilizadas atualmente são:

- `mysql-connector-python`
- `python-dotenv`

As versões utilizadas pelo projeto estão registradas no arquivo:

```text
requirements.txt
```


## 🗺️ Roadmap

### ✅ Concluído

- [x] Modelagem de Produto
- [x] Repository de Produto
- [x] Service de Produto
- [x] Modelagem de Cliente
- [x] Repository de Cliente
- [x] Service de Cliente
- [x] Testes unitários de ProdutoService
- [x] Testes unitários de ClienteService
- [x] Modelagem de Funcionário
- [x] Repository de Funcionário
- [x] Service de Funcionário
- [x] Organização do projeto em repositório próprio
- [x] Configuração do `requirements.txt`

### 🚧 Em desenvolvimento

- [ ] Finalizar testes de FuncionarioService
- [ ] Ampliar cobertura de testes
- [ ] Melhorar validações e tratamento de erros

### 🔜 Próximas etapas

- [ ] Implementar entidade Venda
- [ ] Implementar itens de venda
- [ ] Integrar fluxo de vendas com estoque
- [ ] Criar interface para interação com o sistema
- [ ] Preparar aplicação para deploy
- [ ] Deploy em ambiente AWS


## 📈 Evolução do Projeto

Este projeto está sendo desenvolvido de forma incremental.

A proposta não é apenas implementar funcionalidades, mas utilizar cada nova etapa para praticar conceitos de **desenvolvimento Back-End, organização de código, banco de dados, testes e boas práticas**.

O histórico de commits do repositório registra essa evolução desde as primeiras implementações até a estrutura atual.


## 👨‍💻 Autor

**Jefferson Simplicio**

Desenvolvedor Back-End | Python • MySQL • Java

[LinkedIn](https://www.linkedin.com/in/jefferson-simplicio1) • [GitHub](https://github.com/JeffersonSimplicio1)
