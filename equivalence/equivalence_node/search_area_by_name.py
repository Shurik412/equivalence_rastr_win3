# -*- coding: utf-8 -*-
from equivalence.tables.area import Area


def na_of_the_area_by_name(rastr_win: object, name_area: str) -> str:
    """
    '************************************************************
    ' Назначение:
    ' Входные параметры: Nothing
    ' Возврат:    Nothing
    '************************************************************
    """

    table_area = rastr_win.Tables(Area.table)
    na_by_name = ""
    max_count_area = table_area.Count
    for i in range(0, max_count_area):
        name_ = table_area.Cols(Area.name).Z(i)
        if name_ == name_area:
            na_by_name = table_area.Cols(Area.na).Z(i)
            print(f" - Название района: {name_}; номер района: {na_by_name}")
            break
    if na_by_name == "":
        na_by_name = "None"

    return na_by_name
