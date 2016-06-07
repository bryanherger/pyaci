#!/usr/bin/env python
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree as ET
except ImportError:
  import xml.etree.cElementTree as ET
import idol_query
import edk_query

idol_query.query("dasatinib")
idol_query.query(q_text="dasatinib",q_maxresults=10)
idol_query.query()
print ET.tostring(idol_query.query(q_text="dasatinib",q_maxresults=1))
edk_query.query("Check out espn.com for the latest Boston Red Sox news!")
edk_query.query("Check out espn.com for the latest Boston Red Sox news!",True,True)
edk_query.query("Check out espn.com for the latest Boston Red Sox news!",q_grammars='../grammar/internet.ecr')
print ET.tostring(edk_query.query("Check out espn.com for the latest Boston Red Sox news!"))


