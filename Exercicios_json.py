import json

# Exercicio 1
"""# Considere que o arquivo “notas.txt” apresenta uma listagem com os dados dos alunos de uma turma.
# Cada linha do arquivo apresenta os dados de um aluno, no formato:
# RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4


notas = {}

with open("notas.txt", "r", encoding="utf-8") as file:

    for linha in file:
        dados = linha.split(",")

        rm = dados[0]
        nome = dados[1]
        lista_de_notas = (
        float(dados[2]),
        float(dados[3]),
        float(dados[4]),
        float(dados[5])
        )

        notas[rm] = {
            "nome": nome,
            "Notas": lista_de_notas,
        }




print(json.dumps(notas, ensure_ascii=False, indent=4))
"""
# Exercicio 2
# Considere o arquivo “foods.txt”, com três colunas, no formato abaixo, onde cada linha representa um
# indivíduo com suas respectivas informações.
# NAME,ID,FAVORITEFOOD
# Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato:

import json

foods = {}

with open("foods.txt", "r", encoding="utf-8") as files:

    for linha in files:
        dados = linha.strip().split(",")

        name = dados[0]
        id = dados[1]
        favorite_food = dados[2]

        foods[name] = {
            "id": id,
            "favorite_food": favorite_food
        }

print(json.dumps(foods, ensure_ascii=False, indent=4))

