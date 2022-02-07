from PyQt5 import uic, QtWidgets
import mysql.connector

banco= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "gustavo1324",
    database= "tabela_registro"

)


def entrar_sistema():
    teladelogin.incorreta.setText("")
    login = teladelogin.login.text()
    senha = teladelogin.senha.text()
    sql= "select senha from usuarios where login = '{}'".format(login)
    conexao= banco.cursor()
    conexao.execute(sql)
    senha_banco= conexao.fetchall()

    if senha == senha_banco[0][0]:
        formulario.show()
        teladelogin.close()
        login.setText('')
        senha.setText('')

    else:
        teladelogin.incorreta.setText("LOGIN ou SENHA incorretos!")



def ir_para_cadastro():
    teladecadastro.show()
    teladelogin.close()

def enviar_db():
    teladecadastro.label_2.setText("")
    nome = teladecadastro.nome.text()
    login = teladecadastro.login.text()
    senha = teladecadastro.senha.text()

    if nome== "" or login== "" or senha== ("") :
        teladecadastro.label_2.setText("NOME, LOGIN ou SENHA não preenchidos!")

    else:
        cursor= banco.cursor()
        sql= 'insert into usuarios (nome, login, senha) values (%s, %s,%s)'
        colunas= (str(nome), str(login), str(senha))
        cursor.execute(sql, colunas)
        banco.commit()

        teladecadastro.label_3.setText("DADOS CADASTRADOS COM SUCESSO!")

        teladecadastro.close()
        teladelogin.show()

app = QtWidgets . QApplication([])
teladelogin = uic.loadUi("teladelogin.ui")
teladecadastro = uic.loadUi("teladecadastro.ui")
formulario = uic.loadUi("formulario.ui")
teladelogin.entrar.clicked.connect(entrar_sistema)
teladelogin.cadastrar.clicked.connect(ir_para_cadastro)
teladecadastro.banco.clicked.connect(enviar_db)
teladelogin.senha.setEchoMode(QtWidgets.QLineEdit.Password)
teladelogin.show()
app.exec()
