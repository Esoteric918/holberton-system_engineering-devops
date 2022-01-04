#!/usr/bin/python3
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        usr = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}").json()
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={sys.argv[1]}").json()

        print(f'Employee {usr.get("name")} is done with tasks('
              f'{len([x for x in todos if x.get("completed") == True])}/{len(todos)}):'
              )
        print('\n'.join(f'\t {x.get("title")}'
              for x in todos if x.get('completed') == True))
