arr = np.arange(24)

arr.reshape(6, 4) #valid
arr.reshape(2, 12) #valid
arr.reshape(3, 8) #valid
arr.reshape(4, 7) #invalid
arr.reshape(2, 3, 4) #valid
arr.reshape(24, 1) #valid
arr.reshape(1, 24) #valid 
