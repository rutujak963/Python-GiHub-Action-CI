# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:43:22 2020

@author: Admin
"""
import sys
sys.path.insert(1, '.')
from src.app import index
#import unittest

def test_index():
    assert index() == "Welcome to CI Project"
        
'''
class RegisterNewInstructor(unittest.TestCase):
    def test_index():
        assert index() == "Welcome to CI Project"
'''