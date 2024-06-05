from pymongo import MongoClient

client = MongoClient("mongodb+srv://mrlodin1:220197lady@cluster0.o8ecf4s.mongodb.net/")

db = client["LOJA"]

cliente_collection = db['cliente']
conta_collection = db["conta"]

cliente_collection.insert_one({"nome": "Andre", "cpf": "15637691746", "endereco": "rua 2" })

clientes = cliente_collection.find()
for cliente in clientes:
    print(cliente)

andre = cliente_collection.find_onde({"nome": "Andre"})

conta_collection.insert_one({
    "tipo": "Corrente",
    "agencia": "12345",
    "numero": "56456400",
    "id_cliente": andre["_id"],
    "saldo": 1000
})

contas = conta_collection.find()
for conta in contas:
    print(conta)
