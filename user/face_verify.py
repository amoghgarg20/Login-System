# Face-Recognition and Matching
# Importing Libraries
import tensorflow as tf
import numpy as np
import joblib

# Loading the Keras-Facenet Model
def load_model():
    model_path = "tf_files/keras-facenet-tf23"
    model = tf.keras.models.load_model(model_path,compile=False)
    model.load_weights('tf_files/keras-facenet-h5/model.h5')
    # print("abcd",model)->To check if model has loaded properly or not
    return model

# Converting the signup-image to encoding and storing in binary file
def img_to_encoding(image_path, model,filename):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    embedding = model.predict_on_batch(x_train)
    data = embedding / np.linalg.norm(embedding, ord=2)
    # print(data)
    # print(embedding)
    # print(joblib.dump(data, 'known_encodings'))
    return joblib.dump(data, filename)

# Converting the login-image to encoding and returning the value
def login_img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    embedding = model.predict_on_batch(x_train)
    return embedding / np.linalg.norm(embedding, ord=2)

# Calculating the difference between signup-encoding and login-encoding 
def verify(login_encoding, database_encoding):
    dist = np.linalg.norm(database_encoding - login_encoding)
    # You can see the difference in the encodings in the server
    print('Difference in encodings is:',dist)
    # If difference is less than 0.7 then we consider that the two faces are of the same person
    if dist < 0.7:
        return True
    # Else the face is of different person
    else:
        return False