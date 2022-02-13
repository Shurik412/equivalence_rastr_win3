# -*- coding: utf-8 -*-


def add_cols(rastr_win: object, table: str, name_new_cols: str):
    if rastr_win.Tables(table).Cols.Find(name_new_cols) == (-1):
        rastr_win.Tables(table).Cols.Add(name_new_cols, 1)
    else:
        print(f"Столбец: {name_new_cols} уже добален в таблицу: {table}!")
