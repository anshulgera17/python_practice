def inspect(func, *args):
    def wrapped_func(*args, **kwargs):
        print("function name inspect")
        val = func(*args)
        print(val + "running value")
        return val
    return wrapped_func

@inspect
def combine(a, b):
    return a + b

class User:
    base_url = 'http://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return 'Anshul gera'
    
    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"



    
