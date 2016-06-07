#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree
except ImportError:
  import xml.etree.cElementTree as ElementTree
import idol.aci as aci
import idol.edk as edk
import urllib
import string
import re

def query(q_text='',q_allowoverlaps=False,q_allowmultipleresults=False,q_grammars=None):
  delimiter = "\t"
  # idol server parameters
  query_action = "EduceFromText"
  query_params = ""
  query_valid = False
  if q_text != '':
    query_params = query_params + "&text=" + q_text
    query_valid = True
  if q_allowoverlaps == True:
    query_params = query_params + "&AllowOverlaps=true"
  if q_allowmultipleresults == True:
    query_params = query_params + "&AllowMultipleResults=true"
  if q_grammars != None:
    query_params = query_params + "&Grammars=" + q_grammars
  if query_valid == False:
    print "Missing query parameter: text is required."
    return
  autnresponse = edk.action(query_action+query_params)
  response = autnresponse.find("./response").text
  if response == "SUCCESS":
    for hit in autnresponse.findall(
      "./responsedata/{http://schemas.autonomy.com/aci/}hit"):
      # print ElementTree.tostring(hit)
      nt = hit.find("./normalized_text").text
      print nt
  else:
    print "ACI exception: "+response+"|"+ElementTree.tostring(autnresponse)
  return autnresponse
