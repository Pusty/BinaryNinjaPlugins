import binaryninja

from .XTENSAArch import XTENSA
XTENSA.register()


# built-in view
EM_XTENSA = 94
binaryninja.BinaryViewType['ELF'].register_arch(EM_XTENSA, binaryninja.enums.Endianness.LittleEndian, binaryninja.Architecture['XTENSA'])