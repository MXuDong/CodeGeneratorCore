"""
The element build config, the element will use this config to build the Elements.
"""
from cores.rules.element import Element


# fixme the repeat element.
# update the complete element
def update_hock(be_search, target_value):
    for item in be_search:
        for inner_item in item.get("sons"):
            has_type = inner_item.get("type") is not None
            if not has_type:
                if target_value.get("name") == inner_item.get("name"):
                    inner_item.update({'sons': target_value.get("sons")})
                    inner_item.update({'type': target_value.get("type")})
            else:
                update_hock([inner_item], target_value)


# update the now element
def update_from_template(be_search, target_value):
    for sons in target_value.get("sons"):
        for temp in be_search:
            if sons.get("name") == temp.get("name"):
                sons.update({"sons": temp.get("sons")})
                sons.update({"type": temp.get("type")})


class RuleConfig:
    """
    Config the rules, it provide some method to build.
    """

    def __init__(self):
        self._tree = []

    def _init_by_list(self, dicts, root_element, temp_element):
        res = []
        if not isinstance(dicts, list):
            raise Exception("element error is not list")
        out_element = None
        for item in dicts:
            if isinstance(item, dict):
                for key in item.keys():
                    inner_value = item[key]
                    element_type = ""
                    element_name = key
                    element_require = True
                    sons = []

                    if isinstance(inner_value, dict):
                        if "type" in inner_value.keys():
                            element_type = inner_value.get("type")
                        else:
                            raise Exception("\'" + element_name + "\' must has type.")

                        if "require" in inner_value.keys():
                            temp = inner_value.get("require")
                            if isinstance(temp, bool):
                                element_require = temp

                        if "elements" in inner_value.keys():
                            inner_list = inner_value.get("elements")
                            if isinstance(inner_list, list):
                                for inner_element in inner_list:
                                    if isinstance(inner_element, dict):
                                        for inner_element_key in inner_element.keys():
                                            inner_element_values = inner_element.get(inner_element_key)
                                            if not isinstance(inner_element_values, dict):
                                                raise Exception(
                                                    "Unknown error when deal the \'" + inner_element_key + "\'")
                                            if inner_element_values.get("type") is None:
                                                inner_element_require = True
                                                if "require" in inner_element_values.keys():
                                                    inner_temp = inner_element_values.get("require")
                                                    if isinstance(inner_temp, bool):
                                                        inner_element_require = inner_temp
                                                sons.append(
                                                    {'name': inner_element_key, "require": inner_element_require})
                                            else:
                                                temp_res = self._init_by_list([inner_element], root_element,
                                                                              temp_element)
                                                if temp_res is not None:
                                                    sons.append(temp_res)
                                    else:
                                        sons.append(
                                            {'name': inner_element, "require": True})
                    # 查找元素，并对原有数据进行添加

                    element_item = {'name': key, 'require': element_require, 'type': element_type, 'sons': sons}
                    out_element = element_item
                    update_hock(root_element, element_item)
                    update_hock(temp_element, element_item)

                    if key == 'root':
                        root_element.append(element_item)
                    else:
                        temp_element.append(element_item)

                    res.append(element_item)
        update_from_template(temp_element, out_element)
        if len(res) == 1:
            return res[0]

    def init_by_list(self, target_value):
        res_element = []
        temp_element = []
        self._init_by_list(target_value, res_element, temp_element)
        print(res_element)
        print(temp_element)
