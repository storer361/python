student_data = {'id1':{'name':['sara'],'class':['v'],'subject_interagation':['english,maths,science']},
'id2':
{'name':['david'],'class':['v'],'subject_interagation':['english,maths,science']},
'id3':
{'name':['sara'],'class':['v'],'subject_interagation':['english,maths,science']},
'id4':
{'name':['surya'],'class':['v'],'subject_interagation':['english,maths,science']},}
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)