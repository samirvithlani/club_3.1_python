data = ["raj","parth","amit"] # anyhow 4 less

try:
    if len(data)<4:
        raise ValueError("list is not valid list")
except ValueError as e:
    print(e)    