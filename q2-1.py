for i in range(11):
	for j in range(11):
		if j==0 or j==10:
			print("A",end="")
		elif (j==1 or j==9) and i!=5:
			print("B",end="")
		elif (j==2 or j==8) and (i!=4 and i!=5 and i!=6):
			print("C",end="")
		elif (j==3 or j==7) and (i!=3 and i!=4 and i!=5 and i!=6 and i!=7):
			print("D",end="")
		elif (j==4 or j==6) and (i==0 or i==1 or i==9 or i==10) :
			print("E",end="")
		elif (j==5) and (i==0 or i==10) :
			print("F",end="")
		else:
			print(end=" ")
	print()
	

	
