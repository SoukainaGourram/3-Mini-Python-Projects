import qrcode
from PIL import Image

data = 'stay tuned'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=11,
    border=5,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')

# Convert the image to RGBA mode to support colors
img = img.convert('RGBA')

# Create a transparent overlay with the desired fill color
overlay = Image.new('RGBA', img.size, (255, 0, 0, 128))

# Composite the QR code with the overlay to apply the fill color
img = Image.alpha_composite(img, overlay)

img.save('myqrcode.png')
