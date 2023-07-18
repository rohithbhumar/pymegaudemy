lst = enumerate(["ad", "adad"], start=1)
ls = (list(lst))
print(type(ls[0][0]))

stg = "Bob hit the ball. Bob hit the bat"
stg = stg.split()
# print(stg)
e_stg = enumerate(stg)
dt = dict(e_stg)
print(dt)
