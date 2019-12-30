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

        def __init__(self, target_value, flag_char='$', param_flag='@', value_flag='^'):
            """
            init the VarIterator, and set some chars

            :param flag_char: the string param flag, default is $
            :param param_flag: the params' flag, default is @, the format is @param_name=param_value
            :param value_flag: the values' flag, default is ^, the format is ^value1 value2 or other^
            """
            self.__index = 0
            self.__open_index = -1
            self.__close_index = -1
            self.__flag_char = flag_char
            self.__param_flag = param_flag
            self.__value_flag = value_flag
            self.__target_value = target_value
            pass

    def __init__(self, target_value="", args={}):
        """
        the init method of the Replacer

        :param target_value: the target_value is will be replace string value
        :param args: the args is the value of replace
        """
        self._target_value = target_value
        self._args = args
