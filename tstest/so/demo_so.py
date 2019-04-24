#coding:utf-8

from __future__ import unicode_literals

import requests
import logging
import jsonstruct

from tstest.po.res.demo_res_po import DemoResPO


class DemoSO(object):

    @classmethod
    def send_request(cls, base_url, ruyi_api_req_po,headers):
        json_body = jsonstruct.encode(ruyi_api_req_po)
        full_url = base_url
        logging.info("发送HTTP请求,URL:[%s]", full_url)
        logging.debug("发送HTTP请求,Body:[%s]",json_body)
        resp = requests.post(full_url, headers=headers ,data=json_body)
        logging.info("Receive http response,body:[%s]", resp.text)
        return resp



    @classmethod
    def send_request_wrapper(cls, base_url,demo_req_po,headers):
        res = cls.send_request(base_url, demo_req_po,headers)
        demo_res_po = jsonstruct.decode(res.content, DemoResPO)
        demo_res_po.status_code = res.status_code
        return demo_res_po


