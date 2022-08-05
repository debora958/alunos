import pandas as pd

dataframe = pd.read_csv("notas_alunos.csv")
medias = (dataframe["nota_1"] + dataframe["nota_2"]) / 2

dataframe["media"] = medias 

dataframe.loc[dataframe["media"] >= 7, "situacao"] = "APROVADO"
dataframe.loc[dataframe["media"] < 7, "situacao"] = "REPROVADO"
dataframe.loc[dataframe["faltas"] > 5, "situacao"] = "REPROVADO"

dataframe.to_csv("situacao_alunos.csv", index = False)

maior_numero_de_faltas = dataframe["faltas"].max()
media_geral = dataframe["media"].median()
maior_media = dataframe["media"].max()

print("Maior média: ", + (maior_media))
print("Média geral dos alunos: ", + (media_geral))
print("Maior números de faltas: ", + (maior_numero_de_faltas))

