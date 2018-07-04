# SortBot
This repository only contains the code for the prototype of the image recognition part of [SortBot](http://www.ee.ic.ac.uk/guo.liew15/yr2proj/default.htm), where the aim is to categorise images of recyclables commonly found on the Imperial College Campus into `paper`, `plastic`, `can` or `uncategorised`.

## Development
Assuming that you have a Google Cloud Developer account with proper authorizations.
1. Install the Google Cloud Vision library by running the following command:  
`pip install --upgrade google-cloud-vision`

2. Install the requirements for the project by running `pip install -r requirements.txt`

3. Run the following code in the Google Cloud SDK:  
`gcloud beta auth application-default login`

1. Run the script `sortbot.py` in the Google Cloud SDK. Images used in testing are to be stored in the `resources\` folder and named as `inputx.jpg`, where `x` is an integer and the answer required by the script when prompted for the image,  