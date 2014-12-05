## Example program for checking color codes
## in other progarms such as Sublime Text or
## TextWrangler.

print "Hello world!"
print 5 + 3
print 5 == 4
print 5 >= 4
print 5 <= 4

if 3 == 5:
	print True
else:
	print False

class Memory():
	def __init__(self):
		self.clearMemory()

	def getMemory(self):
		return self.value

	def clearMemory(self):
		self.value = None

	def setMemory(self, value):
		self.value = value

m = Memory()
print "\nm:", m
print ""
print "My Memory:", m.getMemory()
print "[m.setMemory(50)]"
m.setMemory(50)
print "My Memory:", m.getMemory()
print "[m.clearMemory()]"
m.clearMemory()
print "My Memory:", m.getMemory()
print "[del m]"
del m