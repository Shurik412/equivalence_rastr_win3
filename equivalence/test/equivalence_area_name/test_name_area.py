# -*- coding: utf-8 -*-
from equivalence.Load import LoadFile
from equivalence.AstraRastr import RASTR
from equivalence.area_ekv import area_evk_dict
from equivalence.actions.get import GettingParameter
from equivalence.tables.area import Area
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file
from equivalence.area_ekv import area_dict

get_ = GettingParameter(rastr_win=RASTR)
dict_name_area_rastr = {}

load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=fr'{absolute_path_to_file}\ПРМ лето максимум.rg2', name_shabl_russian='режим')

count_area = get_.get_count_table_starting_zero(table=Area.table)
for row in range(0, count_area):
    dict_name_area_rastr[get_.get_cell_row(table=Area.table, column=Area.na, row=row)] = \
        get_.get_cell_row(table=Area.table, column=Area.name, row=row)

for key in dict_name_area_rastr:
    if key in area_dict:
        if dict_name_area_rastr[key] == area_dict[key]:
            print(key, dict_name_area_rastr[key], area_dict[key])
        else:
            print(f' ---- Отличение в названиях: {dict_name_area_rastr[key]} {area_evk_dict[key]}')
    else:
        print(f" ---- Не найден {key}-{dict_name_area_rastr[key]}")
