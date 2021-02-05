def plus_value(x):
    print(f'plus_value {x}')
    def plus(y):
        print(f'value y {y} value x {x}')
        return x + y
    print(f'end {x}')
    return plus


new_func = plus_value(10)
print(f'print1 {new_func(1)}')
new_func2 = plus_value(new_func(100))
print(f'print2 {new_func2(2)}')
print(f'print3 {plus_value(10)(9)}')