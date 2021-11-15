# pip install pyqrcode
# pip install pyzbar
# pip install pillow
# pip install qrcode[pil]
# pip install opencv-python

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Mauricio Lopes da Silva")
qr.png("myCode.png", scale = 8)

d = decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))

# pip install pyqrcode
# pip install pyzbar
# pip install pillow
# pip install qrcode[pil]
# pip install opencv-python
