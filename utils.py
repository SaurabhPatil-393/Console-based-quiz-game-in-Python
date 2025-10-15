"""
Utility functions for the Quiz Game.
Contains functions for animations, colors, formatting, and timer functionality.
"""

import time
import sys
import os
import threading

# Windows compatibility for colors
if os.name == "nt":
    os.system("color")

# Color codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "end": "\033[0m",
    "gold": "\033[33m",
    "silver": "\033[37m",
    "bronze": "\033[33m"
}

# Emojis
EMOJIS = {
    "star": "⭐",
    "check": "✅",
    "cross": "❌",
    "heart": "❤️",
    "brain": "🧠",
    "trophy": "🏆",
    "fire": "🔥",
    "sparkles": "✨",
    "party": "🎉",
    "thinking": "🤔",
    "clap": "👏",
    "rocket": "🚀",
    "question": "❓",
    "clock": "⏰",
    "zap": "⚡",
    "shield": "🛡️",
    "gem": "💎"
}

def print_with_delay(text, delay=0.03, color="white"):
    """
    Print text with a typing animation effect.
    
    Args:
        text (str): Text to print
        delay (float): Delay between each character
        color (str): Color of the text
    """
    colored_text = f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['end']}"
    
    for char in colored_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

def print_centered(text, width=80, color="white"):
    """
    Print text centered on the console.
    
    Args:
        text (str): Text to print
        width (int): Width of the console
        color (str): Color of the text
    """
    colored_text = f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['end']}"
    print(colored_text.center(width))

def print_border(char="=", length=80, color="cyan"):
    """
    Print a border line.
    
    Args:
        char (str): Character to use for border
        length (int): Length of the border
        color (str): Color of the border
    """
    border = char * length
    colored_border = f"{COLORS.get(color, COLORS['cyan'])}{border}{COLORS['end']}"
    print(colored_border)

def print_title(text, border_char="=", border_color="cyan", text_color="yellow"):
    """
    Print a title with borders.
    
    Args:
        text (str): Title text
        border_char (str): Character for border
        border_color (str): Color of border
        text_color (str): Color of text
    """
    print_border(border_char, len(text) + 4, border_color)
    print_centered(f"{EMOJIS['star']} {text} {EMOJIS['star']}", len(text) + 4, text_color)
    print_border(border_char, len(text) + 4, border_color)

def print_options(options, color="white"):
    """
    Print multiple choice options with formatting.
    
    Args:
        options (list): List of option strings
        color (str): Color of the options
    """
    for option in options:
        print_with_delay(f"  {option}", 0.01, color)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, color="cyan"):
    """
    Get user input with colored prompt.
    
    Args:
        prompt (str): Prompt text
        color (str): Color of the prompt
        
    Returns:
        str: User input
    """
    colored_prompt = f"{COLORS.get(color, COLORS['cyan'])}{prompt}{COLORS['end']}"
    return input(colored_prompt)

def print_score(score, total, max_possible_points, color="yellow"):
    """
    Print the score in a formatted way.
    
    Args:
        score (int): Current score
        total (int): Total possible score
        max_possible_points (int): Maximum possible points
        color (str): Color of the score
    """
    percentage = (score / max_possible_points) * 100 if max_possible_points > 0 else 0
    grade_color = "green" if percentage >= 70 else "yellow" if percentage >= 50 else "red"
    
    print_with_delay(f"{EMOJIS['trophy']} Your Score: {score}/{max_possible_points}", 0.02, color)
    print_with_delay(f"{EMOJIS['brain']} Percentage: {percentage:.1f}%", 0.02, grade_color)
    
    # Add performance message
    if percentage >= 90:
        print_with_delay(f"{EMOJIS['party']} Excellent! You're a genius!", 0.02, "green")
    elif percentage >= 70:
        print_with_delay(f"{EMOJIS['clap']} Good job! Well done!", 0.02, "green")
    elif percentage >= 50:
        print_with_delay(f"{EMOJIS['thinking']} Not bad! Keep practicing!", 0.02, "yellow")
    else:
        print_with_delay(f"{EMOJIS['rocket']} Keep learning! You'll get better!", 0.02, "red")

def print_timer(seconds, color="red"):
    """
    Print a countdown timer visualization.
    
    Args:
        seconds (int): Number of seconds to count down
        color (str): Color of the timer
    """
    colored_text = f"{COLORS.get(color, COLORS['red'])}{EMOJIS['clock']} Time: {{}}s{COLORS['end']}"
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{colored_text.format(i)}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f"\r{colored_text.format(0)}\n")
    sys.stdout.flush()

def input_with_timeout(prompt, timeout=10, color="cyan"):
    """
    Get user input with a timeout.
    
    Args:
        prompt (str): Prompt text
        timeout (int): Timeout in seconds
        color (str): Color of the prompt
        
    Returns:
        str: User input or None if timeout
    """
    print_with_delay(f"{EMOJIS['clock']} You have {timeout} seconds to answer!", 0.02, "yellow")
    
    user_input: list = [None]  # Use a list to store the input (mutable)
    input_received = threading.Event()
    
    def get_input():
        colored_prompt = f"{COLORS.get(color, COLORS['cyan'])}{prompt}{COLORS['end']}"
        user_input[0] = input(colored_prompt)
        input_received.set()
    
    # Start input thread
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    
    # Wait for input or timeout
    input_received.wait(timeout)
    
    if input_received.is_set():
        return user_input[0]
    else:
        print_with_delay(f"\n{EMOJIS['cross']} Time's up!", 0.02, "red")
        return None