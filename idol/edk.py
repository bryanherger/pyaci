#!/usr/bin/env python
import httplib
import config
try:
  # python 2.4.3 compatibility
  from elementtree import ElementTree
except ImportError:
  import xml.etree.cElementTree as ElementTree

def action(action_param_value_pairs):
  # build connection to eduction server
  if config.edk_proto == "HTTP":
    conn = httplib.HTTPConnection(config.edk_server, config.edk_aci_port)
  else:
    conn = httplib.HTTPSConnection(config.edk_server, config.edk_aci_port)
  conn.request("GET", "/action="+action_param_value_pairs)
  r1 = conn.getresponse()
  # read the xml as a string
  s = r1.read()
  conn.close()

  # return XML as element tree object
  return ElementTree.fromstring(s)

