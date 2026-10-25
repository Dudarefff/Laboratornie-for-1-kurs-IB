'''variant 10'''

text = input("Введите текст: ")
words = text.split()
count = 0
for word in words:
    cleaned_word = word.strip(".,;:!?").lower()
    if not cleaned_word:
        continue
    if cleaned_word[0] == cleaned_word[-1]:
        print(cleaned_word)
        count += 1
if count == 0:
    print("Нет совпадений и количество 0")
else:
    print(f"Общее количество: {count}")