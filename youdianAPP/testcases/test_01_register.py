import unittest
import os
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR


file_url = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestRegister(unittest.TestCase):
    """ 注册相关类 """


    @data()
    def test_register(self):

        pass