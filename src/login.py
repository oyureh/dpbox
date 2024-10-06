
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='dpbox'
        )
        if connection.is_connected():
            print("Conectado ao banco de dados")
            return connection
    except Error as e:
        print(f"Não conectado: {e}")
        return None

def check_and_insert_user(connection, nome, gmail, senha, telefone):
    cursor = connection.cursor()

    # Verifica se o email já está cadastrado
    cursor.execute("SELECT telefone FROM login WHERE telefone = %s", (gmail,))
    if cursor.fetchone() is not None:
        print("Gmail já cadastrado!")
    else:
        # Insere o novo usuário
        cursor.execute(
            "INSERT INTO login (nome, gmail, senha, telefone) VALUES (%s, %s, %s, %s)",
            (nome, gmail, senha, telefone)
        )
        connection.commit()
        print("Usuário cadastrado!")

def main():
    connection = connect_to_database()
    if connection:
        # Exemplos de dados que você receberia via POST
        nome = "Seu Nome"
        gmail = "seu_email@gmail.com"
        senha = "sua_senha"
        telefone = "123456789"

        check_and_insert_user(connection, nome, gmail, senha, telefone)

        # Fecha a conexão
        connection.close()

if __name__ == "__main__":
    main()
