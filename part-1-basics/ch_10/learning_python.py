with open('learning_python.txt') as file_content:
    content = file_content.read()
    print(content.strip())
print('*'*100)

with open('learning_python.txt') as file_content:
    for content in file_content:
        print(content.strip())
print('*'*100)

with open('learning_python.txt') as file_content:
    lines = file_content.readlines()
    print(lines)
for line in lines:
    print(line.replace('Lorem', 'Spank').strip())


