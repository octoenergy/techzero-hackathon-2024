from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(success=False, error='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(success=False, error='No selected file')
    
    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return jsonify(success=True)
    else:
        return jsonify(success=False, error='File upload failed')

if __name__ == '__main__':
    app.run(debug=True, port=5000)