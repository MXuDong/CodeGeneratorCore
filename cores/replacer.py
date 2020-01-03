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
            self.__index = 0
            self.__open_index = -1
            self.__close_index = -1
            self.__flag_char = flag_char
            self.__param_flag = param_flag
            self.__value_flag = value_flag
            self.__convert_flag = convert_flag
            self.__target_value = target_value

        # Todo: recode func body, the has_next will change __index value to next params
        def has_next(self):
            """
            if the target value has next param, it will return true, else return false
            :return: boolean
            """
            while self.__index < len(self.__target_value):
                if self.__target_value[self.__index] == self.__flag_char:
                    # 前面没有数据，因此不存在转义符，一定存在
                    if self.__index == 0:
                        return True
                    # 前面字符不是转义符
                    if self.__target_value[self.__index - 1] != self.__convert_flag:
                        return True
                if self.__index != 0:
                    # 上一个字符为转义符，对该数据进行转义
                    if self.__target_value[self.__index - 1] == self.__convert_flag:
                        if self.__target_value[self.__index] in [
                            self.__convert_flag,
                            self.__flag_char,
                            self.__param_flag,
                            self.__value_flag
                        ]:
                            self.__target_value = self.__target_value[: self.__index - 1] + self.__target_value[
                                                                                            self.__index:]
                        else:
                            # 非法数据
                            pass  # Todo throw new error
                self.__index += 1

    def __init__(self, target_value="", args={}):
        """
        the init method of the Replacer

        :param target_value: the target_value is will be replace string value
        :param args: the args is the value of replace
        """
        self._target_value = target_value
        self._args = args
