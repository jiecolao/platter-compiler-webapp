from app.lexer.token import Token
from app.lexer.protocol import LexerProtocol


class LexerKeywords(LexerProtocol):

    # --- 'a' ---
    def s1(self):
        self.advance()
        if self.current == "l": return self.s2()
        if self.current == "n": return self.s5()
        if self.current == "p": return self.s8()
        return None  # Failed 'a' path, roll back

    def s2(self):  # al
        self.advance()
        if self.current == "t": return self.s3()
        return None

    def s3(self):  # alt (Accepting State 4)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("alt", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s5(self):  # an
        self.advance()
        if self.current == "d": return self.s6()
        return None

    def s6(self):  # and (Accepting State 7)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("and", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s8(self):  # ap
        self.advance()
        if self.current == "p": return self.s9()
        return None

    def s9(self):  # app
        self.advance()
        if self.current == "e": return self.s10()
        return None

    def s10(self):  # appe
        self.advance()
        if self.current == "n": return self.s11()
        return None

    def s11(self):  # appen
        self.advance()
        if self.current == "d": return self.s12()
        return None

    def s12(self):  # append (Accepting State 13)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("append", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'b' ---
    def s14(self):  # b
        self.advance()
        if self.current == "i": return self.s15()
        return None

    def s15(self):  # bi
        self.advance()
        if self.current == "l": return self.s16()
        return None

    def s16(self):  # bil
        self.advance()
        if self.current == "l": return self.s17()
        return None

    def s17(self):  # bill (Accepting State 18)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("bill", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'c' ---
    def s19(self):  # c
        self.advance()
        if self.current == "h": return self.s20()
        if self.current == "o": return self.s29()
        if self.current == "u": return self.s38()
        return None

    def s20(self):  # ch
        self.advance()
        if self.current == "a": return self.s21()
        if self.current == "e": return self.s25()
        return None

    def s21(self):  # cha
        self.advance()
        if self.current == "r": return self.s22()
        return None

    def s22(self):  # char
        self.advance()
        if self.current == "s": return self.s23()
        return None

    def s23(self):  # chars (Accepting State 24)
        self.advance()
        if self._match_delimiter(self.dtype_dlm):
            return Token("chars", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s25(self):  # che
        self.advance()
        if self.current == "c": return self.s26()
        return None

    def s26(self):  # chec
        self.advance()
        if self.current == "k": return self.s27()
        return None

    def s27(self):  # check (Accepting State 28)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("check", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s29(self):  # cho
        self.advance()
        if self.current == "i": return self.s30()
        if self.current == "p": return self.s34()  # 'copy' starts with 'c-o-p'
        return None

    def s30(self):  # choi
        self.advance()
        if self.current == "c": return self.s31()
        return None

    def s31(self):  # choic
        self.advance()
        if self.current == "e": return self.s32()
        return None

    def s32(self):  # choice (Accepting State 33)
        self.advance()
        if self._match_delimiter(self.whitespace_dlm):
            return Token("choice", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s34(self):  # cop
        self.advance()
        if self.current == "y": return self.s35()
        return None

    def s35(self):  # copy (Accepting State 37)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("copy", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s38(self):  # cu
        self.advance()
        if self.current == "t": return self.s39()
        return None

    def s39(self):  # cut (Accepting State 40)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("cut", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'd' ---
    def s41(self):  # d
        self.advance()
        if self.current == "o": return self.s42()
        return None

    def s42(self):  # do
        self.advance()
        if self.current == "w": return self.s43()
        return None

    def s43(self):  # dow
        self.advance()
        if self.current == "n": return self.s44()
        return None

    def s44(self):  # down (Accepting State 45)
        self.advance()
        if self._match_delimiter(self.flag_dlm):
            return Token("flag_lit", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'f' ---
    def s46(self):  # f
        self.advance()
        if self.current == "a": return self.s47()
        if self.current == "l": return self.s51()
        return None

    def s47(self):  # fa
        self.advance()
        if self.current == "c": return self.s48()
        return None

    def s48(self):  # fac
        self.advance()
        if self.current == "t": return self.s49()
        return None

    def s49(self):  # fact (Accepting State 50)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("fact", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s51(self):  # fl
        self.advance()
        if self.current == "a": return self.s52()
        return None

    def s52(self):  # fla
        self.advance()
        if self.current == "g": return self.s53()
        return None

    def s53(self):  # flag (Accepting State 54)
        self.advance()
        if self._match_delimiter(self.dtype_dlm):
            return Token("flag", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'i' ---
    def s55(self):  # i
        self.advance()
        if self.current == "n": return self.s56()
        return None

    def s56(self):  # in
        self.advance()
        if self.current == "s": return self.s57()
        return None

    def s57(self):  # ins
        self.advance()
        if self.current == "t": return self.s58()
        return None

    def s58(self):  # inst
        self.advance()
        if self.current == "e": return self.s59()
        return None

    def s59(self):  # inste
        self.advance()
        if self.current == "a": return self.s60()
        return None

    def s60(self):  # instea
        self.advance()
        if self.current == "d": return self.s61()
        return None

    def s61(self):  # instead (Accepting State 62)
        self.advance()
        if self._match_delimiter(self.curly_dlm):
            return Token("instead", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'm' ---
    def s63(self):  # m
        self.advance()
        if self.current == "a": return self.s64()
        if self.current == "e": return self.s71()
        return None

    def s64(self):  # ma
        self.advance()
        if self.current == "t": return self.s65()
        return None

    def s65(self):  # mat
        self.advance()
        if self.current == "c": return self.s66()
        return None

    def s66(self):  # matc
        self.advance()
        if self.current == "h": return self.s67()
        return None

    def s67(self):  # match
        self.advance()
        if self.current == "e": return self.s68()
        return None

    def s68(self):  # matche
        self.advance()
        if self.current == "s": return self.s69()
        return None

    def s69(self):  # matches (Accepting State 70)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("matches", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s71(self):  # me
        self.advance()
        if self.current == "n": return self.s72()
        return None

    def s72(self):  # men
        self.advance()
        if self.current == "u": return self.s73()
        return None

    def s73(self):  # menu (Accepting State 74)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("menu", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'n' ---
    def s75(self):  # n
        self.advance()
        if self.current == "e": return self.s76()
        if self.current == "o": return self.s80()
        return None

    def s76(self):  # ne
        self.advance()
        if self.current == "x": return self.s77()
        return None

    def s77(self):  # nex
        self.advance()
        if self.current == "t": return self.s78()
        return None

    def s78(self):  # next (Accepting State 79)
        self.advance()
        if self._match_delimiter(self.term_dlm):
            return Token("next", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s80(self):  # no
        self.advance()
        if self.current == "t": return self.s81()
        return None

    def s81(self):  # not (Accepting State 82)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("not", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'o' ---
    def s83(self):  # o
        self.advance()
        if self.current == "f": return self.s84()
        if self.current == "r": return self.s86()
        return None

    def s84(self):  # of (Accepting State 85)
        self.advance()
        if self._match_delimiter(self.whitespace_dlm):
            return Token("of", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s86(self):  # or (Accepting State 87)
        self.advance()
        if self.current == "d": return self.s88()
        if self._match_delimiter(self.paren_dlm):
            return Token("or", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s88(self):  # ord
        self.advance()
        if self.current == "e": return self.s89()
        return None

    def s89(self):  # orde
        self.advance()
        if self.current == "r": return self.s90()
        return None

    def s90(self):  # order (Accepting State 91)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("order", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'p' ---
    def s92(self):  # p
        self.advance()
        if self.current == "a": return self.s93()
        if self.current == "i": return self.s97()
        if self.current == "o": return self.s102()
        if self.current == "r": return self.s105()
        return None

    def s93(self):  # pa
        self.advance()
        if self.current == "s": return self.s94()
        return None

    def s94(self):  # pas
        self.advance()
        if self.current == "s": return self.s95()
        return None

    def s95(self):  # pass (Accepting State 96)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("pass", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s97(self):  # pi
        self.advance()
        if self.current == "e": return self.s98()
        return None

    def s98(self):  # pie
        self.advance()
        if self.current == "c": return self.s99()
        return None

    def s99(self):  # piec
        self.advance()
        if self.current == "e": return self.s100()
        return None

    def s100(self):  # piece (Accepting State 101)
        self.advance()
        if self._match_delimiter(self.dtype_dlm):
            return Token("piece", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s102(self):  # po
        self.advance()
        if self.current == "w": return self.s103()
        return None

    def s103(self):  # pow (Accepting State 104)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("pow", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s105(self):  # pr
        self.advance()
        if self.current == "e": return self.s106()
        return None

    def s106(self):  # pre
        self.advance()
        if self.current == "p": return self.s107()
        return None

    def s107(self):  # prep
        self.advance()
        if self.current == "a": return self.s108()
        return None

    def s108(self):  # prepa
        self.advance()
        if self.current == "r": return self.s109()
        return None

    def s109(self):  # prepar
        self.advance()
        if self.current == "e": return self.s110()
        return None

    def s110(self):  # prepare (Accepting State 111)
        self.advance()
        if self._match_delimiter(self.whitespace_dlm):
            return Token("prepare", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'r' ---
    def s112(self):  # r
        self.advance()
        if self.current == "a": return self.s113()
        if self.current == "e": return self.s117()
        return None

    def s113(self):  # ra
        self.advance()
        if self.current == "n": return self.s114()
        return None

    def s114(self):  # ran
        self.advance()
        if self.current == "d": return self.s115()
        return None

    def s115(self):  # rand (Accepting State 116)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("rand", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s117(self):  # re
        self.advance()
        if self.current == "m": return self.s118()
        if self.current == "p": return self.s123()
        if self.current == "v": return self.s128()
        return None

    def s118(self):  # rem
        self.advance()
        if self.current == "o": return self.s119()
        return None

    def s119(self):  # remo
        self.advance()
        if self.current == "v": return self.s120()
        return None

    def s120(self):  # remov
        self.advance()
        if self.current == "e": return self.s121()
        return None

    def s121(self):  # remove (Accepting State 122)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("remove", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s123(self):  # rep
        self.advance()
        if self.current == "e": return self.s124()
        return None

    def s124(self):  # repe
        self.advance()
        if self.current == "a": return self.s125()
        return None

    def s125(self):  # repea
        self.advance()
        if self.current == "t": return self.s126()
        return None

    def s126(self):  # repeat (Accepting State 127)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("repeat", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s128(self):  # rev
        self.advance()
        if self.current == "e": return self.s129()
        return None

    def s129(self):  # reve
        self.advance()
        if self.current == "r": return self.s130()
        return None

    def s130(self):  # rever
        self.advance()
        if self.current == "s": return self.s131()
        return None

    def s131(self):  # revers
        self.advance()
        if self.current == "e": return self.s132()
        return None

    def s132(self):  # reverse (Accepting State 133)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("reverse", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 's' ---
    def s134(self):  # s
        self.advance()
        if self.current == "e": return self.s135()
        if self.current == "i": return self.s145()
        if self.current == "o": return self.s151()
        if self.current == "q": return self.s155()
        if self.current == "t": return self.s159()
        return None

    def s135(self):  # se
        self.advance()
        if self.current == "a": return self.s136()
        if self.current == "r": return self.s141()
        return None

    def s136(self):  # sea
        self.advance()
        if self.current == "r": return self.s137()
        return None

    def s137(self):  # sear
        self.advance()
        if self.current == "c": return self.s138()
        return None

    def s138(self):  # searc
        self.advance()
        if self.current == "h": return self.s139()
        return None

    def s139(self):  # search (Accepting State 140)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("search", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s141(self):  # ser
        self.advance()
        if self.current == "v": return self.s142()
        return None

    def s142(self):  # serv
        self.advance()
        if self.current == "e": return self.s143()
        return None

    def s143(self):  # serve (Accepting State 144)
        self.advance()
        if self._match_delimiter(self.whitespace_dlm):
            return Token("serve", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s145(self):  # si
        self.advance()
        if self.current == "p": return self.s146()
        if self.current == "z": return self.s148()
        return None

    def s146(self):  # sip (Accepting State 147)
        self.advance()
        if self._match_delimiter(self.dtype_dlm):
            return Token("sip", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s148(self):  # siz
        self.advance()
        if self.current == "e": return self.s149()
        return None

    def s149(self):  # size (Accepting State 150)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("size", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s151(self):  # so
        self.advance()
        if self.current == "r": return self.s152()
        return None

    def s152(self):  # sor
        self.advance()
        if self.current == "t": return self.s153()
        return None

    def s153(self):  # sort (Accepting State 154)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("sort", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s155(self):  # sq
        self.advance()
        if self.current == "r": return self.s156()
        return None

    def s156(self):  # sqr
        self.advance()
        if self.current == "t": return self.s157()
        return None

    def s157(self):  # sqrt (Accepting State 158)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("sqrt", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s159(self):  # st
        self.advance()
        if self.current == "a": return self.s160()
        if self.current == "o": return self.s164()
        return None

    def s160(self):  # sta
        self.advance()
        if self.current == "r": return self.s161()
        return None

    def s161(self):  # star
        self.advance()
        if self.current == "t": return self.s162()
        return None

    def s162(self):  # start (Accepting State 163)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("start", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s164(self):  # sto
        self.advance()
        if self.current == "p": return self.s165()
        return None

    def s165(self):  # stop (Accepting State 166)
        self.advance()
        if self._match_delimiter(self.term_dlm):
            return Token("stop", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 't' ---
    def s167(self):  # t
        self.advance()
        if self.current == "a": return self.s168()
        if self.current == "o": return self.s176()
        return None

    def s168(self):  # ta
        self.advance()
        if self.current == "b": return self.s169()
        if self.current == "k": return self.s173()
        return None

    def s169(self):  # tab
        self.advance()
        if self.current == "l": return self.s170()
        return None

    def s170(self):  # tabl
        self.advance()
        if self.current == "e": return self.s171()
        return None

    def s171(self):  # table (Accepting State 172)
        self.advance()
        if self._match_delimiter(self.whitespace_dlm):
            return Token("table", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s173(self):  # tak
        self.advance()
        if self.current == "e": return self.s174()
        return None

    def s174(self):  # take (Accepting State 175)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("take", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s176(self):  # to
        self.advance()
        if self.current == "c": return self.s177()
        if self.current == "p": return self.s183()
        if self.current == "s": return self.s189()
        return None

    def s177(self):  # toc
        self.advance()
        if self.current == "h": return self.s178()
        return None

    def s178(self):  # toch
        self.advance()
        if self.current == "a": return self.s179()
        return None

    def s179(self):  # tocha
        self.advance()
        if self.current == "r": return self.s180()
        return None

    def s180(self):  # tochar
        self.advance()
        if self.current == "s": return self.s181()
        return None

    def s181(self):  # tochars (Accepting State 182)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("tochars", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s183(self):  # top
        self.advance()
        if self.current == "i": return self.s184()
        return None

    def s184(self):  # topi
        self.advance()
        if self.current == "e": return self.s185()
        return None

    def s185(self):  # topie
        self.advance()
        if self.current == "c": return self.s186()
        return None

    def s186(self):  # topiec
        self.advance()
        if self.current == "e": return self.s187()
        return None

    def s187(self):  # topiece (Accepting State 188)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("topiece", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s189(self):  # tos
        self.advance()
        if self.current == "i": return self.s190()
        return None

    def s190(self):  # tosi
        self.advance()
        if self.current == "p": return self.s191()
        return None

    def s191(self):  # tosip (Accepting State 192)
        self.advance()
        if self._match_delimiter(self.paren_dlm):
            return Token("tosip", self.get_lexeme(), self.start_line, self.start_col)
        return None

    # --- 'u' ---
    def s193(self):  # u
        self.advance()
        if self.current == "p": return self.s194()
        if self.current == "s": return self.s196()
        return None

    def s194(self):  # up (Accepting State 195)
        self.advance()
        if self._match_delimiter(self.flag_dlm):
            return Token("flag_lit", self.get_lexeme(), self.start_line, self.start_col)
        return None

    def s196(self):  # us
        self.advance()
        if self.current == "u": return self.s197()
        return None

    def s197(self):  # usu
        self.advance()
        if self.current == "a": return self.s198()
        return None

    def s198(self):  # usua
        self.advance()
        if self.current == "l": return self.s199()
        return None

    def s199(self):  # usual (Accepting State 200)
        self.advance()
        if self._match_delimiter(self.colon_dlm):
            return Token("usual", self.get_lexeme(), self.start_line, self.start_col)
        return None
