import pyautogui
import random
import time
import os
from PIL import Image


def find_color_on_screen(rgb_color, tolerance=10):
    screen_width, screen_height = pyautogui.size()
    screenshot = pyautogui.screenshot()

    for x in range(0, screen_width, 5):  # Step by 5 pixels for efficiency
        for y in range(0, screen_height, 5):
            pixel_color = screenshot.getpixel((x, y))
            if all(abs(pixel_color[i] - rgb_color[i]) <= tolerance for i in range(3)):
                return (x, y)

    return None


def read_usernames(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def write_username(username):
    for char in username:
        pyautogui.write(char)
        time.sleep(random.uniform(0.1, 0.3))


def remove_username(filename, username):
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        file.writelines([line for line in lines if line.strip() != username])

def scroll_to_top():
    # Scroll up to the top of the page
    pyautogui.scroll(10000)  # Adjust the scroll amount as necessary


def main():
    filename = "usernames.txt"
    usernames = read_usernames(filename)

    # Prompt user for the number of usernames to process
    num_usernames = int(input("Enter the number of usernames to add to close friends: "))

    # Initialize counter
    count = 0

    # Start by opening Find tool
    pyautogui.hotkey("ctrl", "f")

    for username in usernames:
        if count >= num_usernames:
            print(f"Processed {count} usernames. Exiting.")
            break

        # Find and click near lupa.png
        lupa = pyautogui.locateOnScreen("lupa.png")
        if lupa:
            click_x = lupa.left + lupa.width + random.randint(200, 250)
            click_y = lupa.top + lupa.height // 2
            pyautogui.click(click_x, click_y)
        else:
            print("Couldn't find lupa.png")
            continue

        # Write username
        write_username(username)
        time.sleep(5)  # Wait for results to populate

        # Wait for kruzic.png or kruzic2.png
        kruzic_found = False
        kruzic2_found = False
        start_time = time.time()
        timeout = 10  # Set a timeout of 10 seconds

        while time.time() - start_time < timeout:
            if pyautogui.locateOnScreen("kruzic2.png"):
                print(f"Username @{username} is already added to close friends.")
                kruzic2_found = True
                break
            elif pyautogui.locateOnScreen("kruzic.png"):
                print(f"Adding @{username}...")
                kruzic_found = True
                break

            time.sleep(0.5)

        if kruzic_found:
            # Press CTRL+F, CTRL+A, and input username
            pyautogui.hotkey("ctrl", "f")
            pyautogui.hotkey("ctrl", "a")
            pyautogui.write(username)

            time.sleep(0.5)

            # Search for #ff9632 color
            rgb_color = (255, 150, 50)  # RGB equivalent of #ff9632 color
            color_location = find_color_on_screen(rgb_color)

            if color_location:
                pyautogui.click(color_location)
                print(f"Successfully added @{username} to close friends.")

                # Increment counter
                count += 1

                time.sleep(0.5)
            else:
                print(f"Couldn't find color for @{username}.")

        # Whether kruzic.png or kruzic2.png is found, or if timeout occurs, do this part:

        # We want to scroll to the top, in case we went below the part where we can find lupa.png
        scroll_to_top()

        # Return to starting position and clear
        pyautogui.click(click_x, click_y)
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.press("backspace")

        # Remove username from file
        remove_username(filename, username)

        # Wait a bit before next iteration
        time.sleep(random.uniform(1, 2))

    print(f"Added {count} usernames. Exiting.")


if __name__ == "__main__":
    main()
