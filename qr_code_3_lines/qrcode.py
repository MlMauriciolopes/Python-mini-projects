# Qr Code 

import qrcode

img = qrcode.make("https://www.linkedin.com/in/mlmauriciolopes/")

img.save("myQr.jpg")