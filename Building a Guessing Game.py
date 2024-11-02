"""secret_word = "Ashik"

right_word = " "

while right_word != secret_word:
    right_word = input("Enter Your Right Word: ")
print("You win!")"""


secret_word = "Ashik"
right_word = " "
word_count = 0
word_limit = 3
out_of_word = False

while right_word != secret_word and not(out_of_word):
    if word_count < word_limit:
        right_word = input("Enter Your Right Word: ")
        word_count += 1
    else:
        out_of_word = True

if out_of_word:
    print("YOU LOSE!")
else:
    print("YOU WON!")
