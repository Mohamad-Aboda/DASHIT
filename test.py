import pandas as pd
import pickle

r = pd.read_csv('t2.csv')
print(r)
model = pickle.load(open('Model.pkl', 'rb'))

p = model.predict(r)
print(p)
print('done')