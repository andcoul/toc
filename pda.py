# Create variables
input_string = 'baccabcbcb'
# input_string = 'abcaba'
stack = []
initial_stack_symbol = '$'
current_state = 'q0'
final_state = 'q1'
accepted = False
# initialize the stack
stack.append(initial_stack_symbol)

# Go through the input string
for elt in input_string:
    # First level
    current_state = 'q1'

    if elt != 'b' and elt != 'c':
        continue

    # If read 'b' push to the stack since read a new 'c' then pop all 'b'
    elif elt == 'b':
        # Second level
        current_state = 'q2'
        if stack[-1] == 'c':
            stack.remove('c')
        else:
            stack.append('b')

    # If read 'c' push to the stack since read a new 'b' then pop all 'c'
    elif elt == 'c':
        # Third level
        current_state = 'q3'
        if stack[-1] == 'b':
            stack.remove('b')
        else:
            stack.append('c')

if len(stack) == 1 and stack[-1] == '$':
    stack.remove('$')
    current_state = 'q1'
    accepted = True

print('Stack: ', stack)
print('Current state: ', current_state)
print('Final state: ', final_state)
print('Accepted: ', accepted)

