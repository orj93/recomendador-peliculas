import pandas as pd
import numpy as np

sim_mtx = np.genfromtxt(r'..\data\processed\sim_mtx.csv', delimiter=',')
ratings = pd.read_csv(r'..\data\raw\ratings.csv')
movies = pd.read_csv(r'..\data\interim\clean_movies.csv')

def user_ident(user):
    try:
        return sim_mtx[user]
    except:
        return 'Inserte un número correcto'


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
    indices_totales = indices_totales[0:5]
    indices_totales = np.hstack(indices_totales)
    valores_unicos = list(np.unique(indices_totales))
    return valores_unicos



def get_rows(user):
    rows = get_index(user)
    fila = ratings.iloc[rows]
    return fila


def get_movies(user):
    rows = get_rows(user)
    id_=[]
    for i in rows['movies_id']:
        id_.append(i)
    return id_



def recommender(user):
    movies_index = get_movies(user)
    recomendacion = movies[movies['movie_id'].isin(movies_index)]
    recomendacion = recomendacion[['Film', 'Genre']]    
    return recomendacion

if __name__=='__main__':
    recommender(96)