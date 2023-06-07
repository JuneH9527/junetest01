import pyperclip
import string

charset = set(string.punctuation)
str1 = '/product/api/instance_product/v1/client/product_list'


def replace_and_capitalize(string1, if_remove_first_char=0):
    """
    _后面的一位字母大写，并且去掉该_，再将/替换为_

    '/product/api/instance_product/v1/client/product_list'
    ->  product_api_instanceProduct_v1_client_productList
    """
    while string1.find('_') != -1:
        index = string1.find('_')
        if index == len(string1) - 1:
            string1 = string1[:index]
        else:
            string1 = string1[:index] + string1[index + 1].upper() + string1[index + 2:]
    string1 = string1.replace('/', '_')
    if if_remove_first_char:
        if string1[0] in charset:
            return string1[1:]
        else:
            return string1
    else:
        return string1


pyperclip.copy(replace_and_capitalize(str1, 1))
print(replace_and_capitalize(str1, 1))
