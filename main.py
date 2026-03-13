sentance = "Тут могло бы быть ваше предложение"
words = sentance.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Самое длинное слово:", longest_word)