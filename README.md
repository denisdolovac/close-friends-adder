# Close Friends Adder

This script automates the process of adding usernames to a close friends list on a social media platform. It uses the `pyautogui` library to interact with the screen, perform image recognition, and detect specific colors. The script reads usernames from a text file and processes them one by one, adding them to the close friends list if certain conditions are met.

## Script in Action



## Requirements

1. Python 3.x
2. `pyautogui` library
3. `Pillow` library
4. A text file named `usernames.txt` containing the usernames to be processed
5. Image files: `loupe.png`, `circle.png`, and `circle_blue.png`

## Installation

1. Install Python 3.x from the [official Python website](https://www.python.org/).
2. Install the required libraries by running:
    ```bash
    pip install pyautogui pillow
    ```
3. Add usernames to `usernames.txt`.

## Usage

1. Open your favorite browser and navigate to [Instagram Close Friends](https://www.instagram.com/accounts/close_friends/).
2. Run the script:
    ```bash
    python close-friends-adder.py
    ```
3. Enter the number of usernames to add when prompted.
4. Ensure you click on the browser window before the script starts working.

## Functionality

- Reads usernames from `usernames.txt`.
- Opens the Find tool.
- Locates and clicks near `loupe.png`.
- Types the username and checks for `circle.png` or `circle_blue.png`.
- Adds the username to the close friends list if conditions are met.
- Removes processed usernames from `usernames.txt`.

## Error Handling

- Prints an error if `loupe.png`, `circle.png`, or `circle_blue.png` is not found.
- Prints an error if the specified color is not found on the screen.
