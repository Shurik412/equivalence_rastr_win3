# -*- coding: utf-8 -*-
# Модуль тестирования для получения параметров из RastrWin3
import unittest

from equivalence.AstraRastr import RASTR
from equivalence.Load import LoadFile
from equivalence.actions.add_cols_in_tables import AddCols
from equivalence.tables.Tables import Node
from equivalence.test.model_test_RUSTab.path_model import absolute_path_to_file


class TestAddCols(unittest.TestCase):
    """
    Тестирование класса AddCols
    """

    def setUp(self) -> None:
        # загружаем тестовую 9-ти узловую схему RastrWin3
        LoadFile(
            rastr_win=RASTR
        ).load(
            name_shabl_russian='динамика',
            path_file=rf'{absolute_path_to_file}\model_test_RUSTab\test9.rst')

        self.add_cols = AddCols(
            rastr_win=RASTR,
            table=Node.table
        )

    def test_row(self):
        self.add_cols.add(name_new_cols='test'),
        self.assertEqual(
            first=self.add_cols.find_cols(name_cols='test'),
            second=self.add_cols.find_cols(name_cols='test'),
            msg='')
