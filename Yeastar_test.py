import pyperclip
import string_handler


class YeastarTestTools(object):
    def __init__(self):
        self.sh = string_handler.StringHandler()

    def testcase_rename(self, old_casename, copy=True):
        new_casename = self.sh.replace_and_capitalize(old_casename, '_').replace('/', '_')[1:]
        if copy:
            pyperclip.copy(new_casename)
        return new_casename


if __name__ == '__main__':
    str1 = '/product/api/instance_product/v1/client/product_list'

    ytt = YeastarTestTools()
    print(ytt.testcase_rename(str1))
