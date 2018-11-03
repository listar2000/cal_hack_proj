def hello(name):
    assert isinstance(name, str)
    print('hello! {}'.format(name))