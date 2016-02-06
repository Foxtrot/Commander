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
import time
import string

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
			print ""

	def connect(self):
		self.sock = socket.socket()
		print "[*] Connecting!"
		self.sock.connect((self.server, self.port))
		print "[*] Sending nick and user information"
		self.sock.send('NICK %s\r\n' % self.nick)
		self.sock.send('USER %s 8 * :%s\r\n' % (self.nick, self.nick))
		time.sleep(5)
		self.sock.send('JOIN %s\r\n' % self.channel)
		self.sock.send('PRIVMSG %s :Connected.\r\n' % self.channel)
		print "[*] Connected!"
		print ""

		while True:
			self.buff = self.sock.recv(2048)

			if self.debugmode == "on":
				print self.buff

			if self.buff.find('PING') != -1:
				print "[*] Replying to ping from server"
				self.sock.send('PONG ' + self.buff.split() [1] + '\r\n')


if __name__ == '__main__':
	commander = Commander()
	commander.connect()