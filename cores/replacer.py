"""
Replacer in the cores package, it provide some method and class to deal the string of args or values.

:author: MXuDong
"""


class Replacer:
    """
    Replacer provides some method for the string replace

    :author: MXuDong
    """

    class VarIterator:
        """
        Replacer helper, for the replace the value

        It is an iterator of the string param value
        """

    def __init__(self, target_value="", args={}):
        """
        the init method of the Replacer

        :param target_value: the target_value is will be replace string value
        :param args: the args is the value of replace
        """
        self._target_value = target_value
        self._args = args
