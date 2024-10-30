from sqlalchemy import create_engine, text

# Variáveis de conexão com o banco
host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_produtos'

# Função para conectar ao banco
def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        with engine.connect() as conexao:
            query = 'SELECT * FROM vendas'
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(f'Produto: {item[0]}, Data: {item[1]}, Categoria: {item[2]}, Local: {item[3]}, Valor: {item[4]}')
    except ImportError as e:
        print(f'Erro: {e}')

# Chama função que conecta ao banco de dados
conecta_banco()