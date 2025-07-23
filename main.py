import cv2
import numpy as np
import mediapipe as mp
from keyboard_utils import draw_keyboard, key_positions, get_pressed_key

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

text = ""
click_cooldown = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    draw_keyboard(img, key_positions)
    index_tip = None
    thumb_tip = None

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            lmList = handLms.landmark

            index_tip = (int(lmList[8].x * w), int(lmList[8].y * h))
            thumb_tip = (int(lmList[4].x * w), int(lmList[4].y * h))

            cv2.circle(img, index_tip, 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, thumb_tip, 8, (0, 255, 0), cv2.FILLED)

            distance = int(np.linalg.norm(np.array(index_tip) - np.array(thumb_tip)))

            if distance < 30 and click_cooldown == 0:
                pressed_key = get_pressed_key(index_tip, key_positions)
                if pressed_key:
                    if pressed_key == "CLEAR":
                        text = ""
                    elif pressed_key == "ENTER":
                        text += "\n"
                    elif pressed_key == "SPACE":
                        text += " "
                    else:
                        text += pressed_key
                    click_cooldown = 15

    if click_cooldown > 0:
        click_cooldown -= 1

    cv2.rectangle(img, (50, 600), (1200, 700), (255, 255, 255), -1)
    cv2.putText(img, text, (60, 670), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
