from functools import reduce

class NumberMazeState(object):
	def __init__(self, state, dist, move, laststate):
		self.state = state
		self.dist = dist
		self.move = move #up:1, down:2, left:3, right:4
		self.laststate = laststate
		self.key = 0
		for i in state:
			self.key = self.key * 9 + i

def stateonemove(state):
	if state.state[0] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 0, 1), state.dist + 1, 4, state), 
		NumberMazeState(listswap(state.state, 0, 3), state.dist + 1, 2, state)]
	elif state.state[1] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 1, 0), state.dist + 1, 3, state),
		NumberMazeState(listswap(state.state, 1, 2), state.dist + 1, 4, state), 
		NumberMazeState(listswap(state.state, 1, 4), state.dist + 1, 2, state)]
	elif state.state[2] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 2, 1), state.dist + 1, 3, state), 
		NumberMazeState(listswap(state.state, 2, 5), state.dist + 1, 2, state)]
	elif state.state[3] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 3, 0), state.dist + 1, 1, state),
		NumberMazeState(listswap(state.state, 3, 4), state.dist + 1, 4, state), 
		NumberMazeState(listswap(state.state, 3, 6), state.dist + 1, 2, state)]
	elif state.state[4] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 4, 1), state.dist + 1, 1, state),
		NumberMazeState(listswap(state.state, 4, 3), state.dist + 1, 3, state), 
		NumberMazeState(listswap(state.state, 4, 5), state.dist + 1, 4, state),
		NumberMazeState(listswap(state.state, 4, 7), state.dist + 1, 2, state)]
	elif state.state[5] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 5, 2), state.dist + 1, 1, state),
		NumberMazeState(listswap(state.state, 5, 4), state.dist + 1, 3, state), 
		NumberMazeState(listswap(state.state, 5, 8), state.dist + 1, 2, state)]
	elif state.state[6] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 6, 3), state.dist + 1, 1, state), 
		NumberMazeState(listswap(state.state, 6, 7), state.dist + 1, 4, state)]
	elif state.state[7] == 0:
		onemovestate = [NumberMazeState(listswap(state.state, 7, 4), state.dist + 1, 1, state),
		NumberMazeState(listswap(state.state, 7, 6), state.dist + 1, 3, state), 
		NumberMazeState(listswap(state.state, 7, 8), state.dist + 1, 4, state)]
	else:
		onemovestate = [NumberMazeState(listswap(state.state, 8, 5), state.dist + 1, 1, state), 
		NumberMazeState(listswap(state.state, 8, 7), state.dist + 1, 3, state)]
	return onemovestate

def listswap(listpara,index1,index2):
	listnew = list(listpara)
	listnew[index1], listnew[index2] = listnew[index2], listnew[index1]
	return listnew
	
state = NumberMazeState([1,2,3,4,5,6,7,8,0], 0, 0, 0)
statenum, dist, stateall = 1, 1, reduce(lambda x,y : x*y, range(1,10))/2
stateset = [state]
statesetnext = []
staterecord = {state.key: state}

while(statenum < stateall):
	while(stateset):
		onemovestate = stateonemove(stateset[0])
		for statei in onemovestate:
			if(not(statei.key in staterecord)):
				staterecord[statei.key] = statei
				statesetnext.append(statei)
				statenum = statenum + 1
		stateset.pop(0)
	stateset = statesetnext
	statesetnext = []
	dist = dist + 1
	print("already calculated state num: " + str(statenum) + " current dist: " + str(dist))

question = [2,7,4,8,5,3,6,1,0]
questionkey = reduce(lambda x,y : x*9 + y, question)
originstate = staterecord[questionkey]
print("moves to solve the question: " + str(originstate.dist))
print("solution sequence is:")
while(originstate):
	print(originstate.state[0:3])
	print(originstate.state[3:6])
	print(originstate.state[6:9])
	if(originstate.move == 1):
		print("up")
	elif(originstate.move == 2):
		print("down")
	elif(originstate.move == 3):
		print("left")
	elif(originstate.move == 4):
		print("right")
	else:
		break
	originstate = originstate.laststate
