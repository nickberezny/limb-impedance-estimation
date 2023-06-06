from tensorflow import keras
import time
import pandas as pd

new_model = keras.models.load_model('../src_c/model')

new_row = ({'bedrooms':[3],'bathrooms':[1.5],'sqft_living':[10000],'floors':[2],'waterfront':[0],'view':[0],'condition':[1],'sqft_lot':[20000],'yr_built':[1979],'yr_renovated':[1999]})


df2 = pd.DataFrame(new_row)
print(df2.head())
start_time = time.time()
y_predict = model.predict(df2)
print("--- %s seconds ---" % (time.time() - start_time))
print(y_predict)

new_row = ({'bedrooms':[2],'bathrooms':[1.0],'sqft_living':[20000],'floors':[3],'waterfront':[0],'view':[0],'condition':[1],'sqft_lot':[20000],'yr_built':[1979],'yr_renovated':[1999]})
start_time = time.time()
y_predict = model.predict(df2)
print("--- %s seconds ---" % (time.time() - start_time))
print(y_predict)