import curses
import random
import threading
import time

def draw_stars(buffer, height, width):
    # Define the banner text to display
    banner_text = [
        "██╗   ██╗ █████╗ ███████╗████████╗",
        "██║   ██║██╔══██╗██╔════╝╚══██╔══╝",
        "██║   ██║███████║███████╗   ██║   ",
        "╚██╗ ██╔╝██╔══██║╚════██║   ██║   ",
        " ╚████╔╝ ██║  ██║███████║   ██║   ",
        "  ╚═══╝  ╚═╝  ╚═╝╚══════╝   ╚═╝   ",
        "                                   "
    ]

    # Calculate the position to display the banner text in the middle of the buffer
    banner_x = int((width - len(banner_text[0])) / 2)
    banner_y = int((height - len(banner_text)) / 2)

    # Loop forever
    while True:
        # Clear the buffer
        for i in range(height):
            for j in range(width):
                buffer[i][j] = " "

        # Draw the banner text
        for i, line in enumerate(banner_text):
            for j, c in enumerate(line):
                buffer[banner_y + i][banner_x + j] = c

        # Draw stars
        for i in range(100):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            buffer[y][x] = "*"

        # Pause for a short time before drawing the next frame
        time.sleep(0.1)

def main(stdscr):
    # Disable automatic echoing of keys to the screen
    curses.noecho()

    # Hide the cursor
    curses.curs_set(0)

    # Get the dimensions of the terminal window
    height, width = stdscr.getmaxyx()

    # Create a buffer to hold the stars and banner text
    buffer = [[" " for x in range(width)] for y in range(height)]

    # Create a thread for drawing the stars and banner text
    stars_thread = threading.Thread(target=draw_stars, args=(buffer, height, width))

    # Start the thread
    stars_thread.start()

    # Loop forever
    while True:
        # Copy the buffer to the screen
        for y in range(height):
            for x in range(width):
                try:
                    stdscr.addstr(y, x, buffer[y][x])
                except curses.error as e:
                    # Print the error message and continue the loop
                    print(f"Error writing to screen: {e}")

        # Refresh the screen to show the changes
        stdscr.refresh()

        # Pause briefly before redrawing the screen
        time.sleep(0.05)

if __name__ == "__main__":
    # Initialize the curses library
    curses.wrapper(main)
