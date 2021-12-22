# -*- coding: utf-8 -*-
from equivalence.actions.add_cols_in_tables import add_cols
from equivalence.actions.get import GettingParameter
from equivalence.actions.group_correction import GroupCorr
from equivalence.actions.variable import Variable
from equivalence.calculation.regime import Regime
from equivalence.tables.Generator import Generator
from equivalence.tables.area import Area
from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv


def del_swiches(rastr_win: object,
                area: int) -> None:
    """

    :param rastr_win:
    :param area:
    :return:
    """
    variable_ = Variable(rastr_win=rastr_win)
    group_corr_vetv = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.groupid)
    group_corr_node = GroupCorr(rastr_win=rastr_win, table=Vetv.table, column=Vetv.sel)
    group_corr_area = GroupCorr(rastr_win=rastr_win, table=Area.table)
    get_ = GettingParameter(rastr_win=rastr_win)
    rgm_obj = Regime(rastr_win=RASTR)
    rgm_obj.rgm()
    # добавляем столбцы в таблицы
    add_cols(rastr_win=RASTR, table=Node.table, name_new_cols="sel_new")
    add_cols(rastr_win=RASTR, table=Node.table, name_new_cols="vras_new")
    add_cols(rastr_win=RASTR, table=Node.table, name_new_cols="qmin_new")
    add_cols(rastr_win=RASTR, table=Node.table, name_new_cols="qmax_new")
    add_cols(rastr_win=RASTR, table=Vetv.table, name_new_cols="sel_new2")
    add_cols(rastr_win=RASTR, table=Area.table, name_new_cols="pop_new")
    add_cols(rastr_win=RASTR, table=Area.table, name_new_cols="poq_new")

    group_corr_area.calc_cols(key="", column="pop_new", formula=Area.pop)
    group_corr_area.calc_cols(key="", column="poq_new", formula=Area.poq)

    group_corr_vetv.calc_cols(key="", column="sel_new2", formula=Vetv.sel)
    group_corr_vetv.calc_cols(key="", column=Vetv.sel, formula=0)
    group_corr_node.calc_cols(key="", column=Node.sel, formula=0)

    group_corr_node.calc_cols(key="", column="sel_new", formula=0)
    group_corr_node.calc_cols(key="", column="sel_new", formula=Node.sel)

    group_corr_node.calc_cols(key="", column="vras_new", formula=0)
    group_corr_node.calc_cols(key="", column="vras_new", formula=Node.vras)

    # --------- удаление выключателей ---------------
    group_corr_node.calc_cols(column=Node.sel, key="na<500 | na>600", formula=1)
    group_corr_node.calc_cols(column="sel_new", key="", formula=Node.sel)

    table_vetv = rastr_win.Tables(Vetv.table)
    table_node = rastr_win.Tables(Node.table)

    # убирает sel-узла если на ВЛ с одной стороны выделен узел
    table_vetv.SetSel("iq.sel=1 & ip.sel=0 & !sta")
    row_vetv = table_vetv.FindNextSel(-1)
    while row_vetv != (-1):
        iq1 = table_vetv.Cols(Vetv.iq).Z(row_vetv)
        table_node.SetSel(f"ny={iq1}")
        row_node = table_node.FindNextSel(-1)
        if row_node != (-1):
            variable_.make_changes_row(table=Node.table,
                                       column=Node.sel,
                                       row=row_node,
                                       value=0)
        row_vetv = table_vetv.FindNextSel(row_vetv)

    # убирает sel-узла если на ВЛ с одной стороны выделен узел
    table_vetv.SetSel("iq.sel=0 & ip.sel=1 & !sta")
    row_vetv = table_vetv.FindNextSel(-1)
    while row_vetv != (-1):
        ip1 = table_vetv.Cols(Vetv.ip).Z(row_vetv)
        table_node.SetSel(f"ny={ip1}")
        row_node = table_node.FindNextSel(-1)
        if row_node != (-1):
            variable_.make_changes_row(table=Node.table,
                                       column=Node.sel,
                                       row=row_node,
                                       value=0)
        row_vetv = table_vetv.FindNextSel(row_vetv)

    table_vetv.SetSel("(iq.sel=1 & ip.sel=0)|(ip.sel=1 & iq.sel=0) & tip=2")
    row_vetv = table_vetv.FindNextSel(-1)
    while row_vetv != (-1):
        iq1 = table_vetv.Cols(table_vetv.iq).Z(row_vetv)
        table_node.SetSel(f"ny={iq1}")
        row_node = table_node.FindNextSel(-1)
        if row_node != (-1):
            variable_.make_changes_row(table=Node.table,
                                       column=Node.sel,
                                       row=row_node,
                                       value=0)
        ip1 = table_vetv.Cols(Vetv.ip).Z(row_node)
        table_node.SetSel(f"ny={ip1}")
        row_node = table_node.FindNextSel(-1)
        if row_node != (-1):
            variable_.make_changes_row(table=Node.table,
                                       column=Node.sel,
                                       row=row_node,
                                       value=0)

        table_vetv.SetSel("(iq.sel=1 &ip.sel=0) | (ip.sel=1 &iq.sel=0) & tip=2")
        row_vetv = table_vetv.FindNextSel(-1)

    viborka_ = "(iq.bsh>0 & ip.bsh=0)|(ip.bsh>0 & iq.bsh=0)|ip.sel=0|iq.sel=0)"
    group_corr_vetv.calc_cols(key='1', column=Vetv.groupid, formula=0)
    group_corr_vetv.calc_cols(key=viborka_, column=Vetv.groupid, formula=1)
    # nvet = 0
    flvykl = 0
    # удаление выключателей
    for povet in range(0, 10000):
        table_vetv.SetSel("x<0.01 & x>-0.01 & r<0.005 & r>=0 & (ktr=0 | ktr=1) & !sta & groupid!=1 & b<0.000005")
        ivet = table_vetv.FindNextSel(-1)
        if ivet == (-1):
            break
        ip = get_.get_cell_row(table=Vetv.table, column=Vetv.ip, row=ivet)
        iq = get_.get_cell_row(table=Vetv.table, column=Vetv.iq, row=ivet)
        if ip > iq:
            ny = iq
            ndel = ip
        else:
            ny = ip
            ndel = iq

        ndny = 0
        ndndel = 0
        # Проверка на наличие узла из списка неудаляемых
        # тут должен быть цикл на проверку неудаляемых узлов
        if ndndel == 0 and ndny == 1:
            buff = ny
            ny = ndel
            ndel = buff

        if ndndel == 0 or ndny == 0:  # Если хотя бы один можно удалить
            flvykl = flvykl + 1

            iny = get_.get_cell_index(table=Node.table, viborka=f"ny={ny}")
            idel = get_.get_cell_index(table=Node.table, viborka=f"ny={ndel}")

            pgdel = get_.get_cell_row(table=Node.table, column=Node.pg, row=idel)
            qgdel = get_.get_cell_row(table=Node.table, column=Node.qg, row=idel)
            pndel = get_.get_cell_row(table=Node.table, column=Node.pn, row=idel)
            qndel = get_.get_cell_row(table=Node.table, column=Node.qn, row=idel)
            bshdel = get_.get_cell_row(table=Node.table, column=Node.bsh, row=idel)
            gshdel = get_.get_cell_row(table=Node.table, column=Node.gsh, row=idel)

            pgny = get_.get_cell_row(table=Node.table, column=Node.pg, row=iny)
            qgny = get_.get_cell_row(table=Node.table, column=Node.qg, row=iny)
            pnny = get_.get_cell_row(table=Node.table, column=Node.pn, row=iny)
            qnny = get_.get_cell_row(table=Node.table, column=Node.qn, row=iny)
            bshny = get_.get_cell_row(table=Node.table, column=Node.bsh, row=iny)
            gshny = get_.get_cell_row(table=Node.table, column=Node.gsh, row=iny)

            variable_.make_changes_row(table=Node.table, column=Node.pg, row=iny, value=pgdel + pgny)
            variable_.make_changes_row(table=Node.table, column=Node.qg, row=iny, value=qgdel + qgny)
            variable_.make_changes_row(table=Node.table, column=Node.pn, row=iny, value=pndel + pnny)
            variable_.make_changes_row(table=Node.table, column=Node.qn, row=iny, value=qndel + qnny)
            variable_.make_changes_row(table=Node.table, column=Node.bsh, row=iny, value=bshdel + bshny)
            variable_.make_changes_row(table=Node.table, column=Node.gsh, row=iny, value=gshdel + gshny)

            v1 = get_.get_cell_row(table=Node.table, column=Node.vzd, row=iny)
            v2 = get_.get_cell_row(table=Node.table, column=Node.vzd, row=idel)
            qmax1 = get_.get_cell_row(table=Node.table, column=Node.qmax, row=iny)
            qmax2 = get_.get_cell_row(table=Node.table, column=Node.qmax, row=idel)

            table_generator = RASTR.Tables(Generator.table)
            table_generator.SetSel(f"Node={ndel}")
            igen = table_generator.FindNextSel(-1)
            # Меняем узлы подключения генераторов
            if igen != (-1):
                while igen != (-1):
                    variable_.make_changes_row(table=Generator.table, column=Generator.Node, row=igen, value=ny)
                    igen = table_generator.FindNextSel(igen)

            if v1 != v2 and v1 > 0.3 and v2 > 0.3 and (qmax1 + qmax2) != 0:
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=iny,
                                           value=(v1 * qmax1 + v2 * qmax2) / (qmax1 + qmax2))
                # Делаем средневзвешенное по qmax напряжение

            if v1 == 0 and v2 != 0:
                variable_.make_changes_row(table=Node.table, column=Node.vzd, row=iny, value=v2)

            if v1 != 0 and v2 != 0:
                variable_.make_changes_row(table=Node.table, column=Node.qmin, row=iny, value=(
                        get_.get_cell_row(
                            table=Node.table,
                            column=Node.qmin,
                            row=iny)
                        +
                        get_.get_cell_row(
                            table=Node.table,
                            column=Node.qmin,
                            row=idel)
                )
                                           )
                variable_.make_changes_row(table=Node.table, column=Node.qmax, row=iny, value=qmax1 + qmax2)

            if v1 == 0 and v2 != 0:
                variable_.make_changes_row(table=Node.table, column=Node.qmax, row=iny,
                                           value=get_.get_cell_row(table=Node.table, column=Node.qmax, row=idel))
                variable_.make_changes_row(table=Node.table, column=Node.qmin, row=iny,
                                           value=get_.get_cell_row(table=Node.table, column=Node.qmin, row=idel))

            table_vetv.SetSel(f"(ip={ip} & iq={iq})|(iq={ip} & ip={iq})")
            table_vetv.delrows()

            table_vetv.SetSel(f"iq={ndel}")  # Меняем узлы ветвей с удаляемым узлом)))
            table_vetv.Cols("iq").Calc(ny)

            table_ti = rastr_win.Tables("ti")
            table_ti.SetSel(f"prv_num<15 & id1={ndel}")
            table_ti.Cols("id1").Calc(ny)

            table_ti.SetSel(f"ip={ndel}")
            table_vetv.Cols("ip").Calc(ny)

            table_ti.SetSel(f"prv_num<15 & id2={ndel}")
            table_vetv.Cols("id2").Calc(ny)

            table_node.DelRows()  # Удаляем узел
        else:
            table_vetv.SetSel(f"(ip={ip} & iq={iq})|(iq={ip} & ip={iq})")
            table_vetv.Cols("groupid").Calc(1)
    rgm_obj.rgm()
