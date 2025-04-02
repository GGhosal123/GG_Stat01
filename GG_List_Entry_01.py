## Contains Functions for List Entry

def gg_list_entry_int (n):
    l1= []
    # Append elements to the list 1
    for i in range(n):
        element = int(input(f"Enter element for List {i+1}: "))
        l1.append(element)
    print("List:", l1)
    return l1

def gg_list_entry_char (n):
    l1= []
    # Append elements to the list 1
    for i in range(n):
        element = input(f"Enter element for List {i+1}: ")
        l1.append(element)

    print("List:", l1)
    return l1

def gg_list_entry_str (n):
    l1= []
    # Append elements to the list 1
    for i in range(n):
        element = input(f"Enter element for List {i+1}: ")
        l1.append(element)

    return l1