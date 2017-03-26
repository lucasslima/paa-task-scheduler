#!/usr/bin/python
# -*- encoding: utf-8 -*-
import argparse
import operator
import traceback


def greedy_selection(activities):
    if not activities:  # An empty string or list has false value
        print('Nenhuma atividade foi informada')
        return 0
    activities.sort(key=operator.itemgetter(1))
    schedule = []
    schedule.append(activities[0])
    for activity in activities[1:]:  # Tasks except first one - if activities has only an element, the for loop doesn't execute
        begin, end = activity
        if (begin >= schedule[-1][1]):
            schedule.append(activity)

    return schedule

def find_solution(j, q, opt,activities):
  if j==-1:
    return list(); 
  if (1 + opt[q[j]] > opt[j-1]):
    selected = find_solution(q[j],q,opt,activities)
    selected.append(activities[j])
    return selected
  else:
    return find_solution( j - 1,q,opt,activities)
    
def dynamic_selection(activities):
  activities.sort(key=operator.itemgetter(1))
  opt = [-1] * (len(activities)-1)
  opt[0] = 0
  q = []
  for activity in activities:
    compatible_activities = [x for x in activities if x[1] <= activity[0] ]
    if not compatible_activities:
      q.append(-1)
    else:
      qj = max(compatible_activities,key=lambda x: activities.index(x) )
      qj = activities.index(qj)
      q.append(qj)
  for i in range(1, len(activities)-1):
    opt[i] = max(opt[i-1], opt[ q[i] ] + 1)
  selected_activities = find_solution(len(activities)-1, q, opt,activities)
  return selected_activities


def backtracking_selection(activities):
    schedule = []
    return schedule


def main():
    parser = argparse.ArgumentParser(prog='paa-activity-selection', description='Parses a input file with activities')
    parser.add_argument('--inputfile', type=str, nargs='?', default='input.txt', metavar='I',
                        help='location of input file to be parsed (default: input.txt)')
    parser.add_argument('--method', type=str, nargs='?', default='greedy', metavar='M',
                        help='algorithm to be used to schedule activities (options: greedy, dynamic, backtracking)')
    args = parser.parse_args()
    print('Argumentos recebidos: ')
    print(args)
    inputfile = args.inputfile
    method = args.method

    with open(inputfile) as f:
        activities = [activity.split() for activity in f.read().splitlines()]
        #  print(activities) tarefas
        #  print(activities[0]) primeira tarefa
        #  print(activities[0][0]) inicio da primeira tarefa
        #  print(activities[0][1]) fim da primeira tarefa

    if method == 'backtracking':
        schedule = backtracking_selection(activities)
        method += ' ()'
    elif method == 'dynamic':
        schedule = dynamic_selection(activities)
        method += ' (dinâmico)'
    else:
        schedule = greedy_selection(activities)
        method += ' (guloso)'

    print('{} tarefas foram escalonadas seguindo o método {}'.format(len(schedule), method))
    print(schedule)
    for index, activity in enumerate(schedule):
        print('Tarefa {} início: {} fim: {}'.format(index, activity[0], activity[1]))


if __name__ == "__main__":
    main()
