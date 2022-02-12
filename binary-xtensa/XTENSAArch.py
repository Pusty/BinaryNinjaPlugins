#!/usr/bin/env python

import re

from binaryninja.log import log_info
from binaryninja.architecture import Architecture
from binaryninja.function import RegisterInfo, InstructionInfo, InstructionTextToken
from binaryninja.enums import InstructionTextTokenType, BranchType, FlagRole


from .XTENSADIS import *

class XTENSA(Architecture):
    name = 'XTENSA'

    address_size = 4
    default_int_size = 4
    instr_alignment = 3
    max_instr_length = 3

    # register related stuff
    regs = {
        # main registers
        'a0': RegisterInfo('a0', 4),
        'a1': RegisterInfo('a1', 4),
        'a2': RegisterInfo('a2', 4),
        'a3': RegisterInfo('a3', 4),
        'a4': RegisterInfo('a4', 4),
        'a5': RegisterInfo('a5', 4),
        'a6': RegisterInfo('a6', 4),
        'a7': RegisterInfo('a7', 4),
        'a8': RegisterInfo('a8', 4),
        'a9': RegisterInfo('a9', 4),
        'a10': RegisterInfo('a10', 4),
        'a11': RegisterInfo('a11', 4),
        'a12': RegisterInfo('a12', 4),
        'a13': RegisterInfo('a13', 4),
        'a14': RegisterInfo('a14', 4),
        'a15': RegisterInfo('a15', 4),

        # program counter
        'pc': RegisterInfo('pc', 4),

        # special status
        'sar': RegisterInfo('sar', 4)
    }

    stack_pointer = "a1"

#------------------------------------------------------------------------------
# CFG building
#------------------------------------------------------------------------------

    def get_instruction_info(self, data, addr):
        if len(data) < 2 or len(data) > 3: return None
        obj = decode(data, addr)
        if obj.name == "UNKNOWN": return None
        result = InstructionInfo()
        result.length = obj.len
        
        if obj.name in ["RET", "RET.N"]:
            # RETURN
            result.add_branch(BranchType.FunctionReturn)
            
        if obj.name in ["BALL", "BNALL", "BANY", "BNONE", "BBC", "BBCI", "BBS", "BBSI", "BEQ", "BEQI", "BEQZ", "BNE", "BNEI", "BNEZ", "BGE", "BGEI", "BGEU", "BGEUI", "BGEZ", "BLT", "BLTI", "BLTU", "BLTUI", "BLTZ"]:
            # CONDITIONAL BRANCH
            for l in obj.prop["format"]:
                if l[0] == "TYPE_LABEL":
                    result.add_branch(BranchType.TrueBranch, l[1])
            result.add_branch(BranchType.FalseBranch, addr + obj.len)

        if obj.name in ["J"]:
            # UNCONDITIONAL JUMP
            for l in obj.prop["format"]:
                if l[0] == "TYPE_LABEL":
                    result.add_branch(BranchType.UnconditionalBranch, l[1])
            
        if obj.name in ["CALL0", "CALL4", "CALL8", "CALL12"]:
            # DIRECT CALL
            for l in obj.prop["format"]:
                if l[0] == "TYPE_LABEL":
                    result.add_branch(BranchType.CallDestination, l[1])

        if obj.name in ["JX"]:
            # UNCONDITIONAL JUMP TO REGISTER
            result.add_branch(BranchType.IndirectBranch)    
            
        #if obj.name in ["CALLX0", "CALLX4", "CALLX8", "CALLX12"]:
            # CALL TO REGISTER
        #    result.add_branch(BranchType.IndirectBranch)   
        
        return result
        
        
        
        

    def get_instruction_text(self, data, addr):
        if len(data) < 2 or len(data) > 3: return None
        obj = decode(data, addr)
        if obj.name == "UNKNOWN": return None
        result = []
        result.append(InstructionTextToken(InstructionTextTokenType.InstructionToken, obj.name))
        
        li = obj.prop["format"]
        for i in range(len(li)):
            result.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ' '))
            l = li[i]
            if l[0] == "TYPE_REG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "a"+str(l[1])))
            elif l[0] == "TYPE_FREG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "f"+str(l[1])))    
            elif l[0] == "TYPE_BREG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "b"+str(l[1])))    
            elif l[0] == "TYPE_SREG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "s"+str(l[1])))    
            elif l[0] == "TYPE_UREG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "u"+str(l[1])))    
            elif l[0] == "TYPE_MREG":
                result.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, "m"+str(l[1]))) 
            elif l[0] == "TYPE_IMM":
                result.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, str(l[1]), l[1])) 
            elif l[0] == "TYPE_LABEL":
                result.append(InstructionTextToken(InstructionTextTokenType.CodeRelativeAddressToken, '0x%08x' % (l[1]), l[1]))  # PossibleAddressToken?
                
            if i < len(li)-1:
                result.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ','))
        
        return result, obj.len
        
    def get_flag_write_low_level_il(self, op, size, write_type, flag, operands, il):
        return Architecture.get_flag_write_low_level_il(self, op, size, write_type, flag, operands, il)

    def get_instruction_low_level_il(self, data, addr, il):
        if len(data) < 2 or len(data) > 3: return None
        obj = decode(data, addr)
        if obj.name == "UNKNOWN": return None
        il.append(il.unimplemented())
        return obj.len
