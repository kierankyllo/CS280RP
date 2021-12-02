import time
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import pandas as pd

# Defines a function to expose the raster to the API given a path and the client object 
# returns unknown or an (age, gender) tuple
def getFaceDetails(path_string, face_client):
    
    detected_faces = face_client.face.detect_with_stream(
                open(path_string, 'rb'),
                # You can use enum from FaceAttributeType, or direct string
                return_face_attributes=[
                    'age',  
                    'gender'
                ]
            )
    if not detected_faces:
        unknown = 'undetected'
        return unknown, unknown

    age = int(detected_faces[0].face_attributes.age)
    gender = str(detected_faces[0].face_attributes.gender)
    gender = gender[7:]

    return age, gender

# Define sample size
sample_size = 67228

# This key will serve all examples in this document.
KEY = "ENDPOINT KEY RECIEVED FROM Azure"

# This is the endpoint provided to you from Azure
ENDPOINT = "https://fairface.cognitiveservices.azure.com/"

# Define the path for the fairface raster data, available at https://github.com/joojs/fairface
face_file_path = 'FACE FILE ROOT PATH NOT INCLUDING /VAL'

# Create an authenticated FaceClient object
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Import the training image labels into a dataframe, file must be in root of script
df = pd.read_csv('fairface_label_train.csv', delimiter= ',', skiprows=0, nrows=sample_size, usecols=[0,1,2,3] )

# Add new labels for inference values
df['age_infer'] = ''
df['gender_infer'] = ''

# Timer start
tick = time.perf_counter()

# Iterate through the dataframe and execute inference on test images and record the results in the dataframe
for index, row in df.iterrows():
    age, gender = getFaceDetails(face_file_path+row['file'], face_client)
    #write data to df
    row['age_infer'] = age
    row['gender_infer'] = gender
    #print activity to terminal
    print(row[0], row['age_infer'], row['gender_infer'])

# Timer end
tock = time.perf_counter()

# Output results dataframe to csv
df.to_csv('results.csv')

# Report the experiment completion time
print("Completed", sample_size, f"trials in {tock - tick:0.2f} seconds")

