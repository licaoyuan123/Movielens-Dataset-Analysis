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

#Because here in dataset(ratingMatrix), user index and Item index was substract 1
denseRatingMatrix = dataset.loc[mostUserIndex, mostItemIndex]
#So after selecting the dataset, add the indexes by 1
mostUserIndex = mostUserNonZero.index +1

mostItemIndex = mostItemNonZero.index + 1

np.savetxt('denseRatingMatrix.csv', denseRatingMatrix, delimiter = ',')
np.savetxt('mostUserIndex.csv', mostUserIndex, delimiter = ',')

np.savetxt('mostItemIndex.csv', mostItemIndex, delimiter = ',') 


