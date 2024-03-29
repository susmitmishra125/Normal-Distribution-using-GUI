import numpy as np
from tkinter import Tk, Frame, Entry, GROOVE, RIGHT, Label, Button, RAISED, END
import tkinter
from tkinter import messagebox


###########################################################
#probability distribution function 
def PDF(x):
		return np.exp(-x*x/2)/np.sqrt(8*np.atan(1.0))

#function for Integration using Simpsons 1/3rd rule. Steps=0.01
def simpson(z,h=0.01):
		# if z is below -10 because of computational constraints it is efficient to ouput 0
		if(z<-10):
				return 0
		# it is unecessary to integrate for above 10
		if(z>10):
				return 1.0
		if(z<0):
				flag=-1
				z=z*-1
		else:
			flag=1
		sum=0
		if(z>0):
				m=z/h
				if(m%2==1):
						m=m-1
				x=0
				#ans=(h/3)*(a0+2(a2+a4...)+4(a1+a3...)+az)
				for i in range(int(m)):
						if(i==0):
								sum+=PDF(0)
								continue
						if(i%2==0):
								sum+=2*PDF(i*h)
						if(i%2==1):
								sum+=4*PDF(i*h)
				sum+=PDF(z)
		if(flag==1):
				return  0.5 + h*(sum/3)
		else:
				return 0.5-h*(sum/3)
##################################################################


Solver = Tk()
Solver.title("CDF for Normal distribution")
Solver.geometry('620x168')
Solver.configure(background='#e7fca7')

class Application(Frame):
	def __init__(self, master, *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		self.createWidgets()

	def replaceText(self, text):
		self.input.delete(0, END)
		self.input.insert(0, text)
	def replaceTextoutput1(self, text):
		self.output1.delete(0, END)
		self.output1.insert(0, text)

	def replaceTextinput1(self, text):
		self.input1.delete(0, END)
		self.input1.insert(0, text)

	def replaceTextoutput2(self, text):
		self.output2.delete(0, END)
		self.output2.insert(0, text)

	def replaceTextinput2(self, text):
		self.input2.delete(0, END)
		self.input2.insert(0, text)

	def replaceTextoutput3(self, text):
		self.output3.delete(0, END)
		self.output3.insert(0, text)

	def replaceTextinput3(self, text):
		self.input3.delete(0, END)
		self.input3.insert(0, text)

	def replaceTextoutput4(self, text):
		self.output4.delete(0, END)
		self.output4.insert(0, text)

	def replaceTextinput4(self, text):
		self.input4.delete(0, END)
		self.input4.insert(0, text)



	def appendToinput(self, text):
		self.entryText = self.input.get()
		self.textLength = len(self.entryText)

		if self.entryText == "0":
			self.replaceText(text)
		else:
			self.input.insert(self.textLength, text)

	def calculateExpression(self):#python's calculate function 
		self.expression = self.input.get()

		try:
			self.result = eval(self.expression)
			self.result=round(self.result,2)
			z_transformed=(float(self.result)-float(self.mean.get()))/float(self.variance.get())

			self.replaceTextinput4(self.input3.get())
			self.replaceTextinput3(self.input2.get())
			self.replaceTextinput2(self.input1.get())
			self.replaceTextinput1(self.result)
			
			self.replaceTextoutput4(self.output3.get())
			self.replaceTextoutput3(self.output2.get())
			self.replaceTextoutput2(self.output1.get())

			
			self.result = round(simpson(z_transformed),4)
			self.replaceTextoutput1(self.result)
			self.replaceText('')
			# if(abs(float(self.input1.get())-float(self.mean.get()))>3):
				# messagebox.showinfo(title="Overflow",message='Enter Z values between {} to {} rounded upto 2 decimal places'.format(float(self.mean.get())-3,float(self.mean.get())+3))
		except:
			messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=Solver)

	def clearText(self):#clears input on pressing Clear on Solver
		self.replaceText("")
		self.replaceTextinput1("")
		self.replaceTextoutput1("")
		self.replaceTextinput2("")
		self.replaceTextoutput2("")
		self.replaceTextinput3("")
		self.replaceTextoutput3("")
		self.replaceTextinput4("")
		self.replaceTextoutput4("")
		

	def createWidgets(self):
		self.input = Entry(self, font=("Calibri", 16),width=13, borderwidth=1.5, relief=GROOVE, justify=RIGHT)
		self.input.insert(0, "")
		self.input.grid(row=1, column=1, columnspan=2,sticky="NWNESWSE")
		
		Label(self,text='z:',width=6,font=('Adobe Heiti Std',14),bg='#f7dce3').grid(row=1,column=0)
		# Label(self,text='μ-3 ≤ z ≤ μ+3',width=12,font=('Adobe Heiti Std',14),bg='#77e0f2').grid(row=1,column=5,columnspan=2)
		Label(self,text='z',width=12,font=('Adobe Heiti Std',14),bg='#77e0f2').grid(row=1,column=5,columnspan=2)
		Label(self,text='Φ(z)',width=12,font=('Adobe Heiti Std',14),bg='#77e0f2').grid(row=1,column=7,columnspan=2)
		
		Label(self,text='Mean μ:',width=6,font=('Calibri',14)).grid(row=2,column=3)
		Label(self,text='SD σ:',width=6,font=('Calibri',14)).grid(row=3,column=3)
		self.input1 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.input1.insert(0,'')
		self.input1.grid(row=2,column=5,columnspan=2,sticky="NWNESWSE")

		#Label(self,text='Output1').grid(row=1)

		self.output1 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.output1.insert(0,'')
		self.output1.grid(row=2,column=7,columnspan=2,sticky="NWNESWSE")

		self.input2 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.input2.insert(0,'')
		self.input2.grid(row=3,column=5,columnspan=2,sticky="NWNESWSE")

		#Label(self,text='Output1').grid(row=1)

		self.output2 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.output2.insert(0,'')
		self.output2.grid(row=3,column=7,columnspan=2,sticky="NWNESWSE")


		self.input3 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.input3.insert(0,'')
		self.input3.grid(row=4,column=5,columnspan=2,sticky="NWNESWSE")

		#Label(self,text='Output1').grid(row=1)

		self.output3 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.output3.insert(0,'')
		self.output3.grid(row=4,column=7,columnspan=2,sticky="NWNESWSE")


		self.input4 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.input4.insert(0,'')
		self.input4.grid(row=5,column=5,columnspan=2,sticky="NWNESWSE")

		#Label(self,text='Output1').grid(row=1)

		self.output4 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.output4.insert(0,'')
		self.output4.grid(row=5,column=7,columnspan=2,sticky="NWNESWSE")


		self.output4 =Entry(self, font=("Calibri",16),width=10,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.output4.insert(0,'')
		self.output4.grid(row=5,column=7,columnspan=2,sticky="NWNESWSE")

		self.mean =Entry(self, font=("Calibri",16),width=5,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.mean.insert(0,'0')
		self.mean.grid(row=2,column=4,sticky="NWNESWSE")

		self.variance =Entry(self, font=("Calibri",16),width=5,borderwidth =1.5,relief=GROOVE,justify= RIGHT )
		self.variance.insert(0,'1')
		self.variance.grid(row=3,column=4,sticky="NWNESWSE")
		
		#self.arr = Button(self, font=("Goudy Stout", 11), text="",relief=GROOVE, borderwidth=1)
		#self.arr.grid(row=1, column=4, sticky="NWNESWSE")
#This is the First Row
		"""self.tit=Title(self,font = ('Helvetica',16),text='Φ(z) The CDF of a Standard Normal Distribution :  ',borderwidth=1)
		self.tit.grid(row=5,column=0)"""

		self.sevenButton = Button(self, font=("Helvetica", 11), text="7", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("7"))
		self.sevenButton.grid(row=2, column=0, sticky="NWNESWSE")

		self.eightButton = Button(self, font=("Helvetica", 11), text="8", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("8"))
		self.eightButton.grid(row=2, column=1, sticky="NWNESWSE")

		self.nineButton = Button(self, font=("Helvetica", 11), text="9", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("9"))
		self.nineButton.grid(row=2, column=2, sticky="NWNESWSE")

		self.clearButton = Button(self, font=("Arial", 11), text="Clear", borderwidth=3,relief=RAISED,bg='#a7effc', command=lambda: self.clearText())
		self.clearButton.grid(row=4, column=3,columnspan=2, sticky="NWNESWSE")

#This is the Second Row
		self.fourButton = Button(self, font=("Helvetica", 11), text="4", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("4"))
		self.fourButton.grid(row=3, column=0, sticky="NWNESWSE")

		self.fiveButton = Button(self, font=("Helvetica", 11), text="5", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("5"))
		self.fiveButton.grid(row=3, column=1, sticky="NWNESWSE")

		self.sixButton = Button(self, font=("Helvetica", 11), text="6", borderwidth=1, bg="#415748",fg='white',command=lambda: self.appendToinput("6"))
		self.sixButton.grid(row=3, column=2, sticky="NWNESWSE")

		self.submitbutton = Button(self, font=("Tarjan Pro", 11), text="Submit", borderwidth=3, relief=RAISED,bg="#eb4b73",fg='white',command=lambda: self.calculateExpression())
		self.submitbutton.grid(row=5, column=3, sticky="NWNESWSE", columnspan=2)

#This is the Third Row
		self.oneButton = Button(self, font=("Helvetica", 11), text="1", borderwidth=1,bg="#415748",fg='white',command=lambda: self.appendToinput("1"))
		self.oneButton.grid(row=4, column=0, sticky="NWNESWSE")

		self.twoButton = Button(self, font=("Helvetica", 11), text="2", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("2"))
		self.twoButton.grid(row=4, column=1, sticky="NWNESWSE")

		self.threeButton = Button(self, font=("Helvetica", 11), text="3", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("3"))
		self.threeButton.grid(row=4, column=2, sticky="NWNESWSE")

#		self.minusButton = Button(self, font=("Helvetica", 11), text="-", borderwidth=0, command=lambda: self.appendToinput("-"))
#		self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")


#This is the Fourth Row
		self.zeroButton = Button(self, font=("Helvetica", 11), text="0", borderwidth=1,bg="#415748",fg='white', command=lambda: self.appendToinput("0"))
		self.zeroButton.grid(row=5, column=0, columnspan=2, sticky="NWNESWSE")

		self.dotButton = Button(self, font=("Helvetica", 15), text=".", borderwidth=1, bg='#516156',fg='white',command=lambda: self.appendToinput("."))
		self.dotButton.grid(row=5, column=2, sticky="NWNESWSE")

app = Application(Solver).grid()		
Solver.mainloop()
