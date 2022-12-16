from flask import Flask, abort
import pandas as pd
import os 
import numpy as np

#Iniciando o servidor
server = Flask(__name__)

path = "./dados_estado"
#Página inicial

@server.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@server.route('/<year>/<locate>', methods=['GET', 'POST'])
def index(year, locate):
    year = year.split('&')
    locate = locate.split('&')
    years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2020','2021']
    result = []
    for l in locate:
        data = pd.DataFrame()
        for y in year:
            df = pd.read_csv(path+"/"+y+"_"+l+".csv")
            data = pd.concat([data,df])
        #Análise 1
        badly = {"QT_MAT_BAS": [],
                    "QT_MAT_INF": [],
                    "QT_MAT_FUND": [],
                    "QT_MAT_MED": [],
                    "QT_MAT_PROF": [],
                    "index": []
                    }
        for loc in locate:
            aux = analysis1(data, year, loc)
            for item in badly.keys():
                badly[item].append(aux[item])

        for item in badly.keys():
            badly[item] = [np.min(badly[item]), badly["index"][np.argmin(badly[item])]]
        #Análise 2
        access = {"QT_MAT_BAS": [],
                    "QT_MAT_INF": [],
                    "QT_MAT_FUND": [],
                    "QT_MAT_MED": [],
                    "QT_MAT_PROF": [],
                    "QT_MAT_PROF_TEC": [],
                    "QT_MAT_EJA": [],
                    "QT_MAT_EJA_FUND": [],
                    "QT_MAT_EJA_MED": [],
                    "QT_MAT_ESP": [],
                    "QT_MAT_ESP_CC": [],
                    "QT_MAT_ESP_CE": []}
        
        #Análise por estado
        for loc in locate:
            aux = analysis2(data, loc, year)
            for item in access.keys():
                access[item].append(aux[item])
        
        #Encontrando o menor relativo
        aux_ind = access
        for item in aux_ind.keys():
            aux_ind[item] = list(map(lambda x: x[0], aux_ind[item]))
        df = pd.DataFrame(data=aux_ind)
        df_scaled = (df-df.min())/(df.max()-df.min())


        #(1) O estado x teve um dos seus piores indices acadêmicos no ano y
        #(2) O estado x tem pouco acesso a educação, a quantidade de escolas de acesso y no ano de z é a menor dentro os anos [years]
        #[Dicionário dos piores (1), (state, name, value, year)(2)]
        result.append([str(badly),
                    str(access), l])
    return result

def structData(diretory,year,locate):
    #estruturar os dados
    pasta = diretory
    fulldata = pd.DataFrame()
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for y in year:
            for l in locate:
                data = pd.read_csv(os.path.join(diretorio, str(y+"_"+l+".csv")))
                data = data.fillna(0)
                fulldata = pd.concat([fulldata, data], ignore_index=True)
    return fulldata

def analysis1(df, year, loc):
    #O estado x teve um dos seus piores indices acadêmicos no ano y
    aux_min = {"QT_MAT_BAS": float("inf"),
                "QT_MAT_INF": float("inf"),
                "QT_MAT_FUND": float("inf"),
                "QT_MAT_MED": float("inf"),
                "QT_MAT_PROF": float("inf"),
                "index": None
                }
    for i in year:
        filtered_df = df[df.NU_ANO_CENSO == int(i)]
        filtered_df = filtered_df[filtered_df["SG_UF"] == loc]
        min = {"QT_MAT_BAS": filtered_df["QT_MAT_BAS"].sum(),
                "QT_MAT_INF": filtered_df["QT_MAT_INF"].sum(),
                "QT_MAT_FUND": filtered_df["QT_MAT_FUND"].sum(),
                "QT_MAT_MED": filtered_df["QT_MAT_MED"].sum(),
                "QT_MAT_PROF": filtered_df["QT_MAT_PROF"].sum(),
                "index": int(i)
                }
        if (min["QT_MAT_BAS"] < aux_min["QT_MAT_BAS"]):
            if (min["QT_MAT_INF"] < aux_min["QT_MAT_INF"]):
                if (min["QT_MAT_FUND"] < aux_min["QT_MAT_FUND"]):
                    if (min["QT_MAT_MED"] < aux_min["QT_MAT_MED"]):
                        if (min["QT_MAT_PROF"] < aux_min["QT_MAT_PROF"]):
                            aux_min = min
    return aux_min

def analysis2(df, loc, year):
    #O estado y tem pouco acesso a educação, veja a quantidade de escolas de acesso y no ano de x
    aux_min = {"QT_MAT_BAS": [float("inf"), None],
                "QT_MAT_INF": [float("inf"), None],
                "QT_MAT_FUND": [float("inf"), None],
                "QT_MAT_MED": [float("inf"), None],
                "QT_MAT_PROF": [float("inf"), None],
                "QT_MAT_PROF_TEC": [float("inf"), None],
                "QT_MAT_EJA": [float("inf"), None],
                "QT_MAT_EJA_FUND": [float("inf"), None],
                "QT_MAT_EJA_MED": [float("inf"), None],
                "QT_MAT_ESP": [float("inf"), None],
                "QT_MAT_ESP_CC": [float("inf"), None],
                "QT_MAT_ESP_CE": [float("inf"), None]}
    for i in year:
        filtered_df = df[df.NU_ANO_CENSO == int(i)]
        filtered_df = filtered_df[filtered_df["SG_UF"] == loc]
        min = {"QT_MAT_BAS": filtered_df["QT_MAT_BAS"].sum(),
                "QT_MAT_INF": filtered_df["QT_MAT_INF"].sum(),
                "QT_MAT_FUND": filtered_df["QT_MAT_FUND"].sum(),
                "QT_MAT_MED": filtered_df["QT_MAT_MED"].sum(),
                "QT_MAT_PROF": filtered_df["QT_MAT_PROF"].sum(),
                "QT_MAT_PROF_TEC": filtered_df["QT_MAT_PROF_TEC"].sum(),
                "QT_MAT_EJA": filtered_df["QT_MAT_EJA"].sum(),
                "QT_MAT_EJA_FUND": filtered_df["QT_MAT_EJA_FUND"].sum(),
                "QT_MAT_EJA_MED": filtered_df["QT_MAT_EJA_MED"].sum(),
                "QT_MAT_ESP": filtered_df["QT_MAT_ESP"].sum(),
                "QT_MAT_ESP_CC": filtered_df["QT_MAT_ESP_CC"].sum(),
                "QT_MAT_ESP_CE": filtered_df["QT_MAT_ESP_CE"].sum(),
                "index": int(i)
                }
        findMin = lambda x, y: x if x < y else y
        for item in aux_min.keys():
            if aux_min[item][0] > min[item]:
                    aux_min[item] = [min[item], int(i)]
    return aux_min