"""
This module contains the quiz questions and answers.
Questions are organized by category and difficulty level for better structure.
"""

# Quiz questions stored in dictionaries, now with difficulty levels
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
            }
        ]
    }
}

# Function to get all questions combined
def get_all_questions(difficulty=None):
    """Returns all questions from all categories combined into one list.
    
    Args:
        difficulty (str, optional): Filter by difficulty level ('easy', 'medium', 'hard')
        
    Returns:
        list: List of questions
    """
    all_questions = []
    for category in QUIZ_QUESTIONS:
        if difficulty:
            if difficulty in QUIZ_QUESTIONS[category]:
                all_questions.extend(QUIZ_QUESTIONS[category][difficulty])
        else:
            for level in QUIZ_QUESTIONS[category]:
                all_questions.extend(QUIZ_QUESTIONS[category][level])
    return all_questions

# Function to get questions by category
def get_questions_by_category(category, difficulty=None):
    """Returns questions for a specific category.
    
    Args:
        category (str): Category name
        difficulty (str, optional): Filter by difficulty level ('easy', 'medium', 'hard')
        
    Returns:
        list: List of questions
    """
    if category in QUIZ_QUESTIONS:
        if difficulty:
            return QUIZ_QUESTIONS[category].get(difficulty, [])
        else:
            all_questions = []
            for level in QUIZ_QUESTIONS[category]:
                all_questions.extend(QUIZ_QUESTIONS[category][level])
            return all_questions
    return []

# Function to get questions by difficulty
def get_questions_by_difficulty(difficulty):
    """Returns all questions of a specific difficulty level.
    
    Args:
        difficulty (str): Difficulty level ('easy', 'medium', 'hard')
        
    Returns:
        list: List of questions
    """
    all_questions = []
    for category in QUIZ_QUESTIONS:
        if difficulty in QUIZ_QUESTIONS[category]:
            all_questions.extend(QUIZ_QUESTIONS[category][difficulty])
    return all_questions

# Function to get adaptive difficulty based on performance
def get_adaptive_difficulty(correct_streak, incorrect_streak):
    """Determine difficulty level based on player performance.
    
    Args:
        correct_streak (int): Number of consecutive correct answers
        incorrect_streak (int): Number of consecutive incorrect answers
        
    Returns:
        str: Difficulty level ('easy', 'medium', 'hard')
    """
    if correct_streak >= 3:
        return "hard"
    elif incorrect_streak >= 2:
        return "easy"
    else:
        return "medium"