import numpy as np
from flask import Flask, request
from werkzeug.utils import secure_filename
from main import get_prediction
import os
from plyfile import PlyData
import numpy as np


UPLOAD_FOLDER = 'teeth/'

# Create an app object using the Flask class
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# predict
@app.route('/predict', methods=['POST'])
def submit_file():
    result = {}
    if request.method == 'POST':
        if 'file' not in request.files:
            result =  {'result': 'No file part'}
        file = request.files['file']
        if file == '':
            result =  {'result': 'No file selected for uploading'}
        if file:
            # filename = data['filename']
            # Use werkzeug method to secure filename
            # filename = secure_filename(file)   
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            plydata = PlyData.read(file)
            label = get_prediction(plydata)
            # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result =  {'result': 'Your tooth wear grade is: {}'.format(label)}
    return result


if __name__ == "__main__":
    # Define port so we can map container port to localhost
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port) 
    # app.run()
