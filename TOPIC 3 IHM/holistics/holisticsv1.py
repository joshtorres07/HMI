import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
with mp_holistic.Holistic(
        static_image_mode=True,
        model_complexity=1) as holistic:
    image = cv2.imread("cuerpo2.jpg")
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image_rgb)

    # rostro
    mp_drawing.draw_landmarks(
        image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
        mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(0, 128, 255), thickness=2))

    # Mano izquieda (azul)
    mp_drawing.draw_landmarks(
        image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=1),
        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))

    # Mano derecha (verde)
    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1),
        mp_drawing.DrawingSpec(color=(57, 143, 0), thickness=2))

    # Postura
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(128, 0, 255), thickness=2, circle_radius=1),
        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

    scale_percent = 50
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow("Image", resized_image)
    cv2.imwrite("Holisticsv1.jpg", resized_image)
    # Plot: puntos de referencia y conexiones en matplotlib 3D
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS)
    cv2.waitKey(0)
cv2.destroyAllWindows()
