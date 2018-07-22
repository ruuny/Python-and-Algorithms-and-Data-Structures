def  set_operations_with_dict():
    pairs = [('a', 1), ('b',2), ('c',3)]
    d1 = dict(pairs)
    print(d1)
    
    d2 = {'a':1, 'c':2, 'd':3, 'e':4}
    print(d2)
    
    union = d1.keys() & d2.keys()
    print(union)
    
    union_items = d1.items() & d2.items()
    print(union_items)
    
    subtraction1 = d1.keys() - d2.keys()
    print(subtraction1)
    
    subtraction2 = d2.keys() - d1.keys()
    print(subtraction2)
    
    subtraction_items = d1.items() - d2.items()
    print(subtraction_items)

    """ 딕셔너리의 특정 키를 제외한다. """
    d3 = {key: d2[key] for key in d2.keys() - {'c', 'd'}}
    print(d3)

if __name__ == '__main__':
    set_operations_with_dict()