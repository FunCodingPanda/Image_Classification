# Image_Classification
Using Convolutional Neural Network to Detect Poisonous and Edible Mushrooms 

* My motivation came from wanting to easily identify poisonous and edible mushrooms by simply taking a picture and click enter in an application. 

## Steps to acquiring the data and then cleaning the data 
* Acquiring and Cleaning the Data 
  * Follow instructions from this github account to get the images: https://github.com/ultralytics/flickr_scraper
  * Look for outlier images such are those that are not mushrooms 
  * Resize the images using resize.py 
  * Using the command line to move the images to the poisonous and non poisonous folders from the Flickr folder
* Seperating the data 
  * Move those poisonous and non poisonous folders using the command line to the Validation, Training and Testing folder 
  * Using the training.py to automatically insert the files into the poisonous and non poisonous folders under the folders mentioned above

## How the model was created 
* Mushroom_Capstone.ipynb 
  * The references are at the bottom of the notebook

## The Report on the Captone 
* Final_Capstone_Report.pdf
  * This answers the procedure, process, results and future direction of the project. 

## Information on the data, download from here: https://drive.google.com/file/d/11-Qi9F6d94HUYKUmgdA02T7TNOLpp-gs/view?usp=sharing