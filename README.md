# **Documentação do Compilador de Workflows para D3.js**

Este é um **compilador de workflows do AWS Step Functions**, que transforma um arquivo JSON representando um workflow em uma visualização gráfica com **D3.js**. Ele é modular e segue as etapas clássicas de um compilador: **análise léxica, análise sintática, análise semântica e geração de código**.

---

## **Pré-requisitos**

### 1. **Instalar Python**
O compilador requer **Python 3.6 ou superior**. Verifique a versão instalada com:
```bash
python --version
```

Se necessário, baixe e instale o Python em [python.org/downloads](https://www.python.org/downloads/).

---

### 2. **Instalar o Pytest**
Para executar os testes fornecidos, instale o pytest:
```bash
pip install pytest
```

---

### 3. **Preparar o Ambiente**
Certifique-se de estar no diretório base do projeto. Se o projeto estiver em um repositório Git, clone-o e acesse o diretório:
```bash
git clone <URL_DO_REPOSITORIO>
cd workflow_compiler
```

Se o projeto estiver em um arquivo `.zip`, extraia-o e acesse o diretório.

---

## **Como Usar**

### 1. **Configurar o Arquivo de Entrada**

Edite ou substitua o arquivo `data/step_function.json` com o JSON representando seu workflow do Step Functions.

#### **Estrutura do JSON Esperado**
```json
{
    "StartAt": "State1",
    "States": {
        "State1": {
            "Type": "Task",
            "Next": "State2"
        },
        "State2": {
            "Type": "Choice",
            "Choices": [
                { "Next": "State3", "Condition": "x > 10" }
            ],
            "Default": "State4"
        },
        "State3": {
            "Type": "Task",
            "End": true
        },
        "State4": {
            "Type": "Fail"
        }
    }
}
```

**Regras Importantes:**
- **`StartAt`**: Define o estado inicial.
- **`States`**: Define os estados e suas transições.
- Cada estado deve ter pelo menos um dos seguintes atributos:
  - `Next`: Próximo estado.
  - `Choices`: Condições de transição (para estados de tipo `Choice`).
  - `Default`: Estado padrão (em caso de falha de condição).
  - `End`: Indica o final do workflow.

---

### 2. **Executar o Compilador**

Execute o script principal para processar o JSON e gerar o arquivo HTML:
```bash
python main.py
```

### 3. **Saída Esperada**
- O compilador cria um arquivo chamado **`data/workflow_graph.html`**.
- Este arquivo contém a visualização do workflow usando **D3.js**.

---

### 4. **Visualizar o Workflow**

Abra o arquivo `data/workflow_graph.html` em qualquer navegador moderno (como Chrome, Firefox ou Edge). A visualização incluirá:
- **Nós**: Representando cada estado do workflow.
- **Arestas**: Representando as transições entre os estados.

---

## **Testando o Compilador**

### Executar Todos os Testes

Para garantir que o compilador está funcionando corretamente, execute os testes usando o pytest:
```bash
pytest
```

### Estrutura dos Testes

- **Testes Unitários**:
  - `test_lexer.py`: Valida a análise léxica.
  - `test_parser.py`: Verifica a construção da estrutura sintática.
  - `test_semantic_analyzer.py`: Testa as regras lógicas do workflow.
  - `test_codegen.py`: Testa a geração do grafo e HTML.
- **Teste Integrado**:
  - `test_integration.py`: Verifica o pipeline completo do compilador.

---

## **FAQ**

### 1. Por que estou recebendo um erro de importação ao executar os testes?
Adicione o diretório base ao `PYTHONPATH` antes de rodar o pytest:
```bash
export PYTHONPATH=$(pwd)
pytest
```

---

### 2. O que fazer se o grafo não aparecer no navegador?
Certifique-se de que o arquivo JSON de entrada segue a estrutura esperada. Qualquer erro na formatação ou lógica pode impedir a geração correta do HTML.

---

### 3. Como adicionar novos workflows?
- Crie um novo arquivo JSON na pasta `data/`.
- Substitua o nome do arquivo no `main.py` para apontar para o novo arquivo.
- Execute o compilador novamente:
  ```bash
  python main.py
  ```

---

## **Exemplo de Uso**

### Entrada:
Arquivo `data/step_function.json`:
```json
{
    "StartAt": "State1",
    "States": {
        "State1": {
            "Type": "Task",
            "Next": "State2"
        },
        "State2": {
            "Type": "Task",
            "End": true
        }
    }
}
```

### Comando:
```bash
python main.py
```

### Saída:
- Arquivo gerado: `data/workflow_graph.html`.
- Visualização no navegador: Grafo mostrando dois nós (`State1` e `State2`) conectados.

---

Com essa documentação, você pode facilmente utilizar, testar e expandir o compilador conforme necessário. Se houver dúvidas ou problemas, sinta-se à vontade para pedir mais esclarecimentos! 🚀