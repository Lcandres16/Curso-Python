with open('base.txt', 'r') as file:
    content = file.read()
    print(content)

with open('base.txt', 'r') as file:
    content = file.read()
    print(content[0:2])


with open('base.txt', 'r') as file:
    content = file.read()
    print(content[0:2])


def read_lines(filename, num_lines):
    with open(filename, 'r') as file:
        for _ in range(num_lines):
            line = file.readline()
            if not line:
                break
            print(line.strip())
