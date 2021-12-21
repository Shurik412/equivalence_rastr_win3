# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.actions.selection import SelectionTick, SelectionRemoveTick
from equivalence.area_ekv import area_ekv_dict
from equivalence.calculation.equivalent import Equivalent
from equivalence.calculation.regime import Regime
from equivalence.path_model import PATH_FILE_RASTR_LOAD, PATH_FILE_RASTR_SAVE
from equivalence.tools.tool import changing_number_of_semicolons

start = time.time()

rgm = Regime(rastr_win=RASTR)
eqv = Equivalent(rastr_win=RASTR, switch_command_line=True)
load_ = LoadFile(rastr_win=RASTR)
sel_remove = SelectionRemoveTick(rastr_win=RASTR)

load_.load(path_file=PATH_FILE_RASTR_LOAD, name_shabl_russian='режим')
save_file(rastr_win=RASTR, path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')
for na in area_ekv_dict:
    sel_move = SelectionTick(rastr_win=RASTR, area=na)
    sel_move.vetv_in_area(formula=1)
    sel_move.node_in_area(formula=1)
    eqv.ekv()
    sel_remove.vetv()
    sel_remove.node()
    if rgm.rgm() == 0:
        save_file(rastr_win=RASTR, path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')
    else:
        load_.load(path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')

save_file(path_file=PATH_FILE_RASTR_SAVE, name_shabl_russian='режим')

end = time.time()
print(f'Время работы: {changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
