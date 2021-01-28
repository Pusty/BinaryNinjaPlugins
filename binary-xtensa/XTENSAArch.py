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

        
        
"""
        decoded = decode(data, addr)

        # on error, return nothing
        if decoded.status == DECODE_STATUS.ERROR or decoded.len == 0:
            return None

        # on non-branching, return length
        result = InstructionInfo()
        result.length = decoded.len
        if decoded.typ != INSTRTYPE.JUMP_CALL_RETURN:
            return result

        # jp has several variations
        if decoded.op == OP.JP:
            (oper_type, oper_val) = decoded.operands[0]

            # jp pe,0xDEAD
            if oper_type == OPER_TYPE.COND:
                assert decoded.operands[1][0] == OPER_TYPE.ADDR
                result.add_branch(BranchType.TrueBranch, decoded.operands[1][1])
                result.add_branch(BranchType.FalseBranch, addr + decoded.len)
            # jp (hl); jp (ix); jp (iy)
            elif oper_type in [OPER_TYPE.REG_DEREF, OPER_TYPE.MEM_DISPL_IX, OPER_TYPE.MEM_DISPL_IY]:
                result.add_branch(BranchType.IndirectBranch)
            # jp 0xDEAD
            elif oper_type == OPER_TYPE.ADDR:
                result.add_branch(BranchType.UnconditionalBranch, oper_val)
            else:
                raise Exception('handling JP')

        # jr can be conditional
        elif decoded.op == OP.JR:
            (oper_type, oper_val) = decoded.operands[0]

            # jr c,0xdf07
            if oper_type == OPER_TYPE.COND:
                assert decoded.operands[1][0] == OPER_TYPE.ADDR
                result.add_branch(BranchType.TrueBranch, decoded.operands[1][1])
                result.add_branch(BranchType.FalseBranch, addr + decoded.len)
            # jr 0xdf07
            elif oper_type == OPER_TYPE.ADDR:
                result.add_branch(BranchType.UnconditionalBranch, oper_val)
            else:
                raise Exception('handling JR')

        # djnz is implicitly conditional
        elif decoded.op == OP.DJNZ:
            (oper_type, oper_val) = decoded.operands[0]
            assert oper_type == OPER_TYPE.ADDR
            result.add_branch(BranchType.TrueBranch, oper_val)
            result.add_branch(BranchType.FalseBranch, addr + decoded.len)

        # call can be conditional
        elif decoded.op == OP.CALL:
            (oper_type, oper_val) = decoded.operands[0]
            # call c,0xdf07
            if oper_type == OPER_TYPE.COND:
                assert decoded.operands[1][0] == OPER_TYPE.ADDR
                result.add_branch(BranchType.CallDestination, decoded.operands[1][1])
            # call 0xdf07
            elif oper_type == OPER_TYPE.ADDR:
                result.add_branch(BranchType.CallDestination, oper_val)
            else:
                raise Exception('handling CALL')

        # ret can be conditional
        elif decoded.op == OP.RET:
            if decoded.operands and decoded.operands[0][0] == OPER_TYPE.COND:
                # conditional returns dont' end block
                pass
            else:
                result.add_branch(BranchType.FunctionReturn)

        # ret from interrupts
        elif decoded.op == OP.RETI or decoded.op == OP.RETN:
            result.add_branch(BranchType.FunctionReturn)

        return result
"""  


"""
        decoded = decode(data, addr)
        if decoded.status != DECODE_STATUS.OK or decoded.len == 0:
            return None

        result = []

        # opcode
        result.append(InstructionTextToken( \
            InstructionTextTokenType.InstructionToken, decoded.op.name))

        # space for operand
        if decoded.operands:
            result.append(InstructionTextToken(InstructionTextTokenType.TextToken, ' '))

        # operands
        for i, operand in enumerate(decoded.operands):
            (oper_type, oper_val) = operand

            if oper_type == OPER_TYPE.REG:
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.RegisterToken, self.reg2str(oper_val)))

            elif oper_type == OPER_TYPE.REG_DEREF:
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.BeginMemoryOperandToken, '('))
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.RegisterToken, self.reg2str(oper_val)))
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.EndMemoryOperandToken, ')'))

            elif oper_type == OPER_TYPE.ADDR:
                if oper_val < 0:
                    oper_val = oper_val & 0xFFFF
                txt = '0x%04x' % oper_val
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.PossibleAddressToken, txt, oper_val))

            elif oper_type == OPER_TYPE.ADDR_DEREF:
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.BeginMemoryOperandToken, '('))
                txt = '0x%04x' % oper_val
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.PossibleAddressToken, txt, oper_val))
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.EndMemoryOperandToken, ')'))

            elif oper_type in [OPER_TYPE.MEM_DISPL_IX, OPER_TYPE.MEM_DISPL_IY]:
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.BeginMemoryOperandToken, '('))

                txt = 'IX' if oper_type == OPER_TYPE.MEM_DISPL_IX else 'IY'
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.RegisterToken, txt))

                if oper_val == 0:
                    # omit displacement of 0
                    pass
                elif oper_val >= 16:
                    # (iy+0x28)
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.TextToken, '+'))
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.IntegerToken, '0x%X' % oper_val, oper_val))
                elif oper_val > 0:
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.TextToken, '+'))
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.IntegerToken, '%d' % oper_val, oper_val))
                elif oper_val <= -16:
                    # adc a,(ix-0x55)
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.TextToken, '-'))
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.IntegerToken, '0x%X' % (-oper_val), oper_val))
                else:
                    result.append(InstructionTextToken( \
                        InstructionTextTokenType.IntegerToken, '%d' % oper_val, oper_val))

                result.append(InstructionTextToken( \
                    InstructionTextTokenType.EndMemoryOperandToken, ')'))

            elif oper_type == OPER_TYPE.IMM:
                if oper_val == 0:
                    txt = '0'
                elif oper_val >= 16:
                    txt = '0x%x' % oper_val
                else:
                    txt = '%d' % oper_val

                result.append(InstructionTextToken( \
                    InstructionTextTokenType.IntegerToken, txt, oper_val))

            elif oper_type == OPER_TYPE.COND:
                txt = CC_TO_STR[oper_val]
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.TextToken, txt))

            elif oper_type in [OPER_TYPE.REG_C_DEREF, OPER_TYPE.REG_BC_DEREF, OPER_TYPE.REG_DE_DEREF, \
                OPER_TYPE.REG_HL_DEREF, OPER_TYPE.REG_SP_DEREF]:

                result.append(InstructionTextToken( \
                    InstructionTextTokenType.BeginMemoryOperandToken, '('))
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.RegisterToken, self.reg2str(oper_val)))
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.EndMemoryOperandToken, ')'))

            else:
                raise Exception('unknown operand type: ' + str(oper_type))

            # if this isn't the last operand, add comma
            if i < len(decoded.operands)-1:
                result.append(InstructionTextToken( \
                    InstructionTextTokenType.OperandSeparatorToken, ','))

        # crazy undoc shit
        if decoded.metaLoad:
            extras = []
            (oper_type, oper_val) = decoded.metaLoad
            assert oper_type == OPER_TYPE.REG
            extras.append(InstructionTextToken( \
                InstructionTextTokenType.InstructionToken, 'ld'))
            extras.append(InstructionTextToken( \
                InstructionTextTokenType.TextToken, ' '))
            extras.append(InstructionTextToken( \
                InstructionTextTokenType.RegisterToken, self.reg2str(oper_val)))
            extras.append(InstructionTextToken( \
                InstructionTextTokenType.OperandSeparatorToken, ','))

            result = extras + result

        return result, decoded.len
"""