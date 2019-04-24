#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
from __future__ import unicode_literals


import os
import sys
import logging


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
LOG_FORMAT = "[%(asctime)s]-[%(levelname)s]-[%(module)s]-[%(message)s]"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='../../log/tstest.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
