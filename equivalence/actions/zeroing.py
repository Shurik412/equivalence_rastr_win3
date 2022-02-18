# -*- coding: utf-8 -*-
from equivalence.AstraRastr import RASTR
from equivalence.tables.Tables import Node, Vetv, Generator


class Zeroing:
    """
    Класс обнуления.
    """

    def __init__(self, rastr_win: object = RASTR):
        f"""
        :param rastr_win: 
        """
        self.rastr_win = rastr_win

    def node(self):
        _table = self.rastr_win.Tables(Node.table)
        _table.SetSel("")
        _table.Cols(Node.sel).Calc(0)

    def vetv(self):
        _table = self.rastr_win.Tables(Vetv.table)
        _table.SetSel("")
        _table.Cols(Vetv.sel).Calc(0)

    def generators(self):
        _table = self.rastr_win.Tables(Generator.table)
        _table.SetSel("")
        _table.Cols(Generator.sel).Calc(0)
