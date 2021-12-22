# -*- coding: utf-8 -*-


def add_cols(rastr_win: object, table: str, name_new_cols: str):
    rastr_win.Tables(table).Cols.Add(name_new_cols, 1)

