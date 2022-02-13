# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.delete_switches.swiches import vzd_node
from equivalence.test.model.dirModel import DirModel
from equivalence.tools.tool import changing_number_of_semicolons

# dir_file = fr"L:\SER\Okhrimenko\Project_Py3\equivalence_rastr_win3\equivalence_node\test\Лето_Макс_тест.rg2"
load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')

start = time.time()
vzd_node(rastr_win=RASTR)
end = time.time()
print(
    f'Время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')

save_file(path_file="vzd_node.rg2", name_shabl_russian='режим')
