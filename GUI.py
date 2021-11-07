from tkinter import *
from tkinter import filedialog as f
from tkinter import messagebox
import Stock_FundamentalAnalysis as sf
import time
import threading


def get_input_FolderPath():
	messagebox.showinfo("HINT", "This process will choose companies that outperform the average in 5 recent years from the input file")
	selected = f.askopenfilename()
	input_file_selected.set(selected)

def show_process():
	if(len(input_file_selected.get())<1):
		messagebox.showinfo("ERROR",'Choose input file first')
	else:	
		messagebox.showinfo("Warning", "Please wait, this could take minutes")
		sf.data_collecting(input_file_selected.get(),on_going_state)

def fmtTime(timeStamp):
    timeArray = time.localtime(timeStamp)
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return dateTime


window = Tk()

window.geometry("580x260")
window.title("Stock Screener")

#Creating the widgets
l1 = Label(window, text="Input file location:")
input_file_selected = StringVar()
entry = Entry(window, textvariable=input_file_selected,width=50)
choose_path_button = Button(window, text="Choose file", width=20, command = get_input_FolderPath)
on_going_state = Text(window,height=9)
run_button = Button(window, text="RUN", width=20, command = show_process)


#Positioning the widgets
l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
choose_path_button.grid(row=3, column=1, columnspan=2, pady=5)
on_going_state.grid(row=4, column=1, padx=5, sticky=W)
run_button.grid(row=5, column=1, columnspan=2, pady=5)
on_going_state.insert(5.0,"Results will show here"+"\n")

if(__name__ == "__main__"):
	window.mainloop()