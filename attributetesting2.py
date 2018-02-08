from nose.plugins.attrib import attr

@attr(speed='test1')
def test_ramraju():
	result = 58+96
	print(result)

@attr(speed='test2')
def test_raghu():
	result = 50/2
	print(result)

@attr(speed='noneed')
def test_three():
	result = 55/3
	print(result)

