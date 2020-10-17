# ShapeIdentifier

## Description
Uses OpenCV for image recognition to identify and count the number of black circles, lines, squares, and triangles on a white background using the users webcam. Reduces noise and smoothes image through Gaussian blurring, detects and outlines edges, and detects the objects using contour identification.

Was developed for one of the MATE 2019 sub-problems and to better understand contour identification 

## Installation

Use python3.8~ ✔

`$ cd ShapeIdentifier`

### Option 1:

Install [pip](https://pip.pypa.io/en/stable/installing/) ✔

`$ pip install -r requirements.txt`

### Option 2:

Install [pipenv](https://github.com/pypa/pipenv) ✔

`$ pipenv shell`

`$ pipenv install`

## Running the App

- Make sure you have a webcam and the program has access to it

- `$ python app.py`

- To close app press `q`

## Example

<img src="./src/images/ShapeIdentifier.png">
