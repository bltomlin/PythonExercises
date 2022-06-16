usr_input = int(input())
bytes_num = bytes(usr_input)
ans = int.from_bytes(bytes_num, 'little')
print(ans)
