# -*- coding: utf-8 -*-
# Модуль для удаления строк из таблиц RastrWin3

def full_delete_table(rastr_win: object, table: str, switch_command_line: bool = False) -> None:
    f"""
    Полная очистка таблицы \n
    :param rastr_win: COM - объект Rastr.Astra (win32com);\n
    :param table: таблица RastrWin3;\n
    :param switch_command_line: True/False - выводит сообщения в протокол;\n
    :return: None;\n
    """
    _table = rastr_win.Tables(table)
    _table.DelRowS()
    if switch_command_line:
        print(f"Табилца {table} очищена!")


class Delete:
    def __init__(self, rastr_win: object, table: str):
        self.rastr_win = rastr_win
        self.table = table

    def row(self, id: int) -> None:
        _table = self.rastr_win.Tables(self.table)
        _table.DelRow(id)

    def rows(self) -> None:
        _table = self.rastr_win.Tables(self.table)
        _table.SetSel("")
        _table.DelRowS()


if __name__ == '__main__':
    from equivalence.AstraRastr import RASTR
    from equivalence.Load import LoadFile
    from equivalence.tables.Tables import Node
    from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file

    load_ = LoadFile(RASTR)
    load_.load(path_file=fr'{absolute_path_to_file}\model_test_RUSTab\test9.rst',
               name_shabl_russian='динамика')

    del_obj = Delete(rastr_win=RASTR, table=Node.table)
    tb = RASTR.Tables(Node.table)
    tb.SetSel("")
    print(tb.Count)

    del_obj.row(id=1)
    print(tb.Count)