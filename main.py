import os
import unittest
from tomorrow3 import threads
from BeautifulReport import BeautifulReport

from tpshop.TestCase import HTMLTestRunner


class TestSuit:
    DIR = os.path.dirname(os.path.abspath(__file__))
    casepath = DIR + '/TestCase'
    reportpath = DIR + '/report' + '/report.html'

    def CreateSuite(self, case_path=casepath, rule="test_*.py", report=reportpath):
        Suite = unittest.defaultTestLoader.discover(case_path, pattern=rule)
        return Suite

    def report(self, report=reportpath):
        with open(report, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, description='web自动化测试报告', verbosity=2).run(self.CreateSuite())


# @threads(2)
# def run(test_suite):
#     result = BeautifulReport(test_suite)
#     result.report(filename='report2.html', description='web报告', log_path=reportpath)


if __name__ == '__main__':
    test = TestSuit()
    test.report()
