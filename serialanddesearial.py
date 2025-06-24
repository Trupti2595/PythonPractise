import pickle

data1 = {'name':'Trupti', 'place':'India'}

with open('data1.pkl', 'wb') as file1:
    pickle.dump(data1, file1)

with open('data1.pkl', 'rb') as file1:
    loaded_data = pickle.load(file1)
print(loaded_data)