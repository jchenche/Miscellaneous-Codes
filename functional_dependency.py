#!/usr/bin/env python3

#--- Created to assist with CSC370 (Database) Assignment 1 ---#
#--- This program prints out the candidate keys ---#

from itertools import combinations

def are_marked(target, marked):
    for x in target:
        if marked[x] == False:
            return False
    return True

def mark(right_side, marked):
    for x in right_side:
        marked[x] = True

def all_marked(marked):
    for x in marked:
        if x == False:
            return False
    return True

def get_keys(mapping, source):
    for x in source:
        print(mapping[x], end=", ")
    print()

def is_candidate_key(target, candidate):
    for x in candidate:
        if set(target) >= set(x): # test if target is a superset of some candidate key
            return False
    return True

def find_closure(starting_attrs, dependencies, marked):
    '''Scans all functional dependencies to mark'''
    for y in starting_attrs:
        marked[y] = True

    mark_happened = True
    while not (mark_happened == False or all_marked(marked)):

        mark_happened = False
        for left_side in dependencies.keys():

            if are_marked(left_side, marked) == True:
            # Only mark if everything on the left hand side is marked
                right_side = dependencies[left_side]

                if not are_marked(right_side, marked):
                # Don't mark if everything on the right hand side is already marked
                    mark(right_side, marked)
                    mark_happened = True

def dependency_format_verifier(string):
    count = 0
    for x in string:
        if x == ":":
            count += 1

    if count == 1:
        return True
    else:
        return False

def multi_stripping(target_list):
    for i in range(len(target_list)):
        target_list[i] = target_list[i].strip()

def main():

    num_attr = int(input("Enter the number of attributes: "))
    attributes = [-1 for x in range(num_attr + 1)]
    print("Enter the (distinct) names of the attributes below.")
    for i in range(1, len(attributes)):
        attributes[i] = input("Atribute {}: ".format(i)).strip()

    dependencies = {}
    print("Enter the functional dependencies following the format below and ")
    print("stop by pressing enter without giving a dependency.")
    print("A1, A2, ... , An : B1, B2, ... , Bm")
    print("Where A's are func dep that implies and B's are the ones being implied")
    print("For Example:")
    print("  ID : first name, last name, year of birth")
    print("  course code, school term : course offering")
    print()

    temp = ""
    while True:
        temp = input()
        if temp == "":
            break
        if dependency_format_verifier(temp) == False:
            print("This is not a valid format. Please enter again.")
            continue

        # Separate the functional dependencies into left and right side
        temp = temp.split(":")
        multi_stripping(temp)

        # Separate the left/right side dependencies into individual attributes
        left_side = temp[0].split(",")
        multi_stripping(left_side)
        right_side = temp[1].split(",")
        multi_stripping(right_side)

        # Turn the individual attributes into their corresponding attributes index
        for i in range(len(left_side)):
            left_side[i] = attributes.index(left_side[i])
        for i in range(len(right_side)):
            right_side[i] = attributes.index(right_side[i])

        dependencies[tuple(left_side)] = tuple(right_side)

    print("----------------------")

    size = len(attributes)
    candidate = []
    length = 1
    while length < size:

        attr_combinations = list(combinations(range(1, size), length))
        for x in attr_combinations:
            marked = [False for x in range(size)]
            marked[0] = True # Convenient for looping

            find_closure(x, dependencies, marked)
            if all_marked(marked) == True and is_candidate_key(x, candidate):
                # To print all superkeys, simply remove the second condition
                get_keys(attributes, x)
                candidate.append(x)

        length += 1

    print("Number of keys:", len(candidate))
    print("----------------------")

if __name__ == '__main__':
    main()  