#!/usr/bin/env python
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree as ET
except ImportError:
  import xml.etree.cElementTree as ET
import idol_query

idol_query.query("dasatinib")
idol_query.query(q_text="dasatinib",q_maxresults=10)
idol_query.query()
print ET.tostring(idol_query.query(q_text="dasatinib",q_maxresults=1))


