#exemplo ler arquivo json, pegar registros e salvar em arquivo .csv
''''
from pyspark.sql import SparkSession

if __name__ == "__main__":

    # Criar uma SparkSession
    spark = SparkSession.builder \
        .appName("MeuProjetoSpark") \
        .getOrCreate()


    print("LENDO O ARQUIVO")
    # Ler um arquivo JSON
    df = spark.read.json("files/file.json")

    # Mostrar os primeiros 5 registros
    df.show(5)

    # Selecionar colunas específicas
    df = df.select("email")

    df.show()

    # Filtrar registros
    df_filtered = df.filter(df["email"] == "vanderlei196000@gmail.com")

    df_filtered.show(20, False)


    # Salvar como arquivo Parquet
    
    df_filtered.coalesce(1).write.csv("files/file.csv", header=True)

    # Parar a SparkSession
    spark.stop()
'''

#  2. Ler com spark filtrar pessoas que o email termina em @exemple.com, @example.net, @example.org,  salvar em parquet.
'''
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import BooleanType
from pyspark.sql.functions import udf

# Caminho para o arquivo CSV
caminho_csv = "/home/projeto_1/projeto_1/files/dados_pessoais.csv"

# Verificar se o arquivo existe
if os.path.exists(caminho_csv):

    # Inicializar a Spark Session
    spark = SparkSession.builder \
        .appName("Filtrar E-mails por Domínio") \
        .getOrCreate()

    # Leitura do arquivo CSV
    df = spark.read.csv(caminho_csv, header=True, inferSchema=True)

    # Verifique os nomes das colunas
    print("Colunas disponíveis:", df.columns)

    # Definir os domínios a serem filtrados
    dominios = ["@example.com", "@example.net", "@example.org"]

    # Função para verificar se o e-mail termina com um dos domínios especificados
    def filtrar_dominio(email):
        if email is None:
            return False
        return any(email.endswith(dominio) for dominio in dominios)

    # Registro da função de usuário para ser usada no Spark
    filtrar_dominio_udf = udf(filtrar_dominio, BooleanType())

    # Filtrando os e-mails pelo domínio
    df_filtrado = df.filter(filtrar_dominio_udf(col("Email")))

    # Verifique o DataFrame filtrado
    print("DataFrame filtrado:")
    df_filtrado.show(5)

    # Selecionando apenas as colunas de pessoas e e-mails
    df_selecionado = df_filtrado.select("Nome", "Email")

    # Verifique o DataFrame selecionado
    print("DataFrame selecionado:")
    df_selecionado.show(5)

    # Caminho para salvar o arquivo CSV
    caminho_csv_saida = "/home/projeto_1/projeto_1/files/resultado.csv"

    # Salvar o DataFrame filtrado e selecionado em formato CSV
    df_selecionado.coalesce(1).write.csv(caminho_csv_saida, header=True, mode="overwrite")

    # Encerrar a Spark Session
    spark.stop()

    print("Gravação concluída.")
else:
    print(f"O arquivo {caminho_csv} não foi encontrado.")

'''

'''
# mostrar 5 registros com psyspark
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import BooleanType
from pyspark.sql.functions import udf

caminho_csv = "/home/projeto_1/projeto_1/files/resultado.csv"

# Verificar se o arquivo existe
if os.path.exists(caminho_csv):

    # Inicializar a Spark Session
    spark = SparkSession.builder \
        .appName("Filtrar E-mails por Domínio") \
        .getOrCreate()

    # Leitura do arquivo CSV
    df = spark.read.csv(caminho_csv, header=True, inferSchema=True)

    print("DataFrame filtrado:")
    df.show(5)
'''
'''
# 1. Ler com spark filtrar pessoas com idade maior ou igual a 30 salvar em um json.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, year, date_format
from datetime import datetime

# Criar sessão Spark
spark = SparkSession.builder \
    .appName("FiltrarPessoas") \
    .getOrCreate()

# Carregar o arquivo CSV
df = spark.read.csv("/home/projeto_1/projeto_1/files/dados_pessoais.csv", header=True, inferSchema=True)

# Converter a coluna 'Data de Nascimento' para o formato de data
df = df.withColumn("Data de Nascimento", to_date(col("Data de Nascimento"), "dd/MM/yyyy"))

# Obter o ano atual
current_year = datetime.now().year

# Calcular a idade com base na coluna convertida
df = df.withColumn("Idade", current_year - year(col("Data de Nascimento")))

# Filtrar pessoas com idade maior ou igual a 30
df_filtrado = df.filter(col("Idade") >= 30)

# Selecionar apenas as colunas 'Nome' e formatar 'Data de Nascimento'
df_selecionado = df_filtrado.select("Nome", date_format(col("Data de Nascimento"), "dd/MM/yyyy").alias("Data de Nascimento"))

# Exibir o resultado no terminal
df_selecionado.show()

# Salvar em formato JSON
df_selecionado.write.json("/home/projeto_1/projeto_1/files/pessoas_acima_30.json")

# Encerrar a sessão Spark
spark.stop()
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# Criar sessão Spark
spark = SparkSession.builder \
    .appName("FiltrarDominioEmail") \
    .getOrCreate()

# Carregar o arquivo CSV
df = spark.read.csv("/home/projeto_1/projeto_1/files/dados_pessoais.csv", header=True, inferSchema=True)

# Criar uma coluna de domínio
df = df.withColumn("Dominio", when(col("Email").endswith("@example.com"), "@example.com")
                   .when(col("Email").endswith("@example.net"), "@example.net")
                   .when(col("Email").endswith("@example.org"), "@example.org")
                   .otherwise(None))

# Filtrar e contar os domínios
resultados = df.groupBy("Dominio").agg(count("*").alias("Total"))

# Filtrar apenas os domínios desejados
resultados = resultados.filter(col("Dominio").isNotNull())

# Exibir o resultado no terminal
resultados.show()

# Salvar em formato CSV
resultados.write.csv("/home/projeto_1/projeto_1/files/totais_dominios.csv", header=True)

# Encerrar a sessão Spark
spark.stop()
