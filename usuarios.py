# Importar a biblioteca do MongoDB
from pymongo import MongoClient

# Conectar ao banco de dados
client = MongoClient("localhost", 27017)

# Criar um banco de dados
db = client["db_nosql"]

# Criar uma coleção
collection = db["usuarios"]

# Inserir documentos na coleção
joao = {"nome": "João", "idade": 25}
maria = {"nome": "Maria", "idade": 30}
ana = {"nome": "Ana", "idade": 19}

collection.insert_many([joao, maria, ana])

# Buscar documentos na coleção
busca = collection.find({})

# Imprimir os resultados da busca
for usuario in busca:
    print(usuario)

# Atualizar um documento na coleção
collection.update_one({"nome": "Maria"}, {"$set": {"idade": 31}})

# Excluir um documento da coleção
collection.delete_one({"nome": "Ana"})

# Fechar a conexão com o banco de dados
client.close()