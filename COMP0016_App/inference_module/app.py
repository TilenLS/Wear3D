import numpy as np
from flask import Flask, request
from werkzeug.utils import secure_filename
from main import getPrediction
import os


UPLOAD_FOLDER = 'teeth/'

# Create an app object using the Flask class
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# predict
@app.route('/predict', methods=['POST'])
def submit_file():
    data = request.get_json()
    result = {}
    if request.method == 'POST':
        if 'file' not in data:
            result =  {'result': 'No file part'}
        file = data['file']
        if file == '':
            result =  {'result': 'No file selected for uploading'}
        if file:
            # Use werkzeug method to secure filename
            filename = secure_filename(file)   
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            label = getPrediction(filename)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result =  {'result': 'Your tooth wear grade is: {}'.format(label)}
    return result


if __name__ == "__main__":
    # Define port so we can map container port to localhost
    # port = int(os.environ.get('PORT', 5000)) 
    # app.run(host='0.0.0.0', port=port) 
    app.run()
