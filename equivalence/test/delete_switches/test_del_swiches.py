# -*- coding: utf-8 -*-
import time
from icecream import ic
from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.delete_switches.swiches import del_swiches
from equivalence.test.model.dirModel import DirModel
from equivalence.tools.tool import changing_number_of_semicolons
from equivalence.tables.Tables import Node, Vetv, Generator


load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')

generator = RASTR.Tables(Generator.table)
node = RASTR.Tables(Node.table)
vetv = RASTR.Tables(Vetv.table)

list_ = []
list_2 = []
generator.SetSel("")
j = generator.FindNextSel(-1)
while j != (-1):
    list_.append(generator.Cols(Generator.Node).Z(j))
    j = generator.FindNextSel(j)

start = time.time()
for i in list_:
    node.SetSel(f"ny={i}")
    j = node.FindNextSel(-1)
    if j != (-1):
        list_2.append(node.Cols(Node.name).Z(j))

# del_swiches(rastr_win=RASTR)
end = time.time()
print(f'Время работы: '
      f'{changing_number_of_semicolons(number=(end - start), digits=10)} сек.')

print(len(list_2))
