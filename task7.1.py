initial_string = input("Enter the string: ")
words_list = initial_string.split(sep=' ')
final_dict = {word: words_list.count(word) for word in words_list}
print(final_dict)
