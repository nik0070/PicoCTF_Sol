with open('enc', 'r') as f:
    out = ''
    flag = f.read()
    print(len(flag))
    print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

    