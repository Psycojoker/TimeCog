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

    for event_title, procedures in organisation.items():
        for procedure in procedures:
            pass
