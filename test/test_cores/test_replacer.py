from cores.replacer import Replacer

# strings = "abcdabcd"
# print(strings[:3] + strings[4:])

test = """
$$test
"""
test = """
$test$"""
test = """
test$$"""
test = """
test$test$test"""
test = """
test&$"""
test = """
test
$ @ &@test=^t&^est sdf
asdf ^$
"""

res = Replacer(test)

