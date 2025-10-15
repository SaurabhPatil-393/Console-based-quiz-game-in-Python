"""
Simplified version of the quiz game that can run in online Python environments like Replit.
This version combines all functionality into a single file for easy online execution.
"""

import random
import time
import sys
import os

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

# Quiz questions stored in dictionaries
QUIZ_QUESTIONS = {
    "Python": {
        "easy": [
            {
                "question": "What is the correct file extension for Python files?",
                "options": ["A) .pt", "B) .py", "C) .pyt", "D) .python"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "How do you start a comment in Python?",
                "options": ["A) //", "B) <!--", "C) #", "D) /*"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "Which keyword is used to create a function in Python?",
                "options": ["A) function", "B) def", "C) fun", "D) define"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "Which function is used to display output in Python?",
                "options": ["A) print()", "B) echo()", "C) display()", "D) output()"],
                "answer": "A",
                "points": 10
            },
            {
                "question": "What is the output of print(2 + 3 * 4)?",
                "options": ["A) 20", "B) 14", "C) 11", "D) 18"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "Which data type is used to store text in Python?",
                "options": ["A) int", "B) float", "C) string", "D) boolean"],
                "answer": "C",
                "points": 10
            }
        ],
        "medium": [
            {
                "question": "What does the 'len()' function do?",
                "options": ["A) Returns the length of an object", "B) Creates a new list", 
                           "C) Finds the largest number", "D) Converts to string"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which data type is immutable in Python?",
                "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
                "answer": "D",
                "points": 20
            },
            {
                "question": "What is the output of print(2 ** 3)?",
                "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "What is the correct way to create a list in Python?",
                "options": ["A) list = [1, 2, 3]", "B) list = (1, 2, 3)", 
                           "C) list = {1, 2, 3}", "D) list = <1, 2, 3>"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which method is used to add an element to the end of a list?",
                "options": ["A) insert()", "B) append()", "C) add()", "D) push()"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "What is the output of print(type([]))?",
                "options": ["A) <class 'list'>", "B) <class 'tuple'>", 
                           "C) <class 'dict'>", "D) <class 'set'>"],
                "answer": "A",
                "points": 20
            }
        ],
        "hard": [
            {
                "question": "What is the output of print(type(lambda: None))?",
                "options": ["A) <class 'function'>", "B) <class 'lambda'>", 
                           "C) <class 'NoneType'>", "D) <class 'type'>"],
                "answer": "A",
                "points": 30
            },
            {
                "question": "Which of these is NOT a valid Python decorator?",
                "options": ["A) @property", "B) @staticmethod", "C) @classmethod", "D) @function"],
                "answer": "D",
                "points": 30
            },
            {
                "question": "What does the __init__ method do in a Python class?",
                "options": ["A) Deletes the object", "B) Initializes the object", 
                           "C) Copies the object", "D) Compares the object"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "What is a correct syntax to import a module named 'math'?",
                "options": ["A) import.math", "B) import math", "C) include math", "D) using math"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "Which of the following is NOT a Python loop?",
                "options": ["A) for", "B) while", "C) do-while", "D) None of the above"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "What is the output of print([1, 2, 3] + [4, 5, 6])?",
                "options": ["A) [1, 2, 3, 4, 5, 6]", "B) [5, 7, 9]", 
                           "C) [[1, 2, 3], [4, 5, 6]]", "D) Error"],
                "answer": "A",
                "points": 30
            }
        ]
    },
    "General Knowledge": {
        "easy": [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "How many continents are there in the world?",
                "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "Which is the smallest planet in our solar system?",
                "options": ["A) Earth", "B) Mars", "C) Mercury", "D) Venus"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A) H2O", "B) CO2", "C) NaCl", "D) O2"],
                "answer": "A",
                "points": 10
            }
        ],
        "medium": [
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oganesson"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
                "answer": "C",
                "points": 20
            },
            {
                "question": "In which year did World War II end?",
                "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "Which is the longest river in the world?",
                "options": ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D",
                "points": 20
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["A) China", "B) Japan", "C) South Korea", "D) Thailand"],
                "answer": "B",
                "points": 20
            }
        ],
        "hard": [
            {
                "question": "What is the currency of Sweden?",
                "options": ["A) Euro", "B) Krona", "C) Krone", "D) Mark"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "Which country has the longest coastline in the world?",
                "options": ["A) Russia", "B) Canada", "C) Australia", "D) United States"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "What is the smallest country in the world?",
                "options": ["A) Monaco", "B) Vatican City", "C) San Marino", "D) Liechtenstein"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "Which mountain is the tallest in the world?",
                "options": ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "What is the capital of Canada?",
                "options": ["A) Toronto", "B) Vancouver", "C) Ottawa", "D) Montreal"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "Which is the largest desert in the world?",
                "options": ["A) Sahara Desert", "B) Arabian Desert", "C) Gobi Desert", "D) Antarctic Desert"],
                "answer": "D",
                "points": 30
            }
        ]
    },
    "Technology": {
        "easy": [
            {
                "question": "What does CPU stand for?",
                "options": ["A) Central Processing Unit", "B) Computer Personal Unit", 
                           "C) Central Processor Unit", "D) Central Program Unit"],
                "answer": "A",
                "points": 10
            },
            {
                "question": "Which of these is NOT a programming language?",
                "options": ["A) Python", "B) HTML", "C) Java", "D) C++"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "What is the main purpose of a firewall?",
                "options": ["A) Increase internet speed", "B) Protect against unauthorized access", 
                           "C) Store backup data", "D) Improve graphics performance"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "What does URL stand for?",
                "options": ["A) Universal Resource Locator", "B) Uniform Resource Locator", 
                           "C) Unified Resource Locator", "D) Unique Resource Locator"],
                "answer": "B",
                "points": 10
            },
            {
                "question": "Which company developed the Windows operating system?",
                "options": ["A) Apple", "B) Google", "C) Microsoft", "D) IBM"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "What is the brain of the computer called?",
                "options": ["A) RAM", "B) Motherboard", "C) CPU", "D) Hard Drive"],
                "answer": "C",
                "points": 10
            }
        ],
        "medium": [
            {
                "question": "Which company developed the JavaScript programming language?",
                "options": ["A) Microsoft", "B) Google", "C) Netscape", "D) Apple"],
                "answer": "C",
                "points": 20
            },
            {
                "question": "What is the primary function of RAM?",
                "options": ["A) Store permanent data", "B) Process graphics", 
                           "C) Store temporary data for quick access", "D) Manage network connections"],
                "answer": "C",
                "points": 20
            },
            {
                "question": "What does HTTP stand for?",
                "options": ["A) Hyper Text Transfer Protocol", "B) High Tech Transfer Program", 
                           "C) Home Tool Transmission Process", "D) Hyperlink Text Transmission Procedure"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which of the following is NOT a database management system?",
                "options": ["A) MySQL", "B) PostgreSQL", "C) Oracle", "D) Python"],
                "answer": "D",
                "points": 20
            },
            {
                "question": "What is the full form of IP in IP address?",
                "options": ["A) Internet Protocol", "B) Internal Process", "C) Information Processing", "D) Integrated Program"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which of these is a version control system?",
                "options": ["A) Docker", "B) Kubernetes", "C) Git", "D) Jenkins"],
                "answer": "C",
                "points": 20
            }
        ],
        "hard": [
            {
                "question": "What is the time complexity of binary search?",
                "options": ["A) O(n)", "B) O(log n)", "C) O(n log n)", "D) O(1)"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "Which data structure uses LIFO (Last In, First Out)?",
                "options": ["A) Queue", "B) Linked List", "C) Stack", "D) Tree"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "In blockchain, what does PoW stand for?",
                "options": ["A) Proof of Work", "B) Proof of Wallet", "C) Proof of Wealth", "D) Proof of Wisdom"],
                "answer": "A",
                "points": 30
            },
            {
                "question": "Which of the following is NOT a cloud computing service model?",
                "options": ["A) IaaS", "B) PaaS", "C) SaaS", "D) HaaS"],
                "answer": "D",
                "points": 30
            },
            {
                "question": "What does SQL stand for?",
                "options": ["A) Structured Query Language", "B) Standard Query Language", 
                           "C) Sequential Query Language", "D) Simple Query Language"],
                "answer": "A",
                "points": 30
            },
            {
                "question": "Which algorithm is used for finding the shortest path in a graph?",
                "options": ["A) Binary Search", "B) Merge Sort", "C) Dijkstra's Algorithm", "D) Quick Sort"],
                "answer": "C",
                "points": 30
            }
        ]
    },
    "Science": {
        "easy": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "Which gas do plants absorb from the atmosphere?",
                "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
                "answer": "C",
                "points": 10
            },
            {
                "question": "How many bones are in the human body?",
                "options": ["A) 206", "B) 300", "C) 150", "D) 185"],
                "answer": "A",
                "points": 10
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["A) Heart", "B) Liver", "C) Brain", "D) Skin"],
                "answer": "D",
                "points": 10
            },
            {
                "question": "Which planet is closest to the Sun?",
                "options": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
                "answer": "C",
                "points": 10
            }
        ],
        "medium": [
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Endoplasmic Reticulum"],
                "answer": "C",
                "points": 20
            },
            {
                "question": "What is the speed of light in vacuum?",
                "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which element has the atomic number 1?",
                "options": ["A) Helium", "B) Hydrogen", "C) Lithium", "D) Oxygen"],
                "answer": "B",
                "points": 20
            },
            {
                "question": "What is the chemical formula for table salt?",
                "options": ["A) NaCl", "B) H2O", "C) CO2", "D) CaCO3"],
                "answer": "A",
                "points": 20
            },
            {
                "question": "Which of these is NOT a type of rock?",
                "options": ["A) Igneous", "B) Sedimentary", "C) Metamorphic", "D) Crystalline"],
                "answer": "D",
                "points": 20
            },
            {
                "question": "What force keeps planets in orbit around the Sun?",
                "options": ["A) Magnetic force", "B) Friction", "C) Gravity", "D) Centrifugal force"],
                "answer": "C",
                "points": 20
            }
        ],
        "hard": [
            {
                "question": "What is the study of heredity and variation called?",
                "options": ["A) Ecology", "B) Genetics", "C) Anatomy", "D) Physiology"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "Which subatomic particle has a negative charge?",
                "options": ["A) Proton", "B) Neutron", "C) Electron", "D) Nucleus"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "What is the unit of electrical resistance?",
                "options": ["A) Volt", "B) Ampere", "C) Ohm", "D) Watt"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "Which law states that the current through a conductor is directly proportional to the voltage across it?",
                "options": ["A) Newton's Law", "B) Ohm's Law", "C) Faraday's Law", "D) Coulomb's Law"],
                "answer": "B",
                "points": 30
            },
            {
                "question": "What is the process by which plants make their food using sunlight called?",
                "options": ["A) Respiration", "B) Digestion", "C) Photosynthesis", "D) Fermentation"],
                "answer": "C",
                "points": 30
            },
            {
                "question": "Which element is the most abundant in the Earth's atmosphere?",
                "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Argon"],
                "answer": "C",
                "points": 30
            }
        ]
    }
}

def print_with_delay(text, delay=0.03, color="white"):
    """Print text with a typing animation effect."""
    colored_text = f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['end']}"
    
    for char in colored_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

def print_centered(text, width=80, color="white"):
    """Print text centered on the console."""
    colored_text = f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['end']}"
    print(colored_text.center(width))

def print_border(char="=", length=80, color="cyan"):
    """Print a border line."""
    border = char * length
    colored_border = f"{COLORS.get(color, COLORS['cyan'])}{border}{COLORS['end']}"
    print(colored_border)

def print_options(options, color="white"):
    """Print multiple choice options with formatting."""
    for option in options:
        print_with_delay(f"  {option}", 0.01, color)

def get_user_input(prompt, color="cyan"):
    """Get user input with colored prompt."""
    colored_prompt = f"{COLORS.get(color, COLORS['cyan'])}{prompt}{COLORS['end']}"
    return input(colored_prompt)

def print_score(score, total, max_possible_points, color="yellow"):
    """Print the score in a formatted way."""
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

def get_all_questions(difficulty=None):
    """Returns all questions from all categories combined into one list."""
    all_questions = []
    for category in QUIZ_QUESTIONS:
        if difficulty:
            if difficulty in QUIZ_QUESTIONS[category]:
                all_questions.extend(QUIZ_QUESTIONS[category][difficulty])
        else:
            for level in QUIZ_QUESTIONS[category]:
                all_questions.extend(QUIZ_QUESTIONS[category][level])
    return all_questions

def get_adaptive_difficulty(correct_streak, incorrect_streak):
    """Determine difficulty level based on player performance."""
    if correct_streak >= 3:
        return "hard"
    elif incorrect_streak >= 2:
        return "easy"
    else:
        return "medium"

def select_category():
    """Allow user to select a quiz category."""
    categories = list(QUIZ_QUESTIONS.keys())
    
    print_with_delay(f"{EMOJIS['thinking']} Select a category:", 0.02, "cyan")
    print_with_delay("0) All Categories (Mixed)", 0.02, "yellow")
    
    for i, category in enumerate(categories, 1):
        print_with_delay(f"{i}) {category}", 0.02, "white")
    
    print()
    
    while True:
        try:
            choice = int(get_user_input("Enter category number: ", "cyan"))
            if choice == 0:
                return get_all_questions(), "All Categories"
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                # For simplicity in this version, we'll still return all questions
                # but note the selected category
                return get_all_questions(), selected_category
            else:
                print_with_delay("Invalid choice! Please try again.", 0.02, "red")
        except ValueError:
            print_with_delay("Please enter a valid number!", 0.02, "red")

def select_difficulty():
    """Allow user to select difficulty level."""
    print_with_delay(f"{EMOJIS['shield']} Select difficulty level:", 0.02, "cyan")
    print_with_delay("1) Easy (10 points per question)", 0.02, "green")
    print_with_delay("2) Medium (20 points per question)", 0.02, "yellow")
    print_with_delay("3) Hard (30 points per question)", 0.02, "red")
    print_with_delay("4) Adaptive (Adjusts based on your performance)", 0.02, "purple")
    print()
    
    while True:
        try:
            choice = int(get_user_input("Enter difficulty number: ", "cyan"))
            if choice == 1:
                return "easy"
            elif choice == 2:
                return "medium"
            elif choice == 3:
                return "hard"
            elif choice == 4:
                return "adaptive"
            else:
                print_with_delay("Invalid choice! Please try again.", 0.02, "red")
        except ValueError:
            print_with_delay("Please enter a valid number!", 0.02, "red")

def calculate_time_limit(difficulty):
    """Calculate time limit based on difficulty."""
    if difficulty == "easy":
        return 15
    elif difficulty == "medium":
        return 12
    elif difficulty == "hard":
        return 10
    else:
        return 12  # Default for adaptive

def play_quiz():
    """Main quiz gameplay function."""
    # Introduction
    print_border("*", 80, "cyan")
    print_centered(f"{EMOJIS['brain']} WELCOME TO THE ULTIMATE QUIZ CHALLENGE {EMOJIS['brain']}", 80, "yellow")
    print_border("*", 80, "cyan")
    print()
    
    print_with_delay(f"Hello, Quiz Enthusiast! {EMOJIS['sparkles']}", 0.02, "cyan")
    print_with_delay("Test your knowledge across various topics.", 0.02, "white")
    print_with_delay("Answer carefully - each question counts!", 0.02, "white")
    print()
    
    # Get player name
    player_name = get_user_input("Enter your name: ", "yellow").strip()
    if not player_name:
        player_name = "Anonymous Player"
    
    print_with_delay(f"\nWelcome, {player_name}! {EMOJIS['fire']}", 0.02, "green")
    print_with_delay("Loading quiz questions...", 0.02, "cyan")
    
    # Animation effect
    for i in range(3):
        print_with_delay("." * (i + 1), 0.5, "cyan")
    
    print()
    
    # Select category
    questions, category_info = select_category()
    
    # Select difficulty
    difficulty_mode = select_difficulty()
    
    # Get questions based on difficulty
    if difficulty_mode == "adaptive":
        # For adaptive mode, we'll select a mix of difficulties
        questions = get_all_questions()
    elif difficulty_mode in ["easy", "medium", "hard"]:
        questions = get_all_questions(difficulty_mode)
    
    if not questions:
        print_with_delay("No questions available!", 0.02, "red")
        return 0, 0
    
    # Shuffle questions
    random.shuffle(questions)
    
    # Limit to 10 questions for better gameplay
    questions = questions[:10]
    
    # Initialize score and tracking variables
    score = 0
    max_possible_points = sum(q.get("points", 10) for q in questions)
    correct_streak = 0
    incorrect_streak = 0
    streak_bonus = 0
    
    # Keep track of asked questions to prevent repetition
    asked_questions = set()
    
    # Ask questions
    for i, q in enumerate(questions, 1):
        # For adaptive mode, adjust difficulty based on performance
        current_difficulty = difficulty_mode
        if difficulty_mode == "adaptive":
            current_difficulty = get_adaptive_difficulty(correct_streak, incorrect_streak)
        
        # Add question to asked set to prevent repetition
        asked_questions.add(q['question'])
        
        # Calculate time limit
        time_limit = calculate_time_limit(current_difficulty)
        
        print_border("=", 80, "blue")
        print_centered(f"QUESTION {i} of {len(questions)}", 80, "yellow")
        print_border("=", 80, "blue")
        print()
        
        # Display difficulty indicator
        diff_color = "green" if current_difficulty == "easy" else "yellow" if current_difficulty == "medium" else "red"
        diff_text = current_difficulty.upper()
        print_with_delay(f"{EMOJIS['shield']} Difficulty: {diff_text}", 0.02, diff_color)
        print_with_delay(f"{EMOJIS['gem']} Points: {q.get('points', 10)}", 0.02, "cyan")
        print()
        
        # Display question
        print_with_delay(f"{EMOJIS['question']} {q['question']}", 0.02, "white")
        print()
        
        # Display options
        print_options(q['options'], "cyan")
        print()
        
        # Get user answer (with timeout simulation)
        print_with_delay(f"{EMOJIS['clock']} You have {time_limit} seconds to answer!", 0.02, "yellow")
        user_answer = get_user_input("Your answer (A/B/C/D): ", "green")
        
        # Check answer
        if user_answer and user_answer.strip().upper() == q['answer']:
            print_with_delay(f"\n{EMOJIS['check']} Correct! Well done!", 0.02, "green")
            correct_points = q.get('points', 10)
            score += correct_points
            
            # Add streak bonus
            correct_streak += 1
            incorrect_streak = 0
            
            if correct_streak >= 3:
                streak_bonus = correct_streak * 2
                score += streak_bonus
                print_with_delay(f"{EMOJIS['zap']} {correct_streak}-question streak! Bonus: {streak_bonus} points", 0.02, "yellow")
        else:
            print_with_delay(f"\n{EMOJIS['cross']} Wrong answer!", 0.02, "red")
            correct_streak = 0
            incorrect_streak += 1
            
            # Penalty for wrong answers (except on easy difficulty)
            if current_difficulty != "easy":
                penalty = q.get('points', 10) // 2
                score -= penalty
                print_with_delay(f"{EMOJIS['cross']} Penalty: -{penalty} points", 0.02, "red")
            
            correct_option = next((opt for opt in q['options'] if opt.startswith(q['answer'])), "")
            print_with_delay(f"The correct answer was: {correct_option}", 0.02, "yellow")
        
        print()
        print_border("-", 40, "purple")
        print_with_delay(f"Current Score: {score}", 0.02, "cyan")
        print_border("-", 40, "purple")
        print()
        
        # Pause before next question
        if i < len(questions):
            input("Press Enter to continue to the next question...")
    
    # Final score display
    print_border("*", 80, "gold")
    print_centered(f"QUIZ COMPLETED - RESULTS", 80, "yellow")
    print_border("*", 80, "gold")
    print()
    
    print_with_delay(f"Well done, {player_name}! {EMOJIS['clap']}", 0.02, "cyan")
    print()
    
    # Display score with formatting
    print_score(score, len(questions), max_possible_points, "yellow")
    print()
    
    # Show additional stats
    print_with_delay(f"{EMOJIS['shield']} Category: {category_info}", 0.02, "cyan")
    print_with_delay(f"{EMOJIS['gem']} Difficulty: {difficulty_mode.title()}", 0.02, "cyan")
    print()
    
    return score, max_possible_points

def main():
    """Main function to run the quiz game."""
    while True:
        score, total_points = play_quiz()
        
        print_with_delay("Would you like to play again? (y/n): ", 0.02, "cyan")
        play_again = input().strip().lower()
        
        if play_again not in ['y', 'yes']:
            print_with_delay(f"\nThanks for playing! {EMOJIS['heart']}", 0.02, "cyan")
            print_with_delay("See you next time! 👋", 0.02, "yellow")
            break

if __name__ == "__main__":
    main()