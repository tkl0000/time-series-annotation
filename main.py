import matplotlib.pyplot as plt
import sys
import pandas as pd

path = ""
marker = ""
df = ""

def exit():
    global path
    df.to_csv(path, index=False)
    print('Saved.')

def menu():
    global df
    global marker
    plt.ion()
    plt.plot(df.iloc[:,0], df.iloc[:,1])
    plt.show()
    print('Commands:')
    print('- set [marker]')
    print('- [begin] [end]')
    print('- exit')
    while (True):
        command = input().split(' ')
        if (command[0] == 'set'):
            marker = command[1]
            print(f'Annotator set to {marker}.')
        elif (command[0] == 'exit'):
            exit()
            return
        else:
            begin = int(command[0])
            end = int(command[1])
            df.loc[begin-2:end-2, 'annotation'] = [marker] * (end-begin+1)
            print(df['annotation'])

def get_path():
    global df
    global path
    print('Enter .csv path: ')
    path = input()
    df = pd.read_csv(path)
    df['annotation'] = [''] * df.shape[0]
    menu()

def main():
    global df
    global path
    if (len(sys.argv) == 1):
        get_path()
    else:
        path = sys.argv[1]
        df = pd.read_csv(path)
        df['annotation'] = [''] * df.shape[0]
        menu()

if (__name__ == '__main__'):
    main()