nbr=int(input("please enter the nbr of photocopies you want"))
if nbr>0 and nph<10 :
  pt=0.3*10
elif nph>30 :
  pt=0.3*10+(nph-10)*0.25
else
  pt=0.3*10+20*0.25+(nph-30)*0.2
print("the price of photocopies is:",pt)
