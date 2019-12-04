#!/usr/bin/env python

"""santacards.py - create printable cards, each with their own unique code.

USAGE: $ python santacards.py

East Troy, WI has a unique and fun event every year around Christmas: Santa on
the Square. One of the highlights of this event is getting your picture taken
with Santa and Mrs. Claus. You use to have to wait in line. Lines suck. The
script below eliminates the need for a line by generating a folder full of
printable images that each get stamped with a incrementing number and unique
code. The number is the persons position in line and the code is for folks to
punch into easttroy.org to redeem their photo.
"""

import os
import random
import string
import subprocess

import qrcode
from PIL import Image, ImageDraw, ImageFont

# Create the output folder if it doesn't already exists
if not os.path.exists('cards'):
    os.makedirs('cards')

# Create an empty list for use further down
codes = []

# In 2014 there were 101 cards used. So 200 cards should be plenty.
for i in range(1, 101):

    # Grab a list of characters to use in our code generator
    char_pool = string.ascii_uppercase + string.digits

    # Generate a random code
    r = ''.join([random.choice(char_pool) for n in range(5)])

    # Check generated code against pre-existing codes.
    if r not in codes:
        codes.append(r)

        # Open template image and draw on it
        img = Image.open("template-2019.png")
        draw = ImageDraw.Draw(img)

        # A bit of duplication here. The 2016 design required a smaller
        # font size for the code. TODO: Make this DRY
        num_font = ImageFont.truetype("Inconsolata.otf", 90)
        code_font = ImageFont.truetype("Inconsolata.otf", 62)

        # Draw the text to the image. X,Y cords are in pixels
        # This relies entirely on the graphic design of the card templte.
        draw.text((332, 125), str(i), font=num_font, fill=(249, 237, 40))
        draw.text((307, 800), str(r), font=code_font, fill=(249, 237, 40))

        # Create a QR Code pointing to the picture code URL
        qr = qrcode.QRCode(version=1, box_size=9, border=2)
        qr.add_data('https://easttroy.org/santa/%s' % r)
        qr.make(fit=True)

        # Make and paste the QR Code into the Santa Card
        qr_img = qr.make_image()
        img.paste(qr_img, (232, 472))

        # Save image to filesystem
        img.save('./cards/%02d%s.png' % (i, r))

        print("Created card for #%s, Code: %s" % (i, r))

print("Merging all cards into a single PDF...")

subprocess.call('convert ./cards/* santacards-printable.pdf', shell=True)
