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
        with open('./file/output.json','w') as file :
            file.write(json.dumps(user))

try :
    api_url = "http://jsonplaceholder.typicode.com/todos/5"
    response = requests.get(url=api_url)
    print('response : ',response)
    user = response.json()
    print(user)
    user_check(user)
except FileNotFoundError as f:
    print('FileNotFoundError :',f)
except Exception as e:
    print('except : ',e)