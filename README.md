# Binary Ninja Plugins


----------


## binary-jvm

binary-jvm is a plugin for Binary Ninja providing functionality to analyze Java Class files and disassemble the code within them.
It also provides the functionality to NOP out instructions, change branch conditions or even assemble full instructions (that don't require additional meta data) at a given position.

For using this plugin just drop the binary-jvm folder into your plugin folder.


![boolFunction](/docs/boolFunction.PNG)
![strings](/docs/strings.PNG)
![variables](/docs/variables.PNG)
![patching](/docs/patching.PNG)


## binary-h8300 


binary-h8300 is a plugin for Binary Ninja providing functionality to analyze, disassemble and lift (lifting works but has bugs in it that I will hopefully fix later TM) H8/300 binaries.
Implemented decoding and behavior based on the Renesas H8/300H Software Manual

For using this plugin just drop the binary-h8300 folder into your plugin folder.

## binary-xtensa (Outdated)

*I personally have no need for this right now or in the near future and am not aware of anybody using it - there are also alternative binary ninja plugins for it so I'll probably not further work on this*

binary-xtensa is a plugin for Binary Ninja providing functionality to analyze and disassemble the code within Xtensa ELF Files.
Implemented decoding based on https://0x04.net/~mwk/doc/xtensa.pdf

For using this plugin just drop the binary-xtensa folder into your plugin folder.


![xtensa-graph](/docs/xtensa-graph.png)

