# -*- coding: utf-8 -*-
# Модуль переменных таблицы "Общие параметры эквивалентирования" RastrWin3
from dataclasses import dataclass


@dataclass(frozen=True)
class ComEkviv:
    """
    Таблица "Общие параметры эквивалентирования"
    """
    table: str = 'com_ekviv'
    table_name: str = '"Общие параметры эквивалентирования"'

    selekv: str = 'selekv'  # Отмеченные узлы: (Отмеч)
    met_ekv: str = 'mat_ekv'  # Метод эквивалентирования: (Мет Экв)
    tip_ekv: str = 'tip_ekv'  # Тип эквивалентирования: (Тип Экв)
    ekvgen: str = 'ekvgen'  # Эквивалент узлов с фикс V: (фиксV)
    tip_gen: str = 'tip_gen'  # Тип эквивалентирования генераторов: (Тип Ген)
    kfc_x: str = 'kfc_x'  # Коэффициент для Xg_ген: (К_X_Ген)
    pot_gen: str = 'pot_gen'  # Учет потерь при разносе генерации: (dP_Ген)
    kpn: str = 'kpn'  # Доля нагрузки, пересчитываемая в шунт: (d_наг)
    tip_sxn: str = 'tip_sxn'  # Учитывать СХН при эквивалентировании: (СХН)
    smart: str = 'smart'  # "Умное" эквивалентирование: (Smart)
    zmax: str = 'zmax'  # Удаление ветвей с сопротивлением большим: (Z_max)
    otm_n: str = 'otm_n'  # Отмечать узлы после эквивалентирования: (Отм)
