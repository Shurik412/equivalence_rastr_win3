# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.test.model.dirModel import DirModel
from equivalence.tools.tool import changing_number_of_semicolons

start = time.time()

load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')

del_swiches_new(rastr_win=RASTR,
                VIBORKA="tip=2 & sta=0 & (ip.na<500 | ip.na>600) & ip.na!=8082 & ip.na!=8037 & ip.na!=5329 & ip.na!=5230 & (iq.na<500 | iq.na>600) & iq.na!=8082 & iq.na!=8037 & iq.na!=5329 & iq.na!=5230")

end = time.time()
print(f'Время работы: '
      f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')

save_file(path_file="del_switches_vikl.rg2", name_shabl_russian='режим')
