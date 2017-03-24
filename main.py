#!/usr/bin/python
# -*- encoding: utf-8 -*-
import argparse


def greedy_scheduler(tasks):
    if not tasks:  # An empty string or list has false value
        print('Nenhuma atividade foi informada')
        return 0

    schedule = []
    schedule.append(tasks[0])
    for task in tasks[1:]:  # Tasks except first one - if tasks has only an element, the for loop doesn't execute
        begin, end = task
        if (begin >= schedule[-1][1]):
            schedule.append(task)

    return schedule


def dynamic_scheduler(tasks):
    schedule = []
    return schedule


def backtracking_scheduler(tasks):
    schedule = []
    return schedule


def main():
    parser = argparse.ArgumentParser(prog='paa-task-scheduler', description='Parses a input file with tasks')
    parser.add_argument('--inputfile', type=str, nargs='?', default='input.txt', metavar='I',
                        help='location of input file to be parsed (default: input.txt)')
    parser.add_argument('--method', type=str, nargs='?', default='greedy', metavar='M',
                        help='algorithm to be used to schedule tasks (options: greedy, dynamic, backtracking)')
    args = parser.parse_args()
    print('Argumentos recebidos: ')
    print(args)
    inputfile = args.inputfile
    method = args.method

    with open(inputfile) as f:
        tasks = [task.split() for task in f.read().splitlines()]
        #  print(tasks) tarefas
        #  print(tasks[0]) primeira tarefa
        #  print(tasks[0][0]) inicio da primeira tarefa
        #  print(tasks[0][1]) fim da primeira tarefa

    if method == 'backtracking':
        schedule = backtracking_scheduler(tasks)
        method += ' ()'
    elif method == 'dynamic':
        schedule = dynamic_scheduler(tasks)
        method += ' (dinâmico)'
    else:
        schedule = greedy_scheduler(tasks)
        method += ' (guloso)'

    print('{} tarefas foram escalonadas seguindo o método {}'.format(len(schedule), method))
    print(schedule)
    for index, task in enumerate(schedule):
        print('Tarefa {} início: {} fim: {}'.format(index, task[0], task[1]))


if __name__ == "__main__":
    main()
