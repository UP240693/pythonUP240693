# Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills']:
    print(person['skills'][len(person['skills']) // 2])
    print("Python" in person['skills'])
    if ['Javascript', 'React'] == person['skills']:
        print('Front End Developer')
    elif ['Node', 'MongoDB', 'React'] == person['skills']:
        print('Full Stack Developer')
    else:
        print("Unknown Title")

if person['is_marred']:
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is married")
else:
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is not married")