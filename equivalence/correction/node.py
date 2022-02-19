# -*- coding: utf-8 -*-
from equivalence.tables.Tables import Node, Vetv


def removing_nodes_without_branches(rastr_win: object):
    # ************************************************************
    #  Назначение: Удаление узлов без связи с ветвями
    #  Входные параметры: Nothing
    #  Возврат:    Nothing
    # ************************************************************
    table_node = rastr_win.Tables(Node.table)
    table_vetv = rastr_win.Tables(Vetv.table)
    for i in range(0, table_node.Count - 1):
        id_ny = table_node.Cols(Node.ny).Z(i)
        table_vetv.SetSel(f"ip.ny={id_ny} | iq.ny={id_ny}")
        col_vetv = table_vetv.FindNextSel(-1)
        if col_vetv == (-1):
            table_node.Cols(Node.sel).SetZ(i, 1)
    table_node.SetSel("sel=1")
    table_node.DelRowS()
