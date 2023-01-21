import cv2

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the flower image
flower = cv2.imread('flower.jpg')

# Load the image with the faces
img = cv2.imread('image_with_faces.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over the detected faces and replace them with the flower image
for (x, y, w, h) in faces:
    flower_resized = cv2.resize(flower, (w, h))
    img[y:y+h, x:x+w] = flower_resized

# Save the output image
cv2.imwrite('output.jpg', img)
