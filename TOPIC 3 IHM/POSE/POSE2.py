import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
with mp_pose.Pose(static_image_mode=False) as pose:
    start_time = time.time()
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = 30
    out = cv2.VideoWriter('video_pose.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        if results.pose_landmarks is not None:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
        cv2.imshow("Frame", frame)
        out.write(frame)
        if time.time() - start_time > 5:
            break
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
