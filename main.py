"""
Main Quiz Game Application.
This is the entry point for the Quiz Game.
"""

import random
import time
from questions import (
    get_all_questions, get_questions_by_category, get_questions_by_difficulty,
    get_adaptive_difficulty, QUIZ_QUESTIONS
)
from utils import (
    print_with_delay, print_centered, print_border, print_title, 
    print_options, clear_screen, get_user_input, print_score, 
    input_with_timeout, EMOJIS
)

# Create scores.txt file if it doesn't exist
SCORES_FILE = "scores.txt"

def initialize_scores_file():
    """Create scores.txt if it doesn't exist."""
    try:
        with open(SCORES_FILE, "x") as f:
            f.write("# Quiz Game Scores\n")
            f.write("# Format: Player Name | Score | Date\n")
    except FileExistsError:
        pass  # File already exists

def save_score(name, score, total_points):
    """
    Save player score to file.
    
    Args:
        name (str): Player name
        score (int): Player score
        total_points (int): Total possible points
    """
    from datetime import datetime
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    percentage = (score / total_points) * 100 if total_points > 0 else 0
    
    with open(SCORES_FILE, "a") as f:
        f.write(f"{name} | {score}/{total_points} ({percentage:.1f}%) | {timestamp}\n")

def get_player_stats(name):
    """
    Get statistics for a specific player.
    
    Args:
        name (str): Player name
        
    Returns:
        dict: Player statistics
    """
    try:
        with open(SCORES_FILE, "r") as f:
            scores = f.readlines()[2:]  # Skip header lines
            
        player_scores = []
        for line in scores:
            if "|" in line:
                parts = line.strip().split("|")
                if len(parts) >= 3 and parts[0].strip().lower() == name.lower():
                    score_part = parts[1].strip()
                    if "/" in score_part and "(" in score_part and ")" in score_part:
                        score_data = score_part.split()
                        score_value = int(score_data[0].split("/")[0])
                        total_value = int(score_data[0].split("/")[1])
                        percentage_str = score_data[1].replace("(", "").replace(")", "").replace("%", "")
                        percentage = float(percentage_str)
                        player_scores.append({
                            "score": score_value,
                            "total": total_value,
                            "percentage": percentage,
                            "date": parts[2].strip()
                        })
        
        if not player_scores:
            return None
            
        # Calculate statistics
        total_games = len(player_scores)
        avg_score = sum(s["score"] for s in player_scores) / total_games
        avg_percentage = sum(s["percentage"] for s in player_scores) / total_games
        best_score = max(s["score"] for s in player_scores)
        best_percentage = max(s["percentage"] for s in player_scores)
        
        return {
            "name": name,
            "games_played": total_games,
            "average_score": round(avg_score, 1),
            "average_percentage": round(avg_percentage, 1),
            "best_score": best_score,
            "best_percentage": best_percentage
        }
    except FileNotFoundError:
        return None

def show_player_stats():
    """Display statistics for a specific player."""
    player_name = get_user_input("Enter player name: ", "cyan").strip()
    if not player_name:
        print_with_delay("No name entered!", 0.02, "red")
        return
        
    stats = get_player_stats(player_name)
    if not stats:
        print_with_delay(f"No statistics found for '{player_name}'!", 0.02, "yellow")
        return
        
    print_title(f"STATISTICS FOR {player_name.upper()}", "=", "purple", "cyan")
    print()
    print_with_delay(f"{EMOJIS['brain']} Games Played: {stats['games_played']}", 0.02, "white")
    print_with_delay(f"{EMOJIS['gem']} Average Score: {stats['average_score']}", 0.02, "white")
    print_with_delay(f"{EMOJIS['shield']} Average Percentage: {stats['average_percentage']}%", 0.02, "white")
    print_with_delay(f"{EMOJIS['trophy']} Best Score: {stats['best_score']}", 0.02, "green")
    print_with_delay(f"{EMOJIS['star']} Best Percentage: {stats['best_percentage']}%", 0.02, "green")
    print()
    print_border("-", 50, "purple")

def show_high_scores():
    """Display high scores from the scores file."""
    try:
        with open(SCORES_FILE, "r") as f:
            scores = f.readlines()[1:]  # Skip header
            
        if not scores:
            print_with_delay("No scores recorded yet!", 0.02, "yellow")
            return
            
        print_title("HIGH SCORES", "=", "purple", "cyan")
        print()
        
        # Sort scores by percentage (descending)
        scored_entries = []
        for line in scores:
            if "|" in line:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    score_part = parts[1].strip()
                    if "(" in score_part and ")" in score_part:
                        percentage_str = score_part[score_part.find("(")+1:score_part.find(")")]
                        try:
                            percentage = float(percentage_str.replace("%", ""))
                            scored_entries.append((percentage, line.strip()))
                        except ValueError:
                            continue
        
        # Sort by percentage descending
        scored_entries.sort(key=lambda x: x[0], reverse=True)
        
        # Display top 5 scores
        for i, (percentage, entry) in enumerate(scored_entries[:5]):
            rank_color = "yellow" if i == 0 else "white" if i == 1 else "purple" if i == 2 else "cyan"
            rank_emoji = EMOJIS["trophy"] if i == 0 else EMOJIS["star"] if i < 3 else "  "
            print_with_delay(f"{rank_emoji} {entry}", 0.02, rank_color)
            
        print()
        print_border("-", 50, "purple")
    except FileNotFoundError:
        print_with_delay("No scores recorded yet!", 0.02, "yellow")

def select_category():
    """
    Allow user to select a quiz category.
    
    Returns:
        tuple: (questions_list, mode_info)
    """
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
                return get_all_questions(), selected_category
            else:
                print_with_delay("Invalid choice! Please try again.", 0.02, "red")
        except ValueError:
            print_with_delay("Please enter a valid number!", 0.02, "red")

def select_difficulty():
    """
    Allow user to select difficulty level.
    
    Returns:
        str: Selected difficulty level
    """
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
    """
    Calculate time limit based on difficulty.
    
    Args:
        difficulty (str): Difficulty level
        
    Returns:
        int: Time limit in seconds
    """
    if difficulty == "easy":
        return 15
    elif difficulty == "medium":
        return 12
    elif difficulty == "hard":
        return 10
    else:
        return 12  # Default for adaptive

def calculate_bonus_points(time_left, time_limit, difficulty):
    """
    Calculate bonus points for quick answers.
    
    Args:
        time_left (int): Time remaining
        time_limit (int): Total time limit
        difficulty (str): Difficulty level
        
    Returns:
        int: Bonus points
    """
    if time_left <= 0:
        return 0
    
    # Calculate percentage of time remaining
    time_percentage = time_left / time_limit
    
    # Bonus points based on difficulty
    base_bonus = 0
    if difficulty == "easy":
        base_bonus = 2
    elif difficulty == "medium":
        base_bonus = 5
    elif difficulty == "hard":
        base_bonus = 10
    
    # More bonus for faster answers
    bonus = int(base_bonus * time_percentage * 2)
    return bonus

def play_quiz():
    """Main quiz gameplay function.
    
    Returns:
        tuple: (score, total_points)
    """
    # Introduction
    clear_screen()
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
    
    # Limit to 15 questions for better gameplay (increased from 10)
    questions = questions[:15]
    
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
            # Get a question of appropriate difficulty that hasn't been asked yet
            diff_questions = get_questions_by_difficulty(current_difficulty)
            # Filter out already asked questions
            available_questions = [q for q in diff_questions if q['question'] not in asked_questions]
            
            # If we've run out of unique questions in this difficulty, use any available
            if not available_questions:
                available_questions = diff_questions
                
            if available_questions:
                q = random.choice(available_questions)
        
        # Add question to asked set to prevent repetition
        asked_questions.add(q['question'])
        
        # Calculate time limit
        time_limit = calculate_time_limit(current_difficulty)
        
        clear_screen()
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
        
        # Get user answer with timeout
        user_answer = input_with_timeout("Your answer (A/B/C/D): ", time_limit, "green")
        
        # Calculate time-based bonus
        time_left = time_limit if user_answer is not None else 0
        bonus_points = calculate_bonus_points(time_left, time_limit, current_difficulty)
        
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
            
            # Add time bonus
            if bonus_points > 0:
                score += bonus_points
                print_with_delay(f"{EMOJIS['clock']} Time bonus: {bonus_points} points", 0.02, "cyan")
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
    clear_screen()
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
    
    # Save score
    save_score(player_name, score, max_possible_points)
    print_with_delay(f"{EMOJIS['star']} Your score has been saved!", 0.02, "green")
    print()
    
    return score, max_possible_points

def main():
    """Main function to run the quiz game."""
    # Initialize scores file
    initialize_scores_file()
    
    while True:
        clear_screen()
        print_border("*", 80, "cyan")
        print_centered(f"{EMOJIS['brain']} PYTHON QUIZ GAME {EMOJIS['brain']}", 80, "yellow")
        print_border("*", 80, "cyan")
        print()
        
        print_with_delay("1) Start New Quiz", 0.02, "cyan")
        print_with_delay("2) View High Scores", 0.02, "cyan")
        print_with_delay("3) View Player Statistics", 0.02, "cyan")
        print_with_delay("4) Exit", 0.02, "cyan")
        print()
        
        choice = get_user_input("Select an option (1-4): ", "yellow").strip()
        
        if choice == "1":
            # Play the quiz
            score, total_points = play_quiz()
            
            # Show high scores
            print()
            show_high_scores()
        elif choice == "2":
            clear_screen()
            show_high_scores()
            print()
        elif choice == "3":
            clear_screen()
            show_player_stats()
            print()
        elif choice == "4":
            print_with_delay(f"\nThanks for playing! {EMOJIS['heart']}", 0.02, "cyan")
            print_with_delay("See you next time! 👋", 0.02, "yellow")
            break
        else:
            print_with_delay("Invalid choice! Please select 1, 2, 3, or 4.", 0.02, "red")
        
        if choice in ["1", "2", "3"]:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()