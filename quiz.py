import json
from random import shuffle

def quizGenerator(n_perguntas=5) -> list:
    with open('perguntas.json', 'r', encoding='utf-8') as arquivo:
        perguntas = json.load(arquivo)
    shuffle(perguntas["perguntas"])
    if n_perguntas > 10:
        return perguntas["perguntas"][:10]
    else:
        return perguntas["perguntas"][:n_perguntas]


if __name__ == '__main__':
    quizGenerator()

