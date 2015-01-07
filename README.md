Santa Cards
===========

![Pictures with Santa](http://static.easttroy.org.s3.amazonaws.com/pictures_w_santa_2014_cover_art.jpg?)

East Troy, WI has a unique and fun event every year around Christmas: Santa on the Square. One of the highlights of this event is getting your picture taken with Santa and Mrs. Claus. You use to have to wait in line. Lines suck. This script eliminates the need for a line by generating a folder full of printable images that each get stamped with a incrementing number and unique code. The number is the persons position in line and the code is used to redeem the photo on easttroy.org

## Requirements

* Python 2.7 or higher
* Imagemagick
* Python Image Library

## Installation

The script should be able to run as-is, but if you're python environment is lacking the Python Image Library, you can install it through pip:

> pip install -r requirements.txt

## Usage

``$ python santacards.py``

A directory will be created alongside this script, filled with PNG images and a PDF file consolidating all the PNG files.

## Credits

This project is maintained by the [East Troy Computer Club](http://etcc.io/) in partnership with the [East Troy Area Chamber of Commerce](http://easttroy.org/). It's open-sourced for educational and collaborative use.
