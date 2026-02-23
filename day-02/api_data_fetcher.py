import requests
import json

def user_check(user) :
    dump=0
    for key,value in user.items() :
        if key == 'completed' and value == False :
            print(f'User details completed- \nUserId : {user['userId']}\nTitle : {user['title']}')
            dump=1
    if dump==1:
        user.pop('completed')
        user.pop('id')
        with open('output.json','w') as file :
            file.write(json.dumps(user))
        
api_url = "http://jsonplaceholder.typicode.com/todos/3"
response = requests.get(url=api_url)
user = response.json()

user_check(user)
# print(dir(user))
# print(user.pop.__doc__)