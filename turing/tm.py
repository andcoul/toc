class Turing_Machine:
    """
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@|||| TM that decides  {#n  +m  = k |  n+m=k} ||||@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
    def __init__(self, state, write_head, tape_list):
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list

    def getState(self):
        return self.state

    def getHead(self):
        return self.write_head

    def getList(self):
        return self.tape_list

    def updateMachine(self, character_list):
        # Initial State
        """
        :param character_list: List of character for test
        :return:
        """
        # @@@@@@@@ Start state @@@@@@@@
        if self.state == 'start':
            if self.tape_list[self.write_head] == '#':
                ### STATE ###
                self.state = 'q0'
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q0 @@@@@@@@
        elif self.state == 'q0':
            if self.tape_list[self.write_head] == 'a':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '+':
                ### STATE ###
                self.state = 'q1'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q1 @@@@@@@@
        elif self.state == 'q1':
            if self.tape_list[self.write_head] == 'a':
                ### STATE ###
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '=':
                ### STATE ###
                self.state = 'q2'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q2 @@@@@@@@
        elif self.state == 'q2':
            if self.tape_list[self.write_head] == 'a':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '.':
                ### STATE ###
                self.state = 'q7'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            else:
                pass
        # @@@@@@@@ state q4 @@@@@@@@
        elif self.state == 'q3':
            if self.tape_list[self.write_head] == '#':
                ### STATE ###
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head += 1
            elif self.tape_list[self.write_head] == 'a':
                ### STATE ###
                self.state = 'q4'
                ### WRITE ###
                self.tape_list[self.write_head] = 'X'
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '=':
                ### STATE ###
                self.state = 'q5'
                ### WRITE ### (Unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '+':
                ### STATE ###
                self.state = self.state
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == 'X':
                ### STATE ###
                self.state = self.state
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q5 @@@@@@@@
        elif self.state == 'q4':
            if self.tape_list[self.write_head] == '=':
                ### STATE ###
                self.state = 'q6'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == 'a':
                ### STATE ###
                self.state = self.state
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '+':
                ### STATE ###
                self.state = self.state
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q6 @@@@@@@@
        elif self.state == 'q5':
            if self.tape_list[self.write_head] == 'X':
                ### STATE ###
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '.':
                ### STATE ###
                self.state = 'accept'
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q7 @@@@@@@@
        elif self.state == 'q6':
            if self.tape_list[self.write_head] == 'a':
                ### STATE ###
                self.state = 'q7'
                ### WRITE ###
                self.tape_list[self.write_head] = 'X'
                ### MOVE ### (right)
                self.write_head += 1
            elif self.tape_list[self.write_head] == 'X':
                ### STATE ###
                self.state = self.state
                ### MOVE ### (right)
                self.write_head += 1
            else:
                pass
        # @@@@@@@@ state q9 @@@@@@@@
        elif self.state == 'q7':
            if self.tape_list[self.write_head] == 'a':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            elif self.tape_list[self.write_head] == '+':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            elif self.tape_list[self.write_head] == '=':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            elif self.tape_list[self.write_head] == 'X':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            elif self.tape_list[self.write_head] == '#':
                ### STATE ###
                self.state = 'q3'
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head += 1
            elif self.tape_list[self.write_head] == '.':
                ### STATE ### (unchanged)
                self.state = self.state
                ### WRITE ### (unchanged)
                self.tape_list[self.write_head] = self.tape_list[self.write_head]
                ### MOVE ### (left)
                self.write_head -= 1
            else:
                pass
