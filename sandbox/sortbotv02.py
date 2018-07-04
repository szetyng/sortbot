#!/usr/bin/env python

# Selected only the relevant code for sortbot
# Adding stuff to make it sortbot
# code from quickstart.py

# Example Usage:
# python sortbotv02.py

# input = imgnr

def sortbotv002():
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision

    # Instantiates a client
    vision_client = vision.Client()

    # Path to image file
    imgnr = 1
    imgnr_s = str(imgnr)
    inputimg = "resources/input" + imgnr_s + ".jpg"

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        inputimg)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    # Performs label detection on the image file
    labels = image.detect_labels()

    recycle = "unsorted"
    category = 0

    print('Labels:')
    for label in labels:
        print(("%s %c %s") % (label.description, ':', label.score))
        if "paper" in label.description:
            recycle = "paper"
            break
        elif "plastic" in label.description:
            recycle = "plastic"
            break
        elif "can" in label.description:
            recycle = "can"
            break

        elif "coffee" in label.description:
            recycle = "paper"
            break
        elif "bottle" in label.description:
            recycle = "plastic"
            break

    if recycle != "unsorted":
        print("\nIt belongs in", recycle)

    if recycle == "paper":
        category = 1
    elif recycle == "plastic":
        category = 2
    elif recycle == "can":
        category = 3
   

if __name__ == '__main__':
    sortbotv002()
