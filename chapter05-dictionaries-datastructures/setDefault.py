spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

# Alternatively
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'white')
print(spam)

spam.setdefault('color', 'black')
print(spam)