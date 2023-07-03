import time
import pyautogui

def type_and_paste(sentence, interval):
    """
    Automatically types a sentence and pastes it at the cursor position.
    Args:
        sentence (str): The sentence to be typed and pasted.
        interval (int): Time interval in seconds between each typing action.
    """
    time.sleep(2)  # Wait for 2 seconds before starting

    try:
        while True:
            current_pos = pyautogui.position()  # Get the current cursor position
            pyautogui.typewrite(sentence)  # Type the sentence
            pyautogui.hotkey('ctrl', 'v')  # Paste the sentence at the cursor position
            pyautogui.press('enter')  # Press Enter to simulate submitting the sentence
            pyautogui.moveTo(current_pos)  # Move the cursor back to its original position
            time.sleep(interval)  # Wait for the specified interval before typing again

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Change the values below to customize the script
SENTENCE_TO_TYPE = "Hello, World!"
TYPING_INTERVAL = 2  # seconds

if __name__ == "__main__":
    type_and_paste(SENTENCE_TO_TYPE, TYPING_INTERVAL)
    
