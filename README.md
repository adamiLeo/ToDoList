
### **Documentação do Projeto: To-Do List Web App com Banco de Dados**

Autor: Leonardo da Silva Adami RA: 2421311
Vinicius Henrique Macedo RA: 2420695
Vinicius Sato RA: 2420673
Curso: Análise e Desenvolvimento de Sistemas 
Disciplina: Banco de Dados

-----

#### 1. Introdução / Resumo do Projeto

Este documento detalha o desenvolvimento de uma aplicação web do tipo "To-Do List" (Lista de Tarefas). O objetivo principal do projeto é demonstrar a aplicação de conceitos fundamentais de bancos de dados relacionais em um ambiente prático e funcional.

A aplicação permite que o usuário gerencie suas tarefas diárias através de uma interface web interativa. O sistema foi construído utilizando uma arquitetura cliente-servidor, onde o front-end (cliente, rodando no navegador) se comunica com um back-end (servidor) responsável pela lógica de negócios e pela persistência dos dados em um banco de dados SQLite.

Foram implementadas todas as operações essenciais de manipulação de dados (CRUD - Create, Read, Update, Delete), além de funcionalidades mais avançadas como a edição de tarefas e a atribuição de níveis de prioridade, que exigiram a modificação do esquema (schema) do banco de dados após sua criação inicial.

-----

#### **2. Tecnologias Utilizadas**

  * **Back-end:** **Python 3** com o micro-framework **Flask**. Flask foi escolhido por sua simplicidade e flexibilidade, sendo ideal para a criação do servidor web e da API RESTful que responde às requisições do front-end.

  * **Banco de Dados:** **SQLite 3**. Um sistema de gerenciamento de banco de dados relacional embutido, que funciona a partir de um único arquivo. É ideal para projetos de pequeno e médio porte por sua simplicidade, portabilidade e por não necessitar de um servidor dedicado.

  * **Front-end:** **HTML5**, **CSS3** e **JavaScript**. A estrutura da página foi criada com HTML, a estilização com CSS para uma interface limpa e moderna, e o JavaScript foi utilizado para criar a interatividade, realizando chamadas assíncronas (via `fetch API`) ao back-end para manipular os dados sem a necessidade de recarregar a página a cada ação.

  * **Ambiente de Desenvolvimento:** **GitHub Codespaces**. Um ambiente de desenvolvimento em nuvem que permite a codificação, execução e depuração do projeto diretamente no navegador, eliminando a necessidade de configuração de ambiente local.

-----

#### **3. Estrutura do Banco de Dados**

O banco de dados da aplicação, chamado `tarefas.db`, contém uma única tabela principal que armazena todas as informações das tarefas.

  * **Tabela: `tarefas`**
    Esta tabela é o coração da aplicação, guardando os detalhes de cada tarefa inserida pelo usuário.

| Nome da Coluna | Tipo de Dado | Restrições (Constraints) | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único para cada tarefa, gerado automaticamente. |
| `descricao` | `TEXT` | `NOT NULL` | O texto que descreve a tarefa a ser feita. |
| `concluida` | `INTEGER` | `NOT NULL DEFAULT 0` | Um campo booleano (0 para 'não', 1 para 'sim') que indica o status da tarefa. |
| `prioridade` | `INTEGER` | `NOT NULL DEFAULT 1` | Nível de prioridade da tarefa. (1=Baixa, 2=Média, 3=Alta). |

  * **Código SQL para Criação da Tabela:**
    ```sql
    CREATE TABLE tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        concluida INTEGER NOT NULL DEFAULT 0,
        prioridade INTEGER NOT NULL DEFAULT 1
    );
    ```

-----

#### **4. Funcionalidades da Aplicação**

A interface web permite ao usuário realizar as seguintes ações, que correspondem diretamente às operações CRUD no banco de dados:

  * **Adicionar Tarefas (Create):** O usuário pode inserir a descrição de uma nova tarefa, selecionar um nível de prioridade e adicioná-la à lista. Isso executa uma operação `INSERT` na tabela `tarefas`.
  * **Visualizar Tarefas (Read):** Todas as tarefas são listadas na página principal. A lista é ordenada por prioridade (da mais alta para a mais baixa) como critério principal, e pela data de criação como critério de desempate. Isso é feito com uma operação `SELECT ... ORDER BY`.
  * **Marcar como Concluída (Update):** Cada tarefa possui um checkbox que, ao ser marcado/desmarcado, atualiza o campo `concluida` no banco de dados através de uma operação `UPDATE`.
  * **Editar Tarefas (Update):** Um botão de edição permite que o usuário altere o texto de uma tarefa já existente, disparando outra operação `UPDATE`.
  * **Excluir Tarefas (Delete):** Um botão de exclusão remove permanentemente a tarefa da lista e do banco de dados através de uma operação `DELETE`.
  * **Feedback Visual:** As tarefas exibem uma borda colorida correspondente à sua prioridade (Vermelho=Alta, Amarelo=Média, Azul=Baixa), facilitando a identificação visual.

-----

#### **5. Estrutura dos Arquivos do Projeto**

O projeto está organizado da seguinte forma:

```
/projeto_todolist
|
|-- app.py             # Lógica do back-end (Flask) e rotas da API
|-- tarefas.db         # O arquivo do banco de dados SQLite
|-- requirements.txt   # Lista de dependências Python (Flask)
|
|-- templates/
|   |-- index.html     # Estrutura HTML da página principal
|
|-- static/
|   |-- style.css      # Código de estilização da página
```

-----

#### **6. Como Executar o Projeto**

1.  **Pré-requisitos:** Ter o Python 3 e o `pip` instalados.
2.  **Clonar o Repositório:** `git clone [URL_DO_REPOSITORIO]`
3.  **Instalar Dependências:** Navegue até a pasta do projeto e execute `pip install -r requirements.txt`.
4.  **Executar a Aplicação:** No mesmo terminal, execute o comando `python app.py`. O servidor Flask será iniciado.
5.  **Acessar no Navegador:** Abra seu navegador e acesse o endereço `http://127.0.0.1:5000`.


