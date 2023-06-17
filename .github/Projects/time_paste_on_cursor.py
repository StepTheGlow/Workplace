import pyautogui
import time

def type_and_paste(sentence):
    # Wait for a few seconds to switch to the desired window or text field
    time.sleep(2)

    # Type the sentence
    pyautogui.typewrite(sentence)

    # Copy the typed sentence
    pyautogui.hotkey("c", "c")

    # Move the cursor to the desired location
    pyautogui.click()

    # Paste the copied text
    pyautogui.hotkey("c", "p")

# Example usage
sentence_to_type = "keo aso?"
type_and_paste(sentence_to_type)
  
