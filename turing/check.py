# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Checking step @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import string
import sys

from turing.tm import Turing_Machine


def check_language(initial_string):
    # Define Character Set
    character_list = list(string.ascii_lowercase)
    character_list.append(' ')  # to allow for spaces

    # Initial string
    print('Checking...' + initial_string)
    print('- - -')
    initial_list = list(initial_string)

    # Quick check that you only used allow characters
    for i in initial_list:
        if i not in character_list and i != '#' and i != '+' and i != '=':
            print('Error! Initial character >', i, '< not in allowed character list!')
            sys.exit()

    # Append list
    initial_list.append('.')

    # Set up the turing machine
    i_write_head = 0
    i_state = 'start'  # initial state
    i_tape_list = initial_list

    # Initiate the class
    run_machine = Turing_Machine(i_state, i_write_head, i_tape_list)
    print(run_machine.getState(), run_machine.getHead(), run_machine.getList())

    # Run the machine
    ctr = 0
    while run_machine.getState() != 'accept' and ctr < 3000:
        run_machine.updateMachine(character_list)
        print(run_machine.getState(), run_machine.getHead(), run_machine.getList())
        ctr += 1
    print('- - -')

    # Printout result
    if run_machine.getState() == 'accept':
        print(initial_string, 'is an accepted string! Steps:', ctr)
    else:
        print(initial_string, 'is NOT an accepted string! Steps:', ctr)
