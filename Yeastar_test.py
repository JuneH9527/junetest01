import pyperclip
import string_handler


class YeastarTestTools(object):
    def __init__(self):
        self.sh = string_handler.StringHandler()

    # 1. 接口测试用例重命名
    def testcase_rename(self, old_casename, copy=True):
        new_casename = self.sh.replace_and_capitalize(old_casename, '_').replace('/', '_')[1:]
        if copy:
            pyperclip.copy(new_casename)
        return new_casename

    # 2. 合并日志sql、日志参数为完整的sql
    def sql_string_merge(self, sql_str, param_str, copy=True):
        def param_str_to_param_list(param_str):
            param_str = str(param_str)
            param_list = []
            for i in param_str.split('),'):                 # 1.按'),'分隔字符串，变成一个个列表
                i = i.strip()
                index = i.rfind('(')                        # 2.找最后一个'('的位置
                param_list.append(i[:index])
            return param_list

        param_list = param_str_to_param_list(param_str)      # 1.转成param_list
        print(param_list)
        str_cp = sql_str
        for i in param_list:        # 2.替换?项
            str_cp = str_cp.replace("?", f"'{i}'", 1)

        if copy:
            pyperclip.copy(str_cp)
        return str_cp


if __name__ == '__main__':
    ytt = YeastarTestTools()

    # 1. 接口测试用例重命名
    # str1 = '/product/api/instance_product/v1/client/product_list'
    # print(ytt.testcase_rename(str1))

    # 2. 合并sql与参数
    sql_str = """SELECT COUNT(*) FROM (SELECT i.id, i.uc_id, any_value(i.product_id) AS productId, any_value(i.product_types) AS productTypes, any_value(i.oem_id) AS oemId, any_value(i.sales) AS sales, any_value(i.master_id) AS masterId, any_value(i.slave_id) AS slaveId, any_value(i.device_bind_flag) AS deviceBindFlag, any_value(i.slave_device_type) AS slaveDeviceType, any_value(i.equipment_purchase_time) AS equipmentPurchaseTime, any_value(i.model) AS model, any_value(i.product_catalog_id) AS productCatalogId, any_value(i.product_catalog) AS productCatalogName, any_value(i.pid) AS pid, any_value(i.ycm_type) AS ycmType, any_value(i.admin_email) AS adminEmail, any_value(i.customer_email) AS customerEmail, any_value(i.partner_email) AS partnerEmail, any_value(i.distributor_email) AS distributorEmail, any_value(i.assign_customer) AS assignCustomer, any_value(i.assign_partner) AS assignPartner, any_value(i.assign_distributor) AS assignDistributor, CASE i.product_id WHEN 13 THEN (CASE WHEN u.colleagued = 0 THEN u.user_name ELSE u.owner_name END) ELSE any_value(i.owner_email) END AS ownerEmail, any_value(i.zone_code) AS zoneCode, any_value(i.offering_id) AS offeringId, any_value(i.product_no) AS productNo, any_value(i.ycm_sn) AS ycmSn, any_value(i.customer_country) AS customerCountry, any_value(i.partner_country) AS partnerCountry, any_value(i.distributor_country) AS distributorCountry, any_value(g.goods_name) AS goodsName, any_value(g.goods_short_name) AS goodsShortName, any_value(i.activation_status) AS activationStatus, any_value(ai.create_code_time) AS createCodeTime, any_value(ai.activation_method) AS activationMethod, any_value(g.`status`) AS status, any_value(g.auto_renew_status) AS autoRenewStatus, any_value(g.expire_time) AS expireTime, any_value(g.key_factor) keyFactor, any_value(g.key_factor_value) AS keyFactorValue, any_value(g.key_factor_unit) AS keyFactorUnit, any_value(g.id) AS planInstanceGoodsId, any_value(i.virtual_model) AS virtualModel, any_value(i.create_time) AS createTime, any_value(i.first_subscription_time) AS firstSubscriptionTime, any_value(yu.extensions_used) AS extensionsUsed, any_value(yu.pbx_number_used) AS pbxNumberUsed, any_value(ir.comments) AS comments, any_value(g.subscription_status) AS subscriptionStatus FROM instance i LEFT JOIN user u ON i.uc_id = u.uc_id LEFT JOIN instance_goods g ON g.instance_id = i.id AND g.goods_type = 'plan' AND (g.goods_status = 'valid' OR g.goods_status = 'expired') AND g.deleted = 0 LEFT JOIN instance_goods ga ON ga.instance_id = i.id AND ga.goods_type = 'addOn' AND (ga.goods_status = 'valid' OR ga.goods_status = 'expired') AND ga.deleted = 0 LEFT JOIN instance_activation_info ai ON ai.instance_id = i.id LEFT JOIN instance_ycm_used yu ON yu.instance_id = i.id LEFT JOIN instance_remark ir ON ir.instance_id = i.id AND ir.uc_id = ? WHERE (i.zone_code = ? AND i.product_id = ? AND i.deleted = ? AND (slave_device_type <> ? OR slave_device_type IS NULL) AND CONCAT_WS("", i.product_no, i.ycm_sn, i.customer_email, i.owner_email, i.partner_email, i.distributor_email, i.product_category_key, i.pid, i.oem_id, i.admin_email, u.user_name, u.owner_name, i.sales) LIKE '%pp-%') GROUP BY i.id ORDER BY i.create_time DESC) TOTAL"""
    param_str = "0(String), oversea(String), 12(String), 0(Integer), force_bind(String)"
    print(ytt.sql_string_merge(sql_str, param_str))

    # 3.1
