# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  b_channel, g_channel, r_channel = cv2.split(frame)
  alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
  frame = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces in the image
  faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
  )

  mustache = cv2.imread('redhat.png', cv2.IMREAD_UNCHANGED)
  alpha_s = mustache[:,:,3]/255.0 # extract it
  alpha_l = 1.0 - alpha_s   # invert b/w
  (wH, wW) = mustache.shape[:2]
#  (B, G, R, A) = cv2.split(mustache)
#  B = cv2.bitwise_and(B, B, mask=A)
#  G = cv2.bitwise_and(G, G, mask=A)
#  R = cv2.bitwise_and(R, R, mask=A)
#  mustache = cv2.merge([B, G, R, A])
  # Draw a rectangle around the faces
  #
  xoffset = 50
  yoffset = - 100
  for (x, y, w, h) in faces:
    for c in range(0,3):
      try:
        frame[y + yoffset :y + wH + yoffset, x + xoffset  :x + wW + xoffset , c] =  (alpha_s * mustache[:, :, c] + alpha_l * frame[y  + yoffset :y + wH + yoffset, x + xoffset :x + wW + xoffset, c])
      except:
        continue

#      frame = cv2.addWeighted(frame,0.5,frame,1,0,frame)
  # Display the resulting frame
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
