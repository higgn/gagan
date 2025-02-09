import random

def get_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "Stay hungry, stay foolish. - Steve Jobs",
        "The best error message is the one that never shows up.",
        "First, solve the problem. Then, write the code. - John Johnson",
        "Talk is cheap. Show me the code. - Linus Torvalds",
    ]
    return random.choice(quotes)