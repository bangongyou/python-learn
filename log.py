import functools

def log(text):
	def decorator(func):
		# 绑定func.__name__到wrapper上
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s %s():" % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('exec')
def now():
	print('2015-03-01')

def now2():
	print('2016-03-01')

#print("now.__name__ is %s " % now.__name__)

now()
log('call')(now2)()