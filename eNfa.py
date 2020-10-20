from automata.fa.nfa import NFA

# NFA from the first experience in automata
nfa = NFA(
    states={'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q1': {'0': {'q1'}, '1': {'q1', 'q2'}},
        'q2': {'0': {'q3'}, '': {'q3'}},
        'q3': {'1': {'q4'}},
        'q4': {'0': {'q4'}, '1': {'q4'}},
    },
    initial_state='q1',
    final_states={'q4'}

)

if __name__ == '__main__':
    if nfa.accepts_input('0000'):
        print('accepted')
    else:
        print('rejected')
