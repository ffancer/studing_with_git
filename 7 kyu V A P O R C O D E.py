def vaporcode(s):
    s = s.split()
    s = ''.join(s)
    answer = ''

    for i in s:
        answer += i.upper() + '  '

    return answer[:-2]


print(vaporcode("Lets go to the movies"), "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
print(vaporcode("Why isn't my code working?"), "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")
