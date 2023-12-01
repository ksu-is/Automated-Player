#By Andy Lau
from pynput.keyboard import Key, Listener
import pyautogui
import tkinter as tk
from threading import Thread

# ======== settings ========
delay = 2.5  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
increase_key = '='
decrease_key = '-'
# ==========================

pause = True
running = True


def on_press(key):
    global running, pause, delay

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")
    elif key == increase_key:
        delay += 0.1
        show_message("Increased Delay: {} sec".format(delay))
    elif key == decrease_key:
        delay = max(0.1, delay - 0.1)
        show_message("Decreased Delay: {} sec".format(delay))


def show_message(message):
    msg_label.config(text=message)
    msg_label.after(2000, clear_message)


def clear_message():
    msg_label.config(text="")


def display_controls():
    print("AutoClicker by Andy Lau")
    print("- Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("- Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t + = Increase Delay")
    print("\t - = Decrease Delay")
    print("\t ESC = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    global msg_label
    lis = Listener(on_press=on_press)
    lis.start()

    # Create a simple GUI
    root = tk.Tk()
    root.title("AutoClicker Controls")
    msg_label = tk.Label(root, text="", font=("Helvetica", 12))
    msg_label.pack(pady=20)

    display_controls()

    def autoclicker_loop():
        while running:
            if not pause:
                pyautogui.click(pyautogui.position())
                pyautogui.PAUSE = delay

    # Start the autoclicker loop in a separate thread
    autoclicker_thread = Thread(target=autoclicker_loop)
    autoclicker_thread.start()

    # Run the GUI main loop
    root.mainloop()

    # Stop the autoclicker thread when the GUI is closed
    autoclicker_thread.join()
    lis.stop()


if __name__ == "__main__":
    main()

