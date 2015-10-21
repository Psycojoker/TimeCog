from django.template import Engine


class InvalidVarException(object):
    def __mod__(self, missing):
        try:
            missing_str = unicode(missing)
        except:
            missing_str = 'Failed to create string representation'
        raise Exception('Unknown template variable %r %s' % (missing, missing_str))

    def __contains__(self, search):
        if search == '%s':
            return True
        return False


Template = Engine(debug=True, string_if_invalid=InvalidVarException()).from_string
