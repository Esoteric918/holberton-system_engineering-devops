#!/usr/bin/python3
"""get todo list for employees and write to a csv file"""
import csv
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

        with open('{}.csv'.format(sys.argv[1]), 'w') as f:
            csv_inp = csv.writer(f, quoting=csv.QUOTE_ALL)
            for td in todos:
                csv_inp.writerow([
                    sys.argv[1],
                    usr.get('username'),
                    td.get('completed'),
                    td.get('title')
                ])
