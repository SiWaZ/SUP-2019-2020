def caesar(s,k):
    for i in range(len(s)):
        n = ord(s[i])
        if 'a' <= s[i] <= 'z':
            if ord('z') >= n + k:
                n += k
                s = s[:i] + chr(n) + s[i+1:]
            else:
                n = (n-26) + k
                s = s[:i] + chr(n) + s[i+1:]
        elif 'A' <= s[i] <= 'Z':
            if ord('Z') >= n + k:
                n += k
                s = s[:i] + chr(n) + s[i+1:]
            else:
                n = (n-26) + k
                s = s[:i] + chr(n) + s[i+1:]

    print(s)

s = input("Saisir un mot: ")
k = int(input("Saisir un clé: "))
caesar(s,k)
