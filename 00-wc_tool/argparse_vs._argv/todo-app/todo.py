'''
    To do list manager
'''

import argparse
import os
import json

task_file = 'tasks.json'

def load_task():
    '''
    Loads JSON file
    '''
    if os.path.exists(task_file):
        with open (task_file, 'r') as file:
            content = json.load(file)
            return content
    return []

def save_task(data):
    if os.path.exists(task_file):
        with open (task_file, 'w') as file:
            json.dump(data, file)

def add_task(task_name, status=False):
    temp_dict = {
        'task': task_name,
        'completed': status
    }
    tasks = load_task()
    tasks.append(temp_dict)
    print(tasks)
    save_task(tasks)
 
def view_tasks():
    tasks = load_task()
    if len(tasks) > 0:
        for i in range(len(tasks)):
            print(tasks[i])


if __name__ == '__main__':
    add_task('Send an email to supervisor', False)