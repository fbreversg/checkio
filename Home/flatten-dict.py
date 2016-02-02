def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    
    #if len(dictionary) == 0:
    #    result
         
    
    while stack:
        print(stack)
        path, current = stack.pop()
        print("path: ", path, "current :", current)
        
        for k, v in current.items():
            print("k: ", k, "v: ", v)
            if len(v) == 0:
                result["/".join((path + (k,)))] = ""
            elif isinstance(v, dict):
                stack.append((path + (k,), v))
                print (stack)
                print("isInstance")
            else:
                result["/".join((path + (k,)))] = v
                print("else")
                
    print (result)
    print ("----------------------")
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    """assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    """
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
"""
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    """