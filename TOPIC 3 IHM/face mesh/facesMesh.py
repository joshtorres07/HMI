import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

index_list = [70, 63, 105, 66, 107, 336, 296, 334, 293, 300,
              122, 196, 3, 51, 281, 248, 419, 351, 37, 0, 267]

with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=3,
        min_detection_confidence=0.5) as face_mesh:
    image = cv2.imread("face1.jpg")
    height, width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)

    print("Face landmarks: ", results.multi_face_landmarks)

    if results.multi_face_landmarks is not None:
        for face_landmarks in results.multi_face_landmarks:
            for index in index_list:
                x = int(face_landmarks.landmark[index].x * width)
                y = int(face_landmarks.landmark[index].y * height)
                cv2.circle(image, (x, y), 2, (255, 0, 255), 25)


    scale_percent = 50
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow("Image", resized_image)
    cv2.waitKey(0)
cv2.destroyAllWindows()