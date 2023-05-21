from passlib.context import CryptContext

# deprecated t
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha:str, hash_senha:str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha
    em texto puro, informado pelo o usuario, e o hasj da senha que estara
    salvo no banco de dados durante a criação da conta.
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha:str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return CRIPTO.hash(senha)
