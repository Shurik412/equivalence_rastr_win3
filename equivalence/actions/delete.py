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
