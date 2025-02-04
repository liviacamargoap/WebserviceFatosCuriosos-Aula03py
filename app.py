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
imagem_aleatoria = ["baiacu.jpg",
                    "lesma-do-mar.jpg",
                    "peixe-morcego.jpg",
                    "polvo-azuis.jpg"
]

frase_aleatoria = [ "Cada espécie marinha tem um papel único que mantém o equilíbrio ecológico do nosso planeta.",
                   "Os ecossistemas marinhos ajudam a regular o clima, absorvendo grandes quantidades de carbono.",
                   "A perda de biodiversidade nos oceanos afeta diretamente as populações humanas que dependem do mar para sustento.",
                   "Os animais marinhos são fundamentais para o equilíbrio dos ecossistemas oceânicos."
]

# Aqui ira ficar todas as minhas rotas
@app.route("/inicial")
def pagina_inicial():
    cor_de_fundo = random.choice(lista_cores)
    return render_template("PaginaInicial.html", cor_de_fundo_html = cor_de_fundo)

@app.route("/")
def pagina_sobre():
    imagem_random = random.choice(imagem_aleatoria)
    cor_de_fundo = random.choice(lista_cores)
    frase_random = random.choice(frase_aleatoria)
    return render_template("PaginaSobre.html", imagem_random_html = imagem_random, cor_de_fundo_html = cor_de_fundo, frase_random_html = frase_random)

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("CadastroFrases.html", frases = frase_aleatoria)


app.run(debug=True, host="0.0.0.0", port=8080)