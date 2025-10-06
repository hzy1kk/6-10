valores = [
    10,
    3 + 2j,
    5.5,
    "amo minha namorada",
    True,
    False,
    [15, 26, 10],
    {"x": "valor"},
    (1, 2, 3),    
    {4, 5, 6}     
]

for valor in valores:
    print(f"valor: {valor} - tipo: {type(valor)}")
