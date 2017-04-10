from os import listdir, system

for archivo in listdir('.'):
    if archivo[-3:] == '.py':
        system('autopep8 --in-place --aggressive --aggressive {}'.format(archivo))
        print(archivo)
