def test(**kargs):
    print(kargs)
    for key in kargs:
        print(key, kargs[key])

test()
test(name = '오쌤', age = 10)