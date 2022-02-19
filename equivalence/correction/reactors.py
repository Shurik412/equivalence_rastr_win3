# -*- coding: utf-8 -*-
from equivalence.tables.Tables import Node


def reactors_change(rastr_win: object):
    # ************************************************************
    #  Назначение:
    #  Входные параметры: Nothing
    #  Возврат:    Nothing
    # ************************************************************
    reactors_table = rastr_win.Tables("Reactors")
    t_node = rastr_win.Tables(Node.table)
    reactors_table.SetSel("")
    reactors_table.Cols("sel").Calc(0)
    reactors_table.SetSel("")
    k = reactors_table.FindNextSel(-1)
    while k != (-1):
        ip1 = reactors_table.Cols("Id1").Z(k)
        B1 = reactors_table.Cols("B").Z(k)
        react_sta = reactors_table.Cols("sta").Z(k)
        t_node.SetSel(f"ny={ip1}")
        count_ = t_node.Count
        if count_ > 0:
            k2 = t_node.FindNextSel(-1)
            while k2 != (-1):
                t_node.Cols("bsh").SetZ(k2, t_node.Cols("bsh").Z(k2) + B1)
                if react_sta == 1:
                    t_node.Cols("sel").SetZ(k2, 1)
                k2 = t_node.FindNextSel(k2)
        k = reactors_table.FindNextSel(k)
    reactors_table.SetSel("")
    reactors_table.DelRowS()
