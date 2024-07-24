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


