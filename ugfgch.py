def f():
    s = '-- inside f()'
    print(s)

print('before calling f()')
f()
print('after calling f()')

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f(6, 'banana',1.74)