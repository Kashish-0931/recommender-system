import streamlit as st
import pickle 
import pandas as pd




def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    similarity_scores=list(enumerate(distances))
    similarity_scores=sorted(similarity_scores,key=lambda x:x[1],reverse=True)
    top_5=similarity_scores[1:6]
    
    recommended_movies=[]
  
    for i in top_5:
        movie_id=i[0]
        
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetching poster From an API


        
    return recommended_movies    


movies_dict=pickle.load((open('movies_dict.pkl','rb')))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load((open('similarity.pkl','rb')))

st.title("Movie Recommender System")
option=st.selectbox("Choose a Movie",movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)

    
