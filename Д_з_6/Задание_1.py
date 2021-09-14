with open('nginx_logs.txt') as f:
    data = (i.split(' ') for i in f.readlines())

res = ((i[0], i[5].replace('"', ''), i[6]) for i in data)

print(next(res))
print(next(res))
print(next(res))
print(next(res))