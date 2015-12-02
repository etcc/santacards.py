#!/usr/bin/env python
#
# santacards.py - creates printable cards, each with their own unique code.
# 
# East Troy, WI has a unique and fun event every year around Christmas: Santa on
# the Square. One of the highlights of this event is getting your picture taken
# with Santa and Mrs. Claus. You use to have to wait in line. Lines suck. The 
# script below eliminates the need for a line by generating a folder full of
# printable images that each get stamped with a incrementing number and unique
# code. The number is the persons position in line and the code is for folks to
# punch into easttroy.org to redeem their photo.
#
# USAGE: $ python santacards.py

import os
import random
import string
import subprocess
import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Create the output folder if it doesn't already exists
if not os.path.exists('cards'):
    os.makedirs('cards')

# Create an empty list for use further down
codes = []
 
# In 2014 there were 101 cards used. So 200 cards should be plenty.
for i in range(1, 201):
 
    # Grab a list of characters to use in our code generator
    char_pool = string.ascii_uppercase + string.digits
 
    # Generate a random code
    r = ''.join([random.choice(char_pool) for n in xrange(5)])
 
    # Check generated code against pre-existing codes.
    if r not in codes:
        codes.append(r)

        # Open template image and draw on it
        img = Image.open("template-2015.png")
        draw = ImageDraw.Draw(img)  
        font = ImageFont.truetype("Inconsolata.otf", 82)

        # Draw the text to the image. X,Y cords are in pixels
        draw.text((1100, 515), str(i), font=font, fill=(249,237,40))
        draw.text((1195, 780), str(r), font=font, fill=(249,237,40))

        # Create a QR Code pointing to the picture code URL
        qr = qrcode.QRCode(version=1, box_size=6, border=2)
        qr.add_data('https://easttroy.org/santa/%s' % r)
        qr.make(fit=True)

        # Make and paste the QR Code into the Santa Card
        qr_img = qr.make_image()
        img.paste(qr_img, (360,760))

        # Save image to filesystem
        img.save('./cards/%02d%s.png' % (i, r))
 
        print "Created card for #%s, Code: %s" % (i, r)

print "Merging all cards into a single PDF..."

subprocess.call('convert ./cards/* santacards-printable.pdf', shell=True)
