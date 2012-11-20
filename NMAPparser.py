#/usr/bin/env python
'''
This program runs NMAP outputs to XML and parses out the IP Address and open ports as objects
'''

#import re
#import cPickle as pickle
#import datetime
import xml.etree.ElementTree as ET
from commands import getoutput
#import re, urllib2, webbrowser
#import json as simplejson

def get_nmap_output_in_xml_object():
    command_line = 'nmap -T4 -A -p 1-1000 -oX -  localhost'
    nmap_xml_object = ET.fromstring(getoutput(command_line))    
    
    return nmap_xml_object

def parse_nmap_xml(nmap_object):
    level_1 = nmap_object.getchildren()
    host_info = level_1[3][1].attrib
    target = host_info['addr']
    
    ports_info = level_1[3][3][1].attrib
    open_ports = ports_info['portid']
    
    return target, open_ports

#import pdb; pdb.set_trace()
nmap_object = get_nmap_output_in_xml_object()
print parse_nmap_xml(nmap_object)
