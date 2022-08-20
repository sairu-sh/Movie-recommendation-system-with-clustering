import pre_processing
from sklearn.cluster import KMeans

def Clustered_final_df(df):
    df['Cluster_Id']=None

    kmeans =KMeans(n_clusters=200)

    features =df[['P_genre','S_Genre','T_Genre']]
    kmeans.fit(features)
    df['Cluster_Id']=kmeans.predict(features)
    return df 

def cluster_everything(input_movie):
    df=pre_processing.pre_process_all()
    print(df)

    df=Clustered_final_df(df)
    print(df)

    df.to_csv('Dataset_to_plot.csv')
    input_movie=input_movie.lower()
    try:
        movie_not_found=df.loc[~df['movie'].str.constraints(input_movie)]
        if len(movie_not_found)==0:
            print("Movie not found")
            return 0
        get_cluster=df['Clustered_Id'].loc[df['Movie'].str.containts(input_movie)].values[0]
        similar_movies_list=df['Movie'].loc[df['Cluster_Id']==get_cluster].values
        return similar_movies_list

    except:
        print("Movie not found")
        return 0
            
test=cluster_everything("The Batman")
