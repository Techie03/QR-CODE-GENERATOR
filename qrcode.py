import pyqrcode
import png
from pyqrcode import QRCode
s = "techie03.hashnode.dev"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)
