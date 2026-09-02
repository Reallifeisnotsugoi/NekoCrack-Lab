# Contributing

Thank you for your interest in the project. The goal of this repository is to
produce technically accurate and reproducible analyses of educational
crackmes.

## New write-up

1. Work only with a crackme, CTF challenge, or program you are authorized to analyse.
2. Add a Markdown file to the appropriate level directory under `writeups/`.
3. Record the challenge author, platform, architecture, source, and tools used.
4. Separate the problem statement, static analysis, dynamic validation, recovered algorithm, and result.
5. Do not publish binaries, third-party source code, secrets, or personal data.
6. When an algorithm can be reproduced, add a minimal script to `tools/` and tests to `tools/tests/`.

## Technical writing

- Explain why each relevant instruction, branch, or data structure matters.
- Keep confirmed observations separate from hypotheses.
- State the numeric base when it is not obvious from context.
- Prefer short disassembly excerpts over large dumps.
- Add descriptive alternative text to every image.
- Include enough information for another analyst to reproduce the result.

## Local validation

Run the full test suite before submitting changes:

```bash
python -m unittest discover -s tools/tests -v
```

A pull request should briefly describe the target, chosen approach, and method
used to validate the conclusion.
