from flask import Flask

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