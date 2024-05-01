# import qrcode as q
# img = q.make("THis is coded  text ")
# img.save("qr.png")


# another method with editing to qr code

import qrcode
from PIL import Image
qr = qrcode.QRCode(version= 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size=10,
        border=4,)

qr.add_data("This is my Text to be codded in QR")
qr.make(fit=True)
img= qr.make_image(fill_color='black', back_color='blue')
img.save("custm_QR.png")