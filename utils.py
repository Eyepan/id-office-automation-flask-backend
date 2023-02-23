import cv2
import os
import pyqrcode


cam = cv2.VideoCapture(0)
c = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
count = 0

nameID = str(input("Enter your Name: ")).lower().replace(" ", "-")
path = 'C:/Users/-NK-/Pictures/Facial recognistion imgs/'+nameID
isExist = os.path.exists(path)

if isExist:
    print("Name is already Taken")
    nameID = str(input("Enter your name again"))

else:
    os.makedirs(path)


while True:
    ret, frame = cam.read()
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = c.detectMultiScale(g, 1.5, 5)

    for x, y, w, h in faces:
        count += 1
        name = 'C:/Users/-NK-/Pictures/Facial recognistion imgs/' + \
            nameID+'/'+str(count)+'.jpg'
        print("creating images : ", name)
        cv2.imwrite(name, frame[y:y+h, x:x+w])

    cv2.imshow("Video Cam", frame)
    if (count > 5):
        break


s = nameID
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
url.png('C:/Users/-NK-/Pictures/QRcodes/'+nameID+'.png', scale=6)
cam.release()
