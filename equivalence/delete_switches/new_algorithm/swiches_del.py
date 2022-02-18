# -*- coding: utf-8 -*-

from equivalence.tables.node import Node
from equivalence.tables.vetv import Vetv


def summa_param2(tnode: object, jmax: int, jmin: int, dp: float, dq: float) -> None:
    """

    :param tnode:
    :param jmax:
    :param jmin:
    :param dp:
    :param dq:
    :return:
    """
    cpn = tnode.Cols(Node.pn)
    cpn_min = tnode.Cols(Node.pn_min)
    cpn_max = tnode.Cols(Node.pn_max)

    cqn = tnode.Cols(Node.qn)
    cqn_min = tnode.Cols(Node.qn_min)
    cqn_max = tnode.Cols(Node.qn_max)

    cpg = tnode.Cols("pg")

    cqg = tnode.Cols("qg")
    cqmin = tnode.Cols("qmin")
    cqmax = tnode.Cols("qmax")

    cvzd = tnode.Cols("vzd")

    cbsh = tnode.Cols("bsh")
    cgsh = tnode.Cols("gsh")

    # добавляем потери к нагрузке суммарного узла
    cpn.SetZ(jmax, (cpn.Z(jmax) + cpn.Z(jmin) + dp))
    cqn.SetZ(jmax, (cqn.Z(jmax) + cqn.Z(jmin) + dq))

    cpg.SetZ(jmax, (cpg.Z(jmax) + cpg.Z(jmin)))
    cqg.SetZ(jmax, (cqg.Z(jmax) + cqg.Z(jmin)))

    cpn_max.SetZ(jmax, (cpn_max.Z(jmax) + cpn_max.Z(jmin)))
    cpn_min.SetZ(jmax, (cpn_min.Z(jmax) + cpn_min.Z(jmin)))

    if cqn_min.Z(jmax) < cqn_min.Z(jmin):
        tnode.Cols(Node.qn_min).SetZ(jmax, cqn_min.Z(jmax))
    else:
        tnode.Cols(Node.qn_min).SetZ(jmax, cqn_min.Z(jmin))

    if cpn_min.Z(jmax) < cqn_min.Z(jmin):
        tnode.Cols(Node.pn_min).SetZ(jmax, cpn_min.Z(jmax))
    else:
        tnode.Cols(Node.pn_min).SetZ(jmax, cqn_min.Z(jmin))

    cbsh.SetZ(jmax, (cbsh.Z(jmax) + cbsh.Z(jmin)))
    cgsh.SetZ(jmax, (cgsh.Z(jmax) + cgsh.Z(jmin)))

    vzd_jmax = tnode.Cols(Node.vzd).Z(jmax)
    vzd_jmin = tnode.Cols(Node.vzd).Z(jmin)

    qmax_jmax = tnode.Cols(Node.qmax).Z(jmax)
    qmax_jmin = tnode.Cols(Node.qmax).Z(jmin)

    if vzd_jmax != vzd_jmin and vzd_jmax > 0.3 and vzd_jmin > 0.3 and (qmax_jmax + qmax_jmin) != 0:
        tnode.Cols(Node.vzd).SetZ(jmax, ((vzd_jmax * qmax_jmax + vzd_jmin * qmax_jmin) / (qmax_jmax + qmax_jmin)))

    if vzd_jmax == 0 and vzd_jmin != 0:
        tnode.Cols(Node.vzd).SetZ(jmax, vzd_jmin)

    if vzd_jmax != 0 and vzd_jmin != 0:
        tnode.Cols(Node.qmin).SetZ(jmax, tnode.Cols(Node.qmin).Z(jmin))
        tnode.Cols(Node.qmax).SetZ(jmax, tnode.Cols(Node.qmax).Z(jmin))


def summa_param(tnode: object, jmax: int, jmin: int, dp: float, dq: float) -> None:
    """

    :param tnode:
    :param jmax:
    :param jmin:
    :param dp:
    :param dq:
    :return:
    """
    cpn = tnode.Cols(Node.pn)
    cqn = tnode.Cols(Node.qn)
    cpg = tnode.Cols("pg")
    cqg = tnode.Cols("qg")
    cqmin = tnode.Cols("qmin")
    cqmax = tnode.Cols("qmax")
    cvzd = tnode.Cols("vzd")
    cbsh = tnode.Cols("bsh")
    cgsh = tnode.Cols("gsh")

    # добавляем потери к нагрузке суммарного узла
    cpn.SetZ(jmax, (cpn.Z(jmax) + cpn.Z(jmin) + dp))
    cqn.SetZ(jmax, (cqn.Z(jmax) + cqn.Z(jmin) + dq))
    cpg.SetZ(jmax, (cpg.Z(jmax) + cpg.Z(jmin)))
    cqg.SetZ(jmax, (cqg.Z(jmax) + cqg.Z(jmin)))
    cqmin.SetZ(jmax, (cqmin.Z(jmax) + cqmin.Z(jmin)))
    cqmax.SetZ(jmax, (cqmax.Z(jmax) + cqmax.Z(jmin)))

    cbsh.SetZ(jmax, (cbsh.Z(jmax) + cbsh.Z(jmin)))
    cgsh.SetZ(jmax, (cgsh.Z(jmax) + cgsh.Z(jmin)))

    if cvzd.Z(jmax) == 0. and cvzd.Z(jmin) != 0.:
        cvzd.SetZ(jmax, cvzd.Z(jmin))


def del_swiches_new(rastr_win: object,
                    VIBORKA: str = "tip=2 & sta=0 & "
                                   "(ip.na<500 | ip.na>600) & ip.na!=8082 & ip.na!=8037 & ip.na!=5329 & ip.na!=5230 & "
                                   "(iq.na<500 | iq.na>600) & iq.na!=8082 & iq.na!=8037 & iq.na!=5329 & iq.na!=5230"
                    ) -> None:
    """

    :param rastr_win:
    :param VIBORKA:
    :return:
    """
    tnode = rastr_win.Tables(Node.table)
    tvetv = rastr_win.Tables(Vetv.table)
    tvetv_while = rastr_win.Tables(Vetv.table)
    cny = tnode.Cols(Node.ny)
    cvzd = tnode.Cols(Node.vzd)
    cip = tvetv.Cols(Vetv.ip)
    ciq = tvetv.Cols(Vetv.iq)

    tvetv.SetSel("")
    tvetv.Cols(Vetv.sel).Calc("0")
    # VIBORKA = "tip=2 & sta=0 & (ip.na<500 | ip.na>600) & ip.na!=8082 & ip.na!=8037 & ip.na!=5329 & ip.na!=5230 & (iq.na<500 | iq.na>600) & iq.na!=8082 & iq.na!=8037 & iq.na!=5329 & iq.na!=5230"
    tvetv.SetSel(VIBORKA)
    tvetv.Cols(Vetv.sel).Calc("1")

    tvetv_while.SetSel("")

    tvetv_while.SetSel("sel=1")
    j1 = tvetv_while.FindNextSel(-1)
    while j1 != (-1):
        if j1 == (-1):
            # print("break")
            break
        n1 = cip.Z(j1)
        n2 = ciq.Z(j1)

        # print(f"Объединяем узлы {n1}, {n2}")

        tnode.SetSel(f"ny={n1}")
        jip = tnode.FindNextSel(-1)
        tnode.SetSel(f"ny={n2}")
        jiq = tnode.FindNextSel(-1)

        if (cvzd.Z(jiq)) != 0.:
            t = n1
            n1 = n2
            n2 = t
            t = jip
            jip = jiq
            jiq = t

        summa_param(tnode, jip, jiq, 0, 0)

        vibor = f"(ip={n1} & iq={n2})|(iq={n1} & ip={n2})"
        tvetv.SetSel(vibor)

        tvetv.DelRowS()
        rastr_win.RenumWP = True
        cny.SetZ(jiq, n1)
        rastr_win.RenumWP = False
        tnode.DelRow(jiq)

        tvetv.SetSel("sel=1")
        j1 = tvetv.FindNextSel(-1)

    tnode.SetSel("")
    tnode.Cols(Node.sel).Calc(0)

    tvetv.SetSel("")
    tvetv.Cols(Vetv.sel).Calc(0)
