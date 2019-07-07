import pandas as pd 
import numpy as np

def recommender(movie_rating):
    #Encontrando os usuários que tem filmes não vistos na base
    empty_movies = pd.DataFrame(movie_rating.set_index(['index']).transpose().isna().sum()).reset_index()
    empty_movies = empty_movies[empty_movies[0]!= 0 ]['index'].tolist()
    
    #Criando um dataframe para inserir os resultados desejados
    df_result = pd.DataFrame(columns=['Usuário de interesse','Usuário com perfil mais próximo','Filme recomendado'],index=range(len(empty_movies)))
    
    #Para cada usuário com espaços vazios na base, vamos encontrar o usuário mais próximo
    for i,user in enumerate(empty_movies):
        
        #Filtrando a base para ter apenas os usuários que viram os mesmos filmes do usuário de interesse
        filmes_vistos = movie_rating.loc[movie_rating['index'] == user].dropna(axis=1).drop(['index'],axis=1).keys().tolist()
        
        #Guardando os filmes não vistos para a parte de recomendação
        filmes_nao_vistos = list(set(movie_rating)-set(filmes_vistos))
        filmes_vistos.append('index')
        
        #Guardando os usuários que já viram os mesmos filmes do usuário de interesse
        users = movie_rating[filmes_vistos].dropna()['index'].tolist()
        
        #Transformando o dataframe em uma matriz
        dataset_values = movie_rating[filmes_vistos].dropna().drop(['index'],axis=1).values
        
        #Pegando o index do usuário com a menor distância
        min_dist_index = pd.DataFrame(np.linalg.norm(dataset_values - dataset_values[:,None], axis=-1))[users.index(user)].drop([users.index(user)],axis=0).idxmin()
        
        #Pegando o filme recomendado
        filme_recomendado = max(movie_rating[filmes_nao_vistos].loc[(movie_rating['index'] == users[min_dist_index])].drop('index',axis = 1))
        
        #Preenchendo a tabela com os resultados
        df_result.iloc[i]['Usuário de interesse'] = user
        df_result.iloc[i]['Usuário com perfil mais próximo'] = users[min_dist_index]
        df_result.iloc[i]['Filme recomendado'] = filme_recomendado
        
        del filmes_vistos,filmes_nao_vistos
            
    return(df_result)
            