#!/usr/bin/python

"""
Commander.py - Python Backend for the WiFi Pineapple Commander module.
Version 2 Codename: Electric Boogaloo

Foxtrot (C) 2016 <foxtrotnull@gmail.com>
"""

import os
import ConfigParser
import sys
import socket

class Commander(object):
	def __init__(self):
		print "[*] WiFi Pineapple Commander Module"

		if os.path.exists('commander.conf'):
			self.config = ConfigParser.RawConfigParser()
			self.config.read('commander.conf')
			if self.config.has_section('Network') and self.config.has_section('Security') and self.config.has_section('Commands') and self.config.has_section('Other'):
				print "[*] Valid configuration file found!"
				print ""
			else:
				print "[!] No valid configuration file found... Exiting!"
				sys.exit(1)

			self.server = self.config.get('Network', 'Server')
			self.port = self.config.getint('Network', 'Port')
			self.nick = self.config.get('Network', 'Nickname')
			self.channel = self.config.get('Network', 'Channel')
			self.master = self.config.get('Security', 'Master')
			self.trigger = self.config.get('Security', 'Trigger')
			self.commands = self.config.options('Commands')
			self.debugmode = self.config.get('Other', 'Debug')

			print "[*] Using the following connection settings:"
			print "    %s" % self.server
			print "    %d" % self.port
			print "    %s" % self.nick
			print "    %s" % self.channel
			print ""

			print "[*] Using the following security settings:"
			print "    Master: %s" % self.master
			print "    Trigger: %s" % self.trigger
			print ""

			print "[*] Listing commands:"
			for self.command in self.commands:
				print "    %s%s" % (self.trigger, self.command)



if __name__ == '__main__':
	commander = Commander()
	commander