# copie este código no seu Power BI e lembre de mudar o caminho para seu arquivo original de csv no seu desktop

import pandas as pd
df_filmes = pd.read_csv("D:\Power BI\Projeto Filmes\IMDB-Movie-Data.csv")
df_filmes = df_filmes.dropna().reset_index()
df_filmes.drop(["index", "Rank"], axis=1, inplace=True)