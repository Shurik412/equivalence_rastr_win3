# -*- coding: utf-8 -*-
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.AstraRastr import RASTR
from equivalence.actions.group_correction import GroupCorr
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file
from equivalence.tables.node import Node
from equivalence.calculation.equivalent import Equivalent
from equivalence.settings.equivalence import set_com_ekviv
# -*- coding: utf-8 -*-
from equivalence.actions.add_cols_in_tables import add_cols
from equivalence.actions.get import GettingParameter
from equivalence.actions.group_correction import GroupCorr
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.actions.selection import set_sel
from equivalence.actions.variable import FindNextSelection
from equivalence.actions.variable import Variable
from equivalence.calculation.regime import Regime
from equivalence.tables.Generator import Generator
from equivalence.tables.area import Area
from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv


load_ = LoadFile(RASTR)
load_.load(path_file=fr'{absolute_path_to_file}\ПРМ лето максимум.rg2', name_shabl_russian='режим')

area_tables = RASTR.Tables("area")
group_corr_area = GroupCorr(rastr_win=RASTR, table=Area.table)
add_cols(rastr_win=RASTR, table=Area.table, name_new_cols="pop_new")
# area_tables.Cols("pop_new").Calc("pop")
group_corr_area.calc_cols(key="", column="pop_new", formula=Area.pop)

print(area_tables.Cols("pop_new").Z(0))

# save_file(rastr_win=RASTR,
#           path_file=fr'{absolute_path_to_file}\ПРМ лето максимум_after.rg2', name_shabl_russian='режим')
