from mtcnn.mtcnn import MTCNN
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation


class PassportPhoto:
    # Cropping function
    def detect_image(self, image, faces):
        for face in faces:
            x, y, w, h = face['box']
            image = image[30: y + int(h + h * 0.5),
                          x - int(w * .45):x + (w + int(w * 0.45))]
            cv2.imwrite(output, image)

    # Background removal function
    def paintBcg(self, path):
        # BG_COLOR = (255, 100, 10)  # light blue
        BG_COLOR = (0, 255, 255)
        MASK_COLOR = (255, 255, 255)

        with mp_selfie_segmentation.SelfieSegmentation(
                model_selection=0) as selfie_segmentation:
            image = cv2.imread(path)
            image = cv2.GaussianBlur(image, (3, 3), 0)
            img_height, img_width, _ = image.shape
            # img = cv2.resize(
            #     image, (img_width - 500, img_height - 700), cv2.INTER_AREA)

            # cv2.imshow('Image', img)
            results = selfie_segmentation.process(
                cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # Draw selfie segmentation on the background image.
            # To improve segmentation around boundaries, consider applying a joint
            # bilateral filter to "results.segmentation_mask" with "image".
            condition = np.stack(
                (results.segmentation_mask, ) * 3, axis=-1) > 0.73
            fg_image = np.zeros(image.shape, dtype=np.uint8)
            fg_image[:] = MASK_COLOR
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
            output_image = np.where(condition, image, bg_image)
            final_img = cv2.GaussianBlur(output_image, (5, 5), 0)
            cv2.imwrite('./Images/final_image.png', final_img)


if __name__ == '__main__':
    filepath = './Images/man.png'
    output = './Images/mantwo_cropped.jpg'
    #
    image = cv2.imread(filepath)
    detector = MTCNN()
    faces = detector.detect_faces(image)

    passport = PassportPhoto()
    passport.detect_image(image, faces)
    passport.paintBcg(output)
