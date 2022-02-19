# -*- coding: utf-8 -*-
# Модуль переменных таблицы параметров "Утяжеление" RastrWin3


class UtCommon:
    """
    Таблица параметров "Утяжеление"
    """
    table: str = 'ut_common'
    table_name: str = '"Утяжеление"'

    maxs: str = 'maxs'  # 'Точность P (Pmax)'
    maxv: str = 'maxv'  # 'Точность V (Vmax)'
    maxd: str = 'maxd'  # 'Точность угла (Dmax)'
    maxa: str = 'maxa'  # 'Точность P района (Amax)'
    iter: str = 'iter'  # 'Макс число итераций (Imax)'
    tip: str = 'tip'  # 'Тип утяжеления (Тип)'
    f_ots: str = 'f_ots'  # 'Формировать описания контр. величин: (ФормКВ:)'
    add_d: str = 'add_d'  # 'Добавлять значения контр. величин после шага (ДобКЗ)'
    ekstr: str = 'ekstr'  # 'Поиск экстремума по контролируемым величинам (Экстремум)'
    kfc: str = 'kfc'  # 'Текущий шаг (Шаг)'
    sum_kfc: str = 'sum_kfc'  # 'Сумарный шаг (Шаг_Сумм)'
    ds: str = 'ds'  # 'Деление шага (ДелШаг)'
    it: str = 'it'  # 'Текущая итерация (Итер)'
    Status: str = 'Status'  # 'Состояние утяжеления (Статус)'
    KorrT: str = 'KorrT'  # 'коррекция по температуре: температура, Гр. (KorrT)'
    KorrPer: str = 'KorrPer'  # 'коррекция по температуре: перегрузка % (KorrPer)'
    KorrVib: str = 'KorrVib'  # 'коррекция по температуре: выборка (KorrVib)'
    enable_contr: str = 'enable_contr'  # 'Включить контроль всех ограничений U,P,I (Включить контр. U,P,I)
    dis_v_contr: str = 'dis_v_contr'  # 'Отключить контроль всех ограничений по напряжению U (Откл контр. U)'
    dis_p_contr: str = 'dis_p_contr'  # 'Отключить контроль всех ограничений по мощности P (Откл контр. P)'
    dis_i_contr: str = 'dis_i_contr'  # 'Отключить контроль всех ограничений по току I (Откл контр. I)'
    ss_calc: str = 'ss_calc'  # 'Как расчитывать УР при утяжелении (Расчет УР)'
    criterion: str = 'criterion'  # 'Критерий устойчивости (Критерий)'
    no_crit_d_ba: str = 'no_crit_d_ba'  # 'Динамика:не учет критерия разворота угла по ЛЭП (Нет критерия: угол по ЛЭП)'
    no_crit_d_coa: str = 'no_crit_d_coa'  # 'Динамика:не учет критерия угла генератора и COA (Нет критерия: угол по Генератору)'
    no_crit_d_ga: str = 'no_crit_d_ga'  # 'Динамика:не учет критерия срабатывания автомата безопасности генератора (Нет критерия: автомат безопасности ген.)'
    save_files_filter: str = 'save_files_filter'  # 'Критерий сохранения файлов (Критерий)'
    save_files_path: str = 'save_files_path'  # 'Папка для сохранения файлов результатов (Путь)'
    stop_u_n: str = 'stop_u_n'  # 'Остановить при переходе к устойчивому/неустойчивому (Остановить)'
    dyn_find_pred: str = 'dyn_find_pred'  # 'Динамика: поиск предела (Динамика: поиск предела)'