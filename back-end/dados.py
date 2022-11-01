import sqlite3
import pandas as pd
import time
import datetime

connection = sqlite3.connect('dados.db')

con = connection.cursor()

def create_table():
    con.execute('CREATE TABLE IF NOT EXISTS exemplo(id_cessao INTEGER PRIMARY KEY AUTOINCREMENT, Originador, Doc_Originador, Cedente, Doc_Cedente, \
                                                      CCB, Id_externo, Cliente, CPF_CNPJ, Endereco, CEP, Cidade, \
                                                      UF, Valor_do_Empréstimo, Valor_Parcela, total_parcelas, \
                                                      Parcela, Data_de_Emissao, Data_de_Vencimento, Preco_de_Aquisicao)')
    

def insert_value():
    df = pd.read_csv("arquivos\\arquivo_exemplo.csv", sep=";", encoding="latin1")
    
    df = df.drop(columns=["Taxa de Juros (a.m.)", "Principal R$", "Juros R$", "IOF R$", "Comissão R$", "Multa", "Mora", "Data de Compra CCB"], axis=0)
    for index, linha in df.iterrows():
        #print(linha)
        con.execute('INSERT INTO exemplo (Originador, Doc_Originador, Cedente, Doc_Cedente, CCB, Id_externo, Cliente, CPF_CNPJ, Endereco, CEP, Cidade, UF, Valor_do_Empréstimo, Valor_Parcela, total_parcelas, Parcela, Data_de_Emissao, Data_de_Vencimento, Preco_de_Aquisicao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', linha)
    
    
if __name__ =='__main__':
    create_table()
    dados = insert_value()
    print(dados)