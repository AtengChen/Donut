__import__('sys').exit((_ := (lambda _builtins, math, time, os, itertools, blessed, jinxed, msvcrt: [

                                 (aa := blessed.Terminal()), [
                        (aj := (0, 0)[0]), (ak := (0, 0)[1])], (ab := (
                 255, 192, 203)), (ac := 1.8), (ad := os.get_terminal_size()), [
             (al := (ad.columns, ad.lines - 1)[0]), (am := (ad.columns, ad.lines - 1)
           [1])], (ae := (al / am)),             (af := (min(al, am) / 4)), (ag := 3.3
         ), jinxed.win32.setcbreak(               msvcrt.get_osfhandle(0)), _builtins.\
        print(aa.enter_fullscreen                   () + aa.clear()), (ah := True), [[(
        an := aa.inkey(timeout=1                     / 60)), (ah := False) if an == 'q'\
        else (ag := (ag + 0.2))                      if an == '\x1b[A' else (ag := (ag - \
       0.2))if an=='\x1b[B'else                      None, (ao := ([0] * (al * am))), (
       ap := ([' '] * (al * am)                      )), [[[(au := math.sin(at / 100)), (
       av := math.cos(aq / 100))                    , (aw := math.sin(aj)), (ax := math.sin(
       aq / 100)), (ay := math.                     cos(aj)), (az := (av + ag)), (ba := (
        1 / (au * az * aw + ax *                   ay + 5))), (bb := math.cos(at / 100)),
          (bc := math.cos(ak)), (                 bd := math.sin(ak)), (be := (au * az * \
            ay - ax * aw)), (bf :=             _builtins.int(al / 2 + af * ba * (bb * az * \
              bc - be * bd) * ae)),(bg := _builtins.int(am / 2 + af * ba * (bb * az * bd + 
               be * bc))), (bh := (bf + al * bg)), (bi := _builtins.int(47 * ((ax * 
                   aw - au * av * ay) * bc - au * av * aw - ax * ay - bb * av * 
                    bd) ** 2)), [ao.__setitem__(bh, ba), (bj := _builtins.int(
                         255 * ba * ac)), (bj := _builtins.min(bj, 255)), (
                               bk := _builtins.int(ab[0] * (bj / 255
                                       ) ** 0.75)), (

       bl := _builtins.int(ab[1] * (bj / 255) ** 0.75)), (bm := _builtins.int(ab[2] * (bj /  \
       255) ** 0.75)), (bn := ' .`:,;\'^"~-_/<>\\*?!vx)c(sCYJ3[]y{}awUX%1S+=ju9olV27r|egnzm6G'
       '8ptHL4q5iO0AF@MTbf&dNZRWhDKQk$PI#EB'), (bo := bn[bi if bi > 0 else 0]), ap.__setitem__
       (bh, aa.color_rgb(bk, bl, bm)(bo))] if 0 <= bg < am and 0 <= bf < al and (ba > ao[bh]) 
       else None] for at in _builtins.range(0, 628, 2)] for aq in _builtins.range(0, 628, 7)],
       _builtins.print(aa.move(0, 0), end=''),[_builtins.print(ap[ar], end='\n'if ar % al == \
       al - 1 else '') for ar in _builtins.range(al * am)],(aj := (aj + 0.05)), (ak := (ak + \
       0.07)),time.sleep(1 / 60)]for ai in itertools.takewhile(lambda condition:ah,itertools.\
       count())],_builtins.print(aa.exit_fullscreen()),0]))(__import__('builtins'),__import__(
       'math'), __import__('time'), __import__('os'), __import__('itertools'), __import__('bl'
       'essed'), __import__('jinxed'), __import__('msvcrt'))[-1])
