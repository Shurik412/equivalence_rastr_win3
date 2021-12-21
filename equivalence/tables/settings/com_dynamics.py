# -*- coding: utf-8 -*-
# Модуль переменных параметров настройки "Общие данные для расчета динамики"
# (таблица "Динамика": com_dynamics) RastrWin3

class ComDynamics:
    """

    """
    table: str = 'com_dynamics'
    table_name: str = '"Общие данные для расчета динамики"'

    Tras: str = 'Tras'  # Время расчета (Tras)
    Hint: str = 'Hint'  # Начальный шаг интегрирования (H_инт)
    Hmin: str = 'Hmin'  # Минимальный шаг интегрирования (H_мин)
    Hmax: str = 'Hmax'  # Максимальный шаг интегрирования (H_макс)
    Hout: str = 'Hout'  # Шаг печати (H_печ)
    Mint: str = 'Mint'  # Основной метод интегрирования (Осн.Метод)
    SMint: str = 'SMint'  # Стартовый метод интегрирования (Старт.Метод)
    IntEpsilon: str = 'IntEpsilon'  # Точность шага интегрирования (dInt)
    InformOnStepChange: str = 'InformOnStepChange'  # Информировать об изменении шага (Выводить шаг)
    Tf: str = 'Tf'  # Постоянная сглаживания угловой скорости (частоты) узла (Tf)
    dEf: str = 'dEf'  # Точность балансировки эдс при учете явнополюсности (dEf)
    Npf: str = 'Npf'  # Макс число пересчетов УР на шаге при учете явнополюсности (Ит)
    Valid: str = 'Valid'  # Контроль входных параметров (Контр.)
    dempfrec: str = 'dempfrec'  # Демпфирование в уравнениях движения (Демпф)
    corrT: str = 'corrT'  # Корректировать Т в парковских моделях (Корр Т)
    IsDemp: str = 'IsDemp'  # Учет демп. момента в моделях с демп контурами (Уч Демп)
    frSXNtoY: str = 'frSXNtoY'  # Напряжения перехода с СХН на шунт (V_минСХРН)
    SXNTolerance: str = 'SXNTolerance'  # Допустимый небаланс СХН (SXNTol)
    SnapPath: str = 'SnapPath'  # Выходной каталог файлов результатов (Кат. результатов)
    MaxResultFiles: str = 'MaxResultFiles'  # Максимальное кол-во файлов результатов (Макс. файлов)
    SnapTemplate: str = 'SnapTemplate'  # Шаблон имени выходного файла (Шаблон имени)
    SnapAutoLoad: str = 'SnapAutoLoad'  # Автозагрузка последнего результата (Автозагрузка)
    SnapMaxCount: str = 'SnapMaxCount'  # Максимальное кол-во слотов результатов (Макс. рез-тов)
    TripGeneratorOnSpeed: str = 'TripGeneratorOnSpeed'  # Отключать генератор при превышении скорости % (Уставка автоматов безопасности)
    PickupDropout: str = 'PickupDropout'  # Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)
    RealtimeCSV: str = 'RealtimeCSV'  # Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)
    PeriodAngle: str = 'PeriodAngle'  # Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)
    ResultFlowDirection: str = 'ResultFlowDirection'  # Положительное направление результатов (Положительное направление результатов)
    TreatWarningsAsErrors: str = 'TreatWarningsAsErrors'  # Считать предупреждения ошибками (Предупреждение=Ошибка)
    EventProcess: str = 'EventProcess'  # Метод обработки дискретных изменений (Дискретные изменения)


com_dynamics_table = 'com_dynamics'
com_dynamics_attributes_list = ['Tras', 'Hint', 'Hmin', 'Hmax', 'Hout', 'Mint', 'SMint', 'IntEpsilon',
                                'InformOnStepChange', 'Tf', 'dEf', 'Npf', 'Valid', 'dempfrec', 'corrT', 'IsDemp',
                                'frSXNtoY', 'SXNTolerance', 'SnapPath', 'MaxResultFiles', 'SnapTemplate',
                                'SnapAutoLoad', 'SnapMaxCount', 'TripGeneratorOnSpeed', 'PickupDropout', 'RealtimeCSV',
                                'PeriodAngle', 'ResultFlowDirection', 'TreatWarningsAsErrors', 'EventProcess', ]
com_dynamics_attributes = {
    'Tras': 'Время расчета (Tras)',
    'Hint': 'Начальный шаг интегрирования (H_инт)',
    'Hmin': 'Минимальный шаг интегрирования (H_мин)',
    'Hmax': 'Максимальный шаг интегрирования (H_макс)',
    'Hout': 'Шаг печати (H_печ)',
    'Mint': 'Основной метод интегрирования (Осн.Метод)',
    'SMint': 'Стартовый метод интегрирования (Старт.Метод)',
    'IntEpsilon': 'Точность шага интегрирования (dInt)',
    'InformOnStepChange': 'Информировать об изменении шага (Выводить шаг)',
    'Tf': 'Постоянная сглаживания угловой скорости (частоты) узла (Tf)',
    'dEf': 'Точность балансировки эдс при учете явнополюсности (dEf)',
    'Npf': 'Макс число пересчетов УР на шаге при учете явнополюсности (Ит)',
    'Valid': 'Контроль входных параметров (Контр.)',
    'dempfrec': 'Демпфирование в уравнениях движения (Демпф)',
    'corrT': 'Корректировать Т в парковских моделях (Корр Т)',
    'IsDemp': 'Учет демп. момента в моделях с демп контурами (Уч Демп)',
    'frSXNtoY': 'Напряжения перехода с СХН на шунт (V_минСХРН)',
    'SXNTolerance': 'Допустимый небаланс СХН (SXNTol)',
    'SnapPath': 'Выходной каталог файлов результатов (Кат. результатов)',
    'MaxResultFiles': 'Максимальное кол-во файлов результатов (Макс. файлов)',
    'SnapTemplate': 'Шаблон имени выходного файла (Шаблон имени)',
    'SnapAutoLoad': 'Автозагрузка последнего результата (Автозагрузка)',
    'SnapMaxCount': 'Максимальное кол-во слотов результатов (Макс. рез-тов)',
    'TripGeneratorOnSpeed': 'Отключать генератор при превышении скорости % (Уставка автоматов безопасности)',
    'PickupDropout': 'Информировать о пуске/возврате автоматики (Информировать о пуске/возврате автоматики)',
    'RealtimeCSV': 'Выводить контролируемые величины в CSV (Выводить контролируемые величины в CSV)',
    'PeriodAngle': 'Отображать углы в диапазоне +/-180 (Отображать углы в диапазоне +/-180)',
    'ResultFlowDirection': 'Положительное направление результатов (Положительное направление результатов)',
    'TreatWarningsAsErrors': 'Считать предупреждения ошибками (Предупреждение=Ошибка)',
    'EventProcess': 'Метод обработки дискретных изменений (Дискретные изменения)'
}
