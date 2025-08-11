import os
import sys
from flask import Flask, render_template, send_from_directory

# Add the parent directory of src to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                os.pardir)))

from src.routes.detection import detection_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'), template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

app.register_blueprint(detection_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


