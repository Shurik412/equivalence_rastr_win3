# -*- coding: utf-8 -*-
from equivalence.AstraRastr import RASTR

import time

from equivalence.tables.Generator import Generator
from equivalence.tables.vetv import Vetv
from equivalence.tables.node import Node
from equivalence.tables.area import Area

from equivalence.Load import LoadFile
from equivalence.Save import save_file

from equivalence.path_model import PATH_FILE_RASTR_LOAD, PATH_FILE_RASTR_SAVE

from equivalence.calculation.regime import Regime
from equivalence.calculation.equivalent import Equivalent
from equivalence.tools.tool import changing_number_of_semicolons

rgm = Regime(rastr_win=RASTR)
eqv = Equivalent(rastr_win=RASTR)
load_ = LoadFile(rastr_win=RASTR)

start = time.time()

load_.load(path_file=PATH_FILE_RASTR_LOAD, name_shabl_russian='режим')


def sel_vetv(rastr_win: object, area: int) -> None:
    _table = rastr_win.Tables(Vetv.table)
    _sel = rastr_win.Cols(Vetv.sel)
    _table.SetSel(f"iq.na={area}&ip.na={area}")
    _sel.Calc("sel=1")


def sel_node(rastr_win: object, area: int) -> None:
    _table = rastr_win.Tables(Node.table)
    _sel = rastr_win.Cols(Node.sel)
    _table.SetSel(f"na={area}")
    _sel.Calc("sel=1")


sel_vetv(rastr_win=RASTR, area=205)
sel_node(rastr_win=RASTR, area=205)

save_file(path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')

end = time.time()
print(f'Время работы: {changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
