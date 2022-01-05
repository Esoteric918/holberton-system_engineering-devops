#!/usr/bin/python3
"""Script that uses REST API"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(sys.argv[1])
                           ).json()
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/?userId={}"
            .format(sys.argv[1])
        ).json()

        print('Employee {} is done with tasks({}/{}):'.format(
            usr.get("name"),
            len([x for x in todos if x.get("completed")]),
            len(todos)
        ))
        print('\n'.join('\t {}'.format(x.get("title"))
              for x in todos if x.get('completed')))
