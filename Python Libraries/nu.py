import numpy as np
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array.ndim)
print(array.shape)
#-------------------#

#-------------------#
aray = np.array([[['A', 'B', 'C'],['D', 'E','F'],['G', 'H','I']]
                ,[['J', 'K', 'L'], ['M','N','O'],['P', 'Q', 'R']]
                ,[['S', 'T', 'U'], ['V','W','X'],['Y', 'Z','']]])
word = aray[0, 0, 0]+aray[2, 0, 0]+aray[2, 0, 0]
print(word)
print(aray)
print(aray.ndim)
print(aray.shape)