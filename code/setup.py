# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 00:04:40 2015

@author: czl
"""

from index_module import IndexModule
from recommendation_module import RecommendationModule
from datetime import *


print('-----start indexing time: %s-----'%(datetime.today()))
im = IndexModule('../config.ini', 'utf-8')
im.construct_postings_lists()
print('-----start recommending time: %s-----'%(datetime.today()))
rm = RecommendationModule('../config.ini', 'utf-8')
rm.find_k_nearest(5, 25, 10)
print('-----finish time: %s-----'%(datetime.today()))