# #!/usr/bin/env
# - ( a well designed program generally consists of several functions that call each other --
# and keep 'main body' code (not in a function) to a minimum)
# - the easiest function to manage is a "pure function": a function that does not refer to outside variables)
#
# - "module": simply, a file with python code
#     1.) script: executable code file
#     2.) module: library code #dual meaning

def dothis(x, y):
    return x + y

print(dothis(2, 3))

def print_these(x=None, y=0, z="yo!"):

print(x, y, z)

#argument matching modes
positional: each armgument is matched to a variable name in def
keyword: each argument is optional, and specifies a default valu in def
variable positional: any number of positional args(will be a tuple) can be passed
    # def printthese(*arg):
    #     print(arg)
    # printthese(2, 4, 5, 8, 7)
variable keyword: any keyword key/value can be passed
    def print_this(**kwargs):
        print(kwargs)
    print_this(this='that', other='another')
    print_this(zz=[1, 2, 3], yy={'a': 1, 'b': 2})

# Raise an exception
raise ValueError('OOOOOOPS!!!!')
