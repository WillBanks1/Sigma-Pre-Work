
x = [20, 50, 12, 6, 14, 8]

def get_max_and_min(x):
    x = sorted(x)
    x = [x[0], x[-1]]

    return x

print(get_max_and_min(x))

