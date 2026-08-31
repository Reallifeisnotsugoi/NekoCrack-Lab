# DonCris — New Year Resolution Vault 2026

| Поле | Значение |
| --- | --- |
| Уровень | 2 |
| Платформа | Windows x86-64 |
| Подход | IDA Pro, x64dbg, восстановление checksum |
| Результат | Unlock code вычисляется для произвольной строки |

## Поиск проверки

Программа последовательно запрашивает текст обещания и код разблокировки. Cross-reference от строки успеха

```text
[SUCCESS] Resolution Accepted! Validation complete.
```

приводит к функции, где видны две важные части:

- проверка `IsDebuggerPresent`, результат которой смешивается с константой `0xDEADBEEF`;
- вызов `calculate_checksum(std::string const&)`, формирующий ожидаемый код.

Anti-debug влияет на путь выполнения при динамическом анализе. Для наблюдения за нормальной логикой использовался x64dbg со ScyllaHide.

## Восстановленный checksum

Декомпилятор дает следующий эквивалент:

```cpp
uint64_t checksum = 2025;
for (size_t i = 0; i < resolution.length(); ++i) {
    checksum = rol64(checksum + (i + 1) * uint8_t(resolution[i]), 3)
             ^ 0x20262026;
}
```

Критические детали реализации:

- символ обрабатывается как беззнаковый байт;
- индекс начинается с 1;
- `ROL` выполняется в 64-битном пространстве;
- результат каждой итерации обрезается до 64 бит.

## Проверка

Для строки `2025` алгоритм возвращает:

```text
315216478454
```

Это же значение можно увидеть в `RAX` после возврата из `calculate_checksum`, что связывает статический анализ с динамическим наблюдением.

Готовая реализация и тест:

```bash
python tools/new_year_resolution.py "2025"
python -m unittest tools.tests.test_keygens.KeygenTests.test_new_year_known_value -v
```

Исходный код находится в [`tools/new_year_resolution.py`](../../tools/new_year_resolution.py).
