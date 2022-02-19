# -*- coding: utf-8 -*-
from equivalence.tables.Tables import Node, Vetv


def off_the_line_from_two_side(rastr_win: object):
    """
    # ********************************************************************************
    #  Назначение: Отключение ЛЭП с двух сторон, если она включена с одной стороны.
    #  Входные параметры:   Nothing
    #  Возврат:             Nothing
    #  :param: rastr_win: object -
    # ********************************************************************************
    """
    vetv_table = rastr_win.Tables(Vetv.table)
    vetvMaxRow = vetv_table.Count - 1
    for i in range(0, vetvMaxRow):
        sta_vetv = vetv_table.Cols("sta").Z(i)
        if sta_vetv == 2 or sta_vetv == 3:
            vetv_table.Cols("sta").SetZ(i, 1)


def remove_line(rastr_win: object):
    """
    # ********************************************************************************
    #  Назначение:
    #  Входные параметры:   Nothing
    #  Возврат:             Nothing
    #  :param: rastr_win: object -
    # ********************************************************************************
    """
    node_table = rastr_win.Tables(Node.table)
    vetv_table = rastr_win.Tables(Vetv.table)
    vetv_table.SetSel("")
    k = vetv_table.FindNextSel(-1)
    while k != (-1):
        ip = vetv_table.Cols(Vetv.ip).Z(k)
        iq = vetv_table.Cols(Vetv.iq).Z(k)

        node_table.SetSel(f"ny={ip}")
        k_ip = node_table.FindNextSel(-1)
        if k_ip == (-1):
            vetv_table.Cols("sel").SetZ(k, 1)

        node_table.SetSel(f"ny={iq}")
        k_iq = node_table.FindNextSel(-1)
        if k_iq == (-1):
            vetv_table.Cols(Vetv.sel).SetZ(k, 1)
        k = vetv_table.FindNextSel(k)


def del_vetv(rastr_win: object):
    """
    # ********************************************************************************
    #  Назначение:
    #  Входные параметры:   Nothing
    #  Возврат:             Nothing
    #  :param: rastr_win: object -
    # ********************************************************************************
    """
    vetv_table = rastr_win.Tables(Vetv.table)
    node_table = rastr_win.Tables(Node.table)

    print(f"До Количество узлов = {node_table.Count}")
    print(f"До Количество ветвей = {vetv_table.Count}")

    vetv_table.SetSel("ip.ny=0|iq.ny=0")
    print(f"Удалено ветвей: {vetv_table.Count}")
    vetv_table.DelRowS()

    print(f"До Количество узлов = {node_table.Count}")
    print(f"До Количество ветвей = {vetv_table.Count}")
