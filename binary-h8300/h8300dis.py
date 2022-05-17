"""
instructions = [
("add.b", "#xx:8, Rd",  [(8, "rd"), "imm"]),
("add.b", "Rs, Rd",     [(0, 8), ("rs", "rd")]),
("add.w", "#xx:16, Rd", [(7, 9), (1, "rd"), "imm", "imm"]),
("add.w", "Rs, Rd",     [(0, 9), ("rs", "rd")]),
("add.l", "#xx:32, ERd", [(7, 0xA), (1, (0, "erd")), "imm", "imm", "imm", "imm"]),
("add.l", "Rs, ERd",     [(0, 0xA), ((1, "ers"), (0, "erd"))]),
("adds", "#1, ERd",      [(0, 0xB), (0, (0, "erd"))],
("adds", "#2, ERd",      [(0, 0xB), (8, (0, "erd"))],
("adds", "#4, ERd",      [(0, 0xB), (9, (0, "erd"))],
("addx", "#xx:8, Rd",    [(9, "rd"), "imm"]),
("addx", "Rs, Rd",       [(0, 0xE), ("rs", "rd"]),
("and.b", "#xx:8, Rd",    [(0xE, "rd"), "imm"]),
("and.b", "Rs, Rd",       [(1, 6), ("rs", "rd"]),
("and.w", "#xx:16, Rd", [(7, 9), (6, "rd"), "imm", "imm"]),
("and.w", "Rs, Rd",     [(6, 6), ("rs", "rd")]),
("and.l", "#xx:32, ERd", [(7, 0xA), (6, (0, "erd")), "imm", "imm", "imm", "imm"]),
("and.l", "Rs, ERd",     [(0, 1), (0xF, 0), (6, 6), ((0, "ers"), (0, "erd"))]),
("andc", "#xx:8, CCR",  [(0, 6), "imm"]),
("band", "#xx:3.Rd", [ (7, 6), ((0, "imm"), "rd") ]),
("band", "#xx:3.@ERd", [ (7, 0xC), ((0, "erd"), 0), (7,6), ((0, "imm"), 0) ]),
("band", "#xx:3.@aa:8", [ (7, 0xE), "abs", (7, 6), ((0, "imm"), 0) ]),
("bt", "d:8",  [(4, 0), "disp"]),
("bt", "d:16", [(5, 8), (0, 0), "disp", "disp"]),
("bf", "d:8",  [(4, 1), "disp"]),
("bf", "d:16", [(5, 8), (1, 0), "disp", "disp"]),
("bhi", "d:8",  [(4, 2), "disp"]),
("bhi", "d:16", [(5, 8), (2, 0), "disp", "disp"]),
("bls", "d:8",  [(4, 3), "disp"]),
("bls", "d:16", [(5, 8), (3, 0), "disp", "disp"]),
("bhs", "d:8",  [(4, 4), "disp"]),
("bhs", "d:16", [(5, 8), (4, 0), "disp", "disp"]),
("blo", "d:8",  [(4, 5), "disp"]),
("blo", "d:16", [(5, 8), (5, 0), "disp", "disp"]),
("bne", "d:8",  [(4, 6), "disp"]),
("bne", "d:16", [(5, 8), (6, 0), "disp", "disp"]),
("beq", "d:8",  [(4, 7), "disp"]),
("beq", "d:16", [(5, 8), (7, 0), "disp", "disp"]),
("bvc", "d:8",  [(4, 8), "disp"]),
("bvc", "d:16", [(5, 8), (8, 0), "disp", "disp"]),
("bvs", "d:8",  [(4, 9), "disp"]),
("bvs", "d:16", [(5, 8), (9, 0), "disp", "disp"]),
("bpl", "d:8",  [(4, 10), "disp"]),
("bpl", "d:16", [(5, 8), (10, 0), "disp", "disp"]),
("bmi", "d:8",  [(4, 11), "disp"]),
("bmi", "d:16", [(5, 8), (11, 0), "disp", "disp"]),
("bge", "d:8",  [(4, 12), "disp"]),
("bge", "d:16", [(5, 8), (12, 0), "disp", "disp"]),
("blt", "d:8",  [(4, 13), "disp"]),
("blt", "d:16", [(5, 8), (13, 0), "disp", "disp"]),
("bgt", "d:8",  [(4, 14), "disp"]),
("bgt", "d:16", [(5, 8), (14, 0), "disp", "disp"]),
("ble", "d:8",  [(4, 15), "disp"]),
("ble", "d:16", [(5, 8), (15, 0), "disp", "disp"]),
]
"""

"""
formatImmedate8    = "ooooddddiiiiiiii"
formatImmedate16   = "01111001ooooddddiiiiiiiiiiiiiiii"
formatImmedate32   = "01111010oooo0dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
formatRegister8    = "oooooooossssdddd"
formatRegister16   = "oooooooossssdddd"
formatRegister32   = "oooooooo1sss0ddd"
formatAdds         = "00001011oooo0ddd"
formatAnd32        = "00000001111100000110oooo0sss0ddd"
formatOnlyImm8     = "ooooooooiiiiiiii"
formatBitR8        = "oooooooobiiidddd"
formatBitR32       = "oooooooo0ddd0000ppppppppbiii0000"
formatBitAbs       = "ooooooooaaaaaaaappppppppbiii0000"
formatBitRR32      = "oooooooo0ddd0000ppppppppnnnn0000"
formatBitRAbs      = "ooooooooaaaaaaaappppppppnnnn0000"
formatOnlyImm16    = "ooooooooppppppppiiiiiiiiiiiiiiii"
formatOnlyRd       = "ooooooooppppdddd"
formatNop          = "oooooooopppppppp"

FORMAT_IMMEDIATE8  = 0
FORMAT_IMMEDIATE16 = 1
FORMAT_IMMEDIATE32 = 2
FORMAT_REGISTER8   = 3
FORMAT_REGISTER16  = 4
FORMAT_REGISTER32  = 5
FORMAT_ADDS        = 6
FORMAT_AND32       = 7
FORMAT_ONLY_IMM8   = 8
FORMAT_BITS_R8     = 9
FORMAT_BITS_R32    = 10
FORMAT_BITS_ABS    = 11
FORMAT_BITS_RR32   = 12
FORMAT_BITS_RABS   = 13
FORMAT_ONLY_IMM16  = 14
FORMAT_ONLY_RD     = 15
FORMAT_NOP         = 16

insts = [
("add.b", [(FORMAT_IMMEDIATE8, 0x8, "ADD.B #xx:8,Rd"), (FORMAT_REGISTER8, 0x08, "ADD.B Rs,Rd")]),
("add.w", [(FORMAT_IMMEDIATE16, 0x1, "ADD.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x09, "ADD.W Rs,Rd")]),
("add.l", [(FORMAT_IMMEDIATE32, 0x1, "ADD.L #xx:32,ERd"), (FORMAT_REGISTER32, 0x0A, "ADD.L ERs,ERd")]),
("adds",  [(FORMAT_ADDS, 0x0, "ADDS #1,ERd"), (FORMAT_ADDS, 0x8, "ADDS #2,ERd"), (FORMAT_ADDS, 0x9, "ADDS #4,ERd")]),
("addx",  [(FORMAT_IMMEDIATE8, 0x9, "ADDX #xx:8,Rd"), (FORMAT_REGISTER8, 0x0E, "ADDX Rs,Rd")]),
("and.b", [(FORMAT_IMMEDIATE8, 0xE, "AND.B #xx:8,Rd"), (FORMAT_REGISTER8, 0x16, "AND.B Rs,Rd")]),
("and.w", [(FORMAT_IMMEDIATE16, 0x6, "AND.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x66, "AND.W Rs,Rd")]),
("and.l", [(FORMAT_IMMEDIATE32, 0x6, "AND.L #xx:32,ERd"), (FORMAT_AND32, 0x6, "AND.L ERs,ERd")]),
("andc",  [(FORMAT_ONLY_IMM8, 0x6, "ANDC #xx:8,CCR")]),
("band",  [(FORMAT_BITS_R8, 0x76, "BAND #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7C, "BAND #xx:3,@ERd", 0x76, 0), (FORMAT_BITS_ABS, 0x7E, "BAND #xx:3,@aa:8", 0x76, 0)]),
("bt",     [(FORMAT_ONLY_IMM8, 0x40, "BT d:8"), (FORMAT_ONLY_IMM16, 0x58, "BT d:16", 0x00)]),
("bf",     [(FORMAT_ONLY_IMM8, 0x41, "BF d:8"), (FORMAT_ONLY_IMM16, 0x58, "BF d:16", 0x10)]),
("bhi",    [(FORMAT_ONLY_IMM8, 0x42, "BHI d:8"), (FORMAT_ONLY_IMM16, 0x58, "BHI d:16", 0x20)]),
("bls",    [(FORMAT_ONLY_IMM8, 0x43, "BLS d:8"), (FORMAT_ONLY_IMM16, 0x58, "BLS d:16", 0x30)]),
("bhs",    [(FORMAT_ONLY_IMM8, 0x44, "BHS d:8"), (FORMAT_ONLY_IMM16, 0x58, "BHS d:16", 0x40)]),
("blo",    [(FORMAT_ONLY_IMM8, 0x45, "BLO d:8"), (FORMAT_ONLY_IMM16, 0x58, "BLO d:16", 0x50)]),
("bne",    [(FORMAT_ONLY_IMM8, 0x46, "BNE d:8"), (FORMAT_ONLY_IMM16, 0x58, "BNE d:16", 0x60)]),
("beq",    [(FORMAT_ONLY_IMM8, 0x47, "BEQ d:8"), (FORMAT_ONLY_IMM16, 0x58, "BEQ d:16", 0x70)]),
("bvc",    [(FORMAT_ONLY_IMM8, 0x48, "BVC d:8"), (FORMAT_ONLY_IMM16, 0x58, "BVC d:16", 0x80)]),
("bvs" ,   [(FORMAT_ONLY_IMM8, 0x49, "BVS d:8"), (FORMAT_ONLY_IMM16, 0x58, "BVS d:16", 0x90)]),
("bpl" ,   [(FORMAT_ONLY_IMM8, 0x4A, "BPL d:8"), (FORMAT_ONLY_IMM16, 0x58, "BPL d:16", 0xA0)]),
("bmi",    [(FORMAT_ONLY_IMM8, 0x4B, "BMI d:8"), (FORMAT_ONLY_IMM16, 0x58, "BMI d:16", 0xB0)]),
("bge",    [(FORMAT_ONLY_IMM8, 0x4C, "BGE d:8"), (FORMAT_ONLY_IMM16, 0x58, "BGE d:16", 0xC0)]),
("blt" ,   [(FORMAT_ONLY_IMM8, 0x4D, "BLT d:8"), (FORMAT_ONLY_IMM16, 0x58, "BLT d:16", 0xD0)]),
("bgt",    [(FORMAT_ONLY_IMM8, 0x4E, "BGT d:8"), (FORMAT_ONLY_IMM16, 0x58, "BGT d:16", 0xE0)]),
("ble",    [(FORMAT_ONLY_IMM8, 0x4F, "BLE d:8"), (FORMAT_ONLY_IMM16, 0x58, "BLE d:16", 0xF0)]),
("bclr",  [(FORMAT_BITS_R8, 0x72, "BCLR #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7D, "BCLR #xx:3,@ERd", 0x72, 0), (FORMAT_BITS_ABS, 0x7F, "BCLR #xx:3,@aa:8", 0x72, 0),
 (FORMAT_REGISTER8, 0x62, "BCLR Rs,Rd"), (FORMAT_BITS_RR32, 0x7D, "BCLR Rn,@ERd", 0x62), (FORMAT_BITS_RABS, 0x7F, "BCLR Rn,@aa:8", 0x62)]),
("biand",  [(FORMAT_BITS_R8, 0x76, "BIAND #xx:3,Rd", 1), (FORMAT_BITS_R32, 0x7C, "BIAND #xx:3,@ERd", 0x76, 1), (FORMAT_BITS_ABS, 0x7E, "BIAND #xx:3,@aa:8", 0x76, 1)]),
("bild",  [(FORMAT_BITS_R8, 0x77, "BILD #xx:3,Rd", 1), (FORMAT_BITS_R32, 0x7C, "BILD #xx:3,@ERd", 0x77, 1), (FORMAT_BITS_ABS, 0x7E, "BILD #xx:3,@aa:8", 0x77, 1)]),
("bior",  [(FORMAT_BITS_R8, 0x74, "BIOR #xx:3,Rd", 1), (FORMAT_BITS_R32, 0x7C, "BIOR #xx:3,@ERd", 0x74, 1), (FORMAT_BITS_ABS, 0x7E, "BIOR #xx:3,@aa:8", 0x74, 1)]),
("bist",  [(FORMAT_BITS_R8, 0x67, "BIST #xx:3,Rd", 1), (FORMAT_BITS_R32, 0x7D, "BIST #xx:3,@ERd", 0x67, 1), (FORMAT_BITS_ABS, 0x7F, "BIST #xx:3,@aa:8", 0x67, 1)]),
("bixor",  [(FORMAT_BITS_R8, 0x75, "BIXOR #xx:3,Rd", 1), (FORMAT_BITS_R32, 0x7C, "BIXOR #xx:3,@ERd", 0x75, 1), (FORMAT_BITS_ABS, 0x7E, "BIXOR #xx:3,@aa:8", 0x75, 1)]),
("bld",  [(FORMAT_BITS_R8, 0x77, "BLD #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7C, "BLD #xx:3,@ERd", 0x77, 0), (FORMAT_BITS_ABS, 0x7E, "BLD #xx:3,@aa:8", 0x77, 0)]),
("bnot",  [(FORMAT_BITS_R8, 0x71, "BNOT #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7D, "BNOT #xx:3,@ERd", 0x71, 0), (FORMAT_BITS_ABS, 0x7F, "BNOT #xx:3,@aa:8", 0x71, 0),
 (FORMAT_REGISTER8, 0x61, "BNOT Rs,Rd"), (FORMAT_BITS_RR32, 0x7D, "BNOT Rn,@ERd", 0x61), (FORMAT_BITS_RABS, 0x7F, "BNOT Rn,@aa:8", 0x61)]),
("bor",  [(FORMAT_BITS_R8, 0x74, "BOR #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7C, "BOR #xx:3,@ERd", 0x74, 0), (FORMAT_BITS_ABS, 0x7E, "BIOR #xx:3,@aa:8", 0x74, 0)]),
("bset",  [(FORMAT_BITS_R8, 0x70, "BSET #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7D, "BSET #xx:3,@ERd", 0x70, 0), (FORMAT_BITS_ABS, 0x7F, "BSET #xx:3,@aa:8", 0x70, 0),
 (FORMAT_REGISTER8, 0x60, "BSET Rs,Rd"), (FORMAT_BITS_RR32, 0x7D, "BSET Rn,@ERd", 0x60), (FORMAT_BITS_RABS, 0x7F, "BSET Rn,@aa:8", 0x60)]),
("bsr",  [(FORMAT_ONLY_IMM8, 0x55, "BSR d:8"), (FORMAT_ONLY_IMM16, 0x5C, "BSR d:16", 0x00)]),
("bst",  [(FORMAT_BITS_R8, 0x67, "BST #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7D, "BST #xx:3,@ERd", 0x67, 0), (FORMAT_BITS_ABS, 0x7F, "BST #xx:3,@aa:8", 0x67, 0)]),
("btst",  [(FORMAT_BITS_R8, 0x73, "BTST #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7C, "BTST #xx:3,@ERd", 0x73, 0), (FORMAT_BITS_ABS, 0x7E, "BTST #xx:3,@aa:8", 0x73, 0),
 (FORMAT_REGISTER8, 0x63, "BTST Rs,Rd"), (FORMAT_BITS_RR32, 0x7C, "BTST Rn,@ERd", 0x63), (FORMAT_BITS_RABS, 0x7E, "BTST Rn,@aa:8", 0x63)]),
("bxor",  [(FORMAT_BITS_R8, 0x75, "BXOR #xx:3,Rd", 0), (FORMAT_BITS_R32, 0x7C, "BXOR #xx:3,@ERd", 0x75, 0), (FORMAT_BITS_ABS, 0x7E, "BXOR #xx:3,@aa:8", 0x75, 0)]),
("cmp.b", [(FORMAT_IMMEDIATE8, 0xA, "CMP.B #xx:8,Rd"), (FORMAT_REGISTER8, 0x1C, "CMP.B Rs,Rd")]),
("cmp.w", [(FORMAT_IMMEDIATE16, 0x2, "CMP.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x1D, "CMP.W Rs,Rd")]),
("cmp.l", [(FORMAT_IMMEDIATE32, 0x2, "CMP.L #xx:32,ERd"), (FORMAT_REGISTER32, 0x1F, "CMP.L ERs,ERd")]),
("daa",   [(FORMAT_ONLY_RD, 0x0F, "DAA Rd", 0)]),
("das",   [(FORMAT_ONLY_RD, 0x1F, "DAS Rd", 0)]),
("dec.b",   [(FORMAT_ONLY_RD, 0x1A, "DEC.B Rd", 0)]),
("dec.w",   [(FORMAT_ONLY_RD, 0x1B, "DEC.W #1,Rd", 0x5), (FORMAT_ONLY_RD, 0x1B, "DEC.W #2,Rd", 0xD)]),
("dec.l",   [(FORMAT_ONLY_RD, 0x1B, "DEC.L #1,ERd", 0x7), (FORMAT_ONLY_RD, 0x1B, "DEC.L #2,ERd", 0xF)]),

#AND.L ERs,ERd L 0 1 F 0 6 6 0 ers 0 erd
#DIVXS.B Rs,Rd B 0 1 D 0 5 1 rs rd

("divxu",   [(FORMAT_REGISTER16, 0x51, "DIVXU.B Rs,Rd"), (FORMAT_REGISTER16, 0x53, "DIVXU.W Rs,ERd")]),
# eepmov
("exts.w",   [(FORMAT_ONLY_RD, 0x17, "EXTS.W Rd", 0x0D)]),
("exts.l",   [(FORMAT_ONLY_RD, 0x17, "EXTS.L ERd", 0x0F)]),
("extu.w",   [(FORMAT_ONLY_RD, 0x17, "EXTU.W Rd", 0x05)]),
("extu.l",   [(FORMAT_ONLY_RD, 0x17, "EXTU.L ERd", 0x07)]),
("inc.b",   [(FORMAT_ONLY_RD, 0x0A, "INC.B Rd", 0)]),
("inc.w",   [(FORMAT_ONLY_RD, 0x0B, "INC.W #1,Rd", 0x5), (FORMAT_ONLY_RD, 0x0B, "INC.W #2,Rd", 0xD)]),
("inc.l",   [(FORMAT_ONLY_RD, 0x0B, "INC.L #1,ERd", 0x7), (FORMAT_ONLY_RD, 0x0B, "INC.L #2,ERd", 0xF)]),

("mulxu",   [(FORMAT_REGISTER16, 0x50, "MULXU.B Rs,Rd"), (FORMAT_REGISTER16, 0x52, "MULXU.W Rs,ERd")]),
("neg.b",   [(FORMAT_ONLY_RD, 0x17, "NEG.B Rd", 0x08)]),
("neg.w",   [(FORMAT_ONLY_RD, 0x17, "NEG.W Rd", 0x09)]),
("neg.l",   [(FORMAT_ONLY_RD, 0x17, "NEG.L ERd", 0x0B)]),
("nop",     [(FORMAT_NOP,     0x00, "NOP", 0x00)]), 
("not.b",   [(FORMAT_ONLY_RD, 0x17, "NOT.B Rd", 0x00)]),
("not.w",   [(FORMAT_ONLY_RD, 0x17, "NOT.W Rd", 0x01)]),
("not.l",   [(FORMAT_ONLY_RD, 0x17, "NOT.L ERd", 0x03)]),
("or.b", [(FORMAT_IMMEDIATE8, 0xC, "OR.B #xx:8,Rd"), (FORMAT_REGISTER8, 0x14, "OR.B Rs,Rd")]),
("or.w", [(FORMAT_IMMEDIATE16, 0x4, "OR.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x64, "OR.W Rs,Rd")]),
("or.l", [(FORMAT_IMMEDIATE32, 0x4, "OR.L #xx:32,ERd"), (FORMAT_AND32, 0x4, "OR.L ERs,ERd")]),
("orc",  [(FORMAT_ONLY_IMM8, 0x4, "ORC #xx:8,CCR")]),
#("pop.w",   [(FORMAT_ONLY_RD, 0x6D, "POP.W Rd", 0x07)]),
#("pop.l",   [(FORMAT_ONLY_RD, 0x17, "POP.L ERd", 0x03)]),
#("push.w",   [(FORMAT_ONLY_RD, 0x6D, "PUSH.W Rd", 0x0F)]),
#("push.l",   [(FORMAT_ONLY_RD, 0x17, "PUSH.L ERd", 0x03)]),
("rotl.b",   [(FORMAT_ONLY_RD, 0x12, "ROTL.B Rd", 0x08)]),
("rotl.w",   [(FORMAT_ONLY_RD, 0x12, "ROTL.W Rd", 0x09)]),
("rotl.l",   [(FORMAT_ONLY_RD, 0x12, "ROTL.L ERd", 0x0B)]),
("rotr.b",   [(FORMAT_ONLY_RD, 0x13, "ROTR.B Rd", 0x08)]),
("rotr.w",   [(FORMAT_ONLY_RD, 0x13, "ROTR.W Rd", 0x09)]),
("rotr.l",   [(FORMAT_ONLY_RD, 0x13, "ROTR.L ERd", 0x0B)]),
("rotxl.b",   [(FORMAT_ONLY_RD, 0x12, "ROTXL.B Rd", 0x00)]),
("rotxl.w",   [(FORMAT_ONLY_RD, 0x12, "ROTXL.W Rd", 0x01)]),
("rotxl.l",   [(FORMAT_ONLY_RD, 0x12, "ROTXL.L ERd", 0x03)]),
("rotxr.b",   [(FORMAT_ONLY_RD, 0x13, "ROTXR.B Rd", 0x00)]),
("rotxr.w",   [(FORMAT_ONLY_RD, 0x13, "ROTXR.W Rd", 0x01)]),
("rotxr.l",   [(FORMAT_ONLY_RD, 0x13, "ROTXR.L ERd", 0x03)]),
("rte",     [(FORMAT_NOP,     0x56, "RTE", 0x70)]), 
("rts",     [(FORMAT_NOP,     0x54, "RTS", 0x70)]), 
("shal.b",   [(FORMAT_ONLY_RD, 0x10, "SHAL.B Rd", 0x08)]),
("shal.w",   [(FORMAT_ONLY_RD, 0x10, "SHAL.W Rd", 0x09)]),
("shal.l",   [(FORMAT_ONLY_RD, 0x10, "SHAL.L ERd", 0x0B)]),
("shar.b",   [(FORMAT_ONLY_RD, 0x11, "SHAR.B Rd", 0x08)]),
("shar.w",   [(FORMAT_ONLY_RD, 0x11, "SHAR.W Rd", 0x09)]),
("shar.l",   [(FORMAT_ONLY_RD, 0x11, "SHAR.L ERd", 0x0B)]),
("shll.b",   [(FORMAT_ONLY_RD, 0x10, "SHLL.B Rd", 0x00)]),
("shll.w",   [(FORMAT_ONLY_RD, 0x10, "SHLL.W Rd", 0x01)]),
("shll.l",   [(FORMAT_ONLY_RD, 0x10, "SHLL.L ERd", 0x03)]),
("shlr.b",   [(FORMAT_ONLY_RD, 0x11, "SHLR.B Rd", 0x00)]),
("shlr.w",   [(FORMAT_ONLY_RD, 0x11, "SHLR.W Rd", 0x01)]),
("shlr.l",   [(FORMAT_ONLY_RD, 0x11, "SHLR.L ERd", 0x03)]),
("sleep",     [(FORMAT_NOP,     0x01, "SLEEP", 0x80)]), 
#stc
("sub.b", [(FORMAT_REGISTER8, 0x18, "SUB.B Rs,Rd")]),
("sub.w", [(FORMAT_IMMEDIATE16, 0x3, "SUB.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x19, "SUB.W Rs,Rd")]),
("sub.l", [(FORMAT_IMMEDIATE32, 0x3, "SUB.L #xx:32,ERd"), (FORMAT_REGISTER32, 0x1A, "SUB.L ERs,ERd")]),
("subs.l",   [(FORMAT_ONLY_RD, 0x1B, "SUBS #1,ERd", 0x00), (FORMAT_ONLY_RD, 0x1B, "SUBS #2,ERd", 0x08), (FORMAT_ONLY_RD, 0x1B, "SUBS #4,ERd", 0x09)]),
("subx",  [(FORMAT_IMMEDIATE8, 0xB, "SUBX #xx:8,Rd"), (FORMAT_REGISTER8, 0x1E, "SUBX Rs,Rd")]),
("trapa", [(FORMAT_ONLY_IMM8, 0x57, "TRAPA #x:2")]),
("xor.b", [(FORMAT_IMMEDIATE8, 0xD, "XOR.B #xx:8,Rd"), (FORMAT_REGISTER8, 0x15, "XOR.B Rs,Rd")]),
("xor.w", [(FORMAT_IMMEDIATE16, 0x5, "XOR.W #xx:16,Rd"), (FORMAT_REGISTER16, 0x65, "XOR.W Rs,Rd")]),
("xor.l", [(FORMAT_IMMEDIATE32, 0x5, "XOR.L #xx:32,ERd"), (FORMAT_AND32, 0x5, "XOR.L ERs,ERd")]),
("xorc",  [(FORMAT_ONLY_IMM8, 0x5, "XORC #xx:8,CCR")])
] 

def applyPar(inp, cha, num):

    maxbitlen = inp.count(cha)
    
    if num >= 2**maxbitlen:
        print("ERROR MAX BITLEN",inp, cha, num)
        exit(0)
        
    j = 0
    for i in range(len(inp)):
        if inp[i] == cha:
            inp[i] = str((num >> (maxbitlen-1-j))&1)
            j = j + 1
        
    
convInst = []

for inst in insts:
    for fmt in inst[1]:
        typ = fmt[0]
        #print(fmt, typ)
        pattern = ""
        if typ == FORMAT_IMMEDIATE8:
            pattern = list(formatImmedate8)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_IMMEDIATE16:
            pattern = list(formatImmedate16)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_IMMEDIATE32:
            pattern = list(formatImmedate32)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_REGISTER8:
            pattern = list(formatRegister8)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_REGISTER16:
            pattern = list(formatRegister16)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_REGISTER32:
            pattern = list(formatRegister32)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_ADDS:
            pattern = list(formatAdds)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_AND32:
            pattern = list(formatAnd32)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_ONLY_IMM8:
            pattern = list(formatOnlyImm8)
            applyPar(pattern, "o", fmt[1])
        elif typ == FORMAT_BITS_R8:
            pattern = list(formatBitR8)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "b", fmt[3])
        elif typ == FORMAT_BITS_R32:
            pattern = list(formatBitR32)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
            applyPar(pattern, "b", fmt[4])
        elif typ == FORMAT_BITS_ABS:
            pattern = list(formatBitAbs)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
            applyPar(pattern, "b", fmt[4])
        elif typ == FORMAT_BITS_RR32:
            pattern = list(formatBitRR32)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
        elif typ == FORMAT_BITS_RABS:
            pattern = list(formatBitRAbs)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
        elif typ == FORMAT_ONLY_IMM16:
            pattern = list(formatOnlyImm16)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
        elif typ == FORMAT_ONLY_RD:
            pattern = list(formatOnlyRd)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
        elif typ == FORMAT_NOP:
            pattern = list(formatNop)
            applyPar(pattern, "o", fmt[1])
            applyPar(pattern, "p", fmt[3])
        else:
            print("????")
            
        #print(str((fmt[2], ''.join(pattern)))+", ")
        convInst.append((fmt[2], ''.join(pattern)))
            
"""

TYPE_IMM  = "imm" # size, letter
TYPE_REG    = "reg" # size, letter
TYPE_CONST = "const" # const
TYPE_ABS  = "abs" # size, access size, letter
TYPE_REGCCR = "regCCR" #
TYPE_ATABS = "atmem" # size, access size, letter
TYPE_ATREG = "atreg" # size, access size, offset / '+' / '-' / None, letter
TYPE_OFFSET = "offset" # size, letter
TYPE_PCOFFSET = "pcoffset" # size, letter

convInst = [
('ADD.B #xx:8,Rd', '1000ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('ADD.B Rs,Rd', '00001000ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('ADD.W #xx:16,Rd', '011110010001ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('ADD.W Rs,Rd', '00001001ssssdddd', [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('ADD.L #xx:32,ERd', '0111101000010dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('ADD.L ERs,ERd', '000010101sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('ADDS #1,ERd', '0000101100000ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('ADDS #2,ERd', '0000101110000ddd', [(TYPE_CONST, 2), (TYPE_REG, 32, 'd')]),
('ADDS #4,ERd', '0000101110010ddd', [(TYPE_CONST, 4), (TYPE_REG, 32, 'd')]),
('ADDX #xx:8,Rd', '1001ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('ADDX Rs,Rd', '00001110ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('AND.B #xx:8,Rd', '1110ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('AND.B Rs,Rd', '00010110ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('AND.W #xx:16,Rd', '011110010110ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('AND.W Rs,Rd', '01100110ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('AND.L #xx:32,ERd', '0111101001100dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('AND.L ERs,ERd', '0000000111110000011001100sss0ddd' , [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('ANDC #xx:8,CCR', '00000110iiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REGCCR)]),
('BAND #xx:3,Rd', '011101100iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BAND #xx:3,@ERd', '011111000ddd0000011101100iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BAND #xx:3,@aa:8', '01111110aaaaaaaa011101100iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BT o:8', '01000000oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BT o:16', '0101100000000000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BF o:8', '01000001oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BF o:16', '0101100000010000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BHI o:8', '01000010oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BHI o:16', '0101100000100000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BLS o:8', '01000011oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BLS o:16', '0101100000110000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BHS o:8', '01000100oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BHS o:16', '0101100001000000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BLO o:8', '01000101oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BLO o:16', '0101100001010000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BNE o:8', '01000110oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BNE o:16', '0101100001100000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BEQ o:8', '01000111oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BEQ o:16', '0101100001110000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BVC o:8', '01001000oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BVC o:16', '0101100010000000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BVS o:8', '01001001oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BVS o:16', '0101100010010000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BPL o:8', '01001010oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BPL o:16', '0101100010100000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BMI o:8', '01001011oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BMI o:16', '0101100010110000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BGE o:8', '01001100oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BGE o:16', '0101100011000000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BLT o:8', '01001101oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BLT o:16', '0101100011010000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BGT o:8', '01001110oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BGT o:16', '0101100011100000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BLE o:8', '01001111oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BLE o:16', '0101100011110000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BCLR #xx:3,Rd', '011100100iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BCLR #xx:3,@ERd', '011111010ddd0000011100100iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BCLR #xx:3,@aa:8', '01111111aaaaaaaa011100100iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BCLR Rs,Rd', '01100010ssssdddd',  [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('BCLR Rn,@ERd', '011111010ddd000001100010nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ATREG, 32, 8, None,'d')]),
('BCLR Rn,@aa:8', '01111111aaaaaaaa01100010nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ABS, 8, 8, 'd')]),
('BIAND #xx:3,Rd', '011101101iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BIAND #xx:3,@ERd', '011111000ddd0000011101101iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BIAND #xx:3,@aa:8', '01111110aaaaaaaa011101101iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BILD #xx:3,Rd', '011101111iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BILD #xx:3,@ERd', '011111000ddd0000011101111iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BILD #xx:3,@aa:8', '01111110aaaaaaaa011101111iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BIOR #xx:3,Rd', '011101001iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BIOR #xx:3,@ERd', '011111000ddd0000011101001iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BIOR #xx:3,@aa:8', '01111110aaaaaaaa011101001iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BIST #xx:3,Rd', '011001111iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BIST #xx:3,@ERd', '011111010ddd0000011001111iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BIST #xx:3,@aa:8', '01111111aaaaaaaa011001111iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BIXOR #xx:3,Rd', '011101011iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BIXOR #xx:3,@ERd', '011111000ddd0000011101011iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BIXOR #xx:3,@aa:8', '01111110aaaaaaaa011101011iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BLD #xx:3,Rd', '011101110iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BLD #xx:3,@ERd', '011111000ddd0000011101110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BLD #xx:3,@aa:8', '01111110aaaaaaaa011101110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BNOT #xx:3,Rd', '011100010iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BNOT #xx:3,@ERd', '011111010ddd0000011100010iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BNOT #xx:3,@aa:8', '01111111aaaaaaaa011100010iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BNOT Rs,Rd', '01100001ssssdddd',  [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('BNOT Rn,@ERd', '011111010ddd000001100001nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BNOT Rn,@aa:8', '01111111aaaaaaaa01100001nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ABS, 8, 8, 'd')]),
('BOR #xx:3,Rd', '011101000iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BOR #xx:3,@ERd', '011111000ddd0000011101000iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BIOR #xx:3,@aa:8', '01111110aaaaaaaa011101000iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BSET #xx:3,Rd', '011100000iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BSET #xx:3,@ERd', '011111010ddd0000011100000iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BSET #xx:3,@aa:8', '01111111aaaaaaaa011100000iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BSET Rs,Rd', '01100000ssssdddd',  [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('BSET Rn,@ERd', '011111010ddd000001100000nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BSET Rn,@aa:8', '01111111aaaaaaaa01100000nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ABS, 8, 8, 'd')]),
('BSR o:8', '01010101oooooooo', [(TYPE_PCOFFSET, 8, 'o')]),
('BSR o:16', '0101110000000000oooooooooooooooo', [(TYPE_PCOFFSET, 16, 'o')]),
('BST #xx:3,Rd', '011001110iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BST #xx:3,@ERd', '011111010ddd0000011001110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BST #xx:3,@aa:8', '01111111aaaaaaaa011001110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BTST #xx:3,Rd', '011100110iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BTST #xx:3,@ERd', '011111000ddd0000011100110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BTST #xx:3,@aa:8', '01111110aaaaaaaa011100110iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('BTST Rs,Rd', '01100011ssssdddd',  [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('BTST Rn,@ERd', '011111000ddd000001100011nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BTST Rn,@aa:8', '01111110aaaaaaaa01100011nnnn0000',  [(TYPE_REG, 8, 'n'), (TYPE_ABS, 8, 8, 'd')]),
('BXOR #xx:3,Rd', '011101010iiidddd', [(TYPE_IMM, 3, 'i'), (TYPE_REG, 8, 'd')]),
('BXOR #xx:3,@ERd', '011111000ddd0000011101010iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ATREG, 32, 8, None, 'd')]),
('BXOR #xx:3,@aa:8', '01111110aaaaaaaa011101010iii0000', [(TYPE_IMM, 3, 'i'), (TYPE_ABS, 8, 8, 'a')]),
('CMP.B #xx:8,Rd', '1010ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('CMP.B Rs,Rd', '00011100ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('CMP.W #xx:16,Rd', '011110010010ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('CMP.W Rs,Rd', '00011101ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('CMP.L #xx:32,ERd', '0111101000100dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('CMP.L ERs,ERd', '000111111sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('DAA Rd', '000011110000dddd', [(TYPE_REG, 8, 'd')]),
('DAS Rd', '000111110000dddd', [(TYPE_REG, 8, 'd')]),
('DEC.B Rd', '000110100000dddd', [(TYPE_REG, 8, 'd')]),
('DEC.W #1,Rd', '000110110101dddd', [(TYPE_CONST, 1), (TYPE_REG, 16, 'd')]),
('DEC.W #2,Rd', '000110111101dddd', [(TYPE_CONST, 2), (TYPE_REG, 16, 'd')]),
('DEC.L #1,ERd', '0001101101110ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('DEC.L #2,ERd', '0001101111110ddd', [(TYPE_CONST, 2), (TYPE_REG, 32, 'd')]),
('DIVXS.B Rs,Rd',  '000000011101000001010001ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 16, 'd')]),
('DIVXS.W Rs,ERd', '000000011101000001010011ssss0ddd', [(TYPE_REG, 16, 's'), (TYPE_REG, 32, 'd')]),
('DIVXU.B Rs,ERd', '01010001ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 16, 'd')]),
('DIVXU.W Rs,ERd', '01010011ssss0ddd', [(TYPE_REG, 16, 's'), (TYPE_REG, 32, 'd')]),
('EEPMOV.B', '01111011010111000101100110001111', []),
('EEPMOV.W', '01111011110101000101100110001111', []),
('EXTS.W Rd', '000101111101dddd', [(TYPE_REG, 16, 'd')]),
('EXTS.L ERd', '0001011111110ddd', [(TYPE_REG, 32, 'd')]),
('EXTU.W Rd', '000101110101dddd', [(TYPE_REG, 16, 'd')]),
('EXTU.L ERd', '0001011101110ddd', [(TYPE_REG, 32, 'd')]),
('INC.B Rd', '000010100000dddd', [(TYPE_REG, 8, 'd')]),
('INC.W #1,Rd', '000010110101dddd', [(TYPE_CONST, 1), (TYPE_REG, 16, 'd')]),
('INC.W #2,Rd', '000010111101dddd', [(TYPE_CONST, 2), (TYPE_REG, 16, 'd')]),
('INC.L #1,ERd', '0000101101110ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('INC.L #2,ERd', '0000101111110ddd', [(TYPE_CONST, 2), (TYPE_REG, 32, 'd')]),
('JMP @ERn',   '010110010nnn0000', [(TYPE_ATREG, 32, 0, None, 'n')]),
('JMP @aa:24', '01011010aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 0, 'a')]),
('JMP @@aa:8', '01011011aaaaaaaa', [(TYPE_ATABS, 8, 16, 'a')]),
('JSR @ERn',   '010111010nnn0000', [(TYPE_ATREG, 32, 0, None, 'n')]),
('JSR @aa:24', '01011110aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 0, 'a')]),
('JSR @@aa:8', '01011111aaaaaaaa', [(TYPE_ATABS, 8, 16, 'a')]),
('LDC #xx:8,CCR',  '00000111iiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REGCCR)]),
('LDC Rs,CCR',     '000000110000ssss', [(TYPE_REG, 8, 's'), (TYPE_REGCCR)]),
('LDC @ERs,CCR',          '0000000101000000011010010sss0000', [(TYPE_ATREG, 32, 16, None, 's'), (TYPE_REGCCR)]),
('LDC @(o:16,ERs),CCR',   '0000000101000000011011110sss0000oooooooooooooooo', [(TYPE_ATREG, 32, 16, (TYPE_OFFSET, 16, 'o'), 's'), (TYPE_REGCCR)]),
('LDC @(o:24,ERs),CCR',   '0000000101000000011110000sss0000011010110010000000000000oooooooooooooooooooooooo', [(TYPE_ATREG, 32, 16, (TYPE_OFFSET, 24, 'o'), 's'), (TYPE_REGCCR)]),
('LDC @ERs+,CCR',         '0000000101000000011011010sss0000', [(TYPE_ATREG, 32, 16, '+', 's'), (TYPE_REGCCR)]),
('LDC @aa:16,CCR',        '00000001010000000110101100000000aaaaaaaaaaaaaaaa', [(TYPE_ABS, 16, 16, 'a'), (TYPE_REGCCR)]),
('LDC @aa:24,CCR',        '0000000101000000011010110010000000000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 16, 'a'), (TYPE_REGCCR)]),
('MOV.B #xx:8,Rd',  '1111ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('MOV.B Rs,Rd',     '00001100ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('MOV.B @ERs,Rd',   '011010000sssdddd', [(TYPE_ATREG, 32, 8, None, 's'), (TYPE_REG, 8, 'd')]),
('MOV.B @(o:16,ERs),Rd',   '011011100sssddddoooooooooooooooo', [(TYPE_ATREG, 32, 8, (TYPE_OFFSET, 16, 'o'), 's'), (TYPE_REG, 8, 'd')]),
('MOV.B @(o:24,ERs),Rd',   '011110000sss0000011010100010dddd00000000oooooooooooooooooooooooo', [(TYPE_ATREG, 32, 8, (TYPE_OFFSET, 24, 'o'), 's'), (TYPE_REG, 8, 'd')]),
('MOV.B @ERs+,Rd',     '011011000sssdddd', [(TYPE_ATREG, 32, 8, '+', 's'), (TYPE_REG, 8, 'd')]),
('MOV.B @aa:8,Rd',  '0010ddddaaaaaaaa', [(TYPE_ABS, 8, 8, 'a'), (TYPE_REG, 8, 'd')]),
('MOV.B @aa:16,Rd',  '011010100000ddddaaaaaaaaaaaaaaaa', [(TYPE_ABS, 16, 8, 'a'), (TYPE_REG, 8, 'd')]),
('MOV.B @aa:24,Rd',  '011010100010dddd00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 8, 'a'), (TYPE_REG, 8, 'd')]),
('MOV.B Rs,@ERd',  '011010001dddssss', [(TYPE_REG, 8, 's'), (TYPE_ATREG, 32, 8, None, 'd')]),
('MOV.B Rs,@(o:16,ERd)',  '011011101dddssssoooooooooooooooo', [(TYPE_REG, 8, 's'), (TYPE_ATREG, 32, 8, (TYPE_OFFSET, 16, 'o'), 'd')]),
('MOV.B Rs,@(o:24,ERd)',  '011110000ddd0000011010101010ssss00000000oooooooooooooooooooooooo', [(TYPE_REG, 8, 's'), (TYPE_ATREG, 32, 8, (TYPE_OFFSET, 24, 'o'), 'd')]),
('MOV.B Rs,@–ERd',  '011011001dddssss', [(TYPE_REG, 8, 's'), (TYPE_ATREG, 32, 8, '-', 'd')]),
('MOV.B Rs,@aa:8',  '0011ssssaaaaaaaa', [(TYPE_REG, 8, 's'), (TYPE_ABS, 8, 8, 'a')]),
('MOV.B Rs,@aa:16',  '011010101000ssssaaaaaaaaaaaaaaaa', [(TYPE_REG, 8, 's'), (TYPE_ABS, 16, 8, 'a')]),
('MOV.B Rs,@aa:24',  '011010101010ssss00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_REG, 8, 's'), (TYPE_ABS, 24, 8, 'a')]),
('MOV.W #xx:16,Rd',  '011110010000ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('MOV.W Rs,Rd',      '00001101ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('MOV.W @ERs,Rd',    '011010010sssdddd', [(TYPE_ATREG, 32, 16, None, 's'), (TYPE_REG, 16, 'd')]),
('MOV.W @(o:16,ERs),Rd',    '011011110sssddddoooooooooooooooo', [(TYPE_ATREG, 32, 16, (TYPE_OFFSET, 16, 'o'), 's'), (TYPE_REG, 16, 'd')]),
('MOV.W @(o:24,ERs),Rd',    '011110000sss0000011010110010dddd00000000oooooooooooooooooooooooo', [(TYPE_ATREG, 32, 16, (TYPE_OFFSET, 24, 'o'), 's'), (TYPE_REG, 16, 'd')]),
('MOV.W @ERs+,Rd',    '011011010sssdddd', [(TYPE_ATREG, 32, 16, '+', 's'), (TYPE_REG, 16, 'd')]),
('MOV.W @aa:16,Rd',   '011010110000ddddaaaaaaaaaaaaaaaa', [(TYPE_ABS, 16, 16, 'a'), (TYPE_REG, 16, 'd')]),
('MOV.W @aa:24,Rd',   '011010110010dddd00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 16, 'a'), (TYPE_REG, 16, 'd')]),
('MOV.W Rs,@ERd',    '011010011dddssss', [(TYPE_REG, 16, 's'), (TYPE_ATREG, 32, 16, None, 'd')]),
('MOV.W Rs,@(o:16,ERd)',  '011011111dddssssoooooooooooooooo', [(TYPE_REG, 16, 's'), (TYPE_ATREG, 32, 16, (TYPE_OFFSET, 16, 'o'), 'd')]),
('MOV.W Rs,@(o:24,ERd)',  '011110001ddd0000011010111010ssss00000000oooooooooooooooooooooooo', [(TYPE_REG, 16, 's'), (TYPE_ATREG, 32, 16, (TYPE_OFFSET, 24, 'o'), 'd')]),
('MOV.W Rs,@–ERd',    '011011011dddssss', [(TYPE_REG, 16, 's'), (TYPE_ATREG, 32, 16, '-', 'd')]),
('MOV.W Rs,@aa:16',    '011010111000ssssaaaaaaaaaaaaaaaa', [(TYPE_REG, 16, 's'), (TYPE_ABS, 16, 16, 'a')]),
('MOV.W Rs,@aa:24',    '011010111010ssss00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_REG, 16, 's'), (TYPE_ABS, 24, 16, 'a')]),
('MOV.L #xx:32,Rd',    '0111101000000dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('MOV.L ERs,ERd',      '000011111sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('MOV.L @ERs,ERd',         '0000000100000000011010010sss0ddd', [(TYPE_ATREG, 32, 32, None, 's'), (TYPE_REG, 32, 'd')]),
('MOV.L @(o:16,ERs),ERd',  '0000000100000000011011110sss0dddoooooooooooooooo', [(TYPE_ATREG, 32, 32, (TYPE_OFFSET, 16, 'o'), 's'), (TYPE_REG, 32, 'd')]),
('MOV.L @(o:24,ERs),ERd',  '0000000100000000011110000sss00000110101100100ddd00000000oooooooooooooooooooooooo', [(TYPE_ATREG, 32, 32, (TYPE_OFFSET, 24, 'o'), 's'), (TYPE_REG, 32, 'd')]),
('MOV.L @ERs+,ERd',        '0000000100000000011011010sss0ddd', [(TYPE_ATREG, 32, 32, '+', 's'), (TYPE_REG, 32, 'd')]),
('MOV.L @aa:16,ERd',       '00000001000000000110101100000dddaaaaaaaaaaaaaaaa', [(TYPE_ABS, 16, 32, 'a'), (TYPE_REG, 32, 'd')]),
('MOV.L @aa:24,ERd',       '00000001000000000110101100100ddd00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_ABS, 24, 32, 'a'), (TYPE_REG, 32, 'd')]),
('MOV.L ERs,@ERd',         '0000000100000000011010011ddd0sss', [(TYPE_REG, 32, 's'), (TYPE_ATREG, 32, 32, None, 'd')]),
('MOV.L ERs,@(o:16,ERd)',  '0000000100000000011011111ddd0sssoooooooooooooooo', [(TYPE_REG, 32, 's'), (TYPE_ATREG, 32, 32, (TYPE_OFFSET, 16, 'o'), 'd')]),
('MOV.L ERs,@(o:24,ERd)',  '0000000100000000011110000ddd00000110101110100sss00000000oooooooooooooooooooooooo', [(TYPE_REG, 32, 's'), (TYPE_ATREG, 32, 32, (TYPE_OFFSET, 24, 'o'), 'd')]),
('MOV.L ERs,@–ERd',        '0000000100000000011011011ddd0sss', [(TYPE_REG, 32, 's'), (TYPE_ATREG, 32, 32, '-', 'd')]),
('MOV.L ERs,@aa:16',       '00000001000000000110101110000sssaaaaaaaaaaaaaaaa', [(TYPE_REG, 32, 's'), (TYPE_ABS, 16, 32, 'a')]),
('MOV.L ERs,@aa:24',       '00000001000000000110101110100sss00000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_REG, 32, 's'), (TYPE_ABS, 24, 32, 'a')]),
('MOVFPE @aa:16,Rd',  '011010100100ddddaaaaaaaaaaaaaaaa', [(TYPE_ABS, 16, 8, 'a'), (TYPE_REG, 8, 'd')]),
('MOVTPE Rs,@aa:16',  '011010101100ssssaaaaaaaaaaaaaaaa', [(TYPE_REG, 8, 's'), (TYPE_ABS, 16, 8, 'a')]),
('MULXS.B Rs,Rd',  '000000011100000001010000ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 16, 'd')]),
('MULXS.W Rs,ERd', '000000011100000001010010ssss0ddd', [(TYPE_REG, 16, 's'), (TYPE_REG, 32, 'd')]),
('MULXU.B Rs,Rd', '01010000ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 16, 'd')]),
('MULXU.W Rs,ERd', '01010010ssss0ddd', [(TYPE_REG, 16, 's'), (TYPE_REG, 32, 'd')]),
('NEG.B Rd', '000101111000dddd', [(TYPE_REG, 8, 'd')]),
('NEG.W Rd', '000101111001dddd', [(TYPE_REG, 16, 'd')]),
('NEG.L ERd', '0001011110110ddd', [(TYPE_REG, 32, 'd')]),
('NOP', '0000000000000000', []),
('NOT.B Rd', '000101110000dddd', [(TYPE_REG, 8, 'd')]),
('NOT.W Rd', '000101110001dddd', [(TYPE_REG, 16, 'd')]),
('NOT.L ERd', '0001011100110ddd', [(TYPE_REG, 32, 'd')]),
('OR.B #xx:8,Rd', '1100ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('OR.B Rs,Rd', '00010100ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('OR.W #xx:16,Rd', '011110010100ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('OR.W Rs,Rd', '01100100ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('OR.L #xx:32,ERd', '0111101001000dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('OR.L ERs,ERd', '0000000111110000011001000sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('ORC #xx:8,CCR', '00000100iiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REGCCR)]),
('ROTL.B Rd', '000100101000dddd', [(TYPE_REG, 8, 'd')]),
('ROTL.W Rd', '000100101001dddd', [(TYPE_REG, 16, 'd')]),
('ROTL.L ERd', '0001001010110ddd', [(TYPE_REG, 32, 'd')]),
('ROTR.B Rd', '000100111000dddd', [(TYPE_REG, 8, 'd')]),
('ROTR.W Rd', '000100111001dddd', [(TYPE_REG, 16, 'd')]),
('ROTR.L ERd', '0001001110110ddd', [(TYPE_REG, 32, 'd')]),
('ROTXL.B Rd', '000100100000dddd', [(TYPE_REG, 8, 'd')]),
('ROTXL.W Rd', '000100100001dddd', [(TYPE_REG, 16, 'd')]),
('ROTXL.L ERd', '0001001000110ddd', [(TYPE_REG, 32, 'd')]),
('ROTXR.B Rd', '000100110000dddd', [(TYPE_REG, 8, 'd')]),
('ROTXR.W Rd', '000100110001dddd', [(TYPE_REG, 16, 'd')]),
('ROTXR.L ERd', '0001001100110ddd', [(TYPE_REG, 32, 'd')]),
('RTE', '0101011001110000', []),
('RTS', '0101010001110000', []),
('SHAL.B Rd', '000100001000dddd', [(TYPE_REG, 8, 'd')]),
('SHAL.W Rd', '000100001001dddd', [(TYPE_REG, 16, 'd')]),
('SHAL.L ERd', '0001000010110ddd', [(TYPE_REG, 32, 'd')]),
('SHAR.B Rd', '000100011000dddd', [(TYPE_REG, 8, 'd')]),
('SHAR.W Rd', '000100011001dddd', [(TYPE_REG, 16, 'd')]),
('SHAR.L ERd', '0001000110110ddd', [(TYPE_REG, 32, 'd')]),
('SHLL.B Rd', '000100000000dddd', [(TYPE_REG, 8, 'd')]),
('SHLL.W Rd', '000100000001dddd', [(TYPE_REG, 16, 'd')]),
('SHLL.L ERd', '0001000000110ddd', [(TYPE_REG, 32, 'd')]),
('SHLR.B Rd', '000100010000dddd', [(TYPE_REG, 8, 'd')]),
('SHLR.W Rd', '000100010001dddd', [(TYPE_REG, 16, 'd')]),
('SHLR.L ERd', '0001000100110ddd', [(TYPE_REG, 32, 'd')]),
('STC CCR,Rd',   '000000100000dddd', [(TYPE_REGCCR), (TYPE_REG, 8, 'd')]),
('STC CCR,@ERd',        '0000000101000000011010011ddd0000', [(TYPE_REGCCR), (TYPE_ATREG, 32, 16, None, 'd')]),
('STC CCR,@(o:16,ERd)', '0000000101000000011011111ddd0000oooooooooooooooo', [(TYPE_REGCCR), (TYPE_ATREG, 32, 16, (TYPE_OFFSET, 16, 'o'), 'd')]),
('STC CCR,@(o:24,ERd)', '0000000101000000011110000ddd0000011010111010000000000000oooooooooooooooooooooooo', [(TYPE_REGCCR), (TYPE_ATREG, 32, 16, (TYPE_OFFSET, 24, 'o'), 'd')]),
('STC CCR,@–ERd',       '0000000101000000011011011ddd0000', [(TYPE_REGCCR), (TYPE_ATREG, 32, 16, '-', 'd')]),
('STC CCR,@aa:16',       '00000001010000000110101110000000aaaaaaaaaaaaaaaa', [(TYPE_REGCCR), (TYPE_ABS, 16, 16, 'a')]),
('STC CCR,@aa:24',      '0000000101000000011010111010000000000000aaaaaaaaaaaaaaaaaaaaaaaa', [(TYPE_REGCCR), (TYPE_ABS, 24, 16, 'a')]),
('SLEEP', '0000000110000000', []),
('SUB.B Rs,Rd', '00011000ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('SUB.W #xx:16,Rd', '011110010011ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('SUB.W Rs,Rd', '00011001ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('SUB.L #xx:32,ERd', '0111101000110dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('SUB.L ERs,ERd', '000110101sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('SUBS #1,ERd', '0001101100000ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('SUBS #2,ERd', '0001101110000ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('SUBS #4,ERd', '0001101110010ddd', [(TYPE_CONST, 1), (TYPE_REG, 32, 'd')]),
('SUBX #xx:8,Rd', '1011ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('SUBX Rs,Rd', '00011110ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('TRAPA #x:2', '0101011100ii0000', [(TYPE_IMM, 2, 'i')]),
('XOR.B #xx:8,Rd', '1101ddddiiiiiiii', [(TYPE_IMM, 8, 'i'), (TYPE_REG, 8, 'd')]),
('XOR.B Rs,Rd', '00010101ssssdddd', [(TYPE_REG, 8, 's'), (TYPE_REG, 8, 'd')]),
('XOR.W #xx:16,Rd', '011110010101ddddiiiiiiiiiiiiiiii', [(TYPE_IMM, 16, 'i'), (TYPE_REG, 16, 'd')]),
('XOR.W Rs,Rd', '01100101ssssdddd' , [(TYPE_REG, 16, 's'), (TYPE_REG, 16, 'd')]),
('XOR.L #xx:32,ERd', '0111101001010dddiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', [(TYPE_IMM, 32, 'i'), (TYPE_REG, 32, 'd')]),
('XOR.L ERs,ERd', '0000000111110000011001010sss0ddd', [(TYPE_REG, 32, 's'), (TYPE_REG, 32, 'd')]),
('XORC #xx:8,CCR', '00000101iiiiiiii' , [(TYPE_IMM, 8, 'i'), (TYPE_REGCCR)]),
]


def tryToParse2(data, inst):
    match = {}
    bi = 0
    if len(data) < len(inst[1])//8: return None, 0
    for p in inst[1]:
        bit = (data[bi//8]>>(7-(bi%8)))&1
        if p == "1":
            if bit == 0:
                return None, 0
        elif p == "0": 
            if bit == 1:
                return None, 0
        else:
            if p in match:
                match[p] = (match[p]<<1) | bit
            else:
                match[p] = bit
        bi = bi + 1
    return (match, len(inst[1])//8)
    
def applyParsed(match, inst):
    r = inst[0]
    if "s" in match:
        r = r.replace("s", str(match["s"]))
    if "d" in match:
        r = r.replace("d", str(match["d"]))
    if "n" in match:
        r = r.replace("n", str(match["n"]))
    if "i" in match:
        r = r.replace("xx", str(match["i"]))
    if "a" in match:
        r = r.replace("aa", str(match["a"]))
    return r


def tryToParse(data):
    for inst in convInst:
        m, size = tryToParse2(data, inst)
        if m != None:
            return (inst, size, m)
    return (None, None, None)