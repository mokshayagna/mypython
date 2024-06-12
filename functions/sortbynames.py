data = [
('Cricket', 'Dhoni'),
('Music', 'ARRehman'),
('Scriting', 'Python'),
('Singer', 'SPBalu'),
('Singer', 'Chitra'),
('Singer', 'Jesudas')
]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i][1] > data[j][1]:
            data[i], data[j] = data[j], data[i]

for value in data:
    print(value)
