import pandas as pd
import numpy as np

sim_mtx = np.genfromtxt(r'..\data\processed\sim_mtx.csv', delimiter=',')
movies = pd.read_csv(r'..\data\interim\clean_movies.csv')
data = pd.read_csv(r'..\data\processed\pivot_mtx.csv')

def user_ident(user):
    return sim_mtx[user]
    

def get_similar(user):
    user = user_ident(user)
    array = user[(user > 0) & (user < 0.999)]
    array= np.sort(array)[::-1]
    array = np.round(array, 2)
    return list(array)

def get_index(user):
    index_list = get_similar(user)
    indices_totales = []
    for i in index_list:        
        indices = np.where(np.isclose(sim_mtx[user], i, atol=0.01))
        indices_totales.append(indices)  
    indices_totales = np.hstack(indices_totales)
    indices_totales = indices_totales[0][0:len(indices_totales[0])]
    valores_unicos = []
    valores_set = set()

    for i in indices_totales:
        if i not in valores_set:
            valores_set.add(i)
            valores_unicos.append(i)

    return valores_unicos


def get_rows(user):
    rows = get_index(user)
    fila = data.iloc[rows]
    return fila


def get_movies(user):
    index = get_rows(user).index
    max_values=[]    
    for i in index:
        max_value = data.iloc[i].where(data.iloc[user] == 0).max()
        max_values.append(max_value)
    return max_values



def recommender(user):
    index = get_rows(user).index
    movies_values = get_movies(user)
    rows = get_rows(user)
    films = []
    for i, j in zip(index,movies_values): 
        columna_resultado = data.columns[(data.iloc[i] == j) & (data.iloc[user] == 0)]
        films.append(columna_resultado[0])
    return films

def top_5(user):
    films = recommender(user)
    unique_films = []
    for i in films:
        if i not in unique_films:
            unique_films.append(i)
    return unique_films[0:5]


if __name__=='__main__':
    recommender(45)