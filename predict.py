import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("model/medicine_model.keras")

# Prediction function
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction < 0.5:
        result = "Damaged"
        confidence = (1 - prediction) * 100
    else:
        result = "Intact"
        confidence = prediction * 100

    return result, round(confidence,2)

   