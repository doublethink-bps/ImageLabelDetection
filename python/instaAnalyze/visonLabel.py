import io
import json

def visonImageLabelDetection(image_path):
    # Imports the Google Cloud client library
    from google.cloud import vision

    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # Loads the image into memory
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Performs label detection on the image file
    
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels