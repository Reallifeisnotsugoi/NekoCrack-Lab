<p align="center">
  <img width="100%" src="./assets/reverse-engineering-lab-banner.png" alt="Reverse Engineering Lab — binary analysis, control-flow reconstruction, and memory inspection" />
</p>

# Reverse Engineering Lab

[![Tests](https://github.com/Reallifeisnotsugoi/Reverse-Engineering-Lab/actions/workflows/ci.yml/badge.svg)](https://github.com/Reallifeisnotsugoi/Reverse-Engineering-Lab/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?logo=windows11&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Binary%20Analysis-253858)

A structured collection of educational crackme analyses, reconstructed
validation algorithms, and small verification tools. The repository documents
the complete path from initial triage to a reproducible result rather than
publishing passwords or patches without context.

The detailed write-ups are currently written in Russian. Code, commands,
artifacts, and repository structure use English naming conventions.

## Scope

The project demonstrates practical experience in:

- static analysis of Windows PE executables;
- control-flow and cross-reference analysis in IDA Pro;
- dynamic validation with x64dbg and ScyllaHide;
- reconstruction of serial and key-generation routines;
- analysis of anti-debug behaviour and custom virtual machines;
- translation of recovered logic into tested Python implementations.

## Repository structure

```text
Reverse-Engineering-Lab/
├── writeups/
│   ├── level-01/        # strings, xrefs, and basic patching
│   ├── level-02/        # algorithm and keygen reconstruction
│   └── level-03/        # virtual machines and advanced tasks
├── tools/               # clean-room Python implementations
│   └── tests/           # known-value and edge-case tests
└── .github/
    ├── workflows/       # continuous integration
    └── ISSUE_TEMPLATE/  # structured write-up proposals
```

## Analysis index

| Level | Target | Primary technique | Status |
| :---: | --- | --- | :---: |
| 1 | [maxpsgers — Easy crackme](writeups/level-01/easy-crackme.md) | Strings, xrefs, input validation | Complete |
| 1 | [svidnet — ZEXOR v0.1](writeups/level-01/zexor-v0.1.md) | Branch analysis and patching | Complete |
| 2 | [prestdayzero — Bob's gambling](writeups/level-02/bobs-gambling.md) | Static control-flow analysis | Complete |
| 2 | [DonCris — S.N.A.P.](writeups/level-02/santa-network-admin-portal.md) | ELF ID reconstruction | Complete + tool |
| 2 | [DonCris — New Year Resolution Vault 2026](writeups/level-02/new-year-resolution-vault-2026.md) | Pseudocode, anti-debug, dynamic analysis | Complete + tool |
| 2 | [Kryptos — Simple login](writeups/level-02/simple-login.md) | Dynamic analysis and hash recovery | Complete + tool |
| 2 | [wolverine2k — OldSoft KeyGenMe #2](writeups/level-02/oldsoft-keygenme-2.md) | Serial routine decompilation | Complete + tool |
| 2 | [Ploxied — Calculator](writeups/level-02/ploxieds-calculator.md) | Behavioural analysis | Complete |
| 3 | [CorpCons — EasyVM](writeups/level-03/easyvm.md) | Custom instruction-set reconstruction | Complete |
| 3 | [Coder_90 — KeyGenMeV3](writeups/level-03/keygenme-v3.md) | Keygen research | In progress |

## Reproduced algorithms

The scripts in [`tools/`](tools) are independent implementations of recovered
logic and require only the Python standard library.

```bash
python tools/santa_elf_id.py "username"
python tools/new_year_resolution.py "2025"
python tools/simple_login.py "kisikismeowmeow"
python tools/oldsoft_keygenme2.py "username"
```

Run the validation suite locally:

```bash
python -m unittest discover -s tools/tests -v
```

The same suite runs on Python 3.10 and 3.13 through GitHub Actions.

## Methodology

Each investigation follows the same baseline process:

1. Record the source, architecture, and expected program behaviour.
2. Perform initial static triage: strings, imports, cross-references, and control flow.
3. Use a debugger to validate hypotheses that static analysis cannot confirm.
4. Reimplement the recovered algorithm in a minimal, reviewable script.
5. Add known-value tests and document assumptions, limitations, and alternatives.

This format keeps observations, hypotheses, and verified conclusions separate.

## Responsible use

This repository is limited to educational crackmes, CTF challenges, and
software for which explicit analysis permission exists. It does not distribute
challenge binaries, third-party source code, secrets, or personal data.

## Contributing

Corrections and additional technical explanations are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the required write-up structure and local
validation steps.
