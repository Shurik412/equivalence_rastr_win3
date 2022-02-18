# -*- coding: utf-8 -*-
from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.actions.group_correction import GroupCorr
from equivalence.calculation.equivalent import Equivalent
from equivalence.settings.equivalence import set_com_ekviv
from equivalence.tables.Tables import Node
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file

load_ = LoadFile(RASTR)
load_.load(path_file=fr'{absolute_path_to_file}\model_test_RUSTab\test9.rst',
           name_shabl_russian='динамика')

set_com_ekviv(
    selekv=0,
    met_ekv=0,
    tip_ekv=0,
    ekvgen=0,
    tip_gen=1,
    kfc_x='',
    pot_gen=0,
    kpn='',
    tip_sxn=0,
    smart=1,
    zmax=1000,
    otm_n=0,
    rastr_win=RASTR
)

group_corr = GroupCorr(rastr_win=RASTR, table=Node.table, column=Node.sel)
group_corr.calc(key=f"ny<1000", formula=1)

ek = Equivalent(rastr_win=RASTR,
                switch_command_line=False)
RASTR.ekv("")

save_file(rastr_win=RASTR,
          path_file=fr'{absolute_path_to_file}\model_test_RUSTab\save_model_test_RUSTab\test9_GroupCorr.rst',
          name_shabl_russian='динамика')
