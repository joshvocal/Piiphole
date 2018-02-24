import picamera
import boto3

BUCKET = 'test-learn-josh'
COLLECTION_ID = 'friends'
PI_CAMERA_IMAGE = 'image1.jpg'

def index_faces(bucket, key, collection_id, image_id):
    rekognition = boto3.client('rekognition')
    response = rekognition.index_faces(
            Image = {
                "S3Object" : {
                    "Bucket" : bucket,
                    "Name" : key
                }
            },
            CollectionId = collection_id,
            ExternalImageId = image_id
    )

    return response['FaceRecords']


def search_faces_by_image(bucket, key, collection_id):
    rekognition = boto3.client('rekognition')
    response = rekognition.search_faces_by_image(
            Image = {
                "S3Object" : {
                    "Bucket" : bucket,
                    "Name" : key
                }
            },
            CollectionId = collection_id
    )

    return response['FaceMatches'][0]['Face']['ExternalImageId']


def capture_image(pi_camera_image):
    camera = picamera.PiCamera()
    camera.capture(pi_camera_image)
    camera.close()


def upload_image_to_s3(bucket, pi_camera_image):
    s3 = boto3.resource('s3')
    s3.Object(bucket, pi_camera_image).put(Body=open(pi_camera_image, 'rb'))
