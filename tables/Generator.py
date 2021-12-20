# -*- coding: utf-8 -*-
# Модуль параметров таблицы "Генераторы" RastrWin3
from dataclasses import dataclass


@dataclass(frozen=True)
class Generator:
    """
    Параметры таблицы Генераторы ИД
    """
    table = 'Generator'
    table_name: str = '"Генераторы(ИД)"'
    sel: str = 'sel'  #
    sta: str = 'sta'  #
    sta0: str = 'sta0'  #
    Num: str = 'Num'  #
    Name: str = 'Name'  #
    Node: str = 'Node'  #
    ModelType: str = 'ModelType'  #
    Brand: str = 'Brand'  #
    NumBrand: str = 'NumBrand'  #
    ExciterId: str = 'ExciterId'  #
    ARSId: str = 'ARSId'  #
    IVActuatorId: str = 'IVActuatorId'  #
    NumPQ: str = 'NumPQ'  #
    NumSat: str = 'NumSat'  #
    NumXop: str = 'NumXop'  #
    NodeId: str = 'NodeId'  #
    CustomModel: str = 'CustomModel'  #
    Type: str = 'Type'  #
    TypeSat: str = 'TypeSat'  #
    Id: str = 'Id'  #
    disp_num: str = 'disp_num'  #
    ngou: str = 'ngou'  #
    tgA: str = 'tgA'  #
    Vgain: str = 'Vgain'  #
    Tarif: str = 'Tarif'  #
    S: str = 'S'  #
    _adjpq: str = '_adjpq'  #
    Bmin: str = 'Bmin'  #

    # U - напряжение
    modV: str = 'modV'  #
    Eq: str = 'Eq'  #
    Eqnom: str = 'Eqnom'  #
    Eq1: str = 'Eq1'  #
    Eq2: str = 'Eq2'  #
    Vdrop: str = 'Vdrop'  #
    E: str = 'E'  #
    Ed1: str = 'Ed1'  #
    Ed2: str = 'Ed2'  #

    urE: str = 'urE'  #

    urDelta: str = 'urDelta'  #
    Delta: str = 'Delta'  #

    # Р - активная мощность
    P: str = 'P'  #
    Pgconst: str = 'Pgconst'  #
    Pmax: str = 'Pmax'  #
    Pmin: str = 'Pmin'  #
    Pnom: str = 'Pnom'  #
    Pdem: str = 'Pdem'  #

    # Q - реактивная мощность
    Q: str = 'Q'  #
    Qmax: str = 'Qmax'  #
    Qmin: str = 'Qmin'  #

    Ugnom: str = 'Ugnom'  #
    cosFi: str = 'cosFi'  #
    Demp: str = 'Demp'  #
    Mj: str = 'Mj'  #

    # сопротивление
    r: str = 'r'  #
    x: str = 'x'  #
    r0: str = 'r0'  #
    r2: str = 'r2'  #

    # сопротивления оси - d
    xd: str = 'xd'  #
    xd1: str = 'xd1'  #
    xd2: str = 'xd2'  #

    # сопротивления оси - q
    xq: str = 'xq'  #
    xq1: str = 'xq1'  #
    xq2: str = 'xq2'  #

    xl: str = 'xl'  #
    x0: str = 'x0'  #
    x2: str = 'x2'  #

    # I - ток
    Inom: str = 'Inom'  #
    modI: str = 'modI'  #
    i0: str = 'i0'  #
    di0: str = 'di0'  #
    i1: str = 'i1'  #
    di1: str = 'di1'  #
    i2: str = 'i2'  #
    di2: str = 'di2'  #
    ia: str = 'ia'  #
    dia: str = 'dia'  #
    ib: str = 'ib'  #
    dib: str = 'dib'  #
    ic: str = 'ic'  #
    dic: str = 'dic'  #
    ki: str = 'ki'  #
    ke: str = 'ke'  #

    td01: str = 'td01'  # T'd0 Переходная постоянная времени по продольной оси при разомкнутой обмотке статора
    td02: str = 'td02'  # T"d0 Сверхпереходная постоянная времени по продольной оси при разомкнутой обмотке статора

    tq01: str = 'tq01'  # T'q0 Переходная постоянная времени по поперечной оси при разомкнутой обмотке статора
    tq02: str = 'tq02'  # T"q0 Сверхпереходная постоянная времени по поперечной оси при разомкнутой обмотке статора