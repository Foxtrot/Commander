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
		config = ConfigParser.RawConfigParser()
		config.read('commander.conf')
		if config.has_section('Network') & config.has_section('Commands'):
			print "[*] Valid configuration file... proceeding"
			print " "
		else:
			print "[!] Configuration does not have Network or Command blocks."
			sys.exit(1)
	elif os.path.exists('commander.conf'):
		print "[*] Found configuration file!"
		print " "
		config = ConfigParser.RawConfigParser()
		config.read('commander.conf')
		if config.has_section('Network') & config.has_section('Commands'):
			print "[*] Valid configuration file... proceeding"
			print " "
		else:
			print "[!] Configuration does not have Network or Command blocks."
			sys.exit(1)
	else:
		print "[!] Could not find configuration file! Exiting..."
		sys.exit(1)


class Commands(Commander):
	def availableCommands():
		print "[*] Listing commands..."
		
		commands = Commander.config.options('Commands')
		for command in commands:
			print "    " + command

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