"""
A script that automatically types a certain sentence and pastes it at the cursor position every 2 seconds.
Requires the 'pyautogui' library to be installed.
"""

import time
import pyautogui

def type_and_paste(sentence, interval):
    """
    Function to type a sentence and paste it at the cursor position.
    Args:
        sentence (str): The sentence to be typed and pasted.
        interval (int): Time interval in seconds between each typing action.
    """
    time.sleep(2)  # Wait for 2 seconds before starting

    while True:
        current_pos = pyautogui.position()  # Get the current cursor position
        pyautogui.typewrite(sentence)  # Type the sentence
        pyautogui.hotkey('ctrl', 'v')  # Paste the sentence at the cursor position
        pyautogui.press('enter')  # Press Enter to simulate submitting the sentence
        pyautogui.moveTo(current_pos)  # Move the cursor back to its original position
        time.sleep(interval)  # Wait for the specified interval before typing again

# Change the values below to customize the script
SENTENCE_TO_TYPE = "Hello, World!"
TYPING_INTERVAL = 2  # seconds

if __name__ == "__main__":
    type_and_paste(SENTENCE_TO_TYPE, TYPING_INTERVAL)
