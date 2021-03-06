# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:23:08 2022
@author: jankodzbanko
"""
import random
import os
import time

base_list = []

global restart
restart = True

print('May RNGesus have mercy!')
for i in range(3):
    print('*')
    time.sleep(0.2)
time.sleep(0.1)


#function to create a new list.
def create_list():
    time.sleep(0.1)
    first_inp = input('Enter first option: \n')
    with open('list.txt', 'w') as file:
        file.write(first_inp)

#checking for list.txt in current working dir.
if os.path.isfile(os.path.abspath(os.getcwd()) + '\list.txt') == False:
    print('No list to read found, creating new one.')
    for i in range(3):
        print('*')
        time.sleep(0.1)
    create_list()
 
#reads a .txt file with options to choose from, creates list of choosen indexes, sorts them from the biggest to ensure that lowering index wont break
#the script, and then pops out result from base list to a result list, which makes it so all the results are unique, no doubles.
def base_roll():
    base_list.clear()
    time.sleep(0.1)
    with open('list.txt', 'r') as file:
        for line in file:
            base_list.append((line).replace('\n', ''))
    global restart
    restart = False
    global result
    result = []
    number = input('Write a number of options to roll:\n')
    suma = len(base_list)
    baselist_idx = []
    for i in range(suma):
        baselist_idx.append(i)    
    indexes = random.sample(baselist_idx, int(number))
    indexes.sort(reverse=True)
    for k in indexes:
        result.append(base_list.pop(k))
    for count, j in enumerate(result):
        print((count + 1),'-', j)
        count += 1
        time.sleep(0.5)
    time.sleep(0.5)
    decision = input('Restart - 1, exchange 1 for 2 - 2.\n')
    if decision == '1':
        restart = True
    elif decision == '2':
        twoForOne()
        
def view_list():
    with open('list.txt', 'r') as file:
        for line in file:
            base_list.append((line).replace('\n', ''))
    for count, j in enumerate(base_list):
        print((count + 1),'-', j)
        count += 1
        time.sleep(0.2)
        
#def remove_line():
#    removal_idx = input('Which line to remove? Find line number by using full list view.\n')
#    with open('list.txt', 'w') as file:

#asks if the roll is good or not, if not, it pops given var from result and chooses 2 random vars from base list
#if its good, just prints result out
def twoForOne():
    time.sleep(0.1)
    global restart
    restart = False
    exchange_idx = input('Which option would you like to change? Number in order: {}\n'.format(result))
    result.pop(int(exchange_idx) - 1)
    baselist_idx = []
    for i in range(len(base_list)):
        baselist_idx.append(i)
    indexes = random.sample(baselist_idx, 2)
    indexes.sort(reverse=True)
    for k in indexes:
        result.append(base_list.pop(k))
    for count, j in enumerate(result):
        print((count + 1),'-', j)
        time.sleep(0.5)
        count += 1
    time.sleep(0.5)
    decision = input('Restart - 1, Exit - 2.\n')
    if decision == '1':
        restart = True
    elif decision == '2':
        for i in range(3):
            print('*')
            time.sleep(0.1)
        time.sleep(0.1)
        print('Goodbye.')
        restart = False

#option to add a variable to a list, via writing it on a .txt file
def add_aThing():
    time.sleep(0.1)
    with open('list.txt', 'a') as file:
        file.write('\n' + (input('Write a position to add: \n')))

#shall I call it a main menu? :)
def start():
    global restart
    time.sleep(0.2)
    op = input('1 - A roll\n'
               '2 - Add postion to a list\n'
               '3 - Exit\n'
               '4 - View full list\n')
    if op == '1':
        base_roll()
    elif op == '2':
        add_aThing()
    elif op == '4':
        view_list()
    elif op == '3':
        for i in range(3):
            print('*')
            time.sleep(0.1)
        time.sleep(0.1)
        print('Goodbye.')
        restart = False

#basic loop for the script to keep working instead of exiting on any result.
while restart:
    start()