import numpy as np
import pandas as pd


def squares(x):
    return x ** 2


def doubles(x):
    return x * 2


if __name__ == '__main__':
    result1, result2 = squares(3), doubles(3)
    print(result1, result2)

    array = np.array([1,2,3])
    result1, result2 = squares(array), doubles(array)
    print(array)
    print(result1)
    print(result2)

    print()
    df = pd.DataFrame({
        'a':[1,2,3],
        'b':[4,5,6]
    })
    print(df)
    print(squares(df))
    print(doubles(df))

    result = df.apply(squares)
    print(result)

    print(np.sum([1,2,3]))
    result = df.apply(np.sum, axis=0)
    print(result)
    result = df.apply(np.sum, axis=1)
    print(result)

    emp = pd.read_csv('emp_df.csv')
    emp.apply()