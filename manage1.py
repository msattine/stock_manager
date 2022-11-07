import tkinter as tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import random

bg_color = "#3d6466"

class inventory_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.units = tk.StringVar()
		self.dimensions = tk.StringVar()
		self.price = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' : self.item_name.get(),
			'units'     : self.units.get(),
			'dimensions': self.dimensions.get(),
			'price'     : self.price.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.units.set("")
		self.dimensions.set("")
		self.price.set("")
		self.id.set("")

class purchase_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.quantity = tk.StringVar()
		self.date = tk.StringVar()
		self.company = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get(),
			'company'     	: self.company.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.company.set("")
		self.id.set("")

class sale_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.quantity = tk.StringVar()
		self.date = tk.StringVar()
		self.site = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get(),
			'site'     	: self.site.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.site.set("")
		self.id.set("")

class return_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.quantity = tk.StringVar()
		self.date = tk.StringVar()
		self.site = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get(),
			'site'     	: self.site.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.site.set("")
		self.id.set("")

class stock_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.quantity = tk.StringVar()
		self.date = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.id.set("")



def clear_widgets(frame):
	for wdg in frame.winfo_children():
		wdg.destroy()

def load_main_frame():
	clear_widgets(inventory_frame)
	clear_widgets(purchase_frame)
	clear_widgets(sale_frame)
	clear_widgets(return_frame)
	clear_widgets(stock_frame)
	clear_widgets(avail_stock_frame)
	main_frame.tkraise()
	main_frame.pack_propagate(False)
	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo.png")
	#logo_widget = tk.Label(main_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack()
	
	# main_frame widgets
	tk.Label(main_frame, text="Stock Manager", bg=bg_color, fg="white", font=("TkMenuFont", 18)).pack()
	# button widget for inventory
	tk.Button(main_frame, text="Inventory", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_inventory_frame()).pack(pady=20)
	# button widget for purchase
	tk.Button(main_frame, text="Purchase", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_purchase_frame()).pack(pady=20)
	# button widget for Sale
	tk.Button(main_frame, text="Sale", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_sale_frame()).pack(pady=20)
	# button widget for Return
	tk.Button(main_frame, text="Return", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_return_frame()).pack(pady=20)
	# button widget for Stock
	tk.Button(main_frame, text="Stock", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_stock_frame()).pack(pady=20)
	# button widget for Available stock
	tk.Button(main_frame, text="Available Stock", font=("TkHeadingFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_avail_stock_frame()).pack(pady=20)

def inventory_add():
	item = inv_item.get()

	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = '" +item['item_name']+"' ")
	result = cursor.fetchone()

	inv_item.err_msg["text"] = ""
	if int(result[0]) > 0:
		inv_item.err_msg["text"] = "Error: The entry already exists"
	else:
		cursor.execute("INSERT INTO inventory(item_name, units, dimensions, price) VALUES(?,?,?,?)", 
				(item['item_name'], item['units'], item['dimensions'], item['price']))
		conn.commit()
		inv_item.err_msg["text"] = "Success: Added the new item"

def inventory_delete():
	id = inv_item.get_id()
	cursor.execute("SELECT * from inventory")
	result = cursor.fetchall()
	ids = [r[0] for r in result]

	inv_item.err_msg["text"] = ""
	if id in ids:
		cursor.execute("delete from inventory where id = ?", (id,))
		conn.commit()
		inv_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		inv_item.err_msg["text"] = "Entry doesnt exist"

def purchase_add():
	item = pur_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:

		cursor.execute("SELECT COUNT(*) from purchase WHERE item_name = ? and quantity = ? and date = ? and company = ?",
				(item['item_name'], item['quantity'], item['date'], item['company']))
		result = cursor.fetchone()

		pur_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			pur_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO purchase(item_name, quantity, date, company) VALUES(?,?,?,?)", 
					(item['item_name'], item['quantity'], item['date'], item['company']))
			conn.commit()
			pur_item.err_msg["text"] = "Success: Added the new item"
	else:
		pur_item.err_msg["text"] = "Error: Item doesnt exist in the inventory"

def purchase_delete():
	id = pur_item.get_id()
	cursor.execute("SELECT * from purchase")
	result = cursor.fetchall()
	ids = [r[0] for r in result]

	pur_item.err_msg["text"] = ""
	if id in ids:
		cursor.execute("delete from purchase where id = ?", (id,))
		conn.commit()
		pur_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		pur_item.err_msg["text"] = "Entry doesnt exist"

def sale_add():
	item = sl_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		cursor.execute("SELECT COUNT(*) from sale WHERE item_name = ? and quantity = ? and date = ? and site = ?",
				(item['item_name'], item['quantity'], item['date'], item['site']))
		result = cursor.fetchone()

		sl_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			sl_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO sale(item_name, quantity, date, site) VALUES(?,?,?,?)", 
					(item['item_name'], item['quantity'], item['date'], item['site']))
			conn.commit()
			sl_item.err_msg["text"] = "Success: Added the new item"
	else:
		sl_item.err_msg["text"] = "Error: Item doesnt exist in the inventory"

def sale_delete():
	id = sl_item.get_id()
	cursor.execute("SELECT * from sale")
	result = cursor.fetchall()
	ids = [r[0] for r in result]

	sl_item.err_msg["text"] = ""
	if id in ids:
		cursor.execute("delete from sale where id = ?", (id,))
		conn.commit()
		sl_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		sl_item.err_msg["text"] = "Entry doesnt exist"

def return_add():
	item = ret_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		cursor.execute("SELECT COUNT(*) from return WHERE item_name = ? and quantity = ? and date = ? and site = ?",
				(item['item_name'], item['quantity'], item['date'], item['site']))
		result = cursor.fetchone()

		ret_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			ret_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO return(item_name, quantity, date, site) VALUES(?,?,?,?)", 
					(item['item_name'], item['quantity'], item['date'], item['site']))
			conn.commit()
			ret_item.err_msg["text"] = "Success: Added the new item"
	else:
		ret_item.err_msg["text"] = "Error: Item doesnt exist in the inventory"

def return_delete():
	id = ret_item.get_id()
	cursor.execute("SELECT * from return")
	result = cursor.fetchall()
	ids = [r[0] for r in result]

	ret_item.err_msg["text"] = ""
	if id in ids:
		cursor.execute("delete from return where id = ?", (id,))
		conn.commit()
		ret_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		ret_item.err_msg["text"] = "Entry doesnt exist"

def stock_add():
	item = st_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		cursor.execute("SELECT COUNT(*) from stock WHERE item_name = ? and quantity = ? and date = ?",
				(item['item_name'], item['quantity'], item['date']))
		result = cursor.fetchone()

		st_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			st_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO stock(item_name, quantity, date) VALUES(?,?,?)", 
					(item['item_name'], item['quantity'], item['date']))
			conn.commit()
			st_item.err_msg["text"] = "Success: Added the new item"
	else:
		st_item.err_msg["text"] = "Error: Item doesnt exist in the inventory"

def stock_delete():
	id = st_item.get_id()
	cursor.execute("SELECT * from stock")
	result = cursor.fetchall()
	ids = [r[0] for r in result]

	st_item.err_msg["text"] = ""
	if id in ids:
		cursor.execute("delete from stock where id = ?", (id,))
		conn.commit()
		st_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		st_item.err_msg["text"] = "Entry doesnt exist"



def load_view_frame():
	global cur_view
	clear_widgets(inventory_frame)
	clear_widgets(purchase_frame)
	clear_widgets(sale_frame)
	clear_widgets(return_frame)
	clear_widgets(stock_frame)
	view_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(inventory_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# Back button widget
	if cur_view == "Inventory":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_inventory_frame()).pack(pady=20)
	elif cur_view == "Purchase":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_purchase_frame()).pack(pady=20)
	elif cur_view == "Sale":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_sale_frame()).pack(pady=20)
	elif cur_view == "Return":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_return_frame()).pack(pady=20)
	elif cur_view == "Stock":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_stock_frame()).pack(pady=20)

	# inventory_frame widgets
	if cur_view == "Inventory":
		tk.Label(view_frame, text="Inventory List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)
	elif cur_view == "Purchase":
		tk.Label(view_frame, text="Purchase List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)
	elif cur_view == "Sale":
		tk.Label(view_frame, text="Sale List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)
	elif cur_view == "Return":
		tk.Label(view_frame, text="Return List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)
	elif cur_view == "Stock":
		tk.Label(view_frame, text="Stock List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	scrolly = tk.Scrollbar(view_frame,orient=tk.VERTICAL)
	scrollx = tk.Scrollbar(view_frame,orient=tk.HORIZONTAL)
	if cur_view == "Inventory":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","units","dimensions","price"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Purchase":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","company"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Sale":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","site"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Return":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","site"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Stock":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	
	scrollx.pack(side=tk.BOTTOM,fill=tk.X)
	scrolly.pack(side=tk.RIGHT,fill=tk.Y)
	scrollx.config(command=CourseTable.xview)
	scrolly.config(command=CourseTable.yview)
	
	CourseTable.heading("id",text="ID")
	CourseTable.heading("item_name",text="Item Name")
	CourseTable.column("id",width=40)
	CourseTable.column("item_name",width=100)
	CourseTable["show"]="headings"
	if cur_view == "Inventory":
		CourseTable.heading("units",text="Units")
		CourseTable.heading("dimensions",text="Dimensions")
		CourseTable.heading("price",text="Price")
		CourseTable.column("units",width=100)
		CourseTable.column("dimensions",width=100)
		CourseTable.column("price",width=100)
	elif cur_view == "Purchase":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.heading("company",text="Company")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
		CourseTable.column("company",width=100)
	elif cur_view == "Sale":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.heading("site",text="Site")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
		CourseTable.column("site",width=100)
	elif cur_view == "Return":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.heading("site",text="Site")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
		CourseTable.column("site",width=100)
	elif cur_view == "Stock":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
	CourseTable.pack(fill=tk.BOTH,expand=1)

	if cur_view == "Inventory":
		cursor.execute("select * from inventory")
	elif cur_view == "Purchase":
		cursor.execute("select * from purchase")
	elif cur_view == "Sale":
		cursor.execute("select * from sale")
	elif cur_view == "Return":
		cursor.execute("select * from return")
	elif cur_view == "Stock":
		cursor.execute("select * from stock")
	rows=cursor.fetchall()
	CourseTable.delete(*CourseTable.get_children())
	for row in rows:
		CourseTable.insert("", tk.END, values=row)




def load_inventory_frame():
	global cur_view
	cur_view = "Inventory"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = inventory_frame
	cur_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Inventory", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	item_name_label = tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin)
	units_label = tk.Label(cur_frame, font=label_font, text="Units").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	dimensions_label = tk.Label(cur_frame, font=label_font, text="Dimensions").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	price_label = tk.Label(cur_frame, font=label_font, text="Price").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=inv_item.units, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.dimensions, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.price, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	inv_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:inventory_add()).place(x=label_x_margin, y= label_y_margin+5*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:inventory_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+5*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+7*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+7*label_y_gap)

def load_purchase_frame():
	global cur_view
	cur_view = "Purchase"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = purchase_frame
	cur_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Purchase", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Company").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=pur_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=pur_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=pur_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=pur_item.company, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	pur_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:purchase_add()).place(x=label_x_margin, y= label_y_margin+5*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:purchase_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=pur_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+5*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+7*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+7*label_y_gap)

def load_sale_frame():
	global cur_view
	cur_view = "Sale"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = sale_frame
	cur_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Sale", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Site").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=sl_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.site, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	sl_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:sale_add()).place(x=label_x_margin, y= label_y_margin+5*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:sale_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+5*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+7*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+7*label_y_gap)

def load_return_frame():
	global cur_view
	cur_view = "Return"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = return_frame
	cur_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Return", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Site").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=ret_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.site, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	ret_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:return_add()).place(x=label_x_margin, y= label_y_margin+5*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:return_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+5*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+7*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+7*label_y_gap)

def load_stock_frame():
	global cur_view
	cur_view = "Stock"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = stock_frame
	cur_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Stock", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=st_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=st_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=st_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	st_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:stock_add()).place(x=label_x_margin, y= label_y_margin+5*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:stock_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=st_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+5*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+7*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+7*label_y_gap)

def load_avail_stock_frame():
	clear_widgets(main_frame)
	avail_stock_frame.tkraise()

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(stock_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)
	
	# stock_frame widgets
	tk.Label(avail_stock_frame, 
		 text="Available Stock", 
		 bg=bg_color, 
		 fg="white", 
		 font=("TkHeadingFont", 20)
	).pack(pady=25)

	# Back button widget
	tk.Button(
		  avail_stock_frame,
		  text="Back",
		  font=("TkMenuFont", 16),
		  bg="#28393a",
		  fg="white",
		  cursor="hand2",
		  activebackground="#badee2",
		  activeforeground="black",
		  command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin)

# initialize app
root = tk.Tk()
root.title("Stock Manager")
root.eval("tk::PlaceWindow . center")

label_x_margin = 50
entry_x_margin = 170
label_y_margin = 120
label_y_gap = 40
button_gap = 100
label_font = ("TkMenuFont", 12)


main_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
main_frame.grid(row=0, column=0, sticky="nesw")

inventory_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
inventory_frame.grid(row=0, column=0, sticky="nesw")

sale_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
sale_frame.grid(row=0, column=0, sticky="nesw")

return_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
return_frame.grid(row=0, column=0, sticky="nesw")

purchase_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
purchase_frame.grid(row=0, column=0, sticky="nesw")

stock_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
stock_frame.grid(row=0, column=0, sticky="nesw")

avail_stock_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
avail_stock_frame.grid(row=0, column=0, sticky="nesw")

view_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
view_frame.grid(row=0, column=0, sticky="nesw")

inv_item = inventory_item()
pur_item = purchase_item()
sl_item = sale_item()
ret_item = return_item()
st_item = stock_item()

conn =sqlite3.connect("sm.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS inventory(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, units text NOT NULL, dimensions text NOT NULL, price text) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS purchase(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, company text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS sale(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, site text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS return(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, site text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS stock(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL) """);

cur_view = "Inventory"

load_main_frame()




# run app
root.mainloop()
