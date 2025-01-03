from tkinter import *

root = Tk()
root.geometry('400x300+400+200')
root.title('pack布局')


frame=Frame(root,height=3,width=100,bd=5,relief='sunken')
frame.pack()

btn=Button(frame,text='test',bd=2)
btn.pack()

text1=Text(frame,fg='white',bg='#393b40',height=4,width=20,bd=3)
text1.pack()


root.mainloop()