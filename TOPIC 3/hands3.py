# Detecta dos manos
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(static_image_mode=True,
                    max_num_hands=2,
                    min_detection_confidence=0.5) as hands:
    image = cv2.imread("manos2.jpg")
    h, w, _ = image.shape
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
print("Hand landmarks:", results.multi_hand_landmarks)
if results.multi_hand_landmarks is not None:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=4, circle_radius=5),
            mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4))
    image = cv2.flip(image, 1)

    width = 400
    height = 400
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("imagen", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()




