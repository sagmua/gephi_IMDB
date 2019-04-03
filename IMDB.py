



# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





# Leemos el archivo mediante Pandas:
movies = pd.read_csv("movie_metadata.csv")




# Cuantas películas tenemos?
movies.shape




# Eliminamos las duplicadas:
movies = movies.drop_duplicates()
movies.shape



voted_movies = movies[movies['num_voted_users'] >= 34000]


#Ordenamos por las más votadas:
voted_movies = voted_movies.sort_values(by = "imdb_score", ascending = False)





# Nos quedamos sólo con la información deseada, en nuestro caso
# el título de la película, los actores que aparecen en ella, y la valoración:
voted_movies = voted_movies[['movie_title','actor_1_name', 'actor_2_name', 'actor_3_name', 'imdb_score']]




#Una vez llegados a este punto, tenemos que preparar el dataset para Gephi. 
#  nuestro objetivo es generar una lista de adyacencias de los actores que aparecen en películas
# para que Gephi pueda reconocerlo como grafo. Asi que creamos una lista de actores separados por semicolumnas que indiquen adyacencia:



def gephi(df):
    df = df.drop(['movie_title', 'imdb_score'], axis = 1) # drop extra columns
    df = df.replace(' ', '_', regex=True) # replace whitespace by underscore, since Gephi doesn't recognize spaces
    df = df.reset_index(drop=True) # reset indices
    return(df)


voted_movies = gephi(voted_movies)


#Por último guardamos en un fichero de salida:
voted_movies.to_csv("voted_movies.csv", sep = ";", index = False, header = False)



# Hecho, ahora vamos a Gephi