<p align="center">
  <img width="100%" src="./assets/neko-crack-lab-banner.png" alt="NekoCrack Lab — pink cyber-neko reverse engineering laboratory" />
</p>

<h1 align="center">₊˚⊹♡ NekoCrack Lab ♡⊹˚₊</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1100&color=FF65AD&center=true&vCenter=true&width=760&lines=crackmes+%E2%80%A2+keygens+%E2%80%A2+tiny+virtual+machines;from+assembly+to+readable+algorithms+%F0%9F%90%BE;learn+%E2%86%92+verify+%E2%86%92+document" alt="NekoCrack Lab introduction" />
</p>

<p align="center">
  <a href="https://github.com/Reallifeisnotsugoi/NekoCrack-Lab/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Reallifeisnotsugoi/NekoCrack-Lab/ci.yml?branch=main&style=for-the-badge&label=tests&labelColor=FFF0F6&color=FF65AD" alt="Tests" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFF0F6?style=for-the-badge&logo=python&logoColor=FF4FA3" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/focus-reverse_engineering-FDE7F3?style=for-the-badge&logo=hackaday&logoColor=E84A9B" alt="Reverse engineering" />
</p>

<p align="center">୨ৎ ─────── 🐾 ─────── ୨ৎ</p>

Практическая лаборатория по разбору учебных **crackme**: от поиска строк и
анализа ветвлений до восстановления keygen-алгоритмов и устройства небольшой
виртуальной машины.

Здесь фиксируется не только найденный ответ, но и воспроизводимый путь к нему:
точка входа в анализ, важные инструкции, восстановленный алгоритм и проверка
результата. Милое оформление — серьёзная методика. ฅ^•ﻌ•^ฅ

## 🌸 write-up collection

| Сложность | Задание | Подход | Результат |
| :---: | --- | --- | :---: |
| `01` | [maxpsgers — Easy crackme](writeups/level-01/easy-crackme.md) | Строки, xrefs, проверка ввода | ✅ |
| `01` | [svidnet — ZEXOR v0.1](writeups/level-01/zexor-v0.1.md) | Строки, branch patching | ✅ |
| `02` | [prestdayzero — Bob's gambling](writeups/level-02/bobs-gambling.md) | Статический анализ ветвлений | ✅ |
| `02` | [DonCris — S.N.A.P.](writeups/level-02/santa-network-admin-portal.md) | Восстановление ELF ID | ✅ keygen |
| `02` | [DonCris — New Year Resolution Vault 2026](writeups/level-02/new-year-resolution-vault-2026.md) | Псевдокод, anti-debug, динамика | ✅ keygen |
| `02` | [Kryptos — Simple login](writeups/level-02/simple-login.md) | Динамика, восстановление хеша | ✅ keygen |
| `02` | [wolverine2k — OldSoft KeyGenMe #2](writeups/level-02/oldsoft-keygenme-2.md) | Декомпиляция serial-функции | ✅ keygen |
| `02` | [Ploxied — Calculator](writeups/level-02/ploxieds-calculator.md) | Анализ поведения | ✅ |
| `03` | [CorpCons — EasyVM](writeups/level-03/easyvm.md) | Восстановление ISA виртуальной машины | ✅ |
| `03` | [Coder_90 — KeyGenMeV3](writeups/level-03/keygenme-v3.md) | Исследование keygen | 🚧 |

## 🍡 lab structure

```text
NekoCrack-Lab/
├── writeups/
│   ├── level-01/        # базовый анализ и patching
│   ├── level-02/        # восстановление алгоритмов
│   └── level-03/        # VM и более сложные задачи
├── tools/               # чистые реализации keygen-алгоритмов
│   └── tests/           # контрольные значения
└── .github/workflows/   # автоматическая проверка инструментов
```

## 🎀 tiny tools

В [`tools`](tools) лежат независимо написанные реализации восстановленных
алгоритмов на Python. Они используют только стандартную библиотеку.

```bash
python tools/santa_elf_id.py "username"
python tools/new_year_resolution.py "2025"
python tools/simple_login.py "kisikismeowmeow"
python tools/oldsoft_keygenme2.py "username"
```

Запуск всех контрольных примеров:

```bash
python -m unittest discover -s tools/tests -v
```

## 🐈 analysis workflow

1. Зафиксировать источник, архитектуру и ожидаемое поведение программы.
2. Провести первичный статический анализ: строки, импорты, xrefs и граф потока управления.
3. Подтвердить гипотезы в отладчике, если статического анализа недостаточно.
4. Восстановить алгоритм в минимальном скрипте и добавить контрольный тест.
5. Описать ограничения решения и альтернативный путь, например patching.

Основной набор: **IDA Pro · x64dbg · ScyllaHide · Python · C++**.

## 💌 contribute

Уточнения, дополнительные объяснения и новые разборы приветствуются. Перед pull
request загляните в [CONTRIBUTING.md](CONTRIBUTING.md).

> [!IMPORTANT]
> Материалы предназначены только для crackme, CTF и программ, на анализ которых
> у вас есть явное разрешение. Репозиторий не распространяет бинарные файлы;
> оригинальные задания принадлежат их авторам.

<p align="center">୨ৎ ─────── 🐈‍⬛ ─────── ୨ৎ</p>

<p align="center">
  <b>learn softly · analyze deeply · document clearly</b><br />
  <sub>made with curiosity, hex dumps and tiny paw prints ♡</sub><br />
  <sub>ฅ^._.^ฅ</sub>
</p>
