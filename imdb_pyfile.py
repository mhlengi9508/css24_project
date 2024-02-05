# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 04:44:00 2024

@author: 0154505
"""

import pandas as pd
from ydata_profiling import ProfileReport

file = pd.read_csv('movie_dataset.csv')

# Data reading and infomation

print(file)

print(file.info())

print(file.describe())


# Data cleaning

df = pd.DataFrame(file)

mean_rev = df['Revenue (Millions)'].mean()

df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(mean_rev)

df.dropna(subset = ['Metascore'], inplace= True)


# Q1 Highest rated movie

max_rated_movie = df.loc[df['Rating'].idxmax()]['Title']


# Q2 average revenue

rev = df['Revenue (Millions)'].sum()/len(df['Revenue (Millions)'])


# Q3 Revenue for 2015 to 2017

f_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

rev2 = f_df['Revenue (Millions)'].sum()/len(df['Revenue (Millions)'])


# Q4 Movies released in 2016

f2_df = df[df['Year'] == 2016]


# Q5 Movies directed by Christopher Nolan

df4 = df[df['Director'] == 'Christopher Nolan']


# Q6 Rating of at least 8

df3 = df[df['Rating'] >= 8]


# Q7 median rating of movies by Christopher Nolan

med_rating = df4['Rating'].median()


# Q8 Year with highest average rating

movies_yr = df.groupby('Year')['Title'].count()


# Q9 Highest average rating

max_yr = df.loc[df['Rating'].idxmax()]['Year']


# Q10 Percentage increase between 2006 and 2016 

perc_incr = movies_yr.pct_change() * 100

perc_incr = perc_incr.dropna()


# Q11 common actor

actors = df['Actors'].str.split(',').explode()

actor_count = actors.value_counts()


# Q12 unique genres

genr = df['Genre'].str.split(',').explode()

genr_count = genr.value_counts()


# Q13 correlation of numerical features

profile = ProfileReport(df, title = 'Data Profile')

profile.to_file('IMDB profile.html')



















