Santa Cards
===========

East Troy, WI has a unique and fun event every year around Christmas: Santa on the Square. One of the highlights of this event is getting your picture taken with Santa and Mrs. Claus. You use to have to wait in line. Lines suck. This script eliminates the need for a line by generating a folder full of printable images that each get stamped with a incrementing number and unique code. The number is the parties position in line and the code is used to redeem the photo on easttroy.org

![Pictures with Santa](template-2014.png)

## Requirements

* Python 3.7 or higher
* Python Image Library
* Imagemagick >= 7.0.x

## Installation

The script should be able to run as-is, but if your python environment is lacking the Python Image Library, you can install it through pip:

> pip install -r requirements.txt

If you're on OS X, Imagemagick can be installed via homebrew:

> brew install imagemagick

## Usage

``$ ./santacards.py``

A directory will be created alongside this script, filled with PNG images and a PDF file consolidating all the PNG files.

## Credits

This project is maintained by the [East Troy Computer Club](http://etcc.io/) in partnership with the [East Troy Area Chamber of Commerce](http://easttroy.org/). It's open-sourced for educational and collaborative use.
