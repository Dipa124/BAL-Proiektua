import keyboard
import time


def main():
    time.sleep(4)
    num = 0

    for x in range(10000):
        if num < 10:
            keyboard.write("000" + str(num))
            keyboard.press_and_release("enter")
            print("000" + str(num))
        elif 10 <= num < 100:
            keyboard.write("00" + str(num))
            keyboard.press_and_release("enter")
            print("00" + str(num))
        elif 100 <= num < 1000:
            keyboard.write("0" + str(num))
            keyboard.press_and_release("enter")
            print("0" + str(num))
        elif num >= 1000:
            keyboard.write(str(num))
            keyboard.press_and_release("enter")
            print(str(num))
        num += 1
        time.sleep(0.025)
        keyboard.press("Backspace")
        time.sleep(0.02)
        keyboard.press("Backspace")
        time.sleep(0.02)
        keyboard.press("Backspace")
        time.sleep(0.02)
        keyboard.press("Backspace")
        time.sleep(0.02)
        if keyboard.is_pressed("space"):
            exit()


if __name__ == "__main__":
    main()
