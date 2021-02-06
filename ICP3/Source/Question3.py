import numpy as np

#create array w/ random vals
print("\n creating a random array \n")
rand = np.random.uniform(1,20,20)
print(rand)

print("\n reshaped array")
rand = rand.reshape(4,5)
print(rand)


print("\n",np.max(rand,axis=1))

arr=np.where(rand == np.max(rand,axis=1).reshape(-1,1),0,rand)

print("\nFinal Array\n",arr)