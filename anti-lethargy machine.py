import time
from tkinter import messagebox
time1 = input("How often would you like to stand up in minutes? Enter an number. (30, 120, etc.): ")
time2 = int(time1)
time3 = time2 * 60
time4 = input("How long would you like your standing sessions to be? Enter a number. (5, 10, etc.): ")
time5 = int(time4)
time6 = time5 * 60
while status True:
	time.sleep(time3)
	answer = messagebox.askokcancel("Stand up!", "It's been %s minutes and is time for you to stand up!" % time1)
	if answer == False:
		answer2 = messagebox.askyesno("Are you sure?", "Do you really want to quit the program?")
		if answer == True:
			exit()
	
	time.sleep(time6)
	answer3 = messagebox.showinfo("All done", "You can sit back down; it's been %s minutes. You will be alerted next time you must stand." % time4)
	if answer3 == False:
		answer4 = messagebox.askyesno("Are you sure?", "Do you really want to quit the program?")
		if answer == True:
			exit()
