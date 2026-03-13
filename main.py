sentance = "Тут могло бы быть ваше предложение"
words = sentance.split()
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)