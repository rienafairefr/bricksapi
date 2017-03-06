import pickle
from contextlib import contextmanager
from functools import wraps





def memoize(func):
    @wraps(func)
    def wrap(*args,**kwargs):
        with session_scope() as session:
            key = pickle.dumps((args, tuple(kwargs.items())))
            value = session.query(Memoized).get(key)
            if value is None:
                data = func(*args,**kwargs)
                object = Memoized(key=key,data=pickle.dumps(data))
                session.add(object)
                return data
            else:
                pass
            return pickle.loads(value.data)
    return wrap