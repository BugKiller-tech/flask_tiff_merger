from flask import Flask, redirect, render_template, request
from flask.json import jsonify


app = Flask(__name__)



@app.route('/api/merge_tiffs', methods=('POST',))
def merge_tiffs():
  uploaded_files = request.files.getlist('files[]')
  print(uploaded_files)
  return jsonify({ 'status': 'SUCCESS', 'file': 'http://localhost:3000/result/123.tiff', 'base64': 'asdfasfadfadsf' })

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)
