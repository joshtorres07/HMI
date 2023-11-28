import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=1) as holistic:
    start_time = time.time()
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = 30
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(frame_rgb)
        mp_drawing.draw_landmarks(
            frame, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
            mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(0, 128, 255), thickness=2))
        mp_drawing.draw_landmarks(
            frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))
        mp_drawing.draw_landmarks(
            frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(57, 143, 0), thickness=2))
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128, 0, 255), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

        frame = cv2.flip(frame, 1)
        cv2.imshow("Frame", frame)
        out.write(frame)
        if time.time() - start_time > 5:
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
