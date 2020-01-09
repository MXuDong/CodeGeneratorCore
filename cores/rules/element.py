"""
The doc tree, use this to convert. All the yaml will be convert to this format.
"""


class Element:
    """
    all value will be converted to this class.
    """

    def __init__(self, name):
        self._name = ""
        self._value = None
        self.type = None
