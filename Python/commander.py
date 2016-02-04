#!/usr/bin/env python

"""
Commander.py - Python Backend for the WiFi Pineapple Commander module.

Foxtrot (C) 2016 <foxtrotnull@gmail.com>
"""

import ConfigParser
import os
import sys
import socket
import string
import time

class Commander:
	print "[*] WiFi Pineapple Commander"
	print "[*] Looking for Commander.conf..."
	if os.path.exists('commander.conf'):
		print "[*] Found configuration file!"
		print " "
		config = ConfigParser.RawConfigParser()
		config.read('commander.conf')
		if config.has_section('Network') & config.has_section('Commands') & config.has_section('Other'):
			print "[*] Valid configuration file... proceeding"
			print " "
		else:
			print "[!] Configuration is missing either Network, Command or Other block."
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
		port = Commander.config.getint('Network', 'Port')
		nickname = Commander.config.get('Network', 'Nickname')
		channel = Commander.config.get('Network', 'Channel')

		print "[*] Using these connection settings! :"
		print "    Server: " + server
		print "    Port: " + str(port)
		print "    Nickname: " + nickname
		print "    Channel: " + channel
		print " "

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "[*] Connecting!"
		sock.connect((server, port))

		print "[*] Sending nickname and joining " + channel
		sock.send("NICK %s\r\n" % nickname)
		sock.send("USER %s 8 * :%s\r\n" % (nickname, nickname))
		time.sleep(5)
		sock.send("JOIN %s\r\n" % channel)
		sock.send("PRIVMSG %s :Connected!\r\n" % channel)
		print "[*] Connected!"
		print " "

		while True:
			buff = sock.recv(2048)
			debugMode = Commander.config.get('Other', 'Debug')
			if debugMode == "on":
				print "[*] Debug mode is on! Printing buffer..."
				print buff

			if buff.find('PING') != -1:
				print "[*] Replying to ping from server"
				sock.send('PONG ' + buff.split() [1] + '\r\n')

			commands = Commander.config.options('Commands')
			for command in commands:
				if buff.find(command) != -1:
					print "[*] Executing command %s" % command
					sock.send("PRIVMSG %s :Executing command %s\r\n" % (channel, command))


	connect()