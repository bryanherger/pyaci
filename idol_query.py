#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree
except ImportError:
  import xml.etree.cElementTree as ElementTree
import idol.aci as aci
import urllib
import string
import re

def query(q_text='',q_fieldtext='',q_databasematch='',q_maxresults=''):
  delimiter = "\t"
  # idol server parameters
  query_action = "Query"
  query_params = ""
  query_valid = False
  if q_text != '':
    query_params = query_params + "&text=" + q_text
    query_valid = True
  if q_fieldtext != '':
    query_params = query_params + "&fieldtext=" + q_fieldtext
    query_valid = True
  if q_text != '':
    query_params = query_params + "&databasematch=" + q_databasematch
  if q_text != '':
    query_params = query_params + "&maxresults=" + str(q_maxresults)
  if query_valid == False:
    print "Missing query parameter: text or fieldtext are required."
    return
  autnresponse = aci.action(query_action+query_params)
  response = autnresponse.find("./response").text
  if response == "SUCCESS":
    numhits = int(autnresponse.find(
      "./responsedata/{http://schemas.autonomy.com/aci/}numhits").text)
    if numhits > 0:
      print "Hits: "+str(numhits)
      for hit in autnresponse.findall(
        "./responsedata/{http://schemas.autonomy.com/aci/}hit"):
        doc = hit.find("{http://schemas.autonomy.com/aci/}content/DOCUMENT")
        print ElementTree.tostring(doc)
    else:
        print "Query succeeded, but returned no hits: "+ElementTree.tostring(autnresponse)
  else:
    print "ACI exception: "+response+"|"+ElementTree.tostring(autnresponse)
  return autnresponse

def csvquery(min_date='',max_date='',database=''):
  delimiter = "\t"
  # idol server parameters
  query_action = "Query&Text=DREALL&MinDate="+\
    min_date+"&MaxDate="+max_date+"&MaxResults=1000000&DocumentCount=true&"+\
	"databasematch="+database+"&print=none&printfields="
  # iterate over <autn:hit>
  keys = ['GSM_NO','DREDATE','DREDBNAME','CATEGORYTAG','EMPCATEGORYTAG','SENTIMENT']
  for key in keys:
    query_action = query_action+key+"%2C"
  autnresponse = aci.action(query_action)
  response = autnresponse.find("./response").text
  if response == "SUCCESS":
    numhits = int(autnresponse.find(
      "./responsedata/{http://schemas.autonomy.com/aci/}numhits").text)
    if numhits > 0:
      header = ""
      for col in keys:
        header = header+col+delimiter
      print header
      for hit in autnresponse.findall(
        "./responsedata/{http://schemas.autonomy.com/aci/}hit"):
        row = ""
        doc = hit.find("{http://schemas.autonomy.com/aci/}content/DOCUMENT")
        for col in keys:
          cell = doc.find(col)
          if cell != None:
            row = row+(cell.text).encode('utf-8')
          row = row+delimiter
        print row
