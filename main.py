import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import string

# Certifique-se de que os pacotes necessários estejam baixados
nltk.download('punkt')
nltk.download('stopwords')

# Função para processar o texto
def processar_texto(arquivo):
    # Leitura do arquivo de texto
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    # Tokenização do texto em palavras
    palavras = word_tokenize(texto.lower())

    # Remoção de pontuações
    palavras = [palavra for palavra in palavras if palavra not in string.punctuation]

    # Remoção de stopwords (palavras comuns que não agregam muito significado)
    stop_words = set(stopwords.words('portuguese'))
    palavras = [palavra for palavra in palavras if palavra not in stop_words]

    # Contagem de frequência das palavras
    contagem = Counter(palavras)

    return contagem

# Função para gerar o gráfico
def gerar_grafico(contagem):
    palavras, frequencias = zip(*contagem.most_common(20))  # Mostra as 20 palavras mais comuns
    plt.figure(figsize=(10, 5))
    plt.bar(palavras, frequencias, color='blue')
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.title('Frequência das 20 palavras mais comuns')
    plt.xticks(rotation=45)
    plt.show()

# Caminho para o arquivo .txt
arquivo = 'texto.txt'  # Substitua pelo caminho do seu arquivo

# Processar o texto e gerar o gráfico
contagem_palavras = processar_texto(arquivo)
gerar_grafico(contagem_palavras)
