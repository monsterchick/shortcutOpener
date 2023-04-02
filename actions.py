import pyautogui


def find_icon(image):
    try:
        img_pos_box = pyautogui.locateOnScreen(image, confidence=0.7)
        # print(img_pos_box)
        img_center_point = pyautogui.center(img_pos_box)
        # print(img_center_point)
        pyautogui.moveTo(img_center_point)
        pyautogui.doubleClick(duration=1)
    except TypeError:
        print('{i} did not match. Please try again.'.format(i=image.split('\\')[-1]))
