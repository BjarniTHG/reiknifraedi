# -*- coding: utf-8 -*-
"""skil_f2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CvGZP6ieFGZfmKxPDBixDI-yHQ0AIQCQ
"""

import re
class Skil(object):
  """fyrirlestradaemi 2 f. REI"""
  #Bjarni Þór Guðmundsson
  def f2(self,text):
    d = {e: text.count(e) for e in sorted(set(text))}
    return list(d.values())