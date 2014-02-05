class Integer(object):
	def __init__(self,number, hi):
		self.num = number
		self.hi = hi
	def display(self):
		if self.hi :
			print self.hi
		else :
			print(self.hi - self.hi - self.hi)
class neginteger(Integer):
	super(neginteger, self).__init__(number, False)

if __name__ =="__main__":
	number = Integer(3,True)
	number.display()


