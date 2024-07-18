# Задано список: data
#
# потрібно брати по черзі із кожного списку id і класти в список res,
# якщо таке значення вже є в результуючому списку тоді брати наступне з того ж списку
#
# в результат має записатись тільки 5 id
#
# з даним списком має вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


def different_values_gen(arr: list, limit: int = 5):
    res = []
    for k in range(limit):
        for i in (i for i in arr):
            for j in (j for j in i):
                if j['id'] not in res:
                    res.append(j['id'])
                    yield j['id']
                    break
                if len(res) == limit:
                    break


print(list(different_values_gen(data, 5)))


def diff_values(arr: list, lim: int = 5) -> list:
    res = []
    gens = [(i['id'] for i in lst if i['id'] not in res) for lst in arr]

    while True:
        for g in gens:
            if len(res) == lim:
                return res
            res.append(next(g))


print(diff_values(data))
