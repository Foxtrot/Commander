#!/usr/bin/env python

"""
Commander.py - Python Backend for the WiFi Pineapple Commander module.

Foxtrot (C) 2016 <foxtrotnull@gmail.com>
"""

import ConfigParser
import os
import sys

class Commander:
	print "[*] WiFi Pineapple Commander"
	print "[*] Looking for Commander.conf..."
	if os.path.exists('/pineapple/modules/Commander/Python/commander.conf'):
		print "[*] Found configuration file!"
		print " "
		config = ConfigParser.ConfigParser()
		config.read('commander.conf')
	elif os.path.exists('commander.conf'):
		print "[*] Found configuration file!"
		print " "
		config = ConfigParser.ConfigParser()
		config.read('commander.conf')
	else:
		print "[!] Could not find configuration file! Exiting..."
		sys.exit(1)


class Commands(Commander):
	def availableCommands():
		print Commander.config.items('Commands')
		print " "

	availableCommands()


class Client(Commander, Commands):
	def connect():		
		server = Commander.config.get('Network', 'Server')
		port = Commander.config.get('Network', 'Port')
		nickname = Commander.config.get('Network', 'Nickname')
		channel = Commander.config.get('Network', 'Channel')

		print "[*] Using these connection settings! :"
		print "    Server: " + server
		print "    Port: " + port
		print "    Nickname: " + nickname
		print "    Channel: " + channel



	connect()