import pygetwindow as gw
import pyautogui
import win32gui
import time


def main():
    try:
        # Find the window with the title 'CrossWorlds'
        window = gw.getWindowsWithTitle('CrossWorlds')[0]

        # Activate the window
        window.activate()
        time.sleep(3)  # wait a bit for the window to activate

        # Continue left-clicking until the window is inactive
        while window.isActive:
            pyautogui.click()
            # window = gw.getWindowsWithTitle('CrossWorlds')[0]  # Refresh the window object

    except IndexError:
        print("Window 'CrossWorlds' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
