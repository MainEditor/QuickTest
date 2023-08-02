def write_statistics(path, value):
    if value == None:
        return
    file = open(path, 'r').readlines()
    file[-1] = "STAT	" + '	'.join(map(str, file[-1].split('	')[1:] + [value*100]))
    open(path, 'w').writelines(file)