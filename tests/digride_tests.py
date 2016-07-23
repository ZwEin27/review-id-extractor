# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-22 18:34:22


import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digride import DIGRIDE
import groundtruth

def cmp_extraction(ext1, ext2):
    # ext1_len = len(ext1)
    # ext2_len = len(ext2)
    # if ext1_len != ext2_len:
    #     return False
    # return True
    return set(ext1) == set(ext2)

class TestDIGRIDEMethods(unittest.TestCase):
    def setUp(self):
        self.groundtruth_data = groundtruth.load_groundtruth()
        
    def tearDown(self):
        pass

    def test_digride(self):
        total = 0
        correct = 0
        for data in self.groundtruth_data:
            text = data['text']
            ext_gt = data['extraction']
            ext_pd = DIGRIDE.extract(text)
            
            if cmp_extraction(ext_gt, ext_pd):
                correct += 1
            else:
                print '#'*50
                print '### original ###'
                print text.encode('ascii','ignore')
                print '### groundtruth data ###'
                print ext_gt
                print '### extracted data ###'
                print ext_pd

            total += 1
        print 60*'-'
        print 'pass', correct, 'out of', total

    def test_digride_text(self):
        text = ''
        print DIGRIDE.extract(text)
            

if __name__ == '__main__':
    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestDIGPEMethods('test_digride'))
        # suite.addTest(TestDIGPEMethods('test_digride_text'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

