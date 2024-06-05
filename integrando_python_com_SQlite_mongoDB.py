from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, create_engine, Table, UniqueConstraint
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
# É usado para cria um engine do SQLAlchemy que se conecta
# a um banco de dados SQLite em memória.  
# Um banco de dados em memória é volátil e será destruído assim 
# que a aplicação terminar ou a conexão for fechada.

metadata_obj = MetaData()

cliente = Table(
    "cliente",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("nome", String(40), nullable=False),
    # nullable é imperativo não deixar sem informação 
    Column("cpf", String(11), nullable=False),
    Column("endereco", String(100))
)

conta = Table(
    "conta", 
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("tipo", String(10)),
    Column("agencia", String(20)),
    Column("numero", String(20), unique=True),
    Column("id_cliente", Integer, ForeignKey("cliente.id"), nullable=False),
    Column("saldo", Integer) 
)

metadata_obj.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# inserir dados na tabela "cliente"

conn = engine.connect()
conn.execute(cliente.insert(), [
    {"nome": "Andre", "cpf": "15637691746", "endereco": "rua 2"}
])

result = conn.execute(cliente.select())
for row in result:
    print(row)
