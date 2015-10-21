from django.db import transaction


cog_functions = {}

def expose(function):
    cog_functions["%s.%s" % (function.__module__.split(".")[-1], function.__name__)] = function
    return function


def click(organisation_name, organisation):
    organisation_name = organisation_name.replace(".yaml", "").replace(".yml", "")
    print "[%s]" % organisation_name

    if "locations" in organisation:
        locations = organisation["locations"]
        del organisation["locations"]
    else:
        locations = {}

    for kind, functions_call in organisation.items():
        print "[%s:%s]" % (organisation_name, kind)
        for function, arguments in functions_call.items():
            if function not in cog_functions:
                raise Exception("'%s' is not an available function, available functions are:\n    * %s\n" % (function, "\n    * ".join(cog_functions.keys())))

            with transaction.atomic():
                print "[%s:%s:%s]" % (organisation_name, kind, function)
                cog_functions[function](organisation=organisation_name, kind=kind, locations=locations, **arguments)
