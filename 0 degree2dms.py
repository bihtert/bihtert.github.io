x = 70

d = x//1
m = ((x%1)*60)//1
s = (((x%1)*60)%1)*60

print("DMS:", int(d),int(m),format(s,".6f"))

