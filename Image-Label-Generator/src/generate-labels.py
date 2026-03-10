# This script uses AWS Rekognition to detect labels in an image stored in Amazon S3.
# It prints the detected labels and their confidence scores, then displays the image
# with bounding boxes drawn around detected objects.
#
# To use this script:
# 1) Make sure your AWS credentials are configured (e.g., via ~/.aws/credentials or environment variables).
# 2) Update the `image` and `bucket` variables in the main() function below to point to your
#    desired S3 bucket and image file name.
# 3) Run the script with Python (e.g., `python images.py`).

import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(image, bucket):
    #create a rekognition client
    client = boto3.client('rekognition')

    #Detect labels in the photo
    response = client.detect_labels(
        Image={
            'S3Object': {'Bucket': bucket,'Name': image }},
        MaxLabels=10,
    )

    #print the detected labels
    print('Detected labels in ' + image)
    print()
    for label in response['Labels']:
        print("Label:", label['Name'])
        print("Confidence:", label['Confidence'])
        print()

    #load the image from S3
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, image)
    img_data = obj.get()['Body'].read()
    img = Image.open(BytesIO(img_data))

    #Display the image with bounding boxes
    plt.imshow(img)
    ax = plt.gca()
    for Label in response['Labels']:
        for instance in Label['Instances']:
            box = instance['BoundingBox']
            left = img.width * box['Left']
            top = img.height * box['Top']
            width = img.width * box['Width']
            height = img.height * box['Height']
            rect = patches.Rectangle((left, top), width, height, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            label_text = Label['Name'] + ' (' + str(round(instance['Confidence'], 2)) + '%)'
            plt.text(left, top - 2, label_text, color='r', fontsize = 8, bbox = dict(facecolor='white', alpha=0.7))
    plt.show()

    return len(response['Labels'])

def main():
    # ==== CONFIGURE THESE VALUES ==== #
    # Replace with the name of the image file in your S3 bucket.
    image = 'image_name.jpg'
    # Replace with your S3 bucket name where the image is stored.
    bucket = 'S3_Bucket_Name'

    label_count = detect_labels(image, bucket)
    print("Labels detected:", label_count)

if __name__ == "__main__":
    main()
