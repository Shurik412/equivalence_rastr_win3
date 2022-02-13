# -*- coding: utf-8 -*-
from equivalence.tables.Tables import Generator

from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv


def del_swiches_gen(rastr_win: object) -> None:
    tvetv = rastr_win.Tables(Vetv.table)
    tnode = rastr_win.Tables(Node.table)
    tgenerator = rastr_win.Tables(Generator.table)

    tnode.SetSel("")
    tnode.Cols(Node.sel).Calc(0)

    tvetv.SetSel("")
    tvetv.Cols(Vetv.sel).Calc(0)
