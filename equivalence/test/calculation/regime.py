# -*- coding: utf-8 -*-
from RastrWinLib.AstraRastr import RASTR
from RastrWinLib.Load import load_file

load_file(rastr_win=RASTR,
          path_file=r'C:\Users\Ohrimenko_AG\Documents\RastrWin3\test-rastr\RUSTab\test9.rst',
          shabl='динамика')

regim = Regime(rastr_win=RASTR,
               switch_command_line=True)
regim.rgm()
