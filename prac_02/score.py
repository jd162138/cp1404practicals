"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    result = score_grade(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    random_result = score_grade(random_score)
    print(f"Random: {random_score} is {random_result}")

def score_grade(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()