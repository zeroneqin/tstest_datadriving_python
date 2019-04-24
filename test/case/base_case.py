#coding:utf-8

from __future__ import unicode_literals
import pytest
import logging
from base_suite import  BaseSuite

class BaseCase(BaseSuite):



    @pytest.fixture(scope="function", autouse=True)
    def case_fixture(self):
        logging.info("Before case")
        yield
        logging.info("After case")
