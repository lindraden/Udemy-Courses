# Get sentence from user
original = input("Please enter a sentence?: ").strip().lower()

# split sentence into words
words = original.split()

#loop through all of the words and convert
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest_word = word[vowel_pos:]
        new_word = rest_word + cons + "ay"
        new_words.append(new_word)

# stick words together

output = " ".join(new_words)

#output final string

print(output)
