import string

charset = set(string.punctuation)


class StringHandler(object):
    def __init__(self):
        pass

    def replace_and_capitalize(self, input_str, replace_str):
        """
            功能：replace_str后面的一位字母大写，并将replace_str去掉。

            str1 = '/product/api/instance_product/v1/client/product_list'
            replace_and_capitalize(str1, '_')
            ->
            /product/api/instanceProduct/v1/client/productList
        """
        replace_str_len = len(replace_str)
        while input_str.find(replace_str) != -1:
            index = input_str.find(replace_str)
            if index + replace_str_len == len(input_str):       # 确保replace_str在最后一位时，无需做大写处理
                input_str = input_str[:index]
            else:
                input_str = input_str[:index] + input_str[index + replace_str_len].upper() + input_str[index + 1 + replace_str_len:]

        return input_str

