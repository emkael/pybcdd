(Polish README follows below.)

pyBCDD - Python BCalc Double Dummy
==================================

Python port of [BCDD utility](https://github.com/emkael/bcdd).

This project uses [BCalc](http://bcalc.w8.pl/) as a double-dummy engine.

Overview
========

All the BCDD features are described in the [upstream project README](https://github.com/emkael/bcdd/blob/master/doc/README.en.md). This project serves as a direct, one-to-one port, with the exception of differences described below.

What's different from the original BCDD?

 * it's cross-platform: tested on fairly modern Linux distributions, works under Python 2.x *and* Python 3.x and distributes both Windows and Linux [BCalc shared libraries](http://bcalc.w8.pl/download/API_C/)
 * it **does not** provide compiled executable binaries - however, you're free to experiment with such setup on your own (though for Windows non-scripting usage it's recommended to use the original .NET version)
 * as a consequence, it does not follow the upstream release "cycle" - it's expected that this repository represents the state of HEAD of the `master` branch from upstream (slight delay might be possible, though)
 * it's stripped of all interactive elements: while it still prints out the same messages as the upstream version (double dummy table and par contracts), it **does not** prompt for input files interactively, neither does it prompt for a keypress on error

Prerequsites
============

 * Python with a standard library set (as of August 2019 tested on 2.7.14, 3.4.4 and 3.7.4)
 * [BCalc shared libraries](http://bcalc.w8.pl/download/API_C/) in library path (this repo provides 64-bit Windows and Linux libraries, for 32-bit Windows you need to download the proper DLL)

Usage
=====

```
python pybcdd.py PBN_FILE [PBN_FILE [PBN_FILE ...]]
```

Credits and author
==================

`libbcalcdds.dll` and `libbcalcdds.so` are parts of the [BCalc project](http://bcalc.w8.pl) by Piotr Beling

This software was made by [Michał Klichowicz](https://emkael.info).

If you use it, you probably know how to reach me.

If you don't (know how to reach me), you can find it on my website.

---

pyBCDD - Python BCalc Double Dummy
==================================

Port [narzędzia BCDD](https://github.com/emkael/bcdd) dla Pythona.

Projekt używa [BCalc](http://bcalc.w8.pl/) jako silnika obliczeń w widne.

Opis ogólny
===========

Funkcjonalności BCDD opisane są w [README projektu źródłowego](https://github.com/emkael/bcdd/blob/master/doc/README.pl.md). Ten projekt to ścisłe, bezpośrednie przeniesienie BCDD na Pythona, z wyjątkiem różnic opisanych poniżej.

Czym różni się od źródłowego BCDD?

 * działa pod wieloma platformami: testowany na stosunkowo aktualnych dystrybucjach Linuksa, działa spod Pythona 2.x *oraz* Python 3.x i dystrybuuje zarówno Windowsowe, jak i Linuksowe [biblioteki BCalc](http://bcalc.w8.pl/download/API_C/)
 * **nie** dostarcza skompilowanych plików wykonywalnych - nie krępuj się, eksperymentuj z mini samemu (choć na potrzeby nie-skryptowego użycia pod Windowsem zaleca się używania oryginalnej wersji .NET)
 * w konsekwencji, nie podąża za źródłowym "cyklem" wydań - w zamyśle to repozytrium ma odzwierciedlać HEAD gałęzi `master` żródłowego projektu (być może z drobnym opóźnieniem)
 * wyrzucono z niego wszystkie elementy interaktywne: co prawda wciąż wyświeta komunikaty jak wersja źródłowa (tabelę analizy w widne i minimaksa), lecz **nie** pyta interaktywnie o pliki wejściowe ani nie prosi o potwierdzenie zakończenia wykonania w przypadku błędu

Wymagania
=========

 * Python ze standardowym zestawem bibliotek (w sierpniu 2019 testowane w wersjach 2.7.14, 3.4.4 i 3.7.4)
 * [biblioteka BCalc](http://bcalc.w8.pl/download/API_C/) w ścieżce bibliotek (repozytorium dostarcza 64-bitową bibliotekę dla Windows oraz Linuksa, 32-bitowe systemy Windows wymagają ściągnięcia właściwej DLL)

Użycie
======

```
python pybcdd.py PLIK_PBN [PLIK_PBN [PLIK_PBN ...]]
```

Autorzy
=======

`libbcalcdds.dll` i `libbcalcdds.so` to części [projektu BCalc](http://bcalc.w8.pl) autorstwa Piotra Belinga

Autorem tego oprogramowania jest [Michał Klichowicz](https://emkael.info).

Jeśli go używasz (oprogramowania, nie autora), powinieneś wiedzieć, gdzie mnie szukać.

Jeśli nie (wiesz, gdzie mnie szukać), moja strona domowa jest niezłym początkiem.

---

License / Licencja
==================

```
Copyright (C) 2016-2019, Michał Klichowicz
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
   2. Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
         and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
```

---

`Does it get easier?`
