import os

def getlines(filename, newlines=False):
    try:
        user_file = os.path.isfile(filename)
    except IndexError:
        exit('please input a file name')

    #fixed terrible logic by initiating an empty list to report back
    # loop results. Logic similar to 'readlines()'
    file_lines = []
    for lines in open(filename).readlines():
        file_lines.append(lines)

    if newlines == True:
        return file_lines
    else:
        return file_lines.rstrip()



def gettext(filename):
    try:
        open_file = open(filename)
    except IndexError:
        exit('please input a file name')

    return open(filename).read()



def getfields(filename, delimiter=None):
    try:
        user_file = os.path.isfile(filename)
    except IndexError:
        exit('please enter a file name')

    delimter_list = [',', ':', ' ', None]
    if delimiter not in delimter_list:
        raise ValueError('you entered a bad delimiter')

    inner_list = []
    outer_list = []
    open_file = open(filename)
    for lines in open_file.readlines():
        inner_list.append(lines)
        if delimiter in delimter_list:
            lines.split(delimiter)
        elif delimiter == None:
            lines.split()
        outer_list.append(inner_list)

    return outer_list
