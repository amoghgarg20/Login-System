# Sending image to server to convert into encodings
# Importing Libraries
import base64
import numpy as np
import cv2
import mtcnn

# Function to send image to server
class Img:
    def save_image(file):
        image_b64 = file.split(",")[1]
        binary = base64.b64decode(image_b64)
        image = np.asarray(bytearray(binary), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        detector = mtcnn.MTCNN()
        # Detect the face from the photograph
        result = detector.detect_faces(image)
        if result:
            x1, y1, width, height = result[0]['box']
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            face = image[y1:y2, x1:x2]
            # a.jpg is the original photo taken by the user
            IMG_PATH = 'uploads/user_signup/a.jpg' 
            cv2.imwrite(IMG_PATH, image)
            # f.jpg contains only the face of the user and is extracted from a.jpg
            # f.jpg is encoded
            IMG_PATH = 'uploads/user_signup/f.jpg' 
            status = cv2.imwrite(IMG_PATH, face)   
            if status:
                return True
            return False   
        else:
            return False    
        
        
        