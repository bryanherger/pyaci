#!/usr/bin/env python
import httplib
import config
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree
except ImportError:
  import xml.etree.cElementTree as ElementTree

def action(action_param_value_pairs):
  # build connection to IDOL
  if config.aci_proto == "HTTP":
    conn = httplib.HTTPConnection(config.aci_server, config.aci_port)
  else:
    conn = httplib.HTTPSConnection(config.aci_server, config.aci_port)
  conn.request("GET", "/action="+action_param_value_pairs)
  r1 = conn.getresponse()
  # read the xml as a string
  s = r1.read()
  conn.close()

  # return raw text
  return ElementTree.fromstring(s)

