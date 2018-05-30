import numpy as np
import pandas as pd

dataset = pd.read_csv('ratings.dat', sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'],header=None)

print(dataset.shape)


n_users = dataset.user_id.unique().shape[0]
n_movies = 3952   #This is because the items are 3952 However there are 3706 unique items

#n_movies = dataset.movie_id.unique().shape[0]
print('How many users and items: ')
print(n_users)
print(n_movies)

dataset = pd.DataFrame(dataset)

ratingMatrix = np.zeros((n_users, n_movies))
count=0
for line in dataset.itertuples():
	count+=1

	print(line)
	if count>5:
		break


for line in dataset.itertuples():
    ratingMatrix[line[1]-1, line[2]-1] = int(line[3])
np.savetxt('ratingMatrix.csv', ratingMatrix, delimiter = ',') 