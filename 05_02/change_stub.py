
def make_change(target_amount):
    pass
    onep = 1
    twop = 2
    fivep = 5
    tenp = 10
    twentyp = 20
    fiftyp = 50
    oneP = 100
    list = [oneP, fiftyp, fiftyp, twentyp, tenp, fivep, twop, onep]
    end_money = []
    difference = target_amount
    while difference != 0:
        for money in list:
            if money <= difference:
                difference -= money
                end_money.append(money)
                break
    return end_money

print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
print(make_change(568))
