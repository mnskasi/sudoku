import time
import random
from random import shuffle,randint
import threading
import numpy as np
from tkinter import *
from tkinter import ttk,font
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Sudoku")
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(width_value,height_value))
root.configure(bg="white")
res = IntVar(root)
res.set(2)
attempts = 5 
break_flag=0
def check_difficulty(event):
  global attempts
  if res.get() not in range(1,4):
    messagebox.showwarning("Warning","No difficulty selected")
  elif res.get() == 1:
    temp_frame=Frame(root,bg="white",height=height_value,width=width_value)
    temp_frame.place(x=0,y=0)
    attempts=2
    Actual_game()
  elif res.get() == 2:
    temp_frame=Frame(root,bg="white",height=height_value,width=width_value)
    temp_frame.place(x=0,y=0)
    attempts=4
    Actual_game()
  elif res.get() == 3:
    temp_frame=Frame(root,bg="white",height=height_value,width=width_value)
    temp_frame.place(x=0,y=0)
    attempts=6
    Actual_game()


def proceed_to(event):
  for Widget in intro_frame.winfo_children():
    Widget.destroy()
  intro_frame.pack_forget()
  img=Image.open("rules.jpg")
  rules_image=ImageTk.PhotoImage(img)
  points_frame=Frame(root,bg="white")
  points_frame.place(x=100,y=50) 
  rules_label=Label(points_frame,image=rules_image,relief="flat",highlightthickness=0,borderwidth=0)
  rules_label.rules_image=rules_image
  rules_label.pack()
  points_label1=Label(points_frame,bg="white",font=("Bold",18),text="\u2022The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.\n")
  points_label2=Label(points_frame,bg="white",font=("Bold",18),text="\u2022The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. \nEach number can only appear once in a row, column or box.\n")
  points_label3=Label(points_frame,bg="white",font=("Bold",18),text="\u2022The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, \nmust also contain the numbers 1-9, without repetition or omission.\n")
  points_label4=Label(points_frame,bg="white",font=("Bold",18),text="\u2022Every puzzle has just one correct solution.\n")
  points_label1.pack()
  points_label2.pack()
  points_label3.pack()
  points_label4.pack()
  difficulty_frame=Frame(root,bg="white")
  difficulty_frame.place(x=750,y=550)
  Label(difficulty_frame,bg="white",font=("Bold",20),text="Select your difficulty level").pack()
  Radiobutton(difficulty_frame, text = "EASY",font=("Bold",18), variable = res, value = 1, height = 3, width = 30, bg = "white",relief="flat",activebackground="white",highlightthickness=0,borderwidth=0).pack()
  Radiobutton(difficulty_frame, text = "MEDIUM",font=("Bold",18), variable = res, value = 2, height = 3, width = 30, bg = "white",relief="flat",activebackground="white",highlightthickness=0,borderwidth=0).pack()
  Radiobutton(difficulty_frame, text = "HARD", font=("Bold",18),variable = res, value = 3, height = 3, width = 30, bg = "white",relief="flat",activebackground="white",highlightthickness=0,borderwidth=0).pack()
  img1=Image.open("arrow.jpg")
  proceed=ImageTk.PhotoImage(img1)
  B1=Label(difficulty_frame,image=proceed,bg="white")
  B1.proceed=proceed
  B1.pack()
  B1.bind("<Button-1>",check_difficulty)


img=Image.open("Introduction.jpg")
bg_image=ImageTk.PhotoImage(img)
intro_frame=LabelFrame(root,relief="flat",highlightthickness=0,borderwidth=0,bg="white",fg="white")
intro_frame.place(x=600,y=150)
intro_label=Label(intro_frame,image=bg_image,relief="flat",highlightthickness=0,borderwidth=0)
intro_label.pack()
B2=Button(intro_frame,height=10,relief="flat",bg="white",fg="white",activebackground="white",highlightthickness=0,borderwidth=0)
B2.pack()
img1=Image.open("arrow.jpg")
proceed=ImageTk.PhotoImage(img1)
B1=Label(intro_frame,image=proceed,bg="white")
B1.pack(anchor=S)
B1.bind("<Button-1>",proceed_to)

grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
numberList=[1,2,3,4,5,6,7,8,9]
labels=[]
temp_entries=[]
entries=[]
answers=[]
indices=[]
counter=1
grid1 = []

#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
  return True 


def fillGrid(grid):
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      shuffle(numberList)      
      for value in numberList:
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col]=0
def solveGrid(grid):
  global counter
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                counter+=1
                break
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col]=0
    


def mainthread():
  for i in range(len(entries)):
    temp_str=entries[i].get()
    if temp_str=='':
      temp_entries.append(0)
    else:
      temp_entries.append(int(temp_str))

def runner_num (num):
  # for row
  temp_row=[0,0,0,0,0,0,0,0,0]
  for i in range (0,9):
    if grid[num][i]==0:
      index=num*9+i
      temp_index=indices.index(index)
      entry_value=entries[temp_index].get()
      if entry_value != '':
        temp_row[i]=int(entry_value)
    else :
      temp_row[i]=grid[num][i]
  for j in range (1,10):
    if temp_row.count(j) >1 :
      for k in range(9):
        if temp_row[k]==j:
          # print("row is "+str(num)+"column is "+str(k))
          labels[num*9+k].configure(fg="red")
  row_flag=0
  for x in range(1,10):
    if temp_row.count(x)!=1:
      row_flag=1
      break
  if row_flag==0:
    for z in range(num*9,num*9+9):
      labels[z].configure(fg="green")    
  # for column
  temp_col=[0,0,0,0,0,0,0,0,0]
  for i in range (0,9):
    if grid[i][num]==0:
      index=i*9+num
      temp_index=indices.index(index)
      entry_value=entries[temp_index].get()
      if entry_value != '':
        temp_col[i]=int(entry_value)
    else :
      temp_col[i]=grid[i][num]
  for j in range (1,10):
    if temp_col.count(j) >1 :
      for k in range(9):
        if temp_col[k]==j:
          labels[k*9+num].configure(fg="red")
  col_flag=0
  for x in range(1,10):
    if temp_col.count(x)!=1:
      col_flag=1
      break
  if col_flag==0:
    cnt_col=0
    col_num=num
    while cnt_col<9:
      labels[col_num].configure(fg="green")
      col_num+=9
      cnt_col+=1

  temp_block=[0,0,0,0,0,0,0,0,0]
  if num==0:
    for p in range(3):
      for q in range(3):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[p*3+q]=int(entry_value)
        else :
          temp_block[p*3+q]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3):
        for q in range(3):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k].configure(fg="red")
            elif k<6:
              labels[k+6].configure(fg="red")
            else:
              labels[k+12].configure(fg="red")

  elif num==1:
    for p in range(3):
      for q in range(3,6):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[p*3+q-3]=int(entry_value)
        else :
          temp_block[p*3+q-3]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3):
        for q in range(3,6):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+3].configure(fg="red")
            elif k<6:
              labels[k+9].configure(fg="red")
            else:
              labels[k+15].configure(fg="red")


  elif num==2:
    for p in range(3):
      for q in range(6,9):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[p*3+q-6]=int(entry_value)
        else :
          temp_block[p*3+q-6]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3):
        for q in range(6,9):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+6].configure(fg="red")
            elif k<6:
              labels[k+10].configure(fg="red")
            else:
              labels[k+18].configure(fg="red")

  elif num==3:
    for p in range(3,6):
      for q in range(3):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-3)*3+q]=int(entry_value)
        else :
          temp_block[(p-3)*3+q]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3,6):
        for q in range(3):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+27].configure(fg="red")
            elif k<6:
              labels[k+33].configure(fg="red")
            else:
              labels[k+39].configure(fg="red")


  elif num==4:
    for p in range(3,6):
      for q in range(3,6):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-3)*3+q-3]=int(entry_value)
        else :
          temp_block[(p-3)*3+q-3]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3,6):
        for q in range(3,6):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+30].configure(fg="red")
            elif k<6:
              labels[k+36].configure(fg="red")
            else:
              labels[k+42].configure(fg="red")

  elif num==5:
    for p in range(3,6):
      for q in range(6,9):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-3)*3+q-6]=int(entry_value)
        else :
          temp_block[(p-3)*3+q-6]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(3,6):
        for q in range(6,9):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[+33].configure(fg="red")
            elif k<6:
              labels[k+39].configure(fg="red")
            else:
              labels[k+45].configure(fg="red")

  elif num==6:
    for p in range(6,9):
      for q in range(3):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-6)*3+q]=int(entry_value)
        else :
          temp_block[(p-6)*3+q]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(6,9):
        for q in range(3):
          index=p*9+q
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+54].configure(fg="red")
            elif k<6:
              labels[k+60].configure(fg="red")
            else:
              labels[k+66].configure(fg="red")

  elif num==7:
    for p in range(6,9):
      for q in range(3,6):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-6)*3+q-3]=int(entry_value)
        else :
          temp_block[(p-6)*3+q-3]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(6,9):
        for q in range(3,6):
          index=p*9+q
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+57].configure(fg="red")
            elif k<6:
              labels[k+63].configure(fg="red")
            else:
              labels[k+69].configure(fg="red")

  elif num==8:
    for p in range(6,9):
      for q in range(6,9):
        if grid[p][q]==0:
          index=p*9+q
          temp_index=indices.index(index)
          entry_value=entries[temp_index].get()
          if entry_value != '':
            temp_block[(p-6)*3+q-6]=int(entry_value)
        else :
          temp_block[(p-6)*3+q-6]=grid[p][q]
    block_flag=0
    for x in range(1,10):
      if temp_block.count(x)!=1:
        block_flag=1
        break
    if block_flag==0:
      for p in range(6,9):
        for q in range(6,9):
          index=p*9+q
          labels[index].configure(fg="green")
    for j in range (1,10):
      if temp_block.count(j) >1 :
        for k in range(9):
          if temp_block[k]==j:
            if k < 3:
              labels[k+60].configure(fg="red")
            elif k<6:
              labels[k+66].configure(fg="red")
            else:
              labels[k+72].configure(fg="red")

def mainrunner():
  global break_flag
  while break_flag==0:
    for i in range(len(entries)):
      temp_str=entries[i].get()
      if temp_str=='':
        temp_str="0"
      if not temp_str.isnumeric():
        invalid_indice=indices[i]
        labels[invalid_indice].configure(fg="orange")
        continue
      temp_str1=int(temp_str)
      if temp_str1 not in range(0,10):
        invalid_indice=indices[i]
        labels[invalid_indice].configure(fg="orange")
      elif temp_str1!=temp_entries[i]:
        temp_entries[i]=temp_str1
        for b in range(len(labels)):
          labels[b].configure(fg="black")
        success_flag=0
        for m in range(len(entries)):
          strings=entries[m].get()
          if strings=='':
            success_flag=1
            break
          else:
            if (strings.isnumeric):
              num1=int(strings)
              if answers[m]!=num1:
                success_flag=1
                break
            else:
              success_flag=1
              break
        if success_flag==0:
          print("Congratulations")
          frame1=Frame(root,bg="white",height=height_value,width=width_value)
          frame1.place(x=0,y=0)
          won_img=Image.open("win.jpg")
          won_image=ImageTk.PhotoImage(won_img)
          won_label=Label(root,image=won_image,bg="white")
          won_label.won_image=won_image
          won_label.place(x=0,y=0,relwidth=1,relheight=1)
          break_flag=1
        t1=threading.Thread(target=runner_num,args=(0,))
        t2=threading.Thread(target=runner_num,args=(1,))   
        t3=threading.Thread(target=runner_num,args=(2,))
        t4=threading.Thread(target=runner_num,args=(3,))
        t5=threading.Thread(target=runner_num,args=(4,))
        t6=threading.Thread(target=runner_num,args=(5,))
        t7=threading.Thread(target=runner_num,args=(6,))
        t8=threading.Thread(target=runner_num,args=(7,))
        t9=threading.Thread(target=runner_num,args=(8,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t1.join()
        t2.join()   
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

def Actual_game ():
  global counter
  root.configure(bg="white")
  fillGrid(grid)
  for r in range(0,9):
      grid1.append([])
      for c in range(0,9):
        grid1[r].append(grid[r][c])
  global attempts
  while attempts>0:
    #Select a random cell that is not already empty
    row = randint(0,8)
    col = randint(0,8)
    while grid[row][col]==0:
      row = randint(0,8)
      col = randint(0,8)
    #Remember its cell value in case we need to put it back  
    backup = grid[row][col]
    grid[row][col]=0
    #Take a full copy of the grid
    copyGrid = []
    for r in range(0,9):
      copyGrid.append([])
      for c in range(0,9):
          copyGrid[r].append(grid[r][c])
    #Count the number of solutions
    counter=0      
    solveGrid(copyGrid)  
    if counter!=1:
      grid[row][col]=backup
      attempts -= 1
  frame=LabelFrame(root,borderwidth=2,relief="solid",bg="skyblue")   
  frame.place(x=600,y=50)

  f1=LabelFrame(frame,borderwidth=2,relief="solid")
  f1.grid(row=0,column=0)
  f2=LabelFrame(frame,borderwidth=2,relief="solid")
  f2.grid(row=0,column=1)
  f3=LabelFrame(frame,borderwidth=2,relief="solid")
  f3.grid(row=0,column=2)
  f4=LabelFrame(frame,borderwidth=2,relief="solid")
  f4.grid(row=1,column=0)
  f5=LabelFrame(frame,borderwidth=2,relief="solid")
  f5.grid(row=1,column=1)
  f6=LabelFrame(frame,borderwidth=2,relief="solid")
  f6.grid(row=1,column=2)
  f7=LabelFrame(frame,borderwidth=2,relief="solid")
  f7.grid(row=2,column=0)
  f8=LabelFrame(frame,borderwidth=2,relief="solid")
  f8.grid(row=2,column=1)
  f9=LabelFrame(frame,borderwidth=2,relief="solid")
  f9.grid(row=2,column=2)


  for i in range(9):
    x=0
    for k in range(9):
      x=grid[i][k]
      if i<3:
        if k<3:
          if(x!=0):
            E = Label(f1,text=x,fg="black",width=5,font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            labels.append(E)
            E.grid(row=i, column=k,sticky="nsew",ipady=10,pady=2,padx=2)
          else:
            entry = Entry(f1,width=5,fg="black",font=("Bold",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i, column=k,pady=2,padx=2,ipady=10)
            entries.append(entry)
            labels.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
        elif k<6:
          if(x!=0):
            E = Label(f2,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i, column=k-3,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f2,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i, column=k-3,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
        else:  
          if(x!=0):
            E = Label(f3,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i, column=k-6,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f3,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i, column=k-6,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
      elif i<6:
        if k<3:
          if(x!=0):
            E = Label(f4,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-3, column=k,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f4,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-3, column=k,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
        elif k<6:
          if(x!=0):
            E = Label(f5,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-3, column=k-3,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f5,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-3, column=k-3,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
        else:  
          if(x!=0):
            E = Label(f6,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-3, column=k-6,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f6,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-3, column=k-6,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
      else:
        if k<3:
          if(x!=0):
            E = Label(f7,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-6, column=k,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f7,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-6, column=k,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
        elif k<6:
          if(x!=0):
            E = Label(f8,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-6, column=k-3,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f8,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-6, column=k-3,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
        else:  
          if(x!=0):
            E = Label(f9,text=x,width=5,fg="black",font=("Bold",20),bg="#14b1ab",borderwidth=1, relief="groove")
            E.grid(row=i-6, column=k-6,sticky="nsew",ipady=10,pady=2,padx=2)
            labels.append(E)
          else:
            entry = Entry(f9,width=5,fg="black",font=("BOLD",20),bg="#f3ecc2",highlightthickness=0,borderwidth=1,relief="groove",justify="center")
            entry.grid(row=i-6, column=k-6,pady=2,padx=2,ipady=10)
            entries.append(entry)
            answers.append(grid1[i][k])
            indices.append(i*9+k)
            labels.append(entry)
  frame.place(x=600,y=150)
  notes_frame=Frame(root,bg="white")
  img_note=Image.open("note.jpeg")
  notes_image=ImageTk.PhotoImage(img_note)
  notes_label=Label(image=notes_image)
  notes_label.notes_image=notes_image
  notes_frame.place(x=650,y=700)
  notes_label.place(x=300,y=700)
  label1=Label(notes_frame,font=("Bold",18),text=" ",fg="orange",bg="orange")
  label2=Label(notes_frame,font=("Bold",18),text="Invalid entry",fg="orange",bg="white")
  label3=Label(notes_frame,font=("Bold",18),text=" ",fg="red",bg="red")
  label4=Label(notes_frame,font=("Bold",18),text="Conflicting entry i.e multiple entries in a row, column or block",fg="red",bg="white")
  label5=Label(notes_frame,font=("Bold",18),text=" ",fg="green",bg="green")
  label6=Label(notes_frame,font=("Bold",18),text="a row or clolumn or block is completed. \nDoesn't mean it is correct just indicates 1-9 are present",fg="green",bg="white")
  label3.pack()
  label4.pack()
  label5.pack()
  label6.pack()
  label1.pack()
  label2.pack()

  mainthread()
  thr=threading.Thread(target=mainrunner)
  thr.start()

root.mainloop()