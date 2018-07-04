#!/usr/bin/env python

# Selected only the relevant code for sortbot
# Adding stuff to make it sortbot
# Different from v02 because this prints all the labels
# code from quickstart.py

# Example Usage:
# python sortbotv03.py

# input = imgnr

def sortbot():
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from statistics import mode

    # Instantiates a client
    vision_client = vision.Client()

    # Path to image file
    imgnr = input("Which image? ")
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
        if (("paper" in label.description) and (recycle == "unsorted")):
            recycle = "paper"
            continue
        elif(("plastic" in label.description) and (recycle == "unsorted")):
            recycle = "plastic"
            continue
        elif(("can" in label.description) and (recycle == "unsorted")):
            recycle = "can"
            continue

        elif(("bottle" in label.description) and (recycle == "unsorted")):
            recycle = "plastic"
            continue

    if recycle == "paper":
        category = 1
    elif recycle == "plastic":
        category = 2
    elif recycle == "can":
        category = 3

    if recycle != "unsorted":
        print("\nIt belongs in", recycle)
   
   
# Programmer can import sortbotv03
# This code checks if sortbotv03 is being imported
# Or run in the cmd line
if __name__ == '__main__':
    sortbot()

