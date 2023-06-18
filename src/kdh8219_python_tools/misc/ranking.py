from typing import Dict


def ranking(_input: tuple[float, ...]) -> tuple[tuple[int, ...], ...]:
    """
    입력된 숫자들을 내림차순 정렬하고, 같은 숫자끼리 묶어 인덱스 묶음을 반환.

    print(ranking((9,9,7,8,3,5,3,1))) # ((0, 1), (3,), (2,), (5,), (4, 6), (7,))
    """
    _dict: Dict[float, list[int]] = {}
    for index, value in enumerate(_input):
        if not _dict.get(value):
            _dict[value] = []
        _dict[value].append(index)
    return tuple(map(tuple, dict(sorted(_dict.items(), reverse=True)).values()))
