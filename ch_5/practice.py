names = ['JOYCE', 'VIOLET', 'AMBER', 'JULIET', 'ROMEO', 'JEFF', 'CHRIS', 'MIKE']
for name in range(len(names)):
    names[name] = names[name].lower()
print(names)

new_name = 'heatHer'
if (new_name not in names):
    names.append(new_name.lower())
print(names)
