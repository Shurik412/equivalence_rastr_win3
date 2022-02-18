def off_the_line_from_two_side(rastr_win: object):
    # '************************************************************
    # ' Назначение: Отключение ЛЭП с двух сторон, если она включена с одной стороны.
    # ' Входные параметры: Nothing
    # ' Возврат:    Nothing
    # '************************************************************
    ii = 0
    tvetv = rastr_win.Tables(Vetv.table)
    vetvMaxRow = tvetv.Count - 1
    for i in range(0, vetvMaxRow):
        sta = tvetv.Cols("sta").Z(i)
        if sta == 2 or sta == 3:
            tvetv.Cols("sta").SetZ(i, 1)
            ii = ii + 1
    print(f" - Количество ЛЭП с односторонним вкл., переведенных с состояние полного откючения: {ii}")


def remove_line(rastr_win: object):
    node = rastr_win.Tables("node")
    vetv = rastr_win.Tables("vetv")

    vetv.SetSel("")
    vetv.Cols("sel").Calc(0)

    node.SetSel("")
    node.Cols("sel").Calc(0)

    vetv.SetSel("")
    k = vetv.FindNextSel(-1)
    while k != (-1):
        ip = vetv.Cols("ip").Z(k)
        iq = vetv.Cols("iq").Z(k)

        node.SetSel(f"ny={ip}")
        k_ip = node.FindNextSel(-1)
        if k_ip == (-1):
            vetv.Cols("sel").SetZ(k, 1)

        node.SetSel(f"ny={iq}")
        k_iq = node.FindNextSel(-1)
        if k_iq == (-1):
            vetv.Cols("sel").SetZ(k, 1)
            print(f"ip={ip}, iq={iq}")
        k = vetv.FindNextSel(k)


def del_vetv(rastr_win: object):
    vetv = rastr_win.Tables("vetv")
    node = rastr_win.Tables("node")

    NodeColMax = node.Count
    VetvColMax = vetv.Count
    print(f"До Количество узлов = {NodeColMax}")
    print(f"До Количество ветвей = {VetvColMax}")

    vetv.SetSel("ip.ny=0|iq.ny=0")
    t.Printp(f"Удалено ветвей: {vetv.Count}")
    vetv.DelRowS()

    NodeColMax = node.Count
    VetvColMax = vetv.Count
    print(f"До Количество узлов = {NodeColMax}")
    print(f"До Количество ветвей = {VetvColMax}")
