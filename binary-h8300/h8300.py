import struct
import traceback
import os
import math

from binaryninja import *
from types import *

from .h8300dis import *
from .h8300lift import InstructionIL 
            
# https://www.renesas.com/us/en/document/mah/h8300h-series-software-manual?language=en&r=1052456



def decode_instruction(data, addr):
        if len(data) < 2:
            return None, None, None
            
        
        inst, size, match = tryToParse(data) # in h8300dis
        
        if inst == None:
            return None, None, None
            
        return inst, size, match
        
        
def regFrom(reg, size):
    reg_str = "???"
    if size == 8:
        if((reg&0x8) == 0):
            reg_str = "r"+str(reg&7)+"h"
        else:
            reg_str = "r"+str(reg&7)+"l"
    elif size == 16:
        if((reg&0x8) == 0):
            reg_str = "r"+str(reg&7)
        else:
            reg_str = "e"+str(reg&7)
    elif size == 32:
        reg_str = "er"+str(reg)
    return reg_str
    
def signOffset(off, size):
    if size == 8:
        off = off & 0xFF
        return off | (-(off & 0x80))
    elif size == 16:
        off = off & 0xFFFF
        return off | (-(off & 0x8000))
    elif size == 24:
        off = off & 0xFFFFFF
        return off | (-(off & 0x800000))
    elif size == 32:
        off = off & 0xFFFFFFFF
        return off | (-(off & 0x80000000))
    return off

class H8300(Architecture):

    name = 'H8/300'
    
    address_size = 3
    default_int_size = 1
    instr_alignment = 1
    max_instr_length = 10
    
    endianness = Endianness.BigEndian

    # register related stuff
    regs = {
    
        # main registers
        'er0': RegisterInfo('er0', 4),
        'er1': RegisterInfo('er1', 4),
        'er2': RegisterInfo('er2', 4),
        'er3': RegisterInfo('er3', 4),
        'er4': RegisterInfo('er4', 4),
        'er5': RegisterInfo('er5', 4),
        'er6': RegisterInfo('er6', 4),
        'er7': RegisterInfo('er7', 4),
        
        # upper 16 
        
        'e0': RegisterInfo('er0', 2, 2),
        'e1': RegisterInfo('er1', 2, 2),
        'e2': RegisterInfo('er2', 2, 2),
        'e3': RegisterInfo('er3', 2, 2),
        'e4': RegisterInfo('er4', 2, 2),
        'e5': RegisterInfo('er5', 2, 2),
        'e6': RegisterInfo('er6', 2, 2),
        'e7': RegisterInfo('er7', 2, 2),
        
        # lower 16 
        
        'r0': RegisterInfo('er0', 2, 0),
        'r1': RegisterInfo('er1', 2, 0),
        'r2': RegisterInfo('er2', 2, 0),
        'r3': RegisterInfo('er3', 2, 0),
        'r4': RegisterInfo('er4', 2, 0),
        'r5': RegisterInfo('er5', 2, 0),
        'r6': RegisterInfo('er6', 2, 0),
        'r7': RegisterInfo('er7', 2, 0),
        
        # upper 8 of the lower 16
        'r0h': RegisterInfo('er0', 1, 1),
        'r1h': RegisterInfo('er1', 1, 1),
        'r2h': RegisterInfo('er2', 1, 1),
        'r3h': RegisterInfo('er3', 1, 1),
        'r4h': RegisterInfo('er4', 1, 1),
        'r5h': RegisterInfo('er5', 1, 1),
        'r6h': RegisterInfo('er6', 1, 1),
        'r7h': RegisterInfo('er7', 1, 1),
        
        
        # lower 8 
        'r0l': RegisterInfo('er0', 1, 0),
        'r1l': RegisterInfo('er1', 1, 0),
        'r2l': RegisterInfo('er2', 1, 0),
        'r3l': RegisterInfo('er3', 1, 0),
        'r4l': RegisterInfo('er4', 1, 0),
        'r5l': RegisterInfo('er5', 1, 0),
        'r6l': RegisterInfo('er6', 1, 0),
        'r7l': RegisterInfo('er7', 1, 0),
        
        # program counter
        'pc': RegisterInfo('pc', 4),
        
        # flag register
        'ccr': RegisterInfo('ccr', 1),

    }

    stack_pointer = "er7"
    # Interrupt flag, User bit or interrupt mask bit
    # Half-carry flag, Negative flag
    # Zero flag, Overflow flag, Carry flag
    flags = ['i', 'u', 'h', 'u2', 'n', 'z', 'v', 'c']

    flag_roles = {
        'i': FlagRole.SpecialFlagRole,
        'u': FlagRole.SpecialFlagRole,
        'u2': FlagRole.SpecialFlagRole,
        
        'n': FlagRole.NegativeSignFlagRole,
        'z': FlagRole.ZeroFlagRole,
        'h': FlagRole.HalfCarryFlagRole,
        'v': FlagRole.OverflowFlagRole,
        'c': FlagRole.CarryFlagRole
    }
    
    flag_write_types = ['none', '*', 'c', 'z']
    flags_written_by_flag_write_type = {
        'none': [],
        '*': ['h', 'n', 'z', 'v', 'c'],
        'c': ['c'],
        'z': ['z'],
    }
    
    flags_required_for_flag_condition = {
        LowLevelILFlagCondition.LLFC_UGT: ['c', 'z'], # hi
        LowLevelILFlagCondition.LLFC_ULE: ['c', 'z'], # ls
        LowLevelILFlagCondition.LLFC_UGE: ['c'], # cs
        LowLevelILFlagCondition.LLFC_ULT: ['c'], # cs
        LowLevelILFlagCondition.LLFC_NE:  ['z'], # ne
        LowLevelILFlagCondition.LLFC_E:   ['z'], # eq
        LowLevelILFlagCondition.LLFC_NO:  ['v'], # vc
        LowLevelILFlagCondition.LLFC_O:   ['v'], # vs
        LowLevelILFlagCondition.LLFC_POS: ['n'], # pl
        LowLevelILFlagCondition.LLFC_NEG: ['n'], # mi
        LowLevelILFlagCondition.LLFC_SGE: ['n', 'v'], # ge
        LowLevelILFlagCondition.LLFC_SLT: ['n', 'v'], # lt
        LowLevelILFlagCondition.LLFC_SGT: ['n', 'v', 'z'], # gt
        LowLevelILFlagCondition.LLFC_SLE: ['n', 'v', 'z'], # le
    }
    
    
    """
    semantic_flag_classes = ['class_bitstuff']

    semantic_flag_groups = ['group_e', 'group_ne', 'group_lt']
    
    flags_required_for_semantic_flag_group = {
        'group_lt': ['c'],
        'group_e': ['z'],
        'group_ne': ['z']
    }
    
    flag_conditions_for_semantic_flag_group = {
        #'group_e': {None: LowLevelILFlagCondition.LLFC_E},
        #'group_ne': {None: LowLevelILFlagCondition.LLFC_NE}
    }

    # MAP (condition x class) -> flags
    def get_flags_required_for_flag_condition(self, cond, sem_class):
        #LogDebug('incoming cond: %s, incoming sem_class: %s' % (str(cond), str(sem_class)))

        if sem_class == None:
            lookup = {
                # Z, zero flag for == and !=
                LowLevelILFlagCondition.LLFC_E: ['z'],
                LowLevelILFlagCondition.LLFC_NE: ['z'],
                LowLevelILFlagCondition.LLFC_NEG: ['n'],
                LowLevelILFlagCondition.LLFC_UGE: ['c'],
                LowLevelILFlagCondition.LLFC_ULT: ['c']
            }

            if cond in lookup:
                return lookup[cond]

        return []    
    """


    def get_instruction_info(self, data, addr):
    
        inst, size, match = decode_instruction(data, addr)
        
        if inst == None:
            return None
            
        result = InstructionInfo()
        result.length = size
        
        instName = inst[0].split(" ")[0]
        
        JMP_NAMES = ["BHI", "BLS", "BHS", "BLO", "BNE", "BEQ", "BVC", "BPL", "BMI", "BGE", "BLT", "BGT", "BLE" ] # BF never branches
        # "BSR"
        # JMP, JSR

        if not ((instName in JMP_NAMES) or instName == "BT" or instName == "BSR" or instName == "JMP" or instName == "JSR" or instName == "RTS" or instName == "RTE"):
            return result
            
        if instName == "RTE":
            # EXCEPTION RETURN
            result.add_branch(BranchType.FunctionReturn)
        
        if instName == "RTS":
            # RETURN
            result.add_branch(BranchType.FunctionReturn)
            
        if instName == "BT":
            # UNCONDITIONAL JUMP
            for l in inst[2]:
                if l[0] == TYPE_PCOFFSET:
                    result.add_branch(BranchType.UnconditionalBranch, addr + size + signOffset(match[l[2]], l[1]))
        
        
            
        if instName in JMP_NAMES:
            # CONDITIONAL BRANCH
            for l in inst[2]:
                if l[0] == TYPE_PCOFFSET:
                    result.add_branch(BranchType.TrueBranch, addr + size + signOffset(match[l[2]], l[1]))
            result.add_branch(BranchType.FalseBranch, addr + size)


        if instName == "BSR":
            # DIRECT CALL
            for l in inst[2]:
                if l[0] == TYPE_PCOFFSET:
                    result.add_branch(BranchType.CallDestination, addr + size + signOffset(match[l[2]], l[1]))
            
        if instName == "JMP":
            if inst[2][0][0] == TYPE_ABS:
                result.add_branch(BranchType.UnconditionalBranch, match[inst[2][0][3]])
            else:
                # UNCONDITIONAL JUMP TO REGISTER OR DOUBLE MEMORY LOOKUP
                result.add_branch(BranchType.IndirectBranch)    
            
        if instName == "JSR":
            if inst[2][0][0] == TYPE_ABS:
                result.add_branch(BranchType.CallDestination, match[inst[2][0][3]])
            else:
                # UNCONDITIONAL CALL TO REGISTER OR DOUBLE MEMORY LOOKUP
                result.add_branch(BranchType.IndirectBranch)    
            
            
            
        """


        if obj.name in ["CALL0", "CALL4", "CALL8", "CALL12"]:
            # DIRECT CALL
            for l in obj.prop["format"]:
                if l[0] == "TYPE_LABEL":
                    result.add_branch(BranchType.CallDestination, l[1])

        if obj.name in ["JX"]:
            # UNCONDITIONAL JUMP TO REGISTER
            result.add_branch(BranchType.IndirectBranch)    
        """
            
        return result
        

        
    def get_instruction_text(self, data, addr):
        inst, size, match = decode_instruction(data, addr)
        
        if inst == None:
            return None
            
        result = []

        instName = inst[0].split(" ")[0]
        result.append(InstructionTextToken( InstructionTextTokenType.InstructionToken, instName))
        
        """
        TYPE_ATREG = "atreg" # size, access size, offset / '+' / '-' / None, letter
        TYPE_OFFSET = "offset" # size, letter
        TYPE_PCOFFSET = "pcoffset" # size
        """
        
        parIndex = 0
        for l in inst[2]:
            if parIndex > 0:
                result.append(InstructionTextToken(InstructionTextTokenType.TextToken, ','))
            result.append(InstructionTextToken(InstructionTextTokenType.TextToken, ' '))
            
            if l[0] == TYPE_IMM:
                result.append(InstructionTextToken(InstructionTextTokenType.TextToken, '#'))
                result.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, hex(match[l[2]]), match[l[2]]))
            elif l[0] == TYPE_CONST:
                result.append(InstructionTextToken(InstructionTextTokenType.TextToken, '#'))
                result.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, hex(l[1]), l[1]))
            elif l[0] == TYPE_REGCCR:
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "ccr"))
            elif l[0] == TYPE_ABS:
                absAddr = match[l[3]]
                result.append(InstructionTextToken(InstructionTextTokenType.BeginMemoryOperandToken, '@'))
                result.append(InstructionTextToken(InstructionTextTokenType.PossibleAddressToken, hex(absAddr), absAddr))
                result.append(InstructionTextToken(InstructionTextTokenType.EndMemoryOperandToken, ''))
            elif l[0] == TYPE_ATABS:
                absAddr = match[l[3]]
                result.append(InstructionTextToken(InstructionTextTokenType.BeginMemoryOperandToken, '@@'))
                result.append(InstructionTextToken(InstructionTextTokenType.PossibleAddressToken, hex(absAddr), absAddr))
                result.append(InstructionTextToken(InstructionTextTokenType.EndMemoryOperandToken, ''))
            elif l[0] == TYPE_ATREG:
                reg = match[l[4]]
                regStr = regFrom(reg, l[1])
                
                if l[3] == None or l[3] == '-' or l[3] == '+':

                    result.append(InstructionTextToken(InstructionTextTokenType.BeginMemoryOperandToken, '@'))
                    if l[3] == '-':
                        result.append(InstructionTextToken(InstructionTextTokenType.TextToken, '-'))
                    result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, regStr))
                    if l[3] == '+':
                        result.append(InstructionTextToken(InstructionTextTokenType.TextToken, '+'))
                    result.append(InstructionTextToken(InstructionTextTokenType.EndMemoryOperandToken, ''))
                else:
                    offset = signOffset(match[l[3][2]], l[3][1])
                    
                    result.append(InstructionTextToken(InstructionTextTokenType.BeginMemoryOperandToken, '@('))
                    result.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, hex(offset), offset))
                    result.append(InstructionTextToken(InstructionTextTokenType.TextToken, ','))
                    result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, regStr))
                    result.append(InstructionTextToken(InstructionTextTokenType.EndMemoryOperandToken, ')'))
   
            elif l[0] == TYPE_REG:
                reg = match[l[2]]
                regStr = regFrom(reg, l[1])
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, regStr))
            elif l[0] == TYPE_PCOFFSET:
                pcOffset = signOffset(match[l[2]], l[1])
                result.append(InstructionTextToken(InstructionTextTokenType.PossibleAddressToken, hex(addr+pcOffset+size), addr+pcOffset+size))
            #    
            parIndex = parIndex + 1
            
        return result, size
  
    
    def get_flag_write_low_level_il(self, op, size, write_type, flag, operands, il):
        return Architecture.get_flag_write_low_level_il(self, op, size, write_type, flag, operands, il)
        
        

    def get_instruction_low_level_il(self, data, addr, il):
        if len(data) < 2: return None
        inst, size, match = decode_instruction(data, addr)
        if inst == None: return None

        instName = inst[0].split(" ")[0]
        
        args = []
        
        for l in inst[2]:
            if l[0] == TYPE_IMM:
                args.append((TYPE_IMM, math.ceil(l[1]/8), match[l[2]]))
            elif l[0] == TYPE_CONST:
                args.append((TYPE_CONST, l[1]))
            elif l[0] == TYPE_REGCCR:
                args.append((TYPE_REGCCR))
            elif l[0] == TYPE_ABS:
                args.append((TYPE_ABS, math.ceil(l[1]/8), math.ceil(l[2]/8), match[l[3]]))
            elif l[0] == TYPE_ATABS:
                args.append((TYPE_ATABS, math.ceil(l[1]/8), math.ceil(l[2]/8), match[l[3]]))
            elif l[0] == TYPE_ATREG:
                r = regFrom(match[l[4]], l[1])
                sizeO = math.ceil(l[1]/8)
                sizeA = math.ceil(l[2]/8)
                if l[3] == None or l[3] == '-' or l[3] == '+':
                    if l[3] == '-':
                        args.append((TYPE_ATREG, sizeO, sizeA, "-", r))
                    elif l[3] == '+':
                        args.append((TYPE_ATREG, sizeO, sizeA, "+", r))
                    else:
                        args.append((TYPE_ATREG, sizeO, sizeA, "@", r))
                else:
                    args.append((TYPE_ATREG, sizeO, sizeA, "offset", r, signOffset(match[l[3][2]], l[3][1])))
            elif l[0] == TYPE_REG:
                args.append((TYPE_REG, math.ceil(l[1]/8), regFrom(match[l[2]], l[1])))
            elif l[0] == TYPE_PCOFFSET:
                args.append((TYPE_PCOFFSET, math.ceil(l[1]/8), addr+signOffset(match[l[2]], l[1])+size, addr+size))
        
        if InstructionIL.get(instName) is not None:
            instLifted = InstructionIL[instName](il, args)
            if isinstance(instLifted, list):
                for i in instLifted:
                    if isinstance(i, LambdaType):
                        i(il, args)
                    else:    
                        il.append(i)
            elif instLifted is not None:
                il.append(instLifted)
        else:
            il.append(il.unimplemented())
        

        return size
        
H8300.register()
