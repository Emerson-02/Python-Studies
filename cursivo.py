import pywhatkit as kit
import cv2
kit.text_to_handwriting("Emerson do Nascimento Rodrigues", save_to="cursivo.png")

img = cv2.imread("cursivo.png")
cv2.imshow("Texto", img)

cv2.waitKey(0)
cv2.destroyAllWindowns()