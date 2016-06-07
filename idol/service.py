#!/usr/bin/env python
import httplib
import config

def action(action_param_value_pairs):
  # build connection to IDOL
  conn = httplib.HTTPConnection(config.server+":"+str(config.service_port))
  conn.request("GET", "/action="+action_param_value_pairs)
  r1 = conn.getresponse()
  # read the xml as a string
  s = r1.read()
  conn.close()

  # return raw text
  return s
