'''
Proyecto # 1 

Mayra Salazar
Miguel Flores
'''

import sys

def bfs(): 
    pass


def main():
    mapfile = ""
    try:
        mapfile = sys.argv[1]
    except IndexError:
        mapfile = None
        print("Elija un mapa válido")

    if mapfile is None:
        sys.exit(1)

    with open(mapfile, 'r+') as  map:
        pass
    


if __name__ == '__main__':
    main()