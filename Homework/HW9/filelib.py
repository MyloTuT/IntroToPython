def getlines(filename, newlines=False):
    try:
        open_file = open(filename)
    except (IndexError):
        exit('please input a file name')

    for lines in open(filename).readlines():
        if newlines == True:
            return lines
        else:
            return lines.rstrip()



def gettext(filename):
    try:
        open_file = open(filename)
    except (IndexError):
        exit('please input a file name')

    return open(filename).read()



def getfields(filename, delimiter=None):
    try:
        delimiter == ',', ':', ' ', None
    except ValueError:
        exit('please insert a comma, semi-colon, or space')
    try:
        open_file = open(filename)
    except IndexError:
        exit('please enter a file name')

    delimter_list = [',', ':', ' ']
    inner_list = []
    outer_list = []

    for lines in open_file.readlines():
        inner_list.append(lines)
        if delimiter in delimter_list:
            lines.split(delimiter)
        elif delimiter == None:
            lines.split()
        outer_list.append(inner_list)

    return outer_list
