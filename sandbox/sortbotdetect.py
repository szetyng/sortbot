#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_sortbotdetect():
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision

    # Instantiates a client
    vision_client = vision.Client()

    # The name of the image file to annotate
    # Where I eventually need to make changes, make it dynamic? 
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/plasticcup2.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    # Performs label detection on the image file
    labels = image.detect_labels()
    
    print('Labels:')
    for label in labels:
        print(label.description)
        if label.description == 'mug':
            print('recycle to paper')
        elif label.description == 'cup':
            print('recycle to paper')            
    # [END vision_quickstart]


if __name__ == '__main__':
    run_sortbotdetect()
