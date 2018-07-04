#!/usr/bin/env python

# Selected and copied only the relevant code for sortbot
# code from detect.py

# Example Usage:
# python sortbotv00.py labels ./resources/wakeupcat.jpg

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

    for label in labels:
        print(label.description)

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