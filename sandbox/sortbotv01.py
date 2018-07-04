#!/usr/bin/env python

# Selected only the relevant code for sortbot
# Adding stuff to make it sortbot
# code from detect.py

# Example Usage:
# python sortbotv01.py labels ./resources/bottle.jpg

import argparse
import io

from google.cloud import vision

def detect_labels(path):
    """Detects labels in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    labels = image.detect_labels()
    print('Labels:')

    recycle = "unsorted"
    category = 0

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

def run_local(args):
    if args.command == 'labels':
        detect_labels(args.path)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_labels_parser = subparsers.add_parser(
        'labels', help=detect_labels.__doc__)
    detect_labels_parser.add_argument('path')

    args = parser.parse_args()

    run_local(args)