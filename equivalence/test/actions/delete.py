# -*- coding: utf-8 -*-
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.AstraRastr import RASTR
from equivalence.actions.group_correction import GroupCorr
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file
from equivalence.tables.node import Node
from equivalence.tables.Generator import Generator
from equivalence.calculation.equivalent import Equivalent
from equivalence.settings.equivalence import set_com_ekviv

load_ = LoadFile(RASTR)
load_.load(path_file=fr'{absolute_path_to_file}\model_test_RUSTab\test9.rst',
           name_shabl_russian='динамика')

gen = RASTR.Tables(Generator.table)
gen.SetSel("")
gen.DelRowS()

save_file(rastr_win=RASTR,
          path_file=fr'{absolute_path_to_file}\model_test_RUSTab\save_model_test_RUSTab\test9_DelRows.rst',
          name_shabl_russian='динамика')
