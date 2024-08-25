import tkinter as tk
import random

# Dictionary for game rules: key beats value
RULES = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

# Emoji dictionary
EMOJIS = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

# Define the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine winner
def determine_winner(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(list(RULES.keys()))
    result = ""
    
    if computer_choice == user_choice:
        result = "It's a tie! 🤝"
    elif RULES[computer_choice] == user_choice:
        result = "Computer wins! 😔"
        computer_score += 1
    else:
        result = "You win! 🎉"
        user_score += 1
    
    update_scores()
    update_labels(user_choice, computer_choice, result)

# Function to update scores
def update_scores():
    score_label.config(text=f"You: {user_score}  -  Computer: {computer_score}")

# Function to update labels with choices and result
def update_labels(user_choice, computer_choice, result):
    user_label.config(text=f"You chose: {EMOJIS[user_choice]} ({user_choice.capitalize()})")
    computer_label.config(text=f"Computer chose: {EMOJIS[computer_choice]} ({computer_choice.capitalize()})")
    result_label.config(text=result)

# Create GUI elements
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=('Arial', 18, 'bold'), bg='#4CAF50', fg='white')
title_label.pack(pady=10)

button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text=f"Rock {EMOJIS['rock']}", width=15, height=2, bg='#e57373', fg='white', font=('Arial', 14),
                       command=lambda: determine_winner('rock'))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(button_frame, text=f"Paper {EMOJIS['paper']}", width=15, height=2, bg='#64b5f6', fg='white', font=('Arial', 14),
                        command=lambda: determine_winner('paper'))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(button_frame, text=f"Scissors {EMOJIS['scissors']}", width=15, height=2, bg='#81c784', fg='white', font=('Arial', 14),
                            command=lambda: determine_winner('scissors'))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'), bg='#ffffff')
result_label.pack(pady=10)

user_label = tk.Label(root, text="", font=('Arial', 14), bg='#ffffff')
user_label.pack()

computer_label = tk.Label(root, text="", font=('Arial', 14), bg='#ffffff')
computer_label.pack()

score_label = tk.Label(root, text=f"You: {user_score}  -  Computer: {computer_score}", font=('Arial', 14, 'bold'), bg='#ffffff')
score_label.pack(pady=10)

# Run the main loop
root.mainloop()
