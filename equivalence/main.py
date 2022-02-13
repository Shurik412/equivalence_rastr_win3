# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.calculation.equivalent import Equivalent
from equivalence.calculation.regime import Regime
from equivalence.delete_switches.swiches import del_swiches, delete_area, delete_UA, del_switches_gen
from equivalence.path_model import PATH_FILE_RASTR_LOAD, PATH_FILE_RASTR_SAVE, DIR_PATH_FILE_RASTR_SAVE
from equivalence.tools.tool import changing_number_of_semicolons

start = time.time()

rgm = Regime(rastr_win=RASTR)
eqv = Equivalent(rastr_win=RASTR, switch_command_line=True)
load_ = LoadFile(rastr_win=RASTR)
sel_remove = SelectionRemoveTick(rastr_win=RASTR)

load_.load(path_file=PATH_FILE_RASTR_LOAD, name_shabl_russian='режим')

del_swiches(rastr_win=RASTR)
print('1. del_swiches')
save_file(path_file=f"{DIR_PATH_FILE_RASTR_SAVE}\del_swiches.rg2",
          name_shabl_russian='режим')
end = time.time()
print(f'Время работы "1. del_swiches": '
      f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')

del_switches_gen(rastr_win=RASTR)
print('2. del_switches_gen')
save_file(path_file=f"{DIR_PATH_FILE_RASTR_SAVE}\del_switches_gen.rg2",
          name_shabl_russian='режим')
end = time.time()
print(f'Время работы "2. del_switches_gen": '
      f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')

delete_UA(rastr_win=RASTR)
print('3. delete_UA')
save_file(path_file=f"{DIR_PATH_FILE_RASTR_SAVE}\delete_UA.rg2",
          name_shabl_russian='режим')
end = time.time()
print(f'Время работы "3. delete_UA": '
      f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')

delete_area(rastr_win=RASTR)
print('4. delete_area')
save_file(path_file=f"{DIR_PATH_FILE_RASTR_SAVE}\delete_area.rg2",
          name_shabl_russian='режим')
end = time.time()
print(f'Время работы "4. delete_area": '
      f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')

save_file(path_file=PATH_FILE_RASTR_SAVE,
          name_shabl_russian='режим')

print(f"Сохранен файл: {PATH_FILE_RASTR_SAVE}")

end = time.time()
print(f'Время работы: '
      f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.')
