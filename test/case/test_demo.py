#coding:utf-8

from __future__ import unicode_literals
import logging
import pytest
import os
import xlrd
import ConfigParser
import time



from tstest.po.req.demo_req_po import DemoReqPO
from tstest.po.req.demo_req_po_detail import DemoReqPODetail
from tstest.so.demo_so import DemoSO
from tstest.vo.demo_vo import DemoVO

from base_case import BaseCase
from base_suite import  BaseSuite


global okSet
okSet = [\
'什么是个人账户总负债',\
'什么是个人账户总资产',\
'什么是企业总负债',\
'什么是企业总资产',\
'什么是到期日',\
'什么是总负债',\
'什么是总资产',\
'什么是管理费',\
'基金管理费',\
'理财产品到期日',\
'定期存款到期日',\
'基金、理财产品交易日说明',\
'账户管理费',\
'基金-关系-同类型基金',\
'基金-关系-基金公司',\
'基金-关系-所属类型',\
'基金-关系-托管公司',\
'基金-对比（模糊）',\
'基金-属性-业绩基准',\
'基金-属性-代码',\
'基金-属性-全称',\
'基金-属性-净值',\
'基金-属性-初始规模',\
'基金-属性-发行日期',\
'基金-属性-成立分红',\
'基金-属性-成立日期',\
'基金-属性-手续费',\
'基金-属性-托管费',\
'基金-属性-投资仓位',\
'基金-属性-投资对象',\
'基金-属性-投资目标',\
'基金-属性-投资策略',\
'基金-属性-投资风格',\
'基金-属性-收益',\
'基金-属性-收益排名',\
'基金-属性-涨幅',\
'基金-属性-简介',\
'基金-属性-简称',\
'基金-属性-管理费',\
'基金-属性-营销费',\
'基金-属性-评级',\
#'基金-属性-赎回费',\
'基金-属性-赎回起始日',\
'基金-属性-运作方式',\
'基金-属性对比-业绩',\
'基金公司-属性-旗下基金数量',\
'基金公司-属性-旗下基金经理数量',\
'基金经理-属性-学历',\
'推荐理由-基金推荐理由',\
'组合业绩表现',\
'金融市场.表现',\
'金融概念-定义',\
'基金类型-区分'
]


def get_data():
    config_parser = ConfigParser.ConfigParser()
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = root_path + "/config/tstest.cfg"
    config_parser.read(config_path)
    case_file = config_parser.get("case_info", "case_file")
    case_sheet = config_parser.get("case_info", "case_sheet")
    case_sheet_u = case_sheet.decode('utf-8')

    full_path = root_path + case_file
    all_rows=[]
    try:
        wb = xlrd.open_workbook(full_path)
        ws = wb.sheet_by_name(case_sheet_u)
        #skip header
        for row in range(1,ws.nrows):
            all_columns = []
            senario = ws.cell(row, 0).value
            intent = ws.cell(row, 1).value
            question = ws.cell(row, 2).value
            expect_answer = ws.cell(row, 3).value
            all_columns.append(senario)
            all_columns.append(intent)
            all_columns.append(question)
            all_columns.append(expect_answer)
            all_rows.append(all_columns)
    except Exception as e:
        logging.error("Get exception:"+e.message)
    return all_rows

class TestCase(BaseCase):

    @pytest.mark.parametrize("senario,intent,question,expect_answer", get_data())
    def test_case(self,senario,intent,question,expect_answer):

        logging.info("Start case")

        logging.info("Senario:" + senario)
        logging.info("Intent:" + intent)
        logging.info("Question:" + question)
        logging.info("Expect answer regex:" + expect_answer)

        if not intent in okSet:
            logging.warn("Skip, not ready, no need to run")
            pytest.skip("Skip, not ready, not need to run")
        else:
            demo_req_po_detail = DemoReqPODetail()
            demo_req_po_detail.senario = senario
            demo_req_po_detail.intent = intent
            demo_req_po_detail.question = question
            demo_req_po = DemoReqPO()
            demo_req_po.user_id = 123
            demo_req_po.appkey = "demokey123"
            demo_req_po.detail = demo_req_po_detail
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            demo_res_po = DemoSO.send_request_wrapper(BaseSuite.URL, demo_req_po, headers)
            DemoVO.verify(demo_res_po,expect_answer)
            logging.info("End case")
        time.sleep(0.1)






