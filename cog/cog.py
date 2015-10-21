from django.db import transaction


cog_functions = {}

def expose(function):
    cog_functions["%s.%s" % (function.__module__.split(".")[-1], function.__name__)] = function
    return function


def click(organisation_name, organisation):
    if "locations" in organisation:
        locations = organisation["locations"]
        del organisation["locations"]
    else:
        locations = {}

    for event_title, functions_call in organisation.items():
        for function, arguments in functions_call.items():
            if function not in cog_functions:
                raise Exception("'%s' is not an available function, available functions are:\n    * %s\n" % (function, "\n    * ".join(cog_functions.keys())))

            with transaction.atomic():
                print "[%s]" % function
                cog_functions[function](organisation=organisation_name.replace(".yml", ""), title=event_title, **arguments)
