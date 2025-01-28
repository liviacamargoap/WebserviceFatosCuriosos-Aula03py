from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de cores para alterar o fundo do site
lista_cores = ["#02074a", 
            "#171b52", 
            "#0b1061", 
            "#000345", 
            "#020aa3"]

# Lista de imagens para alterar na pag inicial
imagem_aleatoria = ["baiacu.jpeg"

]

# Aqui ira ficar todas as minhas rotas
@app.route("/")
def pagina_sobre():
    cor_de_fundo = random.choice(lista_cores)
    return render_template("PaginaSobre.html", cor_de_fundo_html = cor_de_fundo)


app.run(debug=True, host="0.0.0.0", port=8080)