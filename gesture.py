import cv2
import mediapipe as mp

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (800, 600))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS
        )

        landmarks = results.right_hand_landmarks.landmark
        # Define roots of the fingers (using MCP joints as an approximation)
        finger_roots = [
            landmarks[mp_holistic.HandLandmark.THUMB_CMC],  # Base of the thumb might be considered the CMC
            landmarks[mp_holistic.HandLandmark.INDEX_FINGER_MCP],
            landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_MCP],
            landmarks[mp_holistic.HandLandmark.RING_FINGER_MCP],
            landmarks[mp_holistic.HandLandmark.PINKY_MCP]
        ]

        # Define tips of the fingers
        finger_tips = [
            landmarks[mp_holistic.HandLandmark.THUMB_TIP],
            landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP],
            landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP],
            landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP],
            landmarks[mp_holistic.HandLandmark.PINKY_TIP]
        ]

        # Check if all fingertips are higher (lower Y value) than their corresponding roots
        hand_open = all(tip.y < root.y for tip, root in zip(finger_tips, finger_roots))

        if hand_open:
            with open('hand_detection_result.txt', 'w') as f:
                f.write('jump\n')
            print('Jumping!')
        else:
            with open('hand_detection_result.txt', 'w') as f:
                f.write('no_jump\n')
            #print('not ok')
    else:
        with open('hand_detection_result.txt', 'w') as f:
            f.write('no_jump\n')
        #print('not ok')

    cv2.imshow("Hand Detection", image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
