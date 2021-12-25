def change(st):
    st = st.lower()
    return ''.join(str(int(chr(i) in st)) for i in range(97, 123))

print(change("a **&  bZ"), "11000000000000000000000001")
print(change('Abc e  $$  z'), "11101000000000000000000001")
print(change("!!a$%&RgTT"), "10000010000000000101000000")
print(change(""), "00000000000000000000000000", "empty string should return 26 '0'")
print(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")
print(change("aaaaaaaaaaa"), "10000000000000000000000000")
print(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")
