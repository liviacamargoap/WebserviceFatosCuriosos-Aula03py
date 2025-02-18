from flask import Flask, render_template
import random 
from .data import listas_configuracao as listas
import mysql.connector

# Aqui ira ficar todas as minhas rotas
@app.route("/inicial")
def pagina_inicial():
    cor_de_fundo = random.choice(listas.lista_cores)
    return render_template("PaginaInicial.html", cor_de_fundo_html = cor_de_fundo)

@app.route("/")
def pagina_sobre():
    imagem_random = random.choice(listas.imagem_aleatoria)
    cor_de_fundo = random.choice(listas.lista_cores)
    frase_random = random.choice(listas.frase_aleatoria)
    return render_template("PaginaSobre.html", imagem_random_html = imagem_random, cor_de_fundo_html = cor_de_fundo, frase_random_html = frase_random)

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("CadastroFrases.html", frases = listas.frase_aleatoria)



# @app.route("cores/delete/<indice_cor>")
# def delete_cores(indice_cor):
#     lista_cores.pop(indice_cor)
#     return redirect ("/cores")


app.run(debug=True, host="0.0.0.0", port=8080)