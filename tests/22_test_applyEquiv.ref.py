







def kwfunc(**kwargs):
    print kwargs.items()

def argsfunc(*args):
    print args

def no_apply(*args, **kwargs):
    print args
    print kwargs.items()
    argsfunc(34)
    foo = argsfunc(*args)
    argsfunc(*args)
    argsfunc(34, *args)
    kwfunc(**kwargs)
    kwfunc(x=11, **kwargs)
    no_apply(*args, **kwargs)
    no_apply(34, *args, **kwargs)
    no_apply(x=11, *args, **kwargs)
    no_apply(34, x=11, *args, **kwargs)
    no_apply(42, 34, x=11, *args, **kwargs)

no_apply(1, 2, 4, 8, a=2, b=3, c=5)
