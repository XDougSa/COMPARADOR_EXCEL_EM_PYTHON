#COMPARADOR_EXCEL

import pandas as pd

#sheet_name = 'plan1' (Serve para definir )

df = pd.read_excel('Teste2.xlsx', skiprows=28)

df2 = pd.read_excel('Teste2.xlsx', skiprows=28)

coluna1 = df['Nomes1']  
coluna2 = df2['Nomes2']

nome_coluna_1 = df.columns[1]
nome_coluna_2 = df2.columns[5]

if f"{nome_coluna_1}" in df.columns and f"{nome_coluna_2}" in df2.columns:

  existem_em_df1 = coluna1.isin(coluna2)
  existem_em_df2 = coluna2.isin(coluna1)

  nao_existem_em_df1 = ~existem_em_df1
  nao_existem_em_df2 = ~existem_em_df2

  df1 = coluna1[existem_em_df1].dropna()
  df2 = coluna2[existem_em_df2].dropna()

  df1_ = coluna1[nao_existem_em_df1].dropna()
  df2_ = coluna2[nao_existem_em_df2].dropna()

  print("\nCOMPARAÇÕES:\n\n")

  print(f"\nValores da coluna {nome_coluna_2} presentes na coluna {nome_coluna_1}:\n\n", df1)
  print(f"\nValores da coluna {nome_coluna_1} presentes na coluna {nome_coluna_2}:\n\n", df2)
  print(f"\nValores da coluna {nome_coluna_2} não presentes na coluna {nome_coluna_1}:\n\n", df2_)
  print(f"\nValores da coluna {nome_coluna_1} não presentes na coluna {nome_coluna_2}:\n\n", df1_)
  
else:
  
  print("\nErro: A(s) coluna(s) do seu dataframe não foram encontradas")





