#usr/bin/python3.9
import cv2
import numpy as np

class PIL2CV:
    def pil_to_cv(pil_image):
        cv_image = np.array(pil_image, dtype=np.uint8)
        if cv_image.ndim == 2:
            pass
        elif cv_image.shape[2] == 3:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
        elif cv_image.shape[2] == 4:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGBA2BGRA)
        return cv_image
