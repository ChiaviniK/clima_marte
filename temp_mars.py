# para ler o nosso data set vamos usar pandas
import pandas as pd
#pip install pandas

# para ler o csv
df_marte_clima = pd.read_csv('mod1-stat-descr/mars-weather.csv')
# df_nome_da_variavel = pd.read_csv('caminho do arquivo')
print(df_marte_clima)

#para exibir todos os valores de uma coluna sem repetições
print(df_marte_clima['month'].unique())

df_marte_min_temp = df_marte_clima['min_temp']
df_marte_max_temp = df_marte_clima['max_temp']

# calculando médias
media_max_temp = df_marte_max_temp.mean()
print("a média de temperaturas maximas foi de:",media_max_temp)

media_min_temp = df_marte_min_temp.mean()
print("a média de temperaturas minimo foi de:",media_min_temp)

df_mediana_max_temp = df_marte_clima['max_temp']
mediana_max_temp = df_mediana_max_temp.median()
print(mediana_max_temp)

moda_max_temp = df_marte_max_temp.mode()
print('moda:', moda_max_temp)

# fazer medidas com condições
# criar um frame só com a condição que eu preciso
dados_mes_6 = df_marte_clima[df_marte_clima['month'] == 'Month 6']
print(dados_mes_6)

temp_max_6 = dados_mes_6['max_temp']
media_max_6 = temp_max_6.mean()
print("média da temperatura maxima no mes 6",media_max_6)