from binaryninja import *
from .h8300dis import *

def R(il, arg):
    if arg[0] == TYPE_IMM:
        return il.const(arg[1], arg[2])
    elif arg[0] == TYPE_CONST:
        return il.const(4, arg[1])
    elif arg[0] == TYPE_REGCCR:
        return il.reg(1, "ccr")
    elif arg[0] == TYPE_ABS:
        return il.const(arg[1], arg[3])
    elif arg[0] == TYPE_ATABS:
        return il.load(arg[2], il.const(arg[1], arg[3]))
    elif arg[0] == TYPE_ATREG:
        reg = il.reg(arg[1], arg[4])
        if arg[3] == "@":
            return il.load(arg[2], reg)
        elif arg[3] == "+":
            il.append(il.set_reg(arg[1], arg[4], il.add(arg[1], reg, il.const(arg[1], arg[1]))))
            return il.load(arg[2], il.sub(arg[1], reg, il.const(arg[1], arg[1])) )
        elif arg[3] == "-":
            il.append(il.set_reg(arg[1], arg[4], il.sub(arg[1], reg, il.const(arg[1], arg[1]))))
            return il.load(arg[2], reg)
        elif arg[3] == "offset":
            offset = il.const(3, arg[5])
            return il.load(arg[2], il.add(3, reg, offset))
        else:
            return il.undefined()
            
    elif arg[0] == TYPE_REG:
        return il.reg(arg[1], arg[2])
    elif arg[0] == TYPE_PCOFFSET:
        return il.const(3, arg[2])
        

def W(il, arg, value):
    if arg[0] == TYPE_IMM:
        il.append(il.undefined())
    elif arg[0] == TYPE_CONST:
        il.append(il.undefined())
    elif arg[0] == TYPE_REGCCR:
        il.append(il.set_reg(1, "ccr", value))
    elif arg[0] == TYPE_ABS:
        il.append(il.store(arg[2], R(il, arg), value))
    elif arg[0] == TYPE_ATABS:
        il.append(il.undefined())
    elif arg[0] == TYPE_ATREG:
        reg = il.reg(arg[1], arg[4])
        if arg[3] == "@":
            il.append(il.store(arg[2], reg, value))
        elif arg[3] == "+":
            il.append(il.store(arg[2], reg, value))
            il.append(il.set_reg(arg[1], arg[4], il.add(arg[1], reg, il.const(arg[1], arg[1]))))
        elif arg[3] == "-":
            il.append(il.set_reg(arg[1], arg[4], il.sub(arg[1], reg, il.const(arg[1], arg[1]))))
            il.append(il.store(arg[2], reg, value))
        elif arg[3] == "offset":
            offset = il.const(3, arg[5])
            il.append(il.store(arg[2], il.add(3, reg, offset), value))
        else:
            il.append(il.undefined())
    elif arg[0] == TYPE_REG:
        il.append(il.set_reg(arg[1], arg[2], value))
    elif arg[0] == TYPE_PCOFFSET:
        il.append(il.undefined())
        
        
#def inst_ANDB(self, data, addr, il, inst, size, match):
#    il.append(self.parToILWrite(il, inst[2][1], match, il.and_expr(1, self.parToILRead(il, inst[2][1], match), self.parToILRead(il, inst[2][0], match))))


def CCJ(il, args, cond):
    arg = args[0]
    if arg[0] != TYPE_PCOFFSET:
        return il.unimplemented()
        
    t = il.get_label_for_address(Architecture['H8/300'], arg[2])
    f = il.get_label_for_address(Architecture['H8/300'], arg[3])
    
    condition = il.unimplemented()
    
    if cond == "HI":
        condition = il.not_expr(0, il.or_expr(0, il.flag('c'), il.flag('z')))
    elif cond == "LS":
        condition = il.or_expr(0, il.flag('c'), il.flag('z'))
    elif cond == "HS":
        condition = il.not_expr(0, il.flag('c'))
    elif cond == "LO":
        condition = il.flag('c')
    elif cond == "NE":
        condition = il.not_expr(0, il.flag('z'))
    elif cond == "EQ":
        condition = il.flag('z')
    elif cond == "VC":
        condition = il.not_expr(0, il.flag('v'))
    elif cond == "VS":
        condition = il.flag('v')
    elif cond == "PL":
        condition = il.not_expr(0, il.flag('n'))
    elif cond == "MI":
        condition = il.flag('n')
    elif cond == "GE":
        condition = il.not_expr(0, il.xor_expr(0, il.flag('n'), il.flag('v')))
    elif cond == "LT":
        condition = il.xor_expr(0, il.flag('n'), il.flag('v'))
    elif cond == "GT":
        condition = il.not_expr(0, il.or_expr(0, il.flag('z'), il.xor_expr(0, il.flag('n'), il.flag('v'))))
    elif cond == "LE":
        condition = il.or_expr(0, il.flag('z'), il.xor_expr(0, il.flag('n'), il.flag('v')))
    
    if t and f:
        il.append(il.if_expr(condition, t, f))
        return
        

    if t:
        tmp = il.goto(t)
    else:
        tmp = il.jump(il.const_pointer(3, arg[2]))
        
    t = LowLevelILLabel()
    f = LowLevelILLabel()
        
    il.append(il.if_expr(condition, t, f))
    il.mark_label(t)
    il.append(tmp)
    il.mark_label(f)
    
def BOP(il, args, op):
    c = il.flag('c')
    tb = il.test_bit(4, R(il, args[1]), R(il, args[0]))
    res = c

    if op == "OR":
        res = il.or_expr(0, c, tb)
    elif op == "IOR":
        res = il.or_expr(0, c, il.not_expr(0,tb))
    elif op == "LD":
        res = tb
    elif op == "ILD":
        res = il.not_expr(0,tb)
    elif op == "IXOR":
        res = il.xor_expr(0, c, il.not_expr(0, tb))
    elif op == "XOR":
        res = il.xor_expr(0, c, tb)
    elif op == "IAND":
        res = il.and_expr(0, c, il.not_expr(0, tb))
    elif op == "AND":
        res = il.and_expr(0, c, tb)
    return il.set_flag('c', res)
    
def BSET(il, args, op):
    
    mask = il.shift_left(4, il.const(4, 1), R(il, args[0]))
    val = R(il, args[1])
    valMask = il.and_expr(4, val, il.not_expr(4, mask))
    valBit = il.and_expr(4, val, mask)
    carry = il.zero_extend(4, il.flag('c'))
    carryL = il.shift_left(4, il.const(4, 1), carry)
    carryI = il.zero_extend(4, il.not_expr(0, il.flag('c')))
    carryIL = il.shift_left(4, il.const(4, 1), carryI)
    
    res = val
    
    if op == "CLR":
        res = valMask
    elif op == "SET":
        res = il.or_expr(4, val, mask)
    elif op == "ST":
        res = il.or_expr(4, valMask, carryL)
    elif op == "IST":
        res = il.or_expr(4, valMask, carryIL)
    elif op == "NOT":
        res = il.or_expr(4, valMask, il.and_expr(4, il.not_expr(4, valBit), mask))
    
    return W(il, args[1], res)
    
InstructionIL = {
    "ADD.B": lambda il, args: W(il, args[1], il.add(1, R(il, args[1]), R(il, args[0]), flags='*')),
    "ADD.W": lambda il, args: W(il, args[1], il.add(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "ADD.L": lambda il, args: W(il, args[1], il.add(4, R(il, args[1]), R(il, args[0]), flags='*')),
    "ADDS": lambda il, args: W(il, args[1], il.add(4, R(il, args[1]), R(il, args[0]))),
    "ADDX": lambda il, args: W(il, args[1], il.add_carry(1, R(il, args[1]), R(il, args[0]), il.flag('c'), flags='*')),
    "AND.B": lambda il, args: W(il, args[1], il.and_expr(1, R(il, args[1]), R(il, args[0]), flags='*')),
    "AND.W": lambda il, args: W(il, args[1], il.and_expr(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "AND.L": lambda il, args: W(il, args[1], il.and_expr(4, R(il, args[1]), R(il, args[0]), flags='*')),
    # ANDC
    "BIAND": lambda il, args: BOP(il, args, 'AND'),
    "BT":   lambda il, args: il.jump(il.const_pointer(3, args[0][2])),
    "BF":   lambda il, args: il.nop(),
    "BHI":   lambda il, args: CCJ(il, args, 'HI'),
    "BLS":   lambda il, args: CCJ(il, args, 'LS'),
    "BHS":   lambda il, args: CCJ(il, args, 'HS'),
    "BLO":   lambda il, args: CCJ(il, args, 'LO'),
    "BNE":   lambda il, args: CCJ(il, args, 'NE'),
    "BEQ":   lambda il, args: CCJ(il, args, 'EQ'),
    "BVC":   lambda il, args: CCJ(il, args, 'VC'),
    "BVS":   lambda il, args: CCJ(il, args, 'VS'),
    "BPL":   lambda il, args: CCJ(il, args, 'PL'),
    "BMI":   lambda il, args: CCJ(il, args, 'MI'),
    "BGE":   lambda il, args: CCJ(il, args, 'GE'),
    "BLT":   lambda il, args: CCJ(il, args, 'LT'),
    "BGT":   lambda il, args: CCJ(il, args, 'GT'),
    "BLE":   lambda il, args: CCJ(il, args, 'LE'),
    "BCLR": lambda il, args: BSET(il, args, 'CLR'),
    "BIAND":   lambda il, args: BOP(il, args, 'IAND'),
    "BILD":   lambda il, args: BOP(il, args, 'ILD'),
    "BIOR":   lambda il, args: BOP(il, args, 'IOR'),
    "BIST": lambda il, args: BSET(il, args, 'IST'),
    "BIXOR":   lambda il, args: BOP(il, args, 'IXOR'),
    "BLD":   lambda il, args: BOP(il, args, 'LD'),
    "BNOT": lambda il, args: BSET(il, args, 'NOT'),
    "BOR":   lambda il, args: BOP(il, args, 'OR'),
    "BSET":  lambda il, args: BSET(il, args, 'SET'),
    "BSR":   lambda il, args: il.call(R(il, args[0])),
    "BST": lambda il, args: BSET(il, args, 'ST'),
    "BTST": lambda il, args: il.set_flag('z', il.test_bit(4, R(il, args[1]), R(il, args[0]))),
    "BXOR":   lambda il, args: BOP(il, args, 'XOR'),
    "CMP.B": lambda il, args: il.sub(1, R(il, args[1]), R(il, args[0]), flags='*'),
    "CMP.W": lambda il, args: il.sub(2, R(il, args[1]), R(il, args[0]), flags='*'),
    "CMP.L": lambda il, args: il.sub(4, R(il, args[1]), R(il, args[0]), flags='*'),
    # DAA
    # DAS
    "DEC.B": lambda il, args:  W(il,  args[0], il.sub(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "DEC.W": lambda il, args:  W(il, args[1], il.sub(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "DEC.L": lambda il, args:  W(il, args[1], il.sub(4, R(il, args[1]), R(il, args[0]), flags='*')),
    "DIVXS.B": lambda il, args:  W(il, args[1], 
        il.or_expr(2, 
            il.shift_left(2,
                il.zero_extend(2, il.mod_signed(1, il.low_part(1, R(il, args[1])), R(il, args[0]))),
                il.const(2, 8)
            ),
            il.div_signed(1, il.low_part(1, R(il, args[1])), R(il, args[0]), flags='*')
        )
    ),
    "DIVXS.W": lambda il, args:  W(il, args[1], 
        il.or_expr(4, 
            il.shift_left(4,
                il.zero_extend(4, il.mod_signed(2, il.low_part(2, R(il, args[1])), R(il, args[0]))),
                il.const(4, 8)
            ),
            il.div_signed(2, il.low_part(2, R(il, args[1])), R(il, args[0]), flags='*')
        )
    ),
    "DIVXU.B": lambda il, args:  W(il, args[1], 
        il.or_expr(2, 
            il.shift_left(2,
                il.zero_extend(2, il.mod_unsigned(1, il.low_part(1, R(il, args[1])), R(il, args[0]))),
                il.const(2, 8)
            ),
            il.div_unsigned(1, il.low_part(1, R(il, args[1])), R(il, args[0]), flags='*')
        )
    ),
    "DIVXU.W": lambda il, args:  W(il, args[1], 
        il.or_expr(4, 
            il.shift_left(4,
                il.zero_extend(4, il.mod_unsigned(2, il.low_part(2, R(il, args[1])), R(il, args[0]))),
                il.const(4, 8)
            ),
            il.div_unsigned(2, il.low_part(2, R(il, args[1])), R(il, args[0]), flags='*')
        )
    ),
    # EEPMOV
    "EXTS.W": lambda il, args: W(il, args[0], il.sign_extend(2, il.low_part(1, R(il, args[0])))),
    "EXTS.L": lambda il, args: W(il, args[0], il.sign_extend(4, il.low_part(2, R(il, args[0])))),
    "EXTU.W": lambda il, args: W(il, args[0], il.zero_extend(2, il.low_part(1, R(il, args[0])))),
    "EXTU.L": lambda il, args: W(il, args[0], il.zero_extend(4, il.low_part(2, R(il, args[0])))),
    "INC.B": lambda il, args:  W(il,  args[0], il.add(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "INC.W": lambda il, args:  W(il, args[1], il.add(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "INC.L": lambda il, args:  W(il, args[1], il.add(4, R(il, args[1]), R(il, args[0]), flags='*')),
    "JMP":   lambda il, args: il.jump(R(il, args[0])),
    "JSR":   lambda il, args: il.call(R(il, args[0])),
    # LDC
    "MOV.B": lambda il, args: W(il, args[1], R(il, args[0])),
    "MOV.W": lambda il, args: W(il, args[1], R(il, args[0])),
    "MOV.L": lambda il, args: W(il, args[1], R(il, args[0])),
    # MOVFPE
    # MOVTPE
    "MULXS.B": lambda il, args:  W(il, args[1], il.mult(2, il.sign_extend(2, il.low_part(1, R(il, args[1]))), il.sign_extend(2, R(il, args[0])), flags='*')),
    "MULXS.W": lambda il, args:  W(il, args[1], il.mult(4, il.sign_extend(4, il.low_part(2, R(il, args[1]))), il.sign_extend(4, R(il, args[0])), flags='*')),
    "MULXU.B": lambda il, args:  W(il, args[1], il.mult(2, il.zero_extend(2, il.low_part(1, R(il, args[1]))), il.zero_extend(2, R(il, args[0])), flags='*')),
    "MULXU.W": lambda il, args:  W(il, args[1], il.mult(4, il.zero_extend(4, il.low_part(2, R(il, args[1]))), il.zero_extend(4, R(il, args[0])), flags='*')),
    "NEG.B": lambda il, args: W(il, args[0], il.neg_expr(1, R(il, args[0]), flags='*')),
    "NEG.W": lambda il, args: W(il, args[0], il.neg_expr(2, R(il, args[0]), flags='*')),
    "NEG.L": lambda il, args: W(il, args[0], il.neg_expr(4, R(il, args[0]), flags='*')),
    "NOP":   lambda il, args: il.nop(),
    "NOT.B": lambda il, args: W(il, args[0], il.not_expr(1, R(il, args[0]), flags='*')),
    "NOT.W": lambda il, args: W(il, args[0], il.not_expr(2, R(il, args[0]), flags='*')),
    "NOT.L": lambda il, args: W(il, args[0], il.not_expr(4, R(il, args[0]), flags='*')),
    "OR.B": lambda il, args: W(il, args[1], il.or_expr(1, R(il, args[1]), R(il, args[0]), flags='*')),
    "OR.W": lambda il, args: W(il, args[1], il.or_expr(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "OR.L": lambda il, args: W(il, args[1], il.or_expr(4, R(il, args[1]), R(il, args[0]), flags='*')),
    # ORC
    "ROTL.B": lambda il, args: W(il, args[0], il.rotate_left(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "ROTL.W": lambda il, args: W(il, args[0], il.rotate_left(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "ROTL.L": lambda il, args: W(il, args[0], il.rotate_left(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "ROTR.B": lambda il, args: W(il, args[0], il.rotate_right(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "ROTR.W": lambda il, args: W(il, args[0], il.rotate_right(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "ROTR.L": lambda il, args: W(il, args[0], il.rotate_right(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "ROTXL.B": lambda il, args: W(il, args[0], il.rotate_left_carry(1, R(il, args[0]), il.const(1, 1), il.flag('c'), flags='*')),
    "ROTXL.W": lambda il, args: W(il, args[0], il.rotate_left_carry(2, R(il, args[0]), il.const(2, 1), il.flag('c'),flags='*')),
    "ROTXL.L": lambda il, args: W(il, args[0], il.rotate_left_carry(4, R(il, args[0]), il.const(4, 1), il.flag('c'),flags='*')),
    "ROTXR.B": lambda il, args: W(il, args[0], il.rotate_right_carry(1, R(il, args[0]), il.const(1, 1), il.flag('c'),flags='*')),
    "ROTXR.W": lambda il, args: W(il, args[0], il.rotate_right_carry(2, R(il, args[0]), il.const(2, 1), il.flag('c'),flags='*')),
    "ROTXR.L": lambda il, args: W(il, args[0], il.rotate_right_carry(4, R(il, args[0]), il.const(4, 1), il.flag('c'),flags='*')),
    # RTE
    "RTS":  lambda il, args: il.ret(il.pop(4)),
    "SHAL.B": lambda il, args: W(il, args[0], il.shift_left(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "SHAL.W": lambda il, args: W(il, args[0], il.shift_left(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "SHAL.L": lambda il, args: W(il, args[0], il.shift_left(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "SHAR.B": lambda il, args: W(il, args[0], il.arith_shift_right(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "SHAR.W": lambda il, args: W(il, args[0], il.arith_shift_right(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "SHAR.L": lambda il, args: W(il, args[0], il.arith_shift_right(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "SHLL.B": lambda il, args: W(il, args[0], il.shift_left(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "SHLL.W": lambda il, args: W(il, args[0], il.shift_left(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "SHLL.L": lambda il, args: W(il, args[0], il.shift_left(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "SHLR.B": lambda il, args: W(il, args[0], il.logical_shift_right(1, R(il, args[0]), il.const(1, 1), flags='*')),
    "SHLR.W": lambda il, args: W(il, args[0], il.logical_shift_right(2, R(il, args[0]), il.const(2, 1), flags='*')),
    "SHLR.L": lambda il, args: W(il, args[0], il.logical_shift_right(4, R(il, args[0]), il.const(4, 1), flags='*')),
    "SLEEP":  lambda il, args: il.unimplemented(), # special sleep behavior
    # STC
    "SUB.B": lambda il, args: W(il, args[1], il.sub(1, R(il, args[1]), R(il, args[0]), flags='*')),
    "SUB.W": lambda il, args: W(il, args[1], il.sub(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "SUB.L": lambda il, args: W(il, args[1], il.sub(4, R(il, args[1]), R(il, args[0]), flags='*')),
    "SUBS":  lambda il, args: W(il, args[1], il.sub(4, R(il, args[1]), R(il, args[0]))),
    "SUBX":  lambda il, args: W(il, args[1], il.sub_borrow(4, R(il, args[1]), R(il, args[0]), il.flag('c'), flags='*')),
    "TRAPA": lambda il, args: il.unimplemented(),
    "XOR.B": lambda il, args: W(il, args[1], il.xor_expr(1, R(il, args[1]), R(il, args[0]), flags='*')),
    "XOR.W": lambda il, args: W(il, args[1], il.xor_expr(2, R(il, args[1]), R(il, args[0]), flags='*')),
    "XOR.L": lambda il, args: W(il, args[1], il.xor_expr(4, R(il, args[1]), R(il, args[0]), flags='*')),
    # XORC


}


