
def fizzBuzz(n):
  r = ''
  if n % 3 == 0:
    r += 'Fizz'

  if n % 5 == 0:
    r += 'Buzz'

  if r == '':
    r = n
  
  return r


if __file__ == 'fizzBuzz.py':
	for i in range(1,150):
		print(fizzBuzz(i))