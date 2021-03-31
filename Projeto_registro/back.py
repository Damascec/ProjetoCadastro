import sqlite3

# Cria e ativa a database
dbase = sqlite3.connect('employee_records.db')
c = dbase.cursor()
dbase.execute('''CREATE TABLE IF NOT EXISTS employee_records(
                 ID INT PRIMARY KEY NOT NULL,
                 NAME TEXT NOT NULL)''')

# Aplica todas as mudanças na database
dbase.commit()

# Função que escreve ID NAME dentro da database
def write(ID, NAME):
    c.execute(''' INSERT into employee_records(ID, NAME) VALUES(?, ?)''', (ID, NAME)) # Utiliza o caractere (?) para informar ao banco de dados que ali vai ser inserido um valor que ainda não foi definido
    dbase.commit()


def deletar(x):
    c.execute(''' delete FROM employee_records where NAME=?''', x)
    dbase.commit()

def read_task():
    c = dbase.cursor()
    c.execute('''SELECT NAME from employee_records''')
    data = c.fetchall() # Comando para realizar a busca do nome no banco de dados
    dbase.commit()
    return data