from npy_append_array import NpyAppendArray
import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2],[3,4],[5,6]])

filename='out.npy'

# line may be removed, still works correctly if filename does not exist
np.save(filename, arr1)

npaa = NpyAppendArray(filename)
npaa.append(arr2)
npaa.append(arr2)
npaa.append(arr2)

data = np.load(filename, mmap_mode="r")

print(data)