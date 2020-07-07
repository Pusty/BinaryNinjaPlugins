import struct

class XTENSA_INSTRUCTION():
    name = "UNKNOWN"
    len  = 3
    
instructions = """
ABS              RRR   0110 0000 rrrr 0001 tttt 0000 ABS ar, at
ABS.S            RRR   1111 1010 rrrr ssss 0001 0000 ABS.S fr, fs
ADD              RRR   1000 0000 rrrr ssss tttt 0000 ADD ar, as, at
ADD.N            RRRN            rrrr ssss tttt 1010 ADD.N ar, as, at
ADD.S            RRR   0000 1010 rrrr ssss tttt 0000 ADD.S fr, fs, ft
ADDI             RRI8  iiii iiii 1100 ssss tttt 0010 ADDI at, as, -128..127
ADDI.N           RRRN            rrrr ssss tttt 1011 ADDI.N ar, as, imm
ADDMI            RRI8  iiii iiii 1101 ssss tttt 0010 ADDMI at, as, -32768..32512
ADDX2            RRR   1001 0000 rrrr ssss tttt 0000 ADDX2 ar, as, at
ADDX4            RRR   1010 0000 rrrr ssss tttt 0000 ADDX4 ar, as, at
ADDX8            RRR   1011 0000 rrrr ssss tttt 0000 ADDDX ar, as, at
ALL4             RRR   0000 0000 1001 ssss tttt 0000 ALL4 bt, bs
ALL8             RRR   0000 0000 1011 ssss tttt 0000 ALL8 bt, bs
AND              RRR   0001 0000 rrrr ssss tttt 0000 AND ar, as, at
ANDB             RRR   0000 0010 rrrr ssss tttt 0000 ANDB br, bs, bt
ANDBC            RRR   0001 0010 rrrr ssss tttt 0000 ANDBC br, bs, bt
ANY4             RRR   0000 0000 1000 ssss tttt 0000 ANY4 bt, bs
ANY8             RRR   0000 0000 1010 ssss tttt 0000 ANY8 bt, bs
BALL             RRI8  iiii iiii 0100 ssss tttt 0111 BALL as, at, label
BANY             RRI8  iiii iiii 1000 ssss tttt 0111 BANY as, at, label
BBC              RRI8  iiii iiii 0101 ssss tttt 0111 BBC as, at, label
BBCI             RRI8  iiii iiii 011b ssss bbbb 0111 BBCI as, 0..31, label
BBS              RRI8  iiii iiii 1101 ssss tttt 0111 BBS as, at, label
BBSI             RRI8  iiii iiii 111b ssss bbbb 0111 BBSI as, 0..31, label
BEQ              RRI8  iiii iiii 0001 ssss tttt 0111 BEQ as, at, label
BEQI             RRI8  iiii iiii rrrr ssss 0010 0110 BEQI as, imm, label
BEQZ             RRI12 iiii iiii iiii ssss 0001 0110 BEQZ as, label
BEQZ.N           R16             iiii ssss 10ii 1100 BEQZ.N as, label
BF               RRI8  iiii iiii 0000 ssss 0111 0110 BF bs, label
BGE              RRI8  iiii iiii 1010 ssss tttt 0111 BGE as, at, label
BGEI             BRI8  iiii iiii rrrr ssss 1110 0110 BGEI as, imm, label
BGEU             RRI8  iiii iiii 1011 ssss tttt 0111 BGEU as, at, label
BGEUI            BRI8  iiii iiii rrrr ssss 1111 0110 BGEUI as, imm, label
BLT              RRI8  iiii iiii 0010 ssss tttt 0111 BLT as, at, label
BLTI             BRI8  iiii iiii rrrr ssss 1010 0110 BLTI as, imm, label
BLTU             RRI8  iiii iiii 0011 ssss tttt 0111 BLTU as, at, label
BLTUI            BRI8  iiii iiii rrrr ssss 1011 0110 BLTUI as, imm, label
BLTZ             BRI12 iiii iiii iiii ssss 1001 0110 BLTZ as, label
BNALL            RRI8  iiii iiii 1100 ssss tttt 0111 BNALL as, at, label
BNE              RRI8  iiii iiii 1001 ssss tttt 0111 BNE as, at, label
BNEI             BRI8  iiii iiii rrrr ssss 0110 0110 BNEI as, imm, label
BNEZ             BRI12 iiii iiii iiii ssss 0101 0110 BNEZ as, label
BNEZ.N           RI6             iiii ssss 11ii 1100 BNEZ.N as, label
BNONE            RRI8  iiii iiii 0000 ssss tttt 0111 BNONE as, at, label
BREAK            RRR   0000 0000 0100 ssss tttt 0000 BREAK 0..15, 0..15
BREAK.N          RRRN            1111 ssss 0010 1101 BREAK.N 0..15
BT               RRI8  iiii iiii 0001 ssss 0111 0110 BT bs, label
CALL0            CALL  oooo oooo oooo oooo oo00 0101 CALL0 label
CALL4            CALL  oooo oooo oooo oooo oo01 0101 CALL4 label
CALL8            CALL  oooo oooo oooo oooo oo10 0101 CALL8 label
CALL12           CALL  oooo oooo oooo oooo oo11 0101 CALL12 label
CALLX0           CALLX 0000 0000 0000 ssss 1100 0000 CALLX0 as
CALLX4           CALLX 0000 0000 0000 ssss 1101 0000 CALLX4 as
CALLX8           CALLX 0000 0000 0000 ssss 1110 0000 CALLX8 as
CALLX12          CALLX 0000 0000 0000 ssss 1111 0000 CALLX12 as
CEIL.S           RRR   1011 1010 rrrr ssss tttt 0000 CEIL.S ar, fs, 0..15
CLAMPS           RRR   0011 0011 rrrr ssss tttt 0000 CLAMPS ar, as, 7..22
DHI              RRI8  iiii iiii 0111 ssss 0110 0010 DHI as, 0..1020
DHU              RRI4  iiii 0010 0111 ssss 1000 0010 DHU as, 0..240
DHWB             RRI8  iiii iiii 0111 ssss 0100 0010 DHWB as, 0..1020
DHWBI            RRI8  iiii iiii 0111 ssss 0101 0010 DHWBI as, 0..1020
DII              RRI8  iiii iiii 0111 ssss 0111 0010 DII as, 0..1020
DIU              RRI4  iiii 0011 0111 ssss 1000 0010 DIU as, 0..240
DIWB             RRI4  iiii 0100 0111 ssss 1000 0010 DIWB as, 0..240
DIWBI            RRi4  iiii 0101 0111 ssss 1000 0010 DIWBI as, 0..240
DPFL             RRI4  iiii 0000 0111 ssss 1000 0010 DPFL as, 0..240
DPFR             RRI8  iiii iiii 0111 ssss 0000 0010 DPFR as, 0..1020
DPFRO            RRI8  iiii iiii 0111 ssss 0010 0010 DPFRO as, 0..1020
DPFW             RRI8  iiii iiii 0111 ssss 0001 0010 DPFW as, 0..1020
DPFWO            RRI8  iiii iiii 0111 ssss 0011 0010 DPFWO as, 0..1020
DSYNC            RRR   0000 0000 0010 0000 0011 0000 DSYNC
ENTRY            BRI12 iiii iiii iiii ssss 0011 0110 ENTRY as, 0..32760
ESYNC            RRR   0000 0000 0010 0000 0010 0000 ESYNC
EXCW             RRR   0000 0000 0010 0000 1000 0000 EXCW
EXTUI            RRR   pppp 010i rrrr iiii tttt 0000 EXTUI ar, at, shiftimm, maskimm
EXTW             RRR   0000 0000 0010 0000 1101 0000 EXTW
FLOAT.S          RRR   1100 1010 rrrr ssss tttt 0000 FLOAT.S fr, as, 0..15
FLOOR.S          RRR   1010 1010 rrrr ssss tttt 0000 FLOOR.S ar, fs, 0..15
IDTLB            RRR   0101 0000 1100 ssss 0000 0000 IDTLB as
IHI              RRI8  iiii iiii 0111 ssss 1110 0010 IHI as, 0..1020
IHU              RRI4  iiii 0010 0111 ssss 1101 0010 IHU as, 0..240
III              RRI8  iiii iiii 0111 ssss 1111 0010 III as, 0..1020
IITLB            RRR   0101 0000 0100 ssss 0000 0000 IITLB as
IIU              RRI4  iiii 0011 0111 ssss 1101 0010 IIU as, 0..240
ILL              CALLX 0000 0000 0000 0000 0000 0000 ILL
ILL.N            RRRN            1111 0000 0110 1101 ILL.N
IPF              RRI8  iiii iiii 0111 ssss 1100 0010 IPF as, 0..1020
IPFL             RRI4  iiii 0000 0111 ssss 1101 0010 IPFL as, 0..240
ISYNC            RRR   0000 0000 0010 0000 0000 0000 ISYNC
J                CALL  oooo oooo oooo oooo oo00 0110 J label
JX               CALLX 0000 0000 0000 ssss 1010 0000 JX as
L8UI             RRI8  iiii iiii 0000 ssss tttt 0010 L8UI at, as, 0..255
L16SI            RRI8  iiii iiii 1001 ssss tttt 0010 L16SI at, as, 0..510
L16UI            RRI8  iiii iiii 0001 ssss tttt 0010 L16UI at, as, 0..510
L32AI            RRI8  iiii iiii 1011 ssss tttt 0010 L32AI at, as, 0..1020
L32E             RRI4  0000 1001 rrrr ssss tttt 0000 L32E at, as, -64..-4
L32I             RRI8  iiii iiii 0010 ssss tttt 0010 L32I at, as, 0..1020
L32I.N           RRRN            iiii ssss tttt 1000 L32I.N at, as, 0..60
L32R             R16   iiii iiii iiii iiii tttt 0001 L32R at, label
LDCT             RRR   1111 0001 1000 ssss tttt 0000 LDCT at, as
LDDEC            RRR   1001 0000 00ww ssss 0000 0100 LDDEC mw, as
LDINC            RRR   1000 0000 00ww ssss 0000 0100 LDINC mw, as
LICT             RRR   1111 0001 0000 ssss tttt 0000 LICT at, as
LICW             RRR   1111 0001 0010 ssss tttt 0000 LICW at, as
LOOP             RRI8  iiii iiii 1000 ssss 0111 0110 LOOP as, label
LOOPGTZ          RRI8  iiii iiii 1010 ssss 0111 0110 LOOPGTZ as, label
LOOPNEZ          RRI8  iiii iiii 1001 ssss 0111 0110 LOOPNEZ as ,label
LSI              RRI8  iiii iiii 0000 ssss tttt 0011 LSI ft, as, 0..1020
LSIU             RRI8  iiii iiii 1000 ssss tttt 0011 LSIU ft, as, 0,..1020
LSX              RRR   0000 1000 rrrr ssss tttt 0000 LSX fr, as, at
LSXU             RRR   0001 1000 rrrr ssss tttt 0000 LSXU fr, as, at
MADD.S           RRR   0100 1010 rrrr ssss tttt 0000 MADD.S fr, fs, ft
MAX              RRR   0101 0011 rrrr ssss tttt 0000 MAX ar, as, at
MAXU             RRR   0111 0011 rrrr ssss tttt 0000 MAXU ar, as, at
MEMW             RRR   0000 0000 0010 0000 1100 0000 MEMW
MIN              RRR   0100 0011 rrrr ssss tttt 0000 MIN ar, as, at
MINU             RRR   0110 0011 rrrr ssss tttt 0000 MINU ar, as, at
MOV.N            RRRN            0000 ssss tttt 1101 MOV.N at, as
MOV.S            RRR   1111 1010 rrrr ssss 0000 0000 MOV.S fr, fs
MOVEQZ           RRR   1000 0011 rrrr ssss tttt 0000 MOVEQZ ar, as ,at
MOVEQZ.S         RRR   1000 1011 rrrr ssss tttt 0000 MOVEQZ.S fr, fs, at
MOVF             RRR   1100 0011 rrrr ssss tttt 0000 MOVF ar, as, bt
MOVF.S           RRR   1100 1011 rrrr ssss tttt 0000 MOVF.S fr, fs, bt
MOVGEZ           RRR   1011 0011 rrrr ssss tttt 0000 MOVGEZ ar, as, at
MOVGEZ.S         RRR   1011 1011 rrrr ssss tttt 0000 MOVGEZ.S fr, fs, at
MOVI             RRI8  iiii iiii 1010 iiii tttt 0010 MOVI at, -2048..2047
MOVI.N           RI7             iiii ssss 0iii 1100 MOVI.N as, -32..95
MOVLTZ           RRR   1010 0011 rrrr ssss tttt 0000 MOVLTZ ar, as, at
MOVLTZ.S         RRR   1010 1011 rrrr ssss tttt 0000 MOVLTZ.S fr, fs, at
MOVNEZ           RRR   1001 0011 rrrr ssss tttt 0000 MOVNEZ ar, as, at
MOVNEZ.S         RRR   1001 1011 rrrr ssss tttt 0000 MOVNEZ.S fr, fs, at
MOVSP            RRR   0000 0000 0001 ssss tttt 0000 MOVSP at, as
MOVT             RRR   1101 0011 rrrr ssss tttt 0000 MOVT ar, as, bt
MOVT.S           RRR   1101 1011 rrrr ssss tttt 0000 MOVT.S fr, fs, bt
MSUB.S           RRR   0101 1010 rrrr ssss tttt 0000 MSUB.S fr, fs, ft
MUL.AA.LL        RRR   0111 0100 0000 ssss tttt 0100 MUL.AA.LL as, at
MUL.AA.HL        RRR   0111 0101 0000 ssss tttt 0100 MUL.AA.HL as, at
MUL.AA.LH        RRR   0111 0110 0000 ssss tttt 0100 MUL.AA.LH as, at
MUL.AA.HH        RRR   0111 0111 0000 ssss tttt 0100 MUL.AA.HH as, at
MUL.AD.LL        RRR   0011 0100 0000 ssss 0y00 0100 MUL.AD.LL as, my
MUL.AD.HL        RRR   0011 0101 0000 ssss 0y00 0100 MUL.AD.HL as, my
MUL.AD.LH        RRR   0011 0110 0000 ssss 0y00 0100 MUL.AD.LH as, my
MUL.AD.HH        RRR   0011 0111 0000 ssss 0y00 0100 MUL.AD.HH as, my
MUL.DA.LL        RRR   0110 0100 0x00 0000 tttt 0100 MUL.DA.LL mx, at
MUL.DA.HL        RRR   0110 0101 0x00 0000 tttt 0100 MUL.DA.HL mx, at
MUL.DA.LH        RRR   0110 0110 0x00 0000 tttt 0100 MUL.DA.LH mx, at
MUL.DA.HH        RRR   0110 0111 0x00 0000 tttt 0100 MUL.DA.HH mx, at
MUL.DD.LL        RRR   0010 0100 0x00 0000 0y00 0100 MUL.DD.LL mx, my
MUL.DD.HL        RRR   0010 0101 0x00 0000 0y00 0100 MUL.DD.HL mx, my
MUL.DD.LH        RRR   0010 0110 0x00 0000 0y00 0100 MUL.DD.LH mx, my
MUL.DD.HH        RRR   0010 0111 0x00 0000 0y00 0100 MUL.DD.HH mx, my
MUL.S            RRR   0010 1010 rrrr ssss tttt 0000 MUL.S fr, fs, ft
MUL16S           RRR   1101 0001 rrrr ssss tttt 0000 MUL16S ar, as, at
MUL16U           RRR   1100 0001 rrrr ssss tttt 0000 MUL16U ar, as, at
MULA.AA.LL       RRR   0111 1000 0000 ssss tttt 0100 MULA.AA.LL as, at
MULA.AA.HL       RRR   0111 1001 0000 ssss tttt 0100 MULA.AA.HL as, at
MULA.AA.LH       RRR   0111 1010 0000 ssss tttt 0100 MULA.AA.LH as, at
MULA.AA.HH       RRR   0111 1011 0000 ssss tttt 0100 MULA.AA.HH as, at
MULA.AD.LL       RRR   0011 1000 0000 ssss 0y00 0100 MULA.AD.LL as, my
MULA.AD.HL       RRR   0011 1001 0000 ssss 0y00 0100 MULA.AD.HL as, my
MULA.AD.LH       RRR   0011 1010 0000 ssss 0y00 0100 MULA.AD.LH as, my
MULA.AD.HH       RRR   0011 1011 0000 ssss 0y00 0100 MULA.AD.HH as, my
MULA.DA.LL       RRR   0110 1000 0x00 0000 tttt 0100 MULA.DA.LL mx, at
MULA.DA.HL       RRR   0110 1001 0x00 0000 tttt 0100 MULA.DA.HL mx, at
MULA.DA.LH       RRR   0110 1010 0x00 0000 tttt 0100 MULA.DA.LH mx, at
MULA.DA.HH       RRR   0110 1011 0x00 0000 tttt 0100 MULA.DA.HH mx, at
MULA.DA.LL.LDDEC RRR   0101 1000 0xww ssss tttt 0100 MULA.DA.LL.LDDEC mw, as, mx, at
MULA.DA.HL.LDDEC RRR   0101 1001 0xww ssss tttt 0100 MULA.DA.HL.LDDEC mw, as, mx, at
MULA.DA.LH.LDDEC RRR   0101 1010 0xww ssss tttt 0100 MULA.DA.LH.LDDEC mw, as, mx, at
MULA.DA.HH.LDDEC RRR   0101 1011 0xww ssss tttt 0100 MULA.DA.HH.LDDEC mw, as, mx, at
MULA.DA.LL.LDINC RRR   0100 1000 0xww ssss tttt 0100 MULA.DA.LL.LDINC mw, as, mx, at
MULA.DA.HL.LDINC RRR   0100 1001 0xww ssss tttt 0100 MULA.DA.HL.LDINC mw, as, mx, at
MULA.DA.LH.LDINC RRR   0100 1010 0xww ssss tttt 0100 MULA.DA.LH.LDINC mw, as, mx, at
MULA.DA.HH.LDINC RRR   0100 1011 0xww ssss tttt 0100 MULA.DA.HH.LDINC mw, as, mx, at
MULA.DD.LL       RRR   0010 1000 0x00 0000 0y00 0100 MULA.DD.LL mx, my
MULA.DD.HL       RRR   0010 1001 0x00 0000 0y00 0100 MULA.DD.HL mx, my
MULA.DD.LH       RRR   0010 1010 0x00 0000 0y00 0100 MULA.DD.LH mx, my
MULA.DD.HH       RRR   0010 1011 0x00 0000 0y00 0100 MULA.DD.HH mx, my
MULA.DD.LL.LDDEC RRR   0001 1000 0xww ssss 0y00 0100 MULA.DD.LL.LDDEC mw, as, mx, my
MULA.DD.HL.LDDEC RRR   0001 1001 0xww ssss 0y00 0100 MULA.DD.HL.LDDEC mw, as, mx, my
MULA.DD.LH.LDDEC RRR   0001 1010 0xww ssss 0y00 0100 MULA.DD.LH.LDDEC mw, as, mx, my
MULA.DD.HH.LDDEC RRR   0101 1011 0xww ssss 0y00 0100 MULA.DD.HH.LDDEC mw, as, mx, my
MULA.DD.LL.LDINC RRR   0000 1000 0xww ssss 0y00 0100 MULA.DD.LL.LDINC mw, as, mx, my
MULA.DD.HL.LDINC RRR   0000 1001 0xww ssss 0y00 0100 MULA.DD.HL.LDINC mw, as, mx, my
MULA.DD.LH.LDINC RRR   0000 1010 0xww ssss 0y00 0100 MULA.DD.LH.LDINC mw, as, mx, my
MULA.DD.HH.LDINC RRR   0100 1011 0xww ssss 0y00 0100 MULA.DD.HH.LDINC mw, as, mx, my
MULL             RRR   1000 0010 rrrr ssss tttt 0000 MULL ar, as, at
MULS.AA.LL       RRR   0111 1100 0000 ssss tttt 0100 MULS.AA.LL as, at
MULS.AA.HL       RRR   0111 1101 0000 ssss tttt 0100 MULS.AA.HL as, at
MULS.AA.LH       RRR   0111 1110 0000 ssss tttt 0100 MULS.AA.LH as, at
MULS.AA.HH       RRR   0111 1111 0000 ssss tttt 0100 MULS.AA.HH as, at	
MULS.AD.LL       RRR   0011 1100 0000 ssss 0y00 0100 MULS.AD.LL as, my
MULS.AD.HL       RRR   0011 1101 0000 ssss 0y00 0100 MULS.AD.HL as, my
MULS.AD.LH       RRR   0011 1110 0000 ssss 0y00 0100 MULS.AD.LH as, my
MULS.AD.HH       RRR   0011 1111 0000 ssss 0y00 0100 MULS.AD.HH as, my
MULS.DA.LL       RRR   0110 1100 0x00 0000 tttt 0100 MULS.DA.LL mx, at
MULS.DA.HL       RRR   0110 1101 0x00 0000 tttt 0100 MULS.DA.HL mx, at
MULS.DA.LH       RRR   0110 1110 0x00 0000 tttt 0100 MULS.DA.LH mx, at
MULS.DA.HH       RRR   0110 1111 0x00 0000 tttt 0100 MULS.DA.HH mx, at
MULS.DD.LL       RRR   0010 1100 0x00 0000 0y00 0100 MULS.DD.LL mx, my
MULS.DD.HL       RRR   0010 1101 0x00 0000 0y00 0100 MULS.DD.HL mx, my
MULS.DD.LH       RRR   0010 1110 0x00 0000 0y00 0100 MULS.DD.LH mx, my
MULS.DD.HH       RRR   0010 1111 0x00 0000 0y00 0100 MULS.DD.HH mx, my
MULSH            RRR   1011 0010 rrrr ssss tttt 0000 MULSH ar, as, at
MULUH            RRR   1010 0010 rrrr ssss tttt 0000 MULUH ar, as, at
NEG              RRR   0110 0000 rrrr 0000 tttt 0000 NEG ar, at
NEG.S            RRR   1111 1010 rrrr ssss 0110 0000 NEG.S fr, fs
NOP              RRR   0000 0000 0010 0000 1111 0000 NOP
NOP.N            RRRN            1111 0000 0011 1101 NOP.N
NSA              RRR   0100 0000 1110 ssss tttt 0000 NSA at, as
NSAU             RRR   0100 0000 1111 ssss tttt 0000 NSAU at, as
OEQ.S            RRR   0010 1011 rrrr ssss tttt 0000 OEQ.S br, fs, ft
OLE.S            RRR   0110 1011 rrrr ssss tttt 0000 OLE.S br, fs, ft
OLT.S            RRR   0100 1011 rrrr ssss tttt 0000 OLT.S br, fs, ft
OR               RRR   0010 0000 rrrr ssss tttt 0000 OR ar, as, at
ORB              RRR   0010 0010 rrrr ssss tttt 0000 ORB br, bs, bt
ORBC             RRR   0011 0010 rrrr ssss tttt 0000 ORBC br, bs, bt
PDTLB            RRR   0101 0000 1101 ssss tttt 0000 PDTLB at, as
PITLB            RRR   0101 0000 0101 ssss tttt 0000 PITLB at, as
QUOS             RRR   1101 0010 rrrr ssss tttt 0000 QUOS ar, as, at
QUOU             RRR   1100 0010 rrrr ssss tttt 0000 QUOU ar, as, at
RDTLB0           RRR   0101 0000 1011 ssss tttt 0000 RDTLB0 at, as
RDTLB1           RRR   0101 0000 1111 ssss tttt 0000 RDTLB1 at, as
REMS             RRR   1111 0010 rrrr ssss tttt 0000 REMS ar, as, at
RER              RRR   0100 0000 0110 ssss tttt 0000 RER at, as
RET              CALLX 0000 0000 0000 0000 1000 0000 RET
RET.N            RRRN            1111 0000 0000 1101 RET.N
RETW             CALLX 0000 0000 0000 0000 1001 0000 RETW
RETW.N           RRRN            1111 0000 0001 1101 RETW.N
RFDD             RRR   1111 0001 1110 000s 0001 0000 RFDD
RFDE             RRR   0000 0000 0011 0010 0000 0000 RFDE
RFDO             RRR   1111 0001 1110 0000 0000 0000 RFDO
RFE              RRR   0000 0000 0011 0000 0000 0000 RFE
RFI              RRR   0000 0000 0011 llll 0001 0000 RFI 0..15
RFME             RRR   0000 0000 0011 0000 0010 0000 RFME
RFR              RRR   1111 1010 rrrr ssss 0100 0000 RFR
RFUE             RRR   0000 0000 0011 0001 0000 0000 RFUE
RFWO             RRR   0000 0000 0011 0100 0000 0000 RFWO
RFWU             RRR   0000 0000 0011 0101 0000 0000 RFWU
RITLB0           RRR   0101 0000 0011 ssss tttt 0000 RITLB0 at, as
RITLB1           RRR   0101 0000 0111 ssss tttt 0000 RITLB1 at, as
ROTW             RRR   0100 0000 1000 0000 iiii 0000 ROTW -8..7
ROUND.S          RRR   1000 1010 rrrr ssss tttt 0000 ROUND.S
RSIL             RRR   0000 0000 0110 iiii tttt 0000 RSIL at, 0..15
RSR              RSR   0000 0011 iiii iiii tttt 0000 RSR at, sr
RSYNC            RRR   0000 0000 0010 0000 0001 0000 RSYNC
RUR              RRR   1110 0011 rrrr ssss tttt 0000 RUR ar, ur
S8I              RRI8  iiii iiii 0100 ssss tttt 0010 S8I at, as, 0..255
S16I             RRI8  iiii iiii 0101 ssss tttt 0010 S16I at, as, 0..510
S32C1I           RRI8  iiii iiii 1110 ssss tttt 0010 S32C1I at, as, 0..1020
S32E             RRI4  0100 1001 rrrr ssss tttt 0000 S32E at, as, -64..-4
S32I             RRI8  iiii iiii 0110 ssss tttt 0010 S32I at, as, 0..1020
S32I.N           RRRN            iiii ssss tttt 1001 S32I.N at, as, 0..60
S32RI            RRI8  iiii iiii 1111 ssss tttt 0010 S32RI at, as, 0..1020
SDCT             RRR   1111 0001 1001 ssss tttt 0000 SDCT at, as
SEXT             RRR   0010 0011 rrrr ssss tttt 0000 SEXT ar, as, 7..22
SICT             RRR   1111 0001 0001 ssss tttt 0000 SICT at, as
SICW             RRR   1111 0001 0011 ssss tttt 0000 SICW at, as
SIMCALL          RRR   0000 0000 0101 0001 0000 0000 SIMCALL
SLL              RRR   1010 0001 rrrr ssss 0000 0000 SLL ar, as
SLLI             RRR   000i 0001 rrrr ssss iiii 0000 SLLI ar, as, 1..31
SRA              RRR   1011 0001 rrrr 0000 tttt 0000 SRA ar, at
SRAI             RRR   001i 0001 rrrr iiii tttt 0000 SRAI ar, at, 0..31
SRC              RRR   1000 0001 rrrr ssss tttt 0000 SRC ar, as, at
SRL              RRR   1001 0001 rrrr 0000 tttt 0000 SRL ar, at
SRLI             RRR   0100 0001 rrrr iiii tttt 0000 SRLI ar, at, 0..15
SSA8B            RRR   0100 0000 0011 ssss 0000 0000 SSA8B as
SSA8L            RRR   0100 0000 0010 ssss 0000 0000 SSA8L as
SSAI             RRR   0100 0000 0100 iiii 000i 0000 SSAI 0..31
SSI              RRI8  iiii iiii 0100 ssss tttt 0011 SSI ft, as, 0..1020
SSIU             RRI8  iiii iiii 1100 ssss tttt 0011 SSIU ft, as, 0..1020
SSL              RRR   0100 0000 0001 ssss 0000 0000 SSL as
SSR              RRR   0100 0000 0000 ssss 0000 0000 SSR as
SSX              RRR   0100 1000 rrrr ssss tttt 0000 SSX fr, as, at
SSXU             RRR   0101 1000 rrrr ssss tttt 0000 SSXU fr, as, at
SUB              RRR   1100 0000 rrrr ssss tttt 0000 SUB ar, as, at
SUB.S            RRR   0001 1010 rrrr ssss tttt 0000 SUB.S fr, fs, ft
SUBX2            RRR   1101 0000 rrrr ssss tttt 0000 SUBX2 ar, as, at
SUBX4            RRR   1110 0000 rrrr ssss tttt 0000 SUBX4 ar, as, at
SUBX8            RRR   1111 0000 rrrr ssss tttt 0000 SUBX8 ar, as, at
SYSCALL          RRR   0000 0000 0101 0000 0000 0000 SYSCALL
TRUNC.S          RRR   1001 1010 rrrr ssss tttt 0000 TRUNC.S ar, fs, 0..15
UEQ.S            RRR   0011 1011 rrrr ssss tttt 0000 UEQ.S br, fs, ft
UFLOAT.S         RRR   1101 1010 rrrr ssss tttt 0000 UFLOAT.S fr, as, 0..15
ULE.S            RRR   0111 1011 rrrr ssss tttt 0000 ULE.S br, fs, ft
ULT.S            RRR   0101 1011 rrrr ssss tttt 0000 ULT.S br, fs, ft
UMUL.AA.LL       RRR   0111 0000 0000 ssss tttt 0100 UMUL.AA.LL as, at
UMUL.AA.HL       RRR   0111 0001 0000 ssss tttt 0100 UMUL.AA.HL as, at
UMUL.AA.LH       RRR   0111 0010 0000 ssss tttt 0100 UMUL.AA.LH as, at
UMUL.AA.HH       RRR   0111 0011 0000 ssss tttt 0100 UMUL.AA.HH as, at
UN.S             RRR   0001 1011 rrrr ssss tttt 0000 UN.S br, fs, ft
UTRUNC.S         RRR   1110 1010 rrrr ssss tttt 0000 UTRUNC.S ar, fs, 0..15
WAITI            RRR   0000 0000 0111 iiii 0000 0000 WAITI 0..15
WDTLB            RRR   0101 0000 1110 ssss tttt 0000 WDTLB at, as
WER              RRR   0100 0000 0111 ssss tttt 0000 WER at, as
WFR              RRR   1111 1010 rrrr ssss 0101 0000 WFR fr, as
WITLB            RRR   0101 0000 0110 ssss tttt 0000 WITLB at, as
WSR              RSR   0001 0011 iiii iiii tttt 0000 WSR at, sr
WUR              RSR   1111 0011 iiii iiii tttt 0000 WUR at, ur
XOR              RRR   0011 0000 rrrr ssss tttt 0000 XOR ar, as, at
XORB             RRR   0100 0010 rrrr ssss tttt 0000 XORB br, bs, bt
XSR              RSR   0110 0001 iiii iiii tttt 0000 XSR at, sr
"""

def parse():
    parsed = []
    lines = instructions.split("\n")
    for line in lines:
        if line.strip() == "": continue
        parsed.append(parseLine(line))
    return parsed
        
def parseLine(line):
    name = line[0:16].strip()
    encoding = line[16:23].strip()
    
    code = line[23:53].strip()
    display = line[53:].strip()
    
    enc = code.replace(" ", "")
    
    encP = list(enc)
    for i in range(len(encP)):
        if encP[i] == '1':
            encP[i] = '1'
        else:
            encP[i] = '0'
    maskP = int(''.join(encP),2)
    
    encN = list(enc)
    for i in range(len(encN)):
        if encN[i] == '0':
            encN[i] = '1'
        else:
            encN[i] = '0'
    maskN = int(''.join(encN),2)
    lenE = len(enc)/8
    
    return (name, encoding, code, display, (lenE, maskP, maskN))

#print("...")
partsedInstructions = parse()


def getInstruction(data, l):
    if l >= 3:
        t = struct.unpack(">BBB", data[0:3])
        return (t[0]&0xFF) | ((t[1]&0xFF)<<8) | ((t[2]&0xFF)<<16)
    if l >= 2:
        t = struct.unpack(">BB", data[0:2])
        return (t[0]&0xFF) | ((t[1]&0xFF)<<8)
    return -1
    
    
def tryToParse2(data, bEnc, parsed):
    if bEnc&parsed[4][1] != parsed[4][1]: return False
    if (~bEnc)&parsed[4][2] != parsed[4][2]: return False
    #print(hex(bEnc))
    return True

def tryToParse(data, parsed):
    if parsed[4][0] > len(data): return False
    bEnc = getInstruction(data, parsed[4][0])
    return tryToParse2(data, bEnc, parsed)
    
TYPE_REG = "TYPE_REG"
TYPE_FREG = "TYPE_FREG"
TYPE_BREG = "TYPE_BREG"
TYPE_SREG = "TYPE_SREG"
TYPE_UREG = "TYPE_UREG"
TYPE_MREG = "TYPE_MREG"
TYPE_IMM = "TYPE_IMM"
TYPE_LABEL = "TYPE_LABEL"

def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask
    
printFormat = {
        "ABS": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["t"])],
        "ABS.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["t"])],
        "ADD": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ADD.N": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ADD.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "ADDI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, getSignedNumber(m["i"], 8))],
        "ADDI.N": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_IMM, (-1 if m["t"] == 0 else  m["t"]))],
        "ADDMI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, getSignedNumber(m["i"], 8)<<8)],
        "ADDX2": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ADDX4": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ADDX8": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ALL4": lambda m: [(TYPE_BREG, m["t"]), (TYPE_BREG, m["s"])],
        "ALL8": lambda m: [(TYPE_BREG, m["t"]), (TYPE_BREG, m["s"])],
        "AND": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ANDB": lambda m: [(TYPE_BREG, m["r"]), (TYPE_BREG, m["s"]), (TYPE_BREG, m["t"])],
        "ANDBC": lambda m: [(TYPE_BREG, m["r"]), (TYPE_BREG, m["s"]), (TYPE_BREG, m["t"])],
        "ANY4": lambda m: [(TYPE_BREG, m["t"]), (TYPE_BREG, m["s"])],
        "ANY8": lambda m: [(TYPE_BREG, m["t"]), (TYPE_BREG, m["s"])],
        "BALL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BANY": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BBC": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BBCI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["b"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BBS": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BBSI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["b"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BEQ": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BEQI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BEQZ": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],12)+4)],
        "BEQZ.N": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+m["i"]+4)],
        "BF": lambda m: [(TYPE_BREG, m["s"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BGE": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BGEI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BGEU": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BGEUI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BLT": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BLTI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BLTU": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BLTUI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BLTZ": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],12)+4)],
        "BNALL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BNE": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BNEI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["r"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BNEZ": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],12)+4)],
        "BNEZ.N": lambda m: [(TYPE_REG, m["s"]),(TYPE_LABEL, m["addr"]+m["i"]+4)],
        "BNONE": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "BREAK": lambda m: [(TYPE_IMM, m["s"]), (TYPE_IMM, m["t"])],
        "BREAK.N": lambda m: [(TYPE_IMM, m["s"])],
        "BT": lambda m: [(TYPE_BREG, m["s"]), (TYPE_LABEL, m["addr"]+getSignedNumber(m["i"],8)+4)],
        "CALL0": lambda m: [(TYPE_LABEL, ((m["addr"]>>2)+getSignedNumber(m["o"],18)+1)<<2)],
        "CALL4": lambda m: [(TYPE_LABEL, ((m["addr"]>>2)+getSignedNumber(m["o"],18)+1)<<2)],
        "CALL8": lambda m: [(TYPE_LABEL, ((m["addr"]>>2)+getSignedNumber(m["o"],18)+1)<<2)],
        "CALL12": lambda m: [(TYPE_LABEL, ((m["addr"]>>2)+getSignedNumber(m["o"],18)+1)<<2)],
        "CALLX0": lambda m: [(TYPE_REG, m["s"])],
        "CALLX4": lambda m: [(TYPE_REG, m["s"])],
        "CALLX8": lambda m: [(TYPE_REG, m["s"])],
        "CALLX12": lambda m: [(TYPE_REG, m["s"])],
        "CEIL.S": lambda m: [(TYPE_REG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_IMM, m["t"])],
        "CLAMPS": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["t"]+7)],
        "DHI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DHU": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "DHWB": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DHWBI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DII": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DIU": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "DIWB": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "DIWBI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "DPFL": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "DPFR": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DPFRO": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DPFW": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DPFWO": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "DSYNC": lambda m: [],
        "ENTRY": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<3)],
        "ESYNC": lambda m: [], 
        "EXCW": lambda m: [], 
        "EXTUI": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["t"]),(TYPE_IMM, m["i"]),(TYPE_IMM, m["p"])], 
        "EXTW": lambda m: [], 
        "FLOAT.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["t"]+7)],
        "FLOOR.S": lambda m: [(TYPE_REG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_IMM, m["t"]+7)],
        "IDTLB": lambda m: [(TYPE_REG, m["s"])],
        "IHI": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "IHU": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "III": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "IITLB": lambda m: [(TYPE_REG, m["s"])],
        "IIU": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "ILL": lambda m: [],
        "ILL.N": lambda m: [],
        "IPF": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "IPFL": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<4)],
        "ISYNC": lambda m: [],
        "J": lambda m: [(TYPE_LABEL, m["addr"]+getSignedNumber(m["o"],18)+4)],
        "JX": lambda m: [(TYPE_REG, m["s"])],
        "L8UI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"])],
        "L16SI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<1)],
        "L16UI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<1)],
        "L32AI": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "L32E": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, -4*(m["r"]+1))],
        "L32I": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "L32I.N": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
       # "L32R": lambda m: [(TYPE_REG, m["t"]), (TYPE_LABEL,  ((m["addr"]+3)&0xFFFFFFFC) + (getSignedNumber(m["i"], 16)<<2))],
        "L32R": lambda m: [(TYPE_REG, m["t"]), (TYPE_LABEL, ((m["addr"]+3+(getSignedNumber(m["i"], 16)<<2))&0xfffffffc if getSignedNumber(m["i"], 16) < 0 else (((m["addr"]+3+(getSignedNumber(m["i"], 16)<<2))-0x40000)&0xfffffffc)))],
        "LDCT": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "LDDEC": lambda m: [(TYPE_MREG, m["w"]), (TYPE_REG, m["s"])],
        "LDINC": lambda m: [(TYPE_MREG, m["w"]), (TYPE_REG, m["s"])],
        "LICT": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "LICW": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "LOOP": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+m["i"]+4)],
        "LOOPGTZ": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+m["i"]+4)],
        "LOOPNEZ": lambda m: [(TYPE_REG, m["s"]), (TYPE_LABEL, m["addr"]+m["i"]+4)],
        "LSI": lambda m: [(TYPE_FREG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "LSIU": lambda m: [(TYPE_FREG, m["t"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "LSX": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "LSXU": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MADD.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MAX": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MAXU": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MEMW": lambda m: [],
        "MIN": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MINU": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MOV.N": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "MOV.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"])],
        "MOVEQZ": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MOVEQZ.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MOVF": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_BREG, m["t"])],
        "MOVF.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_BREG, m["t"])],
        "MOVGEZ": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MOVGEZ.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MOVI": lambda m: [(TYPE_REG, m["t"]), (TYPE_IMM, getSignedNumber(m["i"], 12))],
        "MOVI.N": lambda m: [(TYPE_REG, m["s"]), (TYPE_IMM, getSignedNumber((m["i"] | (0x80 if ((m["i"]&0x40)!=0) and ((m["i"]&0x20)!=0) else 0)), 8))], # 7bit positve bias
        "MOVLTZ": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MOVLTZ.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MOVNEZ": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MOVNEZ.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MOVSP": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "MOVT": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_BREG, m["t"])],
        "MOVT.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_BREG, m["t"])],
        "MSUB.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MUL.AD.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MUL.AD.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MUL.AD.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MUL.AD.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MUL.AD.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MUL.AD.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MUL.AD.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MUL.AD.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MUL.DA.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MUL.DA.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MUL.DA.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MUL.DA.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MUL.DD.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MUL.DD.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MUL.DD.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MUL.DD.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MUL.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "MUL16S": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MUL16U": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULA.AA.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULA.AA.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULA.AA.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULA.AA.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULA.AD.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULA.AD.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULA.AD.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULA.AD.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULA.DA.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.LL.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HL.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.LH.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HH.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.LL.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HL.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.LH.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DA.HH.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULA.DD.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.LL.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HL.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.LH.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HH.LDDEC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.LL.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HL.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.LH.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULA.DD.HH.LDINC": lambda m: [(TYPE_MREG, m["w"]),(TYPE_REG, m["s"]), (TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULL": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULS.AA.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULS.AA.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULS.AA.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULS.AA.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULS.AD.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULS.AD.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULS.AD.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULS.AD.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_MREG, m["y"])],
        "MULS.DA.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULS.DA.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULS.DA.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULS.DA.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_REG, m["t"])],
        "MULS.DD.LL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULS.DD.HL": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULS.DD.LH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULS.DD.HH": lambda m: [(TYPE_MREG, m["x"]), (TYPE_MREG, m["y"])],
        "MULSH": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "MULUH": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "NEG": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["t"])],
        "NEG.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"])],
        "NOP": lambda m: [],
        "NOP.N": lambda m: [],
        "NSA": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "NSAU": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "OEQ.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "OLE.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "OLT.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "OR": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "ORB": lambda m: [(TYPE_BREG, m["r"]), (TYPE_BREG, m["s"]), (TYPE_BREG, m["t"])],
        "ORBC": lambda m: [(TYPE_BREG, m["r"]), (TYPE_BREG, m["s"]), (TYPE_BREG, m["t"])],
        "PDTLB": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "PITLB": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "QUOS": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "QUOU": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "RDTLB0": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "RDTLB1": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "REMS": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "RER": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "RET": lambda m: [],
        "RET.N": lambda m: [],
        "RETW": lambda m: [],
        "RETW.N": lambda m: [],
        "RFDD": lambda m: [],
        "RFDE": lambda m: [],
        "RFDO": lambda m: [],
        "RFE": lambda m: [],
        "RFI": lambda m: [(TYPE_IMM, m["l"])],
        "RFME": lambda m: [],
        "RFR": lambda m: [],
        "RFUE": lambda m: [],
        "RFWO": lambda m: [],
        "RFWU": lambda m: [],
        "RITLB0": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"])],
        "RITLB1": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"])],
        "ROTW": lambda m: [(TYPE_IMM, getSignedNumber(m["i"],4))],
        "ROUND.S": lambda m: [],
        "RSIL": lambda m: [(TYPE_REG, m["t"]),(TYPE_IMM, m["i"])],
        "RSR": lambda m: [(TYPE_REG, m["t"]),(TYPE_SREG, m["i"])],
        "RSYNC": lambda m: [],
        "RUR": lambda m: [(TYPE_REG, m["r"]),(TYPE_UREG, 16*m["s"]+m["t"])],
        "S8I": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"])],
        "S16I": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<1)],
        "S32C1I": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "S32E": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, -4*(m["r"]+1))],
        "S32I": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "S32I.N": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "S32RI": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"]<<2)],
        "SDCT": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"])],
        "SEXT": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["t"]+7)],
        "SICT": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"])],
        "SICW": lambda m: [(TYPE_REG, m["t"]),(TYPE_REG, m["s"])],
        "SIMCALL": lambda m: [],
        "SLL": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["s"])],
        "SLLI": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["s"]), (TYPE_IMM, m["i"])],
        "SRA": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["t"])],
        "SRAI": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["t"]), (TYPE_IMM, m["i"])],
        "SRC": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["s"]),(TYPE_REG, m["t"])],
        "SRL": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["t"])],
        "SRLI": lambda m: [(TYPE_REG, m["r"]),(TYPE_REG, m["t"]), (TYPE_IMM, m["i"])],
        "SSA8B": lambda m: [(TYPE_REG, m["s"])],
        "SSA8L": lambda m: [(TYPE_REG, m["s"])],
        "SSAI": lambda m: [(TYPE_IMM, m["i"])],
        "SSI": lambda m: [(TYPE_FREG, m["t"]),(TYPE_REG, m["s"]),(TYPE_IMM, m["i"]<<2)],
        "SSIU": lambda m: [(TYPE_FREG, m["t"]),(TYPE_REG, m["s"]),(TYPE_IMM, m["i"]<<2)],
        "SSL": lambda m: [(TYPE_REG, m["s"])],
        "SSR": lambda m: [(TYPE_REG, m["s"])],
        "SSX": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SSXU": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SUB": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SUB.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "SUBX2": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SUBX4": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SUBX8": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "SYSCALL": lambda m: [],
        "TRUNC.S": lambda m: [(TYPE_REG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_IMM, m["t"])],
        "UEQ.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "UFLOAT.S": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"]), (TYPE_IMM, m["t"])],
        "ULE.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "ULT.S": lambda m: [(TYPE_BREG, m["r"]), (TYPE_FREG, m["s"]), (TYPE_FREG, m["t"])],
        "UMUL.AA.LL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "UMUL.AA.HL": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "UMUL.AA.LH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "UMUL.AA.HH": lambda m: [(TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "UN.S": lambda m: [(TYPE_BREG, m["r"]),(TYPE_FREG, m["s"]),(TYPE_FREG, m["t"])],
        "UTRUNC.S": lambda m: [(TYPE_REG, m["r"]),(TYPE_FREG, m["s"]),(TYPE_IMM, m["t"])],
        "WAITI": lambda m: [(TYPE_IMM, m["i"])],
        "WDTLB": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "WER": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "WFR": lambda m: [(TYPE_FREG, m["r"]), (TYPE_REG, m["s"])],
        "WITLB": lambda m: [(TYPE_REG, m["t"]), (TYPE_REG, m["s"])],
        "WSR": lambda m: [(TYPE_REG, m["t"]), (TYPE_SREG, m["i"])],
        "WUR": lambda m: [(TYPE_REG, m["t"]), (TYPE_UREG, m["i"])],
        "XOR": lambda m: [(TYPE_REG, m["r"]), (TYPE_REG, m["s"]), (TYPE_REG, m["t"])],
        "XORB": lambda m: [(TYPE_BREG, m["r"]), (TYPE_BREG, m["s"]), (TYPE_BREG, m["t"])],
        "XSR": lambda m: [(TYPE_REG, m["t"]), (TYPE_SREG, m["i"])],
}
    
    
"""
.text:401001B0
.text:401001B0 Cache_Read_Enable_New:                  ; CODE XREF: .text:40100452
.text:401001B0                                         ; .text:loc_401006AC ...
.text:401001B0                 addi           , a1, a1, 0xF0
.text:401001B3                 s32i.n         , a0, a1, 0
.text:401001B5                 l32r           , a0, off_401001A8
.text:401001B8                 l8ui           , a0, a0, 0
.text:401001BB                 beqz.n         , a0, loc_401001CF
.text:401001BD ; ---------------------------------------------------------------------------
.text:401001BD                 bnei           , a0, 1, loc_401001DB
.text:401001C0 ; ---------------------------------------------------------------------------
.text:401001C0                 movi.n         , a2, 1
.text:401001C2                 movi.n         , a3, 0
.text:401001C4                 movi.n         , a4, 1
.text:401001C6                 l32r           , a0, dword_401001AC
.text:401001C9                 callx0         , a0
.text:401001CC ; ---------------------------------------------------------------------------
.text:401001CC                 j              , loc_401001DB
.text:401001CF ; ---------------------------------------------------------------------------
.text:401001CF
.text:401001CF loc_401001CF:                           ; CODE XREF: Cache_Read_Enable_New+B
.text:401001CF                 movi.n         , a2, 0
.text:401001D1                 movi.n         , a3, 0
.text:401001D3                 movi.n         , a4, 1
.text:401001D5                 l32r           , a0, dword_401001AC
.text:401001D8                 callx0         , a0
.text:401001DB ; ---------------------------------------------------------------------------
.text:401001DB
.text:401001DB loc_401001DB:                           ; CODE XREF: Cache_Read_Enable_New+D
.text:401001DB                                         ; Cache_Read_Enable_New+1C
.text:401001DB                 l32i.n         , a0, a1, 0
.text:401001DD                 addi           , a1, a1, 0x10
.text:401001E0                 ret.n
.text:401001E0 ; End of function Cache_Read_Enable_New
"""
    
    

def getEnc(data):
    for pI in partsedInstructions:
        if tryToParse(data, pI): return pI
    return None
    
    
    
    
def decodeEnc(data, addr=0):
    pI = getEnc(data)
    if pI == None: return None
    
    bEnc = getInstruction(data, pI[4][0])
    m = {}
    enc = pI[2].replace(" ", "")
    for i in range(len(enc)):
        if enc[i] != '0' and enc[i] != '1':
            v = ((bEnc >> ((8*pI[4][0]-1)-i))&1)
            if enc[i] in m:
                m[enc[i]] = (m[enc[i]] << 1) | v
            else:
                m[enc[i]] =  v
    m["name"] = pI[0]
    m["type"] = pI[1]
    m["len"]  = pI[4][0]
    m["addr"] = addr
    
    if pI[0] in printFormat:
        m["format"] = printFormat[pI[0]](m)
    else:
        m["format"] = []
        
    #print(m)
    
    return m
    
#print(decodeEnc("\x12\xc1\xf0"))
#print(decodeEnc("\x20\xe7\x13"))

def decode(data, addr):
    obj = XTENSA_INSTRUCTION()
    inst = decodeEnc(data, addr)
    if inst != None:
        obj.name = inst["name"]
        obj.len  = inst["len"]
        obj.prop = inst
    return obj