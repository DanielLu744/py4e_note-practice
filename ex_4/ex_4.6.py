def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40:
        rep = hours * rate
        ovp = (hours - 40.0) * (rate * 0.5) 
        pay = rep + ovp
    else:
        pay = hours * rate
        # print("Returning", pay)
    return pay 
hr = input("Enter Hours:")
rt = input("Enter Rate:")
hrs = float(hr)
rte = float(rt)
tp = computepay (hrs, rte)
 
print("Pay",tp) 