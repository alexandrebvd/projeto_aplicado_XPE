import json
from random import shuffle

def quizGenerator() -> list:
    with open('perguntas.json', 'r', encoding='utf-8') as arquivo:
        perguntas = json.load(arquivo)
    
    shuffle(perguntas["perguntas"])

    # print(perguntas["perguntas"][:5])
    return perguntas["perguntas"][:5]


if __name__ == '__main__':
    quizGenerator()

