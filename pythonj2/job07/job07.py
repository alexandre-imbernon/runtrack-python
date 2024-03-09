alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
i = 0
while i < len(alphabet) and i < 27:
    print(alphabet[i:i+(i:=i+1)])