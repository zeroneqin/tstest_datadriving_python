#coding:utf-8

from __future__ import unicode_literals
import pytest
import logging
import ConfigParser
import os

class BaseSuite(object):
    URL = ""





    @pytest.fixture(scope="session", autouse=True)
    def suite_fixture(self):
        logging.info("Before test")
        config_parser = ConfigParser.ConfigParser()
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        BaseSuite.ROOT_PATH = root_path
        config_path = root_path +"/config/tstest.cfg"
        config_parser.read(config_path)
        BaseSuite.URL = config_parser.get("base_info", "url")
        yield

        logging.info("After test")
        pass



