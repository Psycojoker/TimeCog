functions = {}

def expose(function):
    functions["%s.%s" % (function.__module__, function.__name)] = function
    return function


def click(organisation):
    if "locations" in organisation:
        locations = organisation["locations"]
        del organisation["locations"]
    else:
        locations = {}

    for event_title, functions_call in organisation.items():
        for function, arguments in functions_call.items():
            if function not in functions:
                raise Exception("'%s' is not an available function, available functions are:\n%s\n" % (function, functions.keys()))
            print function, arguments
