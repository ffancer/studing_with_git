def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

    return (l*h)*2 + (w*h)*2

print(wallpaper(6.3, 4.5, 3.29), "sixteen")
print(wallpaper(7.8, 2.9, 3.29), "sixteen")
print(wallpaper(6.3, 5.8, 3.13), "seventeen")
print(wallpaper(6.1, 6.7, 2.81), "sixteen")
