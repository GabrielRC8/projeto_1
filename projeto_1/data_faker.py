import pandas as pd
from faker import Faker

# Inicialize o gerador de dados Faker
fake = Faker()

def gerar_dados_pessoais(num_registros):
    # Cria uma lista para armazenar os dados
    dados = []
    
    for _ in range(num_registros):
        registro = {
            'Nome': fake.name(),
            'Endereço': fake.address(),
            'Email': fake.email(),
            'Telefone': fake.phone_number(),
            'Data de Nascimento': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%d/%m/%Y'),
            'País': fake.country()
        }
        dados.append(registro)
    
    return dados

def salvar_em_csv(dados, caminho_arquivo):
    # Cria um DataFrame do pandas com os dados
    df = pd.DataFrame(dados)
    # Salva o DataFrame em um arquivo CSV
    df.to_csv(caminho_arquivo, index=False, encoding='utf-8')

if __name__ == "__main__":
    # Defina o número de registros e o caminho do arquivo
    numero_de_registros = 100
    caminho_arquivo = '/home/projeto_1/projeto_1/files/dados_pessoais.csv'
    
    # Gere os dados fictícios
    dados = gerar_dados_pessoais(numero_de_registros)
    
    # Salve os dados no arquivo CSV
    salvar_em_csv(dados, caminho_arquivo)

    print(f"Dados fictícios salvos em: {caminho_arquivo}")