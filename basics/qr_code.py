#Used to create Quick Response Codes
#Just pass Link, Text
#Scan and verifiy
#Image will be saved in the directory

#For more, read docs

import qrcode
img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")