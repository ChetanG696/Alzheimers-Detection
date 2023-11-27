import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the model without compiling
model = load_model("Xception_model_image.h5", compile=False)

# Ensure the 'uploads' directory exists
uploads_dir = os.path.join(os.path.dirname(__file__), 'MyProject', 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index3.html')
def index3():
    return render_template('index3.html')

@app.route('/Newform.html')
def Newform():
    return render_template('Newform.html')

@app.route('/predictionpage', methods=['POST'])
def predictionpage():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        
        filepath = os.path.join(uploads_dir, f.filename)
        print("upload folder is ", filepath)
        
        f.save(filepath)
        
        # Set the correct target size for the Xception model
        img = image.load_img(filepath, target_size=(299, 299))
        x = image.img_to_array(img) / 255.0  # Scale the pixel values
        x = np.expand_dims(x, axis=0)
        
        y = model.predict(x)
        preds = np.argmax(y, axis=1)
        
        index = ['Mild Impairment', 'Moderate Impairment', 'No Impairment', 'Very Mild Impairment']
        text = "The classified Animal is: " + str(index[preds[0]])
        
        return render_template("predictpage.html",data=preds)

if __name__ == '__main__':
    app.run(debug=False, threaded=False)
