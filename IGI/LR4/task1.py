from utilities import CsvSerializer, PickleSerializer
from entities import Tree
from decorators import try_again_decorator
import data


def get_serializer():
    '''Returns csv/pickle serializer based on user choice.'''
    
    type = input('Choose option (csv/pickle): ')

    while not type.lower() in ['csv', 'pickle']:
        type = input('Try again! csv/pickle? ')

    return CsvSerializer() if type.lower() == 'csv' else PickleSerializer()


@try_again_decorator
def find_and_print_trees(trees):
    askname = input("Enter type to find\n")
    for tree in trees:
        if tree.name == askname:
            print(tree)


@try_again_decorator
def task1():
    '''Serilizes and deserializes given dictionary using csv and pickle.'''

    serializer = get_serializer()

    fileName = 'trees'

    print(f'Given data:\n{data.trees}\n')

    try:
        serializer.serialize(fileName, data.trees, data.columnNames)
        trees = serializer.deserialize(fileName)
    except OSError as err:
        print(f'File error: {err}')
    else:
        print(f'Deserialized data:\n{trees}\n')
        allsum = sum([tree.count for tree in trees])
        print(f'Count of trees:{allsum}')
        print(f'Count of normal trees:{sum([tree.countOfNorm for tree in trees])}')
        print(f'Count % of sick trees:{sum([(tree.count - tree.countOfNorm) for tree in trees]) / allsum * 100}%')

        print('Trees types:')
        names = set({tree.name for tree in trees})
        for nm in names:
            namesum = sum([tree.count for tree in trees if tree.name == nm])
            print(f'% for {nm} is {namesum / allsum * 100}%')

        find_and_print_trees(trees)
