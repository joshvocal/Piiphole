from flask import Flask
import camera_function as c
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ok'

@app.route('/add-face')
def add_face():
    return 'Ok'

@app.route('/upload')
def upload():
    c.upload_image_to_s3(c.BUCKET, c.PI_CAMERA_IMAGE)
    return 'Ok'

@app.route('/search-face')
def search_face():
    print(c.search_faces_by_image(c.BUCKET, c.PI_CAMERA_IMAGE, c.COLLECTION_ID))
    return c.search_faces_by_image(c.BUCKET, c.PI_CAMERA_IMAGE, c.COLLECTION_ID)

@app.route('/take-picture')
def take_picture():
    c.capture_image(c.PI_CAMERA_IMAGE)
    return 'Ok'

if __name__ == "__main__":
    subprocess.call(['./localtunnel.sh &'], shell=True)
    app.run(port=5000)
