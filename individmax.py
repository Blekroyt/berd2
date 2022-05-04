alpha = float(input())
hour = 24
minute = hour/60
second = minute/60
h = alpha//hour
m = (alpha / 24 * 60) % 60
s = (alpha / 24 * 3600) % 60 
print(h, m, s)
