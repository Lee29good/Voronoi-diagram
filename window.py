import tkinter as tk
from tkinter import font , ttk
import random 

class VoronoiDiagram:
  # 創建主視窗,設定視窗大小,設定視窗標題
  def __init__(self, root):
    self.root = root
    self.root.geometry("1200x800")
    self.root.title("Voronoi Diagram")
    self.root.configure(bg="lightgray")
    print("The window has been created")
    
    # 字體設置
    self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
    self.custom_font2 = font.Font(family="Helvetica", size=13, weight="bold")
    self.title_font = font.Font(family="Courier", size=60, weight="bold", slant="italic")
    
    # 創建畫布和功能區域
    self.create_canvas_area()
    self.create_setting_area()
    
    # 點的計數器
    self.point_index = 0 
    #滑鼠事件綁定
    self.canvas.bind("<ButtonPress-1>", self.on_canvas_press)
    self.canvas.bind("<Motion>", self.on_canvas_move)
    self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release) 

  def create_canvas_area(self):
    # 畫布跟標題區域
    canva_area = tk.Frame(self.root, width=620, height=700, borderwidth=2, relief="solid")
    canva_area.grid(row=0, column=0, padx=(25, 0), pady=(50, 25))

    title = tk.Label(canva_area, text="Voronoi Diagram", fg="blue", font=self.title_font)
    title.grid(row=0, column=0, sticky='w')

    #畫布區(600x600)
    self.canvas = tk.Canvas(canva_area, width=590, height=590, borderwidth=2, relief="solid")
    self.canvas.grid(row=1, column=0, sticky='nsew')

  def create_setting_area(self):
    # 功能區域(在右側)
    setting_area = tk.Frame(self.root, width=500, height=700, bg="white")
    setting_area.grid(row=0, column=1, padx=25, pady=(50, 25))
    setting_area.grid_propagate(False)

    # 創建四個功能性區塊
    self.create_vertex_settings(setting_area)
    self.create_operation_settings(setting_area)
    self.create_vertex_record(setting_area)
    self.create_line_record(setting_area)
    
  def create_vertex_settings(self, parent):
    # 點操作區域
    setting1 = tk.Frame(parent, width=230, height=340)
    setting1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
    setting1.grid_propagate(False)

    vertex_frame = tk.Frame(setting1, width=230, height=340)
    vertex_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    vertex_title = tk.Label(vertex_frame, text="<點操作>", fg="blue", font=self.custom_font)
    vertex_title.grid(row=0, columnspan=2, sticky='w')

    self.vertex_position_label = tk.Label(vertex_frame, text="滑鼠位置:", fg="black", font=self.custom_font)
    self.vertex_position_label.grid(row=1, column=0, pady=(20, 0), sticky='w')
    self.vertex_position_value = tk.Label(vertex_frame, text="(X,Y)", fg="black", font=self.custom_font)
    self.vertex_position_value.grid(row=1, column=1, padx=(10,0), pady=(20, 0))

    self.vertex_x_input = self.create_input(vertex_frame, "X(0~600):", 2)
    self.vertex_y_input = self.create_input(vertex_frame, "Y(0~600):", 3)

    add_vertex_button = tk.Button(vertex_frame, text="添加點", bg="lightblue", fg="black", font=self.custom_font2, width=7, command=self.add_vertex)
    add_vertex_button.grid(row=4, columnspan=2, sticky='w')

    self.create_random_vertex_section(vertex_frame)
    
  def create_random_vertex_section(self, parent):
    vertex_random_title = tk.Label(parent, text="~隨機生成點~", fg="blue", font=self.custom_font)
    vertex_random_title.grid(row=5, columnspan=2, pady=(30, 0), sticky='w')

    random_amount_label = tk.Label(parent, text="生成數量:", fg="black", font=self.custom_font)
    random_amount_label.grid(row=6, column=0, sticky='w')
    self.random_amount_input = tk.Entry(parent, width=7)
    self.random_amount_input.grid(row=6, column=1,sticky="w")

    random_button = tk.Button(parent, text="隨機產生", bg="lightblue", fg="black", font=self.custom_font2, width=7, command=self.generate_random_vertices)
    random_button.grid(row=7, columnspan=2, sticky='w')

  def create_input(self, parent, label_text, row):
    label = tk.Label(parent, text=label_text, fg="black", font=self.custom_font)
    label.grid(row=row, column=0, sticky='w')
    entry = tk.Entry(parent, width=7)
    entry.grid(row=row, column=1, sticky="w")
    return entry
  
  def create_operation_settings(self, parent):
    # 執行與檔案區域
    setting2 = tk.Frame(parent, width=230, height=340)
    setting2.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')
    setting2.grid_propagate(False)

    operate_frame = tk.Frame(setting2, width=230, height=150)
    operate_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    operate_title = tk.Label(operate_frame, text="<動作>", fg="blue", font=self.custom_font)
    operate_title.grid(row=0, sticky='w')

    self.create_operation_buttons(operate_frame)

    file_frame = tk.Frame(setting2, width=230, height=150)
    file_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
    file_title = tk.Label(file_frame, text="<檔案>", fg="blue", font=self.custom_font)
    file_title.grid(row=0, sticky='w')

    self.create_file_buttons(file_frame)

  def create_operation_buttons(self, parent):
    buttons = [
      ("執行", self.execute_action),
      ("下一組資料", self.next_data_set),
      ("一步一步執行", self.step_by_step),
      ("清空頁面", self.clear_canvas)
    ]
    for i, (text, command) in enumerate(buttons):
      button = tk.Button(parent, text=text, bg="lightblue", fg="black", font=self.custom_font2, width=10, command=command)
      button.grid(row=i + 1, padx=(25, 0), pady=5)

  def create_file_buttons(self, parent):
    buttons = [
      ("讀取輸入檔", self.load_input_file),
      ("讀取輸出檔", self.load_output_file),
      ("輸出文字檔", self.export_text_file)
    ]
    for i, (text, command) in enumerate(buttons):
      button = tk.Button(parent, text=text, bg="lightblue", fg="black", font=self.custom_font2, width=10, command=command)
      button.grid(row=i + 1, padx=(25, 0), pady=5)

  def create_vertex_record(self, parent):
    # 點資料區域
    setting3 = tk.Frame(parent, width=230, height=340)
    setting3.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
    setting3.grid_propagate(False)

    label3 = tk.Label(setting3, text="<點資料>", fg="blue", font=self.custom_font)
    label3.grid(row=0, sticky='w')

    self.vertex_record = ttk.Treeview(setting3, columns=("index", "x_column", "y_column"), show='headings', height=15)
    self.vertex_record.heading("index", text="index")
    self.vertex_record.heading("x_column", text="X")
    self.vertex_record.heading("y_column", text="Y")
    self.vertex_record.column("index", width=70)
    self.vertex_record.column("x_column", width=70)
    self.vertex_record.column("y_column", width=70)
    self.vertex_record.grid(row=1, padx=7)

  def create_line_record(self, parent):
    # 邊資料區域
    setting4 = tk.Frame(parent, width=230, height=340)
    setting4.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')
    setting4.grid_propagate(False)

    label4 = tk.Label(setting4, text="<邊資料>", fg="blue", font=self.custom_font)
    label4.grid(row=0, sticky='w')

    self.line_record = ttk.Treeview(setting4, columns=("start", "end"), show='headings', height=15)
    self.line_record.heading("start", text="Start")
    self.line_record.heading("end", text="End")
    self.line_record.column("start", width=82)
    self.line_record.column("end", width=82)
    self.line_record.grid(row=1, padx=7)

  ##Canva畫布中的滑鼠事件
  def on_canvas_press(self, event):
    self.is_mouse_pressed = True  # 設置按下狀態
    self.update_coordinates(event.x, event.y)

  def on_canvas_move(self, event):
    if self.is_mouse_pressed:  # 只有在按下時才更新坐標
      self.update_coordinates(event.x, event.y)
      
  def on_canvas_release(self, event):
    self.is_mouse_pressed = False  # 重置按下狀態並固定坐標
    x, y = event.x, event.y
    self.vertex_position_value.config(text=f"({x},{y})")

  def update_coordinates(self, x, y):  
    # 檢查坐標是否在範圍內
    if 0 <= x <= 600 and 0 <= y <= 600:
      # 隨著畫布滑鼠移動，數值的更新
      self.vertex_position_value.config(text=f"({x},{y})")
      self.vertex_x_input.delete(0, tk.END)
      self.vertex_x_input.insert(0, str(x))
      self.vertex_y_input.delete(0, tk.END)
      self.vertex_y_input.insert(0, str(y))

  def add_vertex(self):
    try:
      x = int(self.vertex_x_input.get())
      y = int(self.vertex_y_input.get())
      if 0 <= x <= 600 and 0 <= y <= 600:
        self.point_index += 1
        self.vertex_record.insert("", "end", values=(self.point_index, x, y))
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")
      else:
        self.show_error("坐標必須在(0, 0)到(600, 600)之間。")
    except ValueError:
      self.show_error("請輸入有效的整數坐標。")

  def generate_random_vertices(self):
    try:
      count = int(self.random_amount_input.get())
      if count > 0:
        for _ in range(count):
          x = random.randint(0, 600)
          y = random.randint(0, 600)
          self.add_vertex_to_treeview(x, y)
      else:
        self.show_error("請輸入一個正整數。")
    except ValueError:
      self.show_error("請輸入有效的整數。")

  def add_vertex_to_treeview(self, x, y):
    self.point_index += 1
    self.vertex_record.insert("", "end", values=(self.point_index, x, y))
    self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

  def show_error(self, message):
    error_window = tk.Toplevel(self.root)
    error_window.title("錯誤")
    tk.Label(error_window, text=message, fg="red").pack(padx=20, pady=20)
    tk.Button(error_window, text="關閉", command=error_window.destroy).pack(pady=10)

  def execute_action(self):
    print("執行動作的功能尚未實現。")

  def next_data_set(self):
    print("下一組資料的功能尚未實現。")

  def step_by_step(self):
    print("一步一步執行的功能尚未實現。")

  def clear_canvas(self):
    self.canvas.delete("all")
    self.vertex_record.delete(*self.vertex_record.get_children())
    self.line_record.delete(*self.line_record.get_children())
    self.point_index = 0

  def load_input_file(self):
    print("讀取輸入檔的功能尚未實現。")

  def load_output_file(self):
    print("讀取輸出檔的功能尚未實現。")

  def export_text_file(self):
    print("輸出文字檔的功能尚未實現。")

if __name__ == "__main__":
  root = tk.Tk()
  app = VoronoiDiagram(root)
  root.mainloop()