#!/usr/bin/env python

def get_object(object, key):
    for dictkey, dictvalue in object.items():
        if key == dictkey:
            return dictvalue
        else:
            dictvalue = get_object(dictvalue, key)
    return dictvalue

if __name__ == '__main__':
    object_sample = {"a": {"b": { "c": "d" }}}

    ## Tests 1 Check for the right dict value
    val = get_object(object_sample, "c")
    if val == 'd':
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    # Test 2 Check if the type of returned object is dictionary
    another_object = {"x": {"y": {"z": "a"}}}
    val = get_object(another_object, "x")
    if type(val) is dict:
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    # Test 3 check if returned value is expected
    val = get_object(another_object, "y")
    if val["z"] == "a":
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    # Test 4 Check if the returned value is right key of dict
    val = get_object(another_object, "x")
    if list(val.keys())[0] == "y":
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")
