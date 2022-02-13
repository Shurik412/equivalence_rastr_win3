# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.delete_switches.swiches import del_swiches
from equivalence.path_model import PATH_FILE_RASTR_LOAD
from equivalence.tools.tool import changing_number_of_semicolons

start = time.time()

load_ = LoadFile(rastr_win=RASTR)

load_.load(path_file=PATH_FILE_RASTR_LOAD, name_shabl_russian='режим')
# try:
del_swiches(rastr_win=RASTR)
# except:
#     save_file(rastr_win=RASTR,
#               path_file=r'L:\SER\Okhrimenko\Project_Py3\equivalence_rastr_win3\equivalence_node\test\equivalence_test\test_del_swiches.rg2',
#               name_shabl_russian='режим')

save_file(rastr_win=RASTR,
          path_file=r'L:\SER\Okhrimenko\Project_Py3\equivalence_rastr_win3\equivalence\test\equivalence_test\test_del_swiches.rg2',
          name_shabl_russian='режим')
end = time.time()
print(f'Время работы: {changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
