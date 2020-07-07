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


## binary-xtensa

binary-xtensa is a plugin for Binary Ninja providing functionality to analyze and disassemble the code within Xtensa ELF Files.
Implemented decoding based on https://0x04.net/~mwk/doc/xtensa.pdf

For using this plugin just drop the binary-xtensa folder into your plugin folder.


![xtensa-graph](/docs/xtensa-graph.png)