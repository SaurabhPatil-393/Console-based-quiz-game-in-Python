# 🧠 Console-Based Quiz Game in Python

A stylish and interactive quiz game built with Python that runs in the console/terminal. Test your knowledge across multiple categories with a visually appealing interface featuring colors, emojis, and smooth animations.

## 🎮 Features

- **Modular Design**: Clean separation of concerns with multiple Python files
- **Multiple Categories**: Questions in Python, General Knowledge, and Technology
- **Difficulty Levels**: Easy, Medium, and Hard questions with different point values
- **Adaptive Difficulty**: Game adjusts question difficulty based on your performance
- **Timer Functionality**: Time limits per question with bonus points for quick answers
- **Enhanced Scoring System**: 
  - Streak bonuses for consecutive correct answers
  - Penalty for wrong answers
  - Multipliers for difficulty levels
  - Time-based bonus points
- **Score Tracking**: Saves your scores to a text file for future reference
- **Player Statistics**: Track your performance over time with detailed statistics
- **Visual Appeal**: Colorful console output with emojis and animations
- **User-Friendly**: Intuitive interface with clear instructions
- **Replay Option**: Play multiple rounds without restarting

## 📁 Project Structure

```
├── main.py           # Main game logic and entry point
├── questions.py      # Question database organized by categories and difficulty
├── utils.py          # Utility functions for colors, animations, and formatting
├── scores.txt        # Stores player scores (automatically created)
└── README.md         # This file
```

## ▶️ How to Run

1. Make sure you have Python installed (version 3.6 or higher)
2. Navigate to the project directory in your terminal/command prompt
3. Run the game with:
   ```
   python main.py
   ```
4. Follow the on-screen instructions to play!

## 🎯 How to Play

1. Enter your name when prompted
2. Select a category (or choose "All Categories" for mixed questions)
3. Choose a difficulty level:
   - **Easy**: 10 points per question, 15 seconds per question
   - **Medium**: 20 points per question, 12 seconds per question
   - **Hard**: 30 points per question, 10 seconds per question
   - **Adaptive**: Automatically adjusts based on your performance
4. Answer each question before time runs out by entering A, B, C, or D
5. Earn bonus points for quick answers and streaks
6. See your score at the end with a performance evaluation
7. View the high scores leaderboard or your personal statistics
8. Choose to play again or exit

## 🏆 Scoring System

- **Base Points**: Vary by difficulty level (10/20/30 points)
- **Time Bonus**: Up to 10 bonus points for quick answers
- **Streak Bonus**: 2 extra points for each question in a correct streak
- **Penalty**: Lose half points for wrong answers (except on Easy difficulty)

## 📊 Player Statistics

The game now tracks detailed statistics for each player:
- Total games played
- Average score and percentage
- Best score and percentage
- Performance trends over time

Access your stats from the main menu to track your improvement!

## 🎨 Visual Features

- **Colorful Output**: Different colors for different types of information
- **Emojis**: Visual elements to enhance the gaming experience
- **Typing Animations**: Smooth text display for better engagement
- **Centered Titles**: Professionally formatted headers and borders
- **Progress Tracking**: Current score display after each question
- **Timer Visualization**: Countdown display for each question

## 💾 Score Saving

Scores are automatically saved to `scores.txt` with:
- Player name
- Score and percentage
- Date and time of the quiz

The high scores screen shows the top 5 performances.

## 🛠 Requirements

- Python 3.6+
- No external libraries required (uses only core Python modules)

## 👨‍💻 Author

Created as part of an educational project with a focus on clean code, modular design, and user experience.

Enjoy the quiz game and happy learning!