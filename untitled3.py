import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

video = cv2.VideoCapture(0)
time.sleep(1)

while(1):
#    cv2.waitKey(20)
    ret,pic = video.read()
    if ret == True:
        pic = cv2.flip(pic, 1)
        
        faces = face_cascade.detectMultiScale(pic, 1.1, 5)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(pic, (x,y), (x+w, y+h), (200,50,50),1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(pic,'ME' ,(x,y),font, 0.5, (200,85,30),1, cv2.LINE_AA)
            
        print('Number of faces found : {}'.format(len(faces)))
        cv2.imshow('Output', pic)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        print('frame droped!')
        break
video.release()
cv2.destroyAllWindows()