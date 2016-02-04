# Commander
A WiFi Pineapple Module that allows you to control your device via IRC.

#About
This module allows you to control your WiFi Pineapple over IRC by acting as a client connecting to your specified server. You can then specify custom commands to execute by talking to it like it was a person.

#Configuration File
The Configuration file is split into 3 sections, "Network", "Commands" and "Other".
##Network
This is where you define your Server, Port, Nickname and Channel for the module. You must make your configuration file comply with this format:

```[Network]
Server: irc.example.com
Port: 6667
Nickname: Commander
Channel: #Commander
```

##Commands
The commands block works in the same way as above, but this time you will define your commands in the syntax of "trigger: command". For example:
```[Commands]
example: mkdir /example/ && touch /example/commander
example two: rm -rf /example/
```

##Other
This final block is where you define the special character and a debug option. You will only be able to see debug output if you manually execute the commander.py file over SSH. The special character is the character you will use before your command to use Commander. For example:
```[Other]
Character: !
Debug: off
```

Once your configuration is complete, and you have connected to IRC, you can use your commands in the form of `!example` and `!example two`, where `!` is your special character and `example` is your command trigger.
