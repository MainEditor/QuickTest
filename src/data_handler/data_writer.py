def write_statistics(path, value):
    if value == None:
        return
    file = open(path, 'r').readlines()
    file[-1] = '	'.join(['STAT'] + file[-1][5:].split('	') + [str(value*100)]).replace('		', '	')
    print(file[-1])
    open(path, 'w').writelines(file)