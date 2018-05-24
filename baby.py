from random import choice

questions = [
"Why is the sky blue?: ", "Why is Michael so shit at basketball?: ", "Why is coffee bitter?: "
]

question = choice(questions)
answer = input(question).lower().strip()
while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... okay")
