# Odd and even
The following python expression evaluates to True:
```
(lambda _: (lambda x:{*zip([_ for _ in x[0] for _ in x[1]],
                           [_ for _ in x[1] for _ in x[0]])})([
            *map(range,[2,_])]))(10) == {*enumerate([_%2 for _ in range(10)])}
```
