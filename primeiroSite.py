from flask import Flask

app = Flask(__name__)
#route -> saolourencodaserradoacoes.com/contatos
#função -> o qn  mcmcmue você quer exibir naquela página

@app.route("/")
def homepage():
    return "Vamos pra cima"

@app.route("/contatos")
def contatos():
    return "Nossos contatos são: E-mail: trabalhounivesp@gmail.com Telefone(11)99999-9999"

@app.route("/crianca")
def infantil():
    return "AQUI AS CRIANÇAS BRINCAM E SE DIVERTEM"
#colocar o site no ar

if __name__=="__main__":
    app.run(debug=True)
