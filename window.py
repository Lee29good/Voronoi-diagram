import tkinter as tk
from tkinter import font 

# 創建主視窗,設定視窗大小,設定視窗標題
root = tk.Tk()
root.geometry("1100x800")
root.title("Voronoi diagram")
root.configure(bg="lightgray") 
print("The window has been created")

# 設置字體大小和字體樣式
custom_font = font.Font(family="Helvetica", size=20, weight="bold")
custom_font2 = font.Font(family="Helvetica", size=13, weight="bold")
title_font = font.Font(family="Courier", size=60, weight="bold", slant="italic")

#創建內部圖形視窗(1.畫布視窗：600x600 , 2.功能視窗:400x700)
canva_Area = tk.Frame(root, width=620, height=700, borderwidth=2, relief="solid")
canva_Area.grid(row=0, column=0, padx=(25,0), pady=(50,25))
canva_Area.grid_propagate(False)  
Title = tk.Label(canva_Area, text="Voronoi Diagram", fg="blue", font=title_font)
Title.grid(row=0,column=0,sticky='w')

canvas = tk.Canvas(canva_Area, width=600, height=600, borderwidth=2 , relief="solid")
canvas.grid(row=1, column=0 ,sticky='nsew')

setting_Area = tk.Frame(root, width=400, height=700, bg="white")
setting_Area.grid(row=0, column=1, padx=25, pady=(50,25))
setting_Area.grid_propagate(False)  

#setting area (setting1/2/3/4)裡面佈局

#--第一個setting area (點處理)--
setting1 = tk.Frame(setting_Area, width=180, height=340)
setting1.grid(row=0, column=0 ,padx=10, pady=5,sticky='nsew')
setting1.grid_propagate(False)  

vertex_frame = tk.Frame(setting1, width=180 ,height=340)
vertex_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
vertex_Title = tk.Label(vertex_frame, text="<點操作>", fg="blue", font=custom_font)
vertex_Title.grid(row=0, columnspan=2, sticky='w')
vertex_position = tk.Label(vertex_frame, text="滑鼠位置:", fg="black", font=custom_font)
vertex_position.grid(row=1, column=0, pady=(20,0), sticky='w')
vertex_position = tk.Label(vertex_frame, text="(0,0)", fg="black", font=custom_font)
vertex_position.grid(row=1, column=1 , pady=(20,0))
vertex_x = tk.Label(vertex_frame, text="X(0~600):", fg="black", font=custom_font)
vertex_x.grid(row=2, column=0, sticky='w')
vertex_xInput = tk.Entry(vertex_frame, width=7)
vertex_xInput.grid(row=2, column=1)
vertex_y = tk.Label(vertex_frame, text="Y(0~600):", fg="black", font=custom_font)
vertex_y.grid(row=3, column=0, sticky='w')
vertex_yInput = tk.Entry(vertex_frame, width=7)
vertex_yInput.grid(row=3, column=1)
addveretex_button = tk.Button(vertex_frame, text="添加點", bg="lightblue", fg="black", font=custom_font2, width=7)
addveretex_button.grid(row=4, columnspan=2, sticky='w')

vertex_random_Title = tk.Label(vertex_frame, text="~隨機生成點~", fg="blue", font=custom_font)
vertex_random_Title.grid(row=5, columnspan=2, pady=(30,0), sticky='w')
vertex_random_amount = tk.Label(vertex_frame, text="生成數量:", fg="black", font=custom_font)
vertex_random_amount.grid(row=6, column=0, sticky='w')
vertex_random_Input = tk.Entry(vertex_frame, width=7)
vertex_random_Input.grid(row=6, column=1)
random_button = tk.Button(vertex_frame, text="隨機產生", bg="lightblue", fg="black", font=custom_font2, width=7)
random_button.grid(row=7, columnspan=2, sticky='w')


#--第二個setting area (執行、檔案)--
setting2 = tk.Frame(setting_Area, width=180, height=340)
setting2.grid(row=0, column=1 ,padx=10, pady=5,sticky='nsew')
setting2.grid_propagate(False)  

##setting2->operate_frame
operate_frame = tk.Frame(setting2, width=150, height=150)
operate_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
operate_Title = tk.Label(operate_frame, text="<動作>", fg="blue", font=custom_font)
operate_Title.grid(row=0,sticky='w')
operate_button1 = tk.Button(operate_frame, text="執行", bg="lightblue", fg="black", font=custom_font2, width=10)
operate_button1.grid(row=1, padx=(25,0), pady=5) 
operate_button2 = tk.Button(operate_frame, text="下一組資料", bg="lightblue", fg="black", font=custom_font2, width=10)
operate_button2.grid(row=2, padx=(25,0), pady=5) 
operate_button3 = tk.Button(operate_frame, text="一步一步執行", bg="lightblue", fg="black", font=custom_font2, width=10)
operate_button3.grid(row=3, padx=(25,0), pady=5) 
operate_button4 = tk.Button(operate_frame, text="清空頁面", bg="lightblue", fg="black", font=custom_font2, width=10)
operate_button4.grid(row=4, padx=(25,0), pady=5) 

##setting2->file_frame
file_frame = tk.Frame(setting2, width=150, height=150)
file_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
file_Title = tk.Label(file_frame, text="<檔案>", fg="blue", font=custom_font)
file_Title.grid(row=0,sticky='w')
file_button1 = tk.Button(file_frame, text="讀取輸入檔", bg="lightblue", fg="black", font=custom_font2, width=10)
file_button1.grid(row=1, padx=(25,0), pady=5) 
file_button2 = tk.Button(file_frame, text="讀取輸出檔", bg="lightblue", fg="black", font=custom_font2, width=10)
file_button2.grid(row=2, padx=(25,0), pady=5) 
file_button3 = tk.Button(file_frame, text="輸出文字檔", bg="lightblue", fg="black", font=custom_font2, width=10)
file_button3.grid(row=3, padx=(25,0), pady=5) 

#--第三個setting area (點資料)--
setting3 = tk.Frame(setting_Area, width=180, height=340)
setting3.grid(row=1, column=0 ,padx=10, pady=5,sticky='nsew')
setting3.grid_propagate(False)  
label3 = tk.Label(setting3, text="<點資料>", fg="blue", font=custom_font)
label3.grid(row=0,sticky='w')
frame3 = tk.Frame(setting3, width=180, height=300 ,borderwidth=2 ,relief="solid")
frame3.grid(row=1)


#--第四個setting area (邊資料)--
setting4 = tk.Frame(setting_Area, width=180, height=340)
setting4.grid(row=1, column=1 ,padx=10, pady=5,sticky='nsew')
setting4.grid_propagate(False)  
label4 = tk.Label(setting4, text="<邊資料>", fg="blue", font=custom_font)
label4.grid(row=0,sticky='w')
frame4 = tk.Frame(setting4, width=180, height=300 , borderwidth=2, relief="solid")
frame4.grid(row=1)



# 啟動主循環
root.mainloop()