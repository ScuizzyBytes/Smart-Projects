stack = []

programs = ["PUSH 1", "PUSH 2", "ADD", "PRINT", "HALT"]

for line in programs:
    parts = line.split(" ")
    if parts[0] == "PUSH":
        stack.append(int(parts[1]))
    elif parts[0] == "ADD":
        a = stack.pop()
        b = stack.pop()
        result = a + b
        stack.append(result)
    elif parts[0] == "PRINT":
        print("Current Stack: ", stack)
    elif parts[0] == "HALT":
        break