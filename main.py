"""
main
"""
import pickle


# pylint: disable=C0103
# pylint: disable=R0205
# pylint: disable=R0903
class T(object):
    """
    T
    """
    def __init__(self, name):
        """
        __init__
        """
        self.name = name


data = {
    'a': [1, 2, 3],
    'b': {'test', 'test'},
    'c': {'key', 'value'},
    'd': T('test')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded['a'])
    print(data_loaded['b'])
    print(data_loaded['c'])
    print(data_loaded['d'])
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))
