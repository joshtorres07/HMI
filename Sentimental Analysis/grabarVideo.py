import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Se define el codec y se crea el objeto VideoWriter para poder grabar el video capturado
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.VideoCapture(frame,0)   #invierte la imagen
        # graba el frame pero volteado o de forma inversa (de cabeza)
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
