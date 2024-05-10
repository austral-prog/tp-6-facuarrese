def remove_element(list_to_remove_element):
    length=len(list_to_remove_element)
    print=length
    if length>0:
        del list_to_remove_element[0]
    if length>4:
        del list_to_remove_element[4]
    if length>6:
        del list_to_remove_element[5]
    return (list_to_remove_element)
def add_elements(lista):
    lista.append('Yellow')
    lista.insert(0,'pink')
    return lista
def is_empty(lista):
    if len(lista) == 0:
        print ("It is empty")
    else:
        print ("It is not empty")
def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>3 and len(list_to_compare2)>3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return 0==1

    # Remove this line and implement
def list_of_lists(list_of_lists_to_modify):
    return (list_of_lists_to_modify[0][0:2],list_of_lists_to_modify[1][1:len(list_of_lists_to_modify[1])-1],list_of_lists_to_modify[2][-2:])
