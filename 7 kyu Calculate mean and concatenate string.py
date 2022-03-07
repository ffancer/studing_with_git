def mean(lst):
    return [sum(int(i) for i in lst if i.isdigit()) / 10, ''.join(i for i in lst if i.isalpha())]


lst = ["u", "6", "d", "1", "i", "w", "6", "s", "t", "4", "a", "6", "g", "1", "2", "w", "8", "o", "2", "0"]
print(mean(lst), [3.6, "udiwstagwo"])
lst = ["0", "c", "7", "x", "6", "2", "3", "5", "w", "7", "0", "y", "v", "u", "h", "i", "n", "u", "0", "0"]
print(mean(lst), [3.0, "cxwyvuhinu"])
lst = ["0", "u", "a", "y", "0", "a", "9", "q", "3", "v", "g", "7", "6", "4", "y", "d", "8", "6", "0", "d"]
print(mean(lst), [4.3, "uayaqvgydd"])
lst = ["s", "n", "9", "l", "0", "m", "i", "z", "9", "7", "y", "4", "z", "3", "3", "k", "4", "1", "0", "k"]
print(mean(lst), [4.0, "snlmizyzkk"])
lst = ["5", "v", "u", "k", "8", "4", "9", "b", "9", "g", "5", "z", "3", "f", "6", "u", "i", "6", "6", "t"]
print(mean(lst), [6.1, "vukbgzfuit"])
lst = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "a", "a", "d", "d", "g", "q", "u", "v", "y", "y"]
print(mean(lst), [0.9, "aaddgquvyy"])
lst = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "a", "a", "d", "d", "g", "q", "u", "v", "y", "y"]
print(mean(lst), [1.0, "aaddgquvyy"])
