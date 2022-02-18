# -*- coding: utf-8 -*-
import time

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.Save import save_file
from equivalence.equivalence_node.equalization_full import equivalent_full_to_nodes
from equivalence.test.model.dirModel import DirModel
from equivalence.tools.tool import changing_number_of_semicolons
from equivalence.calculation.equivalent import Equivalent

area_list = [
    "Свердловская область",
    "Челябинская область",
    "Республика Башкортостан",
    "Курганская область",
    "Удмуртская Республика",
    "Кировская область",
    "Тюменская область",
    "Саратовская область",
    "Ульяновская область",
    "Пензенская область",
    "Республика Татарстан (Татарстан)",
    "Чувашская Республика - Чувашия",
    "Республика Мордовия",
    "Республика Марий Эл",
    "Ростовская область",
    "Республика Калмыкия",
    "Волгоградская область",
    "Астраханская область",
    "Мурманская область",
    "Республика Карелия",
    "Новгородская область",
    "Псковская область",
    "Калининградская область",
    # "Архангельская область",
    "Республика Коми",
    # "Москва",
    # "Тульская область",
    # "Ивановская область",
    # "Владимирская область",
    # "Ярославская область",
    # "Костромская область",
    # "Тверская область",
    # "Смоленская область",
    # "Брянская область",
    # "Орловская область",
    # "Курская область",
    # "Липецкая область",
    # "Воронежская область",
    # "Белгородская область",
    # "Тамбовская область",
    # "Вологодская область",
    # "Рязанская область",
    # "Калужская область",
    "Финляндская Республика",
    "Западный регион",
    "Республика Беларусь",
    "Эстонская Республика",
    "Латвийская Республика",
    "Самарская область",
    "Швеция",
    "Нижегородская область",
    "Краснодарский край",
    "Литовская Республика",
    "Ленинградская область",
    "Санкт-Петербург",
    "Южный регион ",
    "Пермский край",
    "Днепровский регион",
    "Донбасский регион",
    "Северный регион",
    "Республика Крым",
    "Юго-Западный регион",
    "Ханты-Мансийский автономный округ - Югра",
    "Оренбургская область",
    # "Московская область",
    "Центральный регион ",
]

# dir_file = fr"L:\SER\Okhrimenko\Project_Py3\equivalence_rastr_win3\equivalence_node\test\Лето_Макс_тест.rg2"
load_ = LoadFile(rastr_win=RASTR)
load_.load(path_file=DirModel.fullDirName, name_shabl_russian='режим')
ekv = Equivalent(rastr_win=RASTR)

start = time.time()
for area in area_list:
    start1 = time.time()
    equivalent_full_to_nodes(rastr_win=RASTR, name_area=area, uhom=160)
    end1 = time.time()
    print(
        f' - Время работы эквивалетнирования {area}: {changing_number_of_semicolons(number=(end1 - start1), digits=3)} сек.'
    )
ekv.ekv()
end = time.time()
print(
    f'Время работы: '
    f'{changing_number_of_semicolons(number=(end - start), digits=3)} сек.'
)

save_file(path_file="equivalent_full_to_nodes.rg2", name_shabl_russian='режим')
