bolts,pr_lose_bolts,cost_bolt = map(int,input().split())
screws,pr_lose_screws,cost_screw = map(int,input().split())


lose_bolts = bolts*(pr_lose_bolts/100)
lose_screw = screws*(pr_lose_screws/100)

b = bolts-lose_bolts
s = screws-lose_screw

pairs = min(b, s)

unusable_bolts = b - pairs
unusable_screws = s - pairs

damage = (lose_bolts + unusable_bolts) * cost_bolt + (lose_screw + unusable_screws) * cost_screw
print(int(damage))