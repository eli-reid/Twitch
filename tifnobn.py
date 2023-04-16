dictd= {
    "test1": "ttttttt",
    "test2": None,
    "test3": "ttttttt",
    "test4": None
}
for k,v in dictd.items():
    if v is None:
        continue
    print(f"{k}:{v}")