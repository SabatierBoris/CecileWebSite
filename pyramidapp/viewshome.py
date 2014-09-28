"""
Blabla
"""
from pyramid.view import view_config


class Test(object):
    """
    Bllibli
    """
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "<Test value='%s' />" % (self.value)


class SubTest(Test):
    """
    Blublu
    """
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    def __init__(self, value):
        super(SubTest, self).__init__(value)
        self.new_value = "BLABLA"

    def __str__(self):
        return "<SubTest value='%s' />" % (self.value)


@view_config(route_name='home', renderer='home.mak')
def home(request):
    """
    Bouboup
    """
    request = request
    val1 = Test('blabla')
    val2 = SubTest('blublu')
    return {'project': 'my project', 'plop': [val1, val2]}
