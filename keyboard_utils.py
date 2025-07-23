import cv2

key_layout = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM"),
    ["SPACE", "ENTER", "CLEAR"]
]

key_positions = []
start_x, start_y = 100, 100
key_w, key_h = 80, 80
gap = 10

for row_index, row in enumerate(key_layout):
    for col_index, key in enumerate(row):
        x = start_x + col_index * (key_w + gap)
        y = start_y + row_index * (key_h + gap)
        key_positions.append((key, (x, y, key_w, key_h)))

def draw_keyboard(img, keys):
    for key, (x, y, w, h) in keys:
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 200, 200), -1)
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 50), 2)
        font_scale = 1.2 if len(key) == 1 else 0.8
        text_size = cv2.getTextSize(key, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2
        cv2.putText(img, key, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 2)

def get_pressed_key(finger_pos, keys):
    fx, fy = finger_pos
    for key, (x, y, w, h) in keys:
        if x < fx < x + w and y < fy < y + h:
            return key
    return None
