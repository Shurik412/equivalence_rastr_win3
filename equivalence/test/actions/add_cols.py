# -*- coding: utf-8 -*-
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.AstraRastr import RASTR
from equivalence.actions.group_correction import GroupCorr
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file
from equivalence.tables.node import Node
from equivalence.calculation.equivalent import Equivalent
from equivalence.settings.equivalence import set_com_ekviv
from equivalence.actions.add_cols_in_tables import add_cols
from equivalence.actions.variable import Variable

load_ = LoadFile(RASTR)
load_.load(path_file=fr'{absolute_path_to_file}\model_test_RUSTab\test9.rst',
           name_shabl_russian='динамика')

add_cols(rastr_win=RASTR, table=Node.table, name_new_cols='sel_new')

print(RASTR.Tables(Node.table).Cols("sel_new").Z(1))
var = Variable(rastr_win=RASTR)
var.make_changes_row(table=Node.table, column='sel_new', row=1, value=1)

save_file(rastr_win=RASTR,
          path_file=fr'',
          name_shabl_russian='динамика')

save_file(rastr_win=RASTR,
          path_file=fr'{absolute_path_to_file}\model_test_RUSTab\save_model_test_RUSTab\test9_add_cols.rst',
          name_shabl_russian='динамика')
