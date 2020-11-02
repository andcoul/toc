from automata.pda.dpda import DPDA

# DPDA which which matches zero or more 'a's, followed by the same
# number of 'b's (accepting by final state)
dpda = DPDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'b', 'c'},
    stack_symbols={'', 'b', 'c', '$'},
    transitions={
        'q0': {
            '': {'': ('q1', ('$',))}  # transition pushes '$' to stack
        },
        'q1': {
            'b': {'$': ('q2', ('b', '$'))},  # transition push 'b' to stack
            'c': {'$': ('q3', ('c', '$'))},  # transition push 'c' to stack
            '': {'$': ('q1', '')},  # remove '$ from stack
        },
        'q2': {
            'b': {'b': ('q2', ('b', 'b'))},  # transition push 'b' to stack
            'c': {'b': ('q2', '')},  # transition pops 'b' from stack
            '': {'$': ('q1', ('$',))}  # transition does not change stack
        },
        'q3': {
            'c': {'c': ('q3', ('c', 'c'))},  # transition push 'b' to stack
            'b': {'c': ('q3', '')},  # transition pops 'b' from stack
            '': {'$': ('q1', ('$',))}  # transition pops 'b' from stack
        }
    },
    initial_state='q0',
    initial_stack_symbol='',
    final_states={'q1'},
    acceptance_mode='final_state'
)

if __name__ == '__main__':
    if dpda.accepts_input('bbbccc'):
        print('accepted')
    else:
        print('rejected')
