# -*- coding: utf-8 -*-


class AddCols:
    def __init__(self, rastr_win: object, table: str):
        self.rastr_win = rastr_win
        self.table = table

    def find_cols(self, name_cols: str):
        return self.rastr_win.Tables(self.table).Cols.Find(name_cols)

    def add(self, name_new_cols):
        if self.find_cols(name_cols=name_new_cols) == (-1):
            self.rastr_win.Tables(self.table).Cols.Add(name_new_cols, 1)
        else:
            pass

    def return_name_cols(self, id: int) -> str:
        return self.rastr_win.Tables(self.table).Cols(id).Name


def add_cols(
        rastr_win: object,
        table: str,
        name_new_cols: str):
    if rastr_win.Tables(table).Cols.Find(name_new_cols) == (-1):
        rastr_win.Tables(table).Cols.Add(name_new_cols, 1)
    else:
        print(f"Столбец: {name_new_cols} уже добален в таблицу: {table}!")


if __name__ == '__main__':
    from equivalence.AstraRastr import RASTR
    from equivalence.Load import LoadFile
    from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file

    load_ = LoadFile(rastr_win=RASTR)
    load_.load(path_file=fr'{absolute_path_to_file}\model_test_RUSTab\test9.rst',
               name_shabl_russian='динамика')

    add = AddCols(rastr_win=RASTR, table="node")
    add.add(name_new_cols='test')
    print(add.find_cols(name_cols='test'))
    print(add.return_name_cols(add.find_cols(name_cols='test')))
    print(add.find_cols('qg'))
    print(add.return_name_cols(10))
    print(RASTR.Tables('node').Cols(10).Name)
