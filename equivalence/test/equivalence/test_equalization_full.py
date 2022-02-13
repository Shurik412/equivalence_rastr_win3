# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.equivalence_node.equalization_full import equivalent_full_to_nodes
from equivalence.test.model.dirModel import DirModel
from equivalence.tools.tool import changing_number_of_semicolons

# dir_file = fr"L:\SER\Okhrimenko\Project_Py3\equivalence_rastr_win3\equivalence_node\test\Лето_Макс_тест.rg2"
load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')

start = time.time()
equivalent_full_to_nodes(rastr_win=RASTR, name_area='Санкт-Петербург', uhom=160)
end = time.time()
print(
    f'Время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.'
)

save_file(path_file="equivalent_full_to_nodes.rg2", name_shabl_russian='режим')
