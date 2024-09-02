
# Projeto de Processamento de Linguagem Natural

Este projeto é um exemplo de como processar texto em Python usando as bibliotecas `nltk` e `matplotlib` para gerar um gráfico da frequência de palavras em um texto.

## Pré-requisitos

- **Python 3.x**
- **pip** (gerenciador de pacotes do Python)

## Configuração do Ambiente

### 1. Clone o Repositório

Clone este repositório para sua máquina local usando o comando:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Crie um Ambiente Virtual

Navegue até o diretório do projeto e crie um ambiente virtual:

```bash
cd nome-do-repositorio
python -m venv env
```

### 3. Ative o Ambiente Virtual

Ative o ambiente virtual:

- **Windows**:
  ```bash
  .\env\Scripts\activate
  ```

- **MacOS/Linux**:
  ```bash
  source env/bin/activate
  ```

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install --upgrade pip
pip install nltk matplotlib
```

### 5. Baixe os Pacotes NLTK

Inicie o interpretador Python e execute os seguintes comandos para baixar os pacotes necessários:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
exit()
```

## Executando o Script

Após configurar o ambiente, você pode executar o script para processar um arquivo de texto e gerar o gráfico de frequência de palavras.

1. Coloque o arquivo de texto (`.txt`) que você deseja processar no diretório do projeto.
2. Execute o script Python:

```bash
python processar_texto.py
```

O script vai gerar um gráfico mostrando as 20 palavras mais frequentes no texto, excluindo as stopwords (palavras comuns como "de", "a", "e", etc.).

## Desativando o Ambiente Virtual

Após terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

## Licença

Este projeto é licenciado sob os termos da licença MIT. Veja o arquivo `LICENSE` para mais detalhes.



Como são chamadas as palavras que ocorrem com muita frequência e que podem não agregar muito significado?

Em processamento de linguagem natural, essas palavras são chamadas de stopwords. Stopwords são palavras que ocorrem com muita frequência em um texto e que geralmente não agregam muito significado semântico ao conteúdo do texto. Exemplos de stopwords em português incluem "de", "a", "e", "o", "que", entre outras.
Para o texto que você analisou (que deve conter no mínimo 2000 palavras), quais seriam essas palavras?

As palavras exatas que seriam consideradas stopwords dependem do conteúdo específico do texto que você está analisando. No entanto, para a maioria dos textos em português, as stopwords comuns incluem:
"de"
"a"
"o"
"que"
"e"
"do"
"da"
"em"
"para"
"com"
Estas são palavras funcionais que ajudam a estruturar as frases, mas que geralmente não carregam um significado específico por si só.

Quais as classes dessas palavras?

As stopwords normalmente pertencem às seguintes classes gramaticais:
Artigos: "o", "a", "os", "as"
Preposições: "de", "em", "para", "com"
Conjunções: "e", "ou", "mas", "porque"
Pronomes: "ele", "ela", "que", "quem"
Essas classes de palavras são essenciais para a estrutura da linguagem, mas, no contexto de análise de texto, elas são frequentemente removidas para focar nas palavras que carregam o verdadeiro conteúdo semântico.