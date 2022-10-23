import tkinter
from tkinter import *
from tokenize import Double

root=Tk();
root.title("Számológép");
root.geometry("570x600+100+200");
root.resizable(False, False);
root.config(bg="#000000");

label_result = Label(root, width=25, height=2, text="");
label_result.pack();

#első sor gombok
Button(root, text="C", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 10, y=100);
Button(root, text="/", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 150, y=100);
Button(root, text="%", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 290, y=100);
Button(root, text="*", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 440, y=100);

#második sor gombok
Button(root, text="7", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 10, y=200);
Button(root, text="8", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 150, y=200);
Button(root, text="9", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 290, y=200);
Button(root, text="-", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 440, y=200);

#harmadik sor gombok
Button(root, text="4", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 10, y=300);
Button(root, text="5", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 150, y=300);
Button(root, text="6", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 290, y=300);
Button(root, text="+", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 440, y=300);

#negyedik sor gombok
Button(root, text="1", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 10, y=400);
Button(root, text="2", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 150, y=400);
Button(root, text="3", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 290, y=400);
Button(root, text="=", width=5, height=3,font=("arial", 30, "bold"),  bd=1).place(x = 440, y=400);

#ötödik sor gombok
Button(root, text="0", width=10, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 15, y=500);
Button(root, text=".", width=5, height=1,font=("arial", 30, "bold"),  bd=1).place(x = 290, y=500);


root.mainloop();