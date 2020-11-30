# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:43:22 2020

@author: Admin
"""
import sys
sys.path.insert(1, '.')
from src.app import index

def test_index():
    assert index() == "Python CI Project"