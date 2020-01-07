"""
Replacer in the cores package, it provide some method and class to deal the string of args or values.

:author: MXuDong
"""
from exceptions.exceptions import ConvertException


class Replacer:
    """
    Replacer provides some method for the string replace

    :author: MXuDong
    """

    def __init__(self, target_value="", args={}):
        """
        the init method of the Replacer

        :param target_value: the target_value is will be replace string value
        :param args: the args is the value of replace
        """
        self._args = args
        self.__var_iterator = VarIterator(target_value=target_value)
        while self.__var_iterator.has_next():
            self.__var_iterator.get_var()


class VarIterator:
    """
    Replacer helper, for the replace the value

    It is an iterator of the string param value
    """

    def __init__(self, target_value="", flag_char='$', param_flag='@', value_flag='^', convert_flag="&"):
        """
        init the VarIterator, and set some chars

        and for the flag must be different, else will has some error for convert_flag

        :param target_value: the target value, which will be replace
        :param flag_char: the string param flag, default is $
        :param param_flag: the params' flag, default is @, the format is @param_name=param_value
        :param value_flag: the values' flag, default is ^, the format is ^value1 value2 or other^
        :param convert_flag: the values' flag, default is &, for the
            flag_char, param_flag, value_flag, convert_flag convert_flag will be turn to itself by
            convert_flag
        """
        self._index = 0
        self._open_index = -1
        self._close_index = -1
        self._flag_char = flag_char
        self._param_flag = param_flag
        self._value_flag = value_flag
        self._convert_flag = convert_flag
        self._target_value = target_value
        self._flag_mod = False

    # Todo: recode func body, the has_next will change __index value to next params
    def has_next(self):
        """
        if the target value has next param, it will return true, else return false
        :return: boolean
        """
        while self._index < len(self._target_value):
            if self._target_value[self._index] == self._flag_char:
                # 前面没有数据，因此不存在转义符，一定存在
                if self._index == 0:
                    self._flag_mod = True
                    return True
                # 前面字符不是转义符
                if self._target_value[self._index - 1] != self._convert_flag:
                    self._flag_mod = True
                    return True
            if self._index != 0:
                # 上一个字符为转义符，对该数据进行转义
                if self._target_value[self._index - 1] == self._convert_flag:
                    if self._target_value[self._index] in [
                        self._convert_flag,
                        self._flag_char,
                        self._param_flag,
                        self._value_flag
                    ]:
                        self._target_value = self._target_value[: self._index - 1] + self._target_value[
                                                                                       self._index:]
                    else:
                        # 非法数据
                        raise ConvertException("invalid convert char :" + self._target_value[self._index])
            self._index += 1
        # 能够循环结束，没有数据
        return False

    def get_var(self):
        """
        get the VarItem for the param, it will return next params, and if the param has no close char_flag, it will
        throw the exception
        """
        if not self._flag_mod:
            raise ConvertException("Get next before get var.")
        self._index += 1
        self._open_index = self._index

        while self._index < len(self._target_value):
            if self._target_value[self._index] == self._flag_char:
                if self._target_value[self._index - 1] != self._convert_flag:
                    self._flag_mod = False
                    self._index += 1
                    return VarItem(self._target_value[self._open_index: self._index - 1])
            self._index += 1

        self._flag_mod = False
        raise ConvertException("invalid param, can't find the close flag in the param, and the open flag is :" +
                               str(self._open_index))


class VarItem:
    """
    this class for the param item, provide some method for the deal.
    """

    def __init__(self, target_value):
        self._params = {}
        self._value = target_value

    def _parse_value(self):

