import numpy as np
import pandas as pd

dataset = pd.read_csv('ratingMatrix.csv',header=None)

print(dataset.shape)

userNonZero =  (dataset!=0).sum(1)

itemNonZero = (dataset[:]!=0).sum()
#print(itemNonzero)

sortUserNonZero = userNonZero.sort_values(ascending=False)
#print(sortUserNonZero)
sortItemNonZero = itemNonZero.sort_values(ascending=False)

#print(len(sortItenNonZero))
#Extract the 100-most ratted user and item
mostUserNonZero = sortUserNonZero.head(100)
mostItemNonZero = sortItemNonZero.head(100)

#print(mostUserNonZero)
print('---===========')
#print(mostItemNonZero)
print(len(mostUserNonZero))


mostUserIndex = mostUserNonZero.index
mostItemIndex = mostItemNonZero.index

denseRatingMatrix = dataset.loc[mostUserIndex, mostItemIndex]


np.savetxt('denseRatingMatrix.csv', denseRatingMatrix, delimiter = ',')
np.savetxt('mostUserIndex.csv', mostUserIndex, delimiter = ',')

np.savetxt('mostItemIndex.csv', mostItemIndex, delimiter = ',') 


