from picamera import PiCamera
from time import sleep
import anvil.server
from PIL import Image
import cv2 as cv
from io import BytesIO

anvil.server.connect("5N3BA5ZDGCASCSSFVNRPHJ6P-FXCF7LO2CJMG4R4W-CLIENT")

camera = PiCamera()
camera.rotation=270
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
imagen=Image.open('image.jpg')
imbio=BytesIO()
imagen.save(imbio,format='JPEG')
anvil.server.call('increase_count',anvil.BlobMedia("image/jpg",imbio.getvalue()))
