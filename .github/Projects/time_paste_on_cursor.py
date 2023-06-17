import time
import pyautogui

def type_and_paste(sentence, interval):
    time.sleep(2)  # Wait for 2 seconds before starting

    while True:
        current_pos = pyautogui.position()  # Get the current cursor position
        pyautogui.typewrite(sentence)  # Type the sentence
        pyautogui.hotkey('ctrl', 'v')  # Paste the sentence at the cursor position
        pyautogui.press('enter')  # Press Enter to simulate submitting the sentence
        pyautogui.moveTo(current_pos)  # Move the cursor back to its original position
        time.sleep(interval)  # Wait for the specified interval before typing again

# Change the values below to customize the script
sentence_to_type = "keo aso?"
typing_interval = 2  # seconds

type_and_paste(sentence_to_type, typing_interval)
    
