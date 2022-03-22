import time
import unittest
from selenium import webdriver


class kk(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
       print("mua")


    def test_sample1(self):
        print("mua1")

    def test_sample2(self):
        print("mua2")

    @classmethod
    def tearDownClass(cls):
        print("muafinal")