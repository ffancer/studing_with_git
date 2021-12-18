def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=len)[-1]


print(longest_word('a b c d e fgh'), "fgh")
print(longest_word('one two three'), "three")
print(longest_word('red blue grey'), "grey")
