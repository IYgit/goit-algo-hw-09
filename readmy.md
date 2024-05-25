### Жадібний алгоритм
Функція `find_coins_greedy` використовує жадібний підхід для видачі решти.

**Переваги**:
- Швидкий та простий.
- Ефективний для стандартних наборів монет.

**Недоліки**:
- Не завжди оптимальний для нестандартних наборів монет.

### Алгоритм динамічного програмування
Функція `find_min_coins` використовує динамічне програмування для знаходження мінімальної кількості монет.

**Переваги**:
- Завжди знаходить оптимальне рішення.
- Підходить для будь-якого набору монет.

**Недоліки**:
- Вища часова та просторова складність.
- Може бути повільним для великих сум.

## Порівняння ефективності
Жадібний алгоритм більш ефективний для стандартних наборів монет та великих сум завдяки низькій часовій складності O(n). Алгоритм динамічного програмування більш універсальний, але його продуктивність знижується при великих сумах через часову складність O(m * n) та використання додаткової пам'яті (де m - сума, яку треба видати, n - кількість номіналів монет). 

Жадібний алгоритм можна використовувати для стандартних наборів монет та невеликих сум. Алгоритм динамічного програмування краще використовувати для складних наборів монет та випадків, де необхідно забезпечити оптимальне рішення.