hr = input("Enter Hours:")
rt = input("Enter Rate:")
hrs = float(hr)
rte = float(rt)
if hrs > 40:
    rep = hrs * rte
    ovp = (hrs - 40.0) * (rte * 0.5) 
    tp = rep + ovp
else:
    tp = hrs * rte 
print("Pay:",tp) 