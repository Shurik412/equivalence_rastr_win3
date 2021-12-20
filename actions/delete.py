# -*- coding: utf-8 -*-
from dynamic_data_RUSTab.actions.get import GettingParameter


def full_delete_table(rastr_win, table: str):
    """

    :param rastr_win:
    :param table:
    :return:
    """
    _table = rastr_win.Tables(table)
    get = GettingParameter(rastr_win=rastr_win)
    for row in range(0, get.get_count_table(table=table)):
        _table.DelRow(row)