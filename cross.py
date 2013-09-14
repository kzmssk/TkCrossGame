import numpy as np

class Cross:
	def __init__(self):
		print 'Cross.__init__'
		print 'create state numpy-range (3,3)'
		self.state=np.zeros((3,3))
	def show_state(self):
		print 'show_state:'
		return self.state
	def set_state(self,x,y, state):
		if state !=1 and state != -1:
			print state
			print "set_state: state value error.   (3,3): state 1 for circle, -1 for x-mark." % state
			return -1
		self.state[x, y]=state
		print "set %s at : [ %d ] [ %d ]" % (state, x, y)
	def check_sum(val):
		if val==3:
			return 1
		elif val==-3:
			return -1
		else:
			return 0
	def check_state(self):
		 print 'check_sate: judge which player is winner'
		 for i in range(3):
		 	check=self.check_sum(self.state[i,:].sum())
		 	if check != 0:
		 		return check
		 for j in range(3):
		 	check=self.check_sum(self.state[:,j].sum())
		 	if check != 0:
		 		return check
		 sum=0
		 for k in range(3):
		 	sum+=self.state[k,k]
		 	check=self.check_sum(sum)
		 	if check!= 0:
		 		return check
		 sum=0
		 for l in range(3):
		 	sum+=self.state[l, 2-l]
		 	check=self.chek_sum(sum)
		 	if check != 0:
		 		return check
		 return 0
	def view_state(self):
		print self.state
