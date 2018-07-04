#!/usr/bin/env python

# Selected only the relevant code for sortbot
# Adding stuff to make it sortbot
# Different from v02 because this prints all the labels
# And finds mode of the labels
# code from quickstart.py

# Example Usage:
# python sortbotv04.py

# input = imgnr

def sortbot():
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from statistics import mode

    # Instantiates a client
    vision_client = vision.Client()

    # Path to image file (obtain from user in the cmd prompt)
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
    # Puts all the labels in a list
    labels = image.detect_labels()

    # Initialises variables involved in categorising the trash
    recycle_l = ["unsorted"]
    recycle = "unsorted"
    category = 0
    tried = False 
    containsFood = False

    # Prints all the labels and their probability
    # Creates a new list with all the categories it is able to sort
    print("\nLabels:")
    for label in labels:
        print(("%s %c %s") % (label.description, ':', label.score))
        if "food" in label.description:
            recycle_l.append("dangerous")
            containsFood = True
        elif "coffee" in label.description:
            recycle_l.append("dangerous")
            containsFood = True

        elif "paper" in label.description:
            recycle_l.append("paper")
            
        elif "plastic" in label.description:
            recycle_l.append("plastic")
            
        elif "can" in label.description:
            recycle_l.append("can")
            

        elif "bottle" in label.description:
            recycle_l.append("plastic")
        elif (("white" in label.description) and (label.score > 0.9)):
            recycle_l.append("paper")

    # Check if it tried categorising the item at all
    try:
        recycle = recycle_l[1]
        tried = True
    except:
        recycle = "unsorted"
        tried = False

    # Code tried categorising item
    # Find the most frequently occuring category
    if tried == True:
        recycle_l.remove("unsorted")
        recycle = mode(recycle_l)

    print("\nDetected possible categories:")
    for stuff in recycle_l:
        print(stuff)

    if recycle == "paper":
        category = 1
    elif recycle == "plastic":
        category = 2
    elif recycle == "can":
        category = 3

    # Check if it contains food
    if containsFood == True:
        recycle = "unsorted"
        category = 0

    print("\nIt belongs in", recycle)
   
   
# Programmer can import sortbotv03
# This code checks if sortbotv03 is being imported
# Or run in the cmd line
if __name__ == '__main__':
    sortbot()

