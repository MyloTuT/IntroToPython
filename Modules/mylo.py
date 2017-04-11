""" mylo.py: print the "Hello World" message """

def hello(arg):
    print('hello, {}!'.format(arg))

def main():
    hello('Python')

if __name__ == '__main__':
    main()
