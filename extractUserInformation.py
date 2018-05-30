import numpy as np
import pandas as pd

#dataset = pd.read_csv('users.dat',header=None)

dataset = pd.read_csv('users.dat', sep='::', names=['user_id', 'gender', 'age', 'occupation'],header=None)
denseUserId = pd.read_csv('mostUserIndex.csv',names=['user_id'],header=None)
print(dataset.shape)
print(denseUserId.shape)
#print(denseUserId.user_id)
#print(denseUserId)
denseUserInfo = dataset.loc[denseUserId.user_id, :]
#print(denseUserInfo)
#np.savetxt('denseUserInfo.csv', denseUserInfo.content, delimiter = ',') 
denseUserInfo.to_csv('denseUserInfowithIndex.csv',header=False)





