program = input()

valid_commands = ["+", "-", "<", ">", ".", ",", "[", "]"]

arr = [0]
ci = 0
user_input = []
loop_table = {}
loop_stack = []

for ip, cmd in enumerate(program):
    if cmd == "[":
        loop_stack.append(ip)
    elif cmd == "]":
        loop_begin = loop_stack.pop()
        loop_table[loop_begin] = ip
        loop_table[ip] = loop_begin

ip = 0
while ip < len(program):
    cmd = program[ip]

    if cmd in valid_commands:
        if cmd == "+":
            arr[ci] += 1
            if arr[ci] == 256:
                arr[ci] = 0
        elif cmd == "-":
            arr[ci] -= 1
            if arr[ci] == -1:
                arr[ci] = 255
        elif cmd == "<":
            ci -= 1
        elif cmd == ">":
            ci += 1
            if ci == len(arr):
                arr.append(0)
        elif cmd == ".":
            print(chr(arr[ci]), end="")
        elif cmd == ",":
            if user_input == []:
                user_input = list(input() + "\n")
            arr[ci] = ord(user_input.pop(0))
        elif cmd == "[":
            if arr[ci] == 0:
                ip = loop_table[ip]
        elif cmd == "]":
            if arr[ci]:
                ip = loop_table[ip]

    ip += 1
