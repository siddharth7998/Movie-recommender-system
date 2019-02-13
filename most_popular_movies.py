# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:13:15 2019

@author: AD
"""
import pandas as pd

#user data
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('u.user', sep='|', names=u_cols,encoding='latin-1')


#ratings data
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols,encoding='latin-1')



#items data:
i_cols = ['movie_id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('u.item', sep='|', names=i_cols,encoding='latin-1')


#train and test data
#ratings_test = pd.read_csv('ua.test', sep='\t', names=r_cols, encoding='latin-1')

#import graphlab

users.head()
ratings.head()
items.head()

users.info()
ratings.info()
items.info()

#d1=pd.merge(ratings,users)
dataset= pd.merge(pd.merge(ratings,users),items)
dataset.head()


ratings_total = dataset.groupby('movie title').size()

ratings_mean= dataset.groupby('movie title')['movie title','rating'].mean()

#modify the dataframes so that we can merge the two
ratings_total = pd.DataFrame({'movie title':ratings_total.index,'total ratings': ratings_total.values})
ratings_mean['movie title'] = ratings_mean.index

final= pd.merge(ratings_mean,ratings_total).sort_values(by='total ratings', ascending=False)


final.describe()

final= final[:300].sort_values(by='rating' , ascending= False)
final.head(10)
