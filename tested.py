class Test:
	test1 = 0
	def __init__(self):
		self.test2 = Test.test1+1
		Test.test1 = Test.test1+1

a = Test()
print(a.test1)
print(Test.test1)
b = Test()
print(b.test1)
print(Test.test1)
c = Test()
print(c.test1)
print(Test.test1)