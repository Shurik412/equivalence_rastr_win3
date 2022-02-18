# -*- coding: utf-8 -*-
import time

from equivalence.test.model.dirModel import DirModel
from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.actions.selection import SelectionRemoveTick
from equivalence.calculation.equivalent import Equivalent
from equivalence.calculation.regime import Regime
from equivalence.equivalence_node.equalization_full import equivalent_full_to_nodes
from equivalence.tables.Tables import Node, Vetv, Generator
from equivalence.tools.tool import changing_number_of_semicolons
from equivalence.delete_switches.new_algorithm.swiches_del import del_swiches_new
from equivalence.delete_switches.swiches import del_swiches
from equivalence.delete_switches.swiches import delete_area, delete_UKR, del_swiches, del_switches_gen, vzd_node
from equivalence.settings.equivalence import set_com_ekviv
from equivalence.settings.regim import set_regim
from equivalence.actions.group_correction import Zeroing

start = time.time()

area_list = [
    ["Свердловская область", 230, 430, 580, 102],
    ["Челябинская область", 230, 430, 580, 103],
    ["Тюменская область", 230, 430, 580, 109],
    ["Курганская область", 230, 430, 580, 105],
    ["Ханты-Мансийский автономный округ - Югра", 230, 430, 580, 8080],
    ["Кировская область", 230, 430, 580, 108],
    # ["Нижегородская область", 160, 170, 250, 2090],
    ["Оренбургская область", 160, 170, 250, 8081],
    ["Пензенская область", 160, 170, 250, 204],
    ["Пермский край", 160, 170, 250, 8074],
    ["Республика Башкортостан", 230, 430, 580, 104],
    ["Республика Марий Эл", 160, 170, 250, 208],
    ["Республика Мордовия", 160, 170, 250, 207],
    ["Республика Татарстан (Татарстан)", 160, 170, 250, 205],
    ["Самарская область", 160, 170, 250, 813],
    ["Саратовская область", 160, 170, 250, 202],
    ["Удмуртская Республика", 160, 170, 250, 107],
    ["Ульяновская область", 160, 170, 250, 203],
    ["Чувашская Республика - Чувашия", 160, 170, 250, 206],
    ["Астраханская область", 160, 170, 250, 312],
    # ["Волгоградская область", 160, 170, 250, 311],
    ["Краснодарский край", 160, 170, 250, 3020],
    ["Республика Калмыкия", 160, 170, 250, 309],
    # ["Ростовская область", 160, 170, 250, 301],
    ["Республика Крым", 160, 170, 250, 8078],
    # ["Архангельская область", 160, 170, 250, 408],
    # ["Ленинградская область", 160, 170, 250, 8071],
    ["Мурманская область", 160, 170, 250, 401],
    ["Калининградская область", 160, 170, 250, 407],
    # ["Новгородская область", 160, 170, 250, 404],
    # ["Псковская область", 160, 170, 250, 405],
    ["Республика Карелия", 160, 170, 250, 402],
    # ["Республика Коми", 160, 170, 250, 409],
    # ["Санкт-Петербург", 160, 170, 250, 8072],
    ["Финляндская Республика", 160, 170, 250, 801],
    ["Эстонская Республика", 160, 170, 250, 805],
    ["Латвийская Республика", 160, 170, 250, 806],
    ["Швеция", 160, 170, 250, 819],
    ["Литовская Республика", 160, 170, 250, 8070],
    # ["Западный регион", 160, 170, 250, 803],
    # ["Центральный регион ", 160, 170, 250, 8083],
    # ["Южный регион ", 160, 170, 250, 8073],
    # ["Днепровский регион", 160, 170, 250, 8075],
    # ["Донбасский регион", 160, 170, 250, 8076],
    # ["Северный регион", 160, 170, 250, 8077],
    # ["Юго-Западный регион", 160, 170, 250, 8079],
    # ["Республика Беларусь", 160, 170, 250, 807],
    # ["Москва", 510],
    # ["Тульская область", 511],
    # ["Ивановская область", 513],
    # ["Владимирская область", 514],
    # ["Ярославская область", 515],
    # ["Костромская область", 516],
    # ["Тверская область", 517],
    # ["Смоленская область", 518],
    # ["Брянская область", 519],
    # ["Орловская область", 521],
    # ["Курская область", 523],
    # ["Липецкая область", 524],
    # ["Воронежская область", 526],
    # ["Белгородская область", 527],
    # ["Тамбовская область", 528],
    # ["Вологодская область", 529],
    # ["Рязанская область", 531],
    # ["Калужская область", 532],
    # ["Московская область", 8082],
]

rgm = Regime(rastr_win=RASTR)
eqv = Equivalent(rastr_win=RASTR)
load_ = LoadFile(rastr_win=RASTR)
sel_remove = SelectionRemoveTick(rastr_win=RASTR)
zeroing_object = Zeroing(rastr_win=RASTR)

load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')

table_node = RASTR.Tables(Node.table)
table_vetv = RASTR.Tables(Vetv.table)

set_com_ekviv(
    zmax=1000,
    otm_n=0,
    smart=0,
    tip_ekv=0,
    ekvgen=0,
    tip_gen=1,
    ek_sh=0,
)

zeroing_object.node()
zeroing_object.vetv()

off_the_line_from_two_side(rastr_win=RASTR)
off_the_generator_if_the_node_off(rastr_win=RASTR)

for area in area_list:
    equivalent_full_to_nodes(
        rastr_win=RASTR,
        name_area=area[0],
        uhom=area[1],
        v_ip_input=area[2],
        v_iq_input=area[3]
    )
    eqv.ekv()

    table_node.SetSel("")
    table_node.Cols(Node.sel).Calc(0)

    table_vetv.SetSel("")
    table_vetv.Cols(Vetv.sel).Calc(0)
    # save_file(rastr_win=RASTR, path_file=f'{area}.rg2', name_shabl_russian='режим')

del_swiches(rastr_win=RASTR)
print('1. del_swiches')
save_file(rastr_win=RASTR, path_file='1_del_swiches.rg2', name_shabl_russian='режим')

del_switches_gen(rastr_win=RASTR)
print('2. del_switches_gen')
save_file(rastr_win=RASTR, path_file='2_del_switches_gen.rg2', name_shabl_russian='режим')

delete_UKR(rastr_win=RASTR)
print('3. delete_UKR')
save_file(rastr_win=RASTR, path_file='3_delete_UKR.rg2', name_shabl_russian='режим')

delete_area(rastr_win=RASTR)
print('4. delete_area')
save_file(rastr_win=RASTR, path_file='4_delete_area.rg2', name_shabl_russian='режим')

vzd_node(rastr_win=RASTR)
print('6. vzd_node')

off_the_line_from_two_side(rastr_win=RASTR)
removing_nodes_without_branches(rastr_win=RASTR)
off_the_generator_if_the_node_off(rastr_win=RASTR)
delete_Generator_without_nodes(rastr_win=RASTR)
reactors_change(rastr_win=RASTR)

remove_line(rastr_win=RASTR)

end = time.time()
print(
    f'Время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.'
)

save_file(rastr_win=RASTR, path_file='main2.rg2', name_shabl_russian='режим')
