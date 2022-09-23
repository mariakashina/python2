import pandas as pd

table = {'laboratory': ['№ 4163', '№ 4166', '№ 4167', '№ 4168'],
         'responsible': ['Katkova', 'Kinzhalov', 'Kinzhalov', 'Kinzhalov'],
         'number of staff': [8, 4, 2, 0]}
frame = pd.DataFrame(table)

print(frame)

frame.index.name = 'id'
frame.columns.name = 'id'
frame['number of students'] = [4, 4, 1, 0]

print(frame)
