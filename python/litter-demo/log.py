def log(func):
    def wrapper(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log # now = log(now)
def now():
    print('this is now')

now()
