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