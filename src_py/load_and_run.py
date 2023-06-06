from tensorflow import keras

new_model = keras.models.load_model('../src_c/model')
new_model.summary()