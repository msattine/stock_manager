import tkinter as tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import random
import pandas as pd
from datetime import datetime
import re
import os

bg_color = "#3d6466"

class inventory_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.units = tk.StringVar()
		self.price = tk.StringVar()
		self.tax = tk.StringVar()
		self.date = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' : self.item_name.get(),
			'units'     : self.units.get(),
			'price'     : self.price.get(),
			'date'		: self.date.get(),
			'tax'       : self.tax.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.units.set("")
		self.price.set("")
		self.tax.set("")
		self.date.set("")
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
		self.to = tk.StringVar()
		self.frm = tk.StringVar()
		self.invoice = tk.StringVar()
		self.vehicle = tk.StringVar()
		self.remarks = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get(),
			'to'     	: self.to.get(),
			'frm'     	: self.frm.get(),
			'invoice'     	: self.invoice.get(),
			'vehicle'     	: self.vehicle.get(),
			'remarks'     	: self.remarks.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.to.set("")
		self.frm.set("")
		self.invoice.set("")
		self.vehicle.set("")
		self.remarks.set("")
		self.id.set("")

class return_item:
	def __init__(self):
		self.item_name = tk.StringVar()
		self.quantity = tk.StringVar()
		self.date = tk.StringVar()
		self.frm = tk.StringVar()
		self.to = tk.StringVar()
		self.err_msg = ""
		self.id = tk.StringVar()
	def get(self):
		return {'item_name' 	: self.item_name.get(),
			'quantity'     	: self.quantity.get(),
			'date'		: self.date.get(),
			'frm'     	: self.frm.get(),
			'to'     	: self.to.get()
			}
	def get_id(self):
		return int(self.id.get())
	def clear(self):
		self.item_name.set("")
		self.quantity.set("")
		self.date.set("")
		self.frm.set("")
		self.to.set("")
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

def get_first_missing_num(ids):
	num = len(ids)
	for l in range(len(ids)):
		if l not in ids:
			num = l
			break
	return num

def load_main_frame():
	clear_widgets(inventory_frame)
	clear_widgets(purchase_frame)
	clear_widgets(sale_frame)
	clear_widgets(return_frame)
	clear_widgets(stock_frame)
	clear_widgets(avail_stock_frame)
	clear_widgets(backup_frame)
	main_frame.tkraise()
	main_frame.pack_propagate(False)
	label_font = 12
	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo.png")
	#logo_widget = tk.Label(main_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack()
	
	# main_frame widgets
	tk.Label(main_frame, text="Stock Manager", bg=bg_color, fg="white", font=("TkMenuFont", 18)).pack()
	# button widget for Stock
	tk.Button(main_frame, text="Old Stock", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_stock_frame()).pack(pady=20)
	# button widget for purchase
	tk.Button(main_frame, text="Purchase", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_purchase_frame()).pack(pady=20)
	# button widget for Sale
	tk.Button(main_frame, text="Sale", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_sale_frame()).pack(pady=20)
	# button widget for Return
	tk.Button(main_frame, text="Return", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_return_frame()).pack(pady=20)
	# button widget for Available stock
	tk.Button(main_frame, text="Available Stock", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_avail_stock_frame()).pack(pady=20)
	# button widget for creating excel sheet
	tk.Button(main_frame, text="Write to Excel", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:write_to_excel_file()).pack(pady=20)
	# button widget for inventory
	tk.Button(main_frame, text="Inventory", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_inventory_frame()).pack(pady=20)
	# button widget for backup and restore
	tk.Button(main_frame, text="Backup and Restore", font=("TkHeadingFont", label_font), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		activeforeground="black", command=lambda:load_backup_frame()).pack(pady=20)

def get_item_name(curs, item_code):
	curs.execute("SELECT * from inventory")
	inv_dict = gen_dict(curs)
	inv_item_code = {}
	for d in inv_dict: inv_item_code[d['item_code']] = d['item_name']
	return inv_item_code[item_code]


def inventory_add():
	item = inv_item.get()

	cursor.execute("SELECT COUNT(*) from inventory WHERE item_name = ? and date = ?", (item['item_name'], item['date']))
	result = cursor.fetchone()
	cursor.execute("select * from inventory")
	inv_dict = gen_dict(cursor)
	inv_item_code = {}
	for d in inv_dict: inv_item_code[d['item_name']] = d['item_code']

	inv_item.err_msg["text"] = ""
	if int(result[0]) > 0:
		inv_item.err_msg["text"] = "Error: The entry already exists"
	else:
		if(item['item_name'] in inv_item_code):
			item_code = inv_item_code[item['item_name']]
		else:
			cursor.execute("SELECT * from inventory")
			result = cursor.fetchall()
			ids = [int(re.sub('ST', '', r[3])) for r in result]
			item_code = "ST%05d" % get_first_missing_num(ids)
		cursor.execute("INSERT INTO inventory(item_name, date, item_code, units, price, tax) VALUES(?,?,?,?,?,?)", 
				(item['item_name'], item['date'], item_code, item['units'], item['price'], item['tax']))
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
		cursor.execute("ALTER TABLE inventory RENAME TO temptable")
		cursor.execute(""" CREATE TABLE inventory(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, date text NOT NULL, item_code text NOT NULL, units text NOT NULL, price text, tax text NOT NULL);""");
		cursor.execute("""INSERT INTO inventory (item_name, date, item_code, units, price, tax) SELECT item_name, date, item_code, units, price, tax FROM temptable ORDER BY id;""") 
		cursor.execute("DROP TABLE temptable;")
		conn.commit()
		inv_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		inv_item.err_msg["text"] = "Entry doesnt exist"

def purchase_add():
	item = pur_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_code = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	print(result)
	if int(result[0]) > 0:
		item_name = get_item_name(cursor, item['item_name'])

		cursor.execute("SELECT COUNT(*) from purchase WHERE item_name = ? and quantity = ? and date = ? and company = ?",
				(item_name, item['quantity'], item['date'], item['company']))
		result = cursor.fetchone()

		pur_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			pur_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO purchase(item_name, quantity, date, company) VALUES(?,?,?,?)", 
					(item_name, item['quantity'], item['date'], item['company']))
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
		cursor.execute("ALTER TABLE purchase RENAME TO temptable")
		cursor.execute(""" CREATE TABLE purchase(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, company text NOT NULL) """);
		cursor.execute("""INSERT INTO purchase (item_name, quantity, date, company) SELECT item_name, quantity, date, company FROM temptable ORDER BY id;""") 
		cursor.execute("DROP TABLE temptable;")
		conn.commit()
		pur_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		pur_item.err_msg["text"] = "Entry doesnt exist"

def sale_add():
	item = sl_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_code = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		item_name = get_item_name(cursor, item['item_name'])
		cursor.execute("SELECT COUNT(*) from sale WHERE item_name = ? and quantity = ? and date = ? and invoice = ?",
				(item_name, item['quantity'], item['date'], item['invoice']))
		result = cursor.fetchone()

		sl_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			sl_item.err_msg["text"] = "Error: The entry with invoice already exists"
		else:
			cursor.execute("INSERT INTO sale(item_name, quantity, date, to_p, frm, invoice, vehicle, remarks) VALUES(?,?,?,?,?,?,?,?)", 
					(item_name, item['quantity'], item['date'], item['to'], item['frm'], item['invoice'], item['vehicle'], item['remarks']))
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
		cursor.execute("ALTER TABLE sale RENAME TO temptable")
		cursor.execute(""" CREATE TABLE sale(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, to_p text NOT NULL, frm text NOT NULL, invoice text NOT NULL, vehicle text NOT NULL, remarks text NOT NULL) """);
		cursor.execute("""INSERT INTO sale (item_name, quantity, date, to_p, frm, invoice, vehicle, remarks) SELECT item_name, quantity, date, to_p, frm, invoice, vehicle, remarks FROM temptable ORDER BY id;""") 
		cursor.execute("DROP TABLE temptable;")
		conn.commit()
		sl_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		sl_item.err_msg["text"] = "Entry doesnt exist"

def return_add():
	item = ret_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_code = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		item_name = get_item_name(cursor, item['item_name'])
		cursor.execute("SELECT COUNT(*) from return WHERE item_name = ? and quantity = ? and date = ? and to_p = ? and frm = ?",
				(item_name, item['quantity'], item['date'], item['to'], item['frm']))
		result = cursor.fetchone()

		ret_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			ret_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO return(item_name, quantity, date, to_p, frm) VALUES(?,?,?,?,?)", 
					(item_name, item['quantity'], item['date'], item['to'], item['frm']))
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
		cursor.execute("ALTER TABLE return RENAME TO temptable")
		cursor.execute(""" CREATE TABLE return(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, to_p text NOT NULL, frm text NOT NULL) """);
		cursor.execute("""INSERT INTO return (item_name, quantity, date, to_p, frm) SELECT item_name, quantity, date, to_p, frm FROM temptable ORDER BY id;""") 
		cursor.execute("DROP TABLE temptable;")
		conn.commit()
		ret_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		ret_item.err_msg["text"] = "Entry doesnt exist"

def stock_add():
	item = st_item.get()
	cursor.execute("SELECT COUNT(*) from inventory WHERE item_code = '" +item['item_name']+"' ")
	result = cursor.fetchone()
	if int(result[0]) > 0:
		item_name = get_item_name(cursor, item['item_name'])
		cursor.execute("SELECT COUNT(*) from stock WHERE item_name = ? and quantity = ? and date = ?",
				(item_name, item['quantity'], item['date']))
		result = cursor.fetchone()

		st_item.err_msg["text"] = ""
		if int(result[0]) > 0:
			st_item.err_msg["text"] = "Error: The entry already exists"
		else:
			cursor.execute("INSERT INTO stock(item_name, quantity, date) VALUES(?,?,?)", 
					(item_name, item['quantity'], item['date']))
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
		cursor.execute("ALTER TABLE stock RENAME TO temptable")
		cursor.execute(""" CREATE TABLE stock(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL) """);
		cursor.execute("""INSERT INTO stock (item_name, quantity, date) SELECT item_name, quantity, date FROM temptable ORDER BY id;""") 
		cursor.execute("DROP TABLE temptable;")
		conn.commit()
		st_item.err_msg["text"] = "Success: Deleted the entry"
	else:
		st_item.err_msg["text"] = "Entry doesnt exist"

def create_db_backup():
	global conn
	global cursor
	conn.close()
	os.system("copy sm.db backup_sm.db")
	conn = sqlite3.connect("sm.db")
	cursor = conn.cursor()

def restore_db():
	global conn
	global cursor
	conn.close()
	if(os.path.exists("backup_sm.db")):
		os.system("copy backup_sm.db sm.db")
		restore_err_msg = "Success: Restored backup"
	else:
		restore_err_msg = "Error: Backup file is not found"
	conn = sqlite3.connect("sm.db")
	cursor = conn.cursor()

def load_view_frame():
	global cur_view
	clear_widgets(inventory_frame)
	clear_widgets(purchase_frame)
	clear_widgets(sale_frame)
	clear_widgets(return_frame)
	clear_widgets(stock_frame)
	clear_widgets(avail_stock_frame)
	clear_widgets(backup_frame)
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
	elif cur_view == "Available_stock":
		tk.Button(view_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_avail_stock_frame()).pack(pady=20)

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
		tk.Label(view_frame, text="Old Stock List", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)
	elif cur_view == "Available_stock":
		tk.Label(view_frame, text="Available Stock", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	scrolly = tk.Scrollbar(view_frame,orient=tk.VERTICAL)
	scrollx = tk.Scrollbar(view_frame,orient=tk.HORIZONTAL)
	if cur_view == "Inventory":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "date", "item_name", "item_code", "units","price", "tax"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Purchase":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","company"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Sale":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","to","from","invoice","vehicle","remarks"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Return":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date","to","from"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Stock":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name","quantity","date"),
				         xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
	elif cur_view == "Available_stock":
		CourseTable=ttk.Treeview(view_frame,columns=("id", "item_name", "item_code", "quantity", "price"),
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
		CourseTable.heading("date",text="Date")
		CourseTable.heading("item_code",text="Item Code")
		CourseTable.heading("units",text="Units")
		CourseTable.heading("price",text="Price")
		CourseTable.heading("tax",text="Tax(%)")
		CourseTable.column("date",width=100)
		CourseTable.column("item_code",width=100)
		CourseTable.column("units",width=100)
		CourseTable.column("price",width=100)
		CourseTable.column("tax",width=100)
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
		CourseTable.heading("to",text="To")
		CourseTable.heading("from",text="From")
		CourseTable.heading("invoice",text="Invoice")
		CourseTable.heading("vehicle",text="Vehicle")
		CourseTable.heading("remarks",text="Remarks")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
		CourseTable.column("to",width=100)
		CourseTable.column("from",width=100)
		CourseTable.column("invoice",width=100)
		CourseTable.column("vehicle",width=100)
		CourseTable.column("remarks",width=100)
	elif cur_view == "Return":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.heading("to",text="To")
		CourseTable.heading("from",text="From")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
		CourseTable.column("to",width=100)
		CourseTable.column("from",width=100)
	elif cur_view == "Stock":
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("date",text="Date")
		CourseTable.column("quantity",width=100)
		CourseTable.column("date",width=100)
	elif cur_view == "Available_stock":
		CourseTable.heading("item_code",text="Item Code")
		CourseTable.heading("quantity",text="Quantity")
		CourseTable.heading("price",text="Price")
		CourseTable.column("item_code",width=100)
		CourseTable.column("quantity",width=100)
		CourseTable.column("price",width=100)
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

	if cur_view == "Available_stock":
		rows = compute_available_stock()
	else:
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

	date_label = tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin)
	item_name_label = tk.Label(cur_frame, font=label_font, text="Item Name").place(x=label_x_margin, y=label_y_margin+1*label_y_gap)
	units_label = tk.Label(cur_frame, font=label_font, text="Units").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	price_label = tk.Label(cur_frame, font=label_font, text="Price").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tax_label = tk.Label(cur_frame, font=label_font, text="Tax").place(x=label_x_margin, y=label_y_margin+4*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.date, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=inv_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.units, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.price, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.tax, width=30).place(x=entry_x_margin, y=label_y_margin+4*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	inv_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:inventory_add()).place(x=label_x_margin, y= label_y_margin+6*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:inventory_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+6*label_y_gap)
	tk.Entry(cur_frame, textvariable=inv_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+6*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+8*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+8*label_y_gap)

def load_purchase_frame():
	global cur_view
	cur_view = "Purchase"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = purchase_frame
	cur_frame.tkraise()

	cursor.execute("SELECT * from inventory")
	result = cursor.fetchall()
	items = [r[1] for r in result] # item_name

	# create a frame widget
	#logo_img = ImageTk.PhotoImage(file="logo1.png")
	#logo_widget = tk.Label(cur_frame, image=logo_img)
	#logo_widget.image = logo_img
	#logo_widget.pack(pady=20)

	# cur_frame widgets
	tk.Label(cur_frame, text="Purchase", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Code").place(x=label_x_margin, y=label_y_margin)
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

	tk.Label(cur_frame, font=label_font, text="Item Code").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="To").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="From").place(x=label_x_margin, y=label_y_margin+4*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Invoice").place(x=label_x_margin, y=label_y_margin+5*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Vehicle").place(x=label_x_margin, y=label_y_margin+6*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Remarks").place(x=label_x_margin, y=label_y_margin+7*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=sl_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.to, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.frm, width=30).place(x=entry_x_margin, y=label_y_margin+4*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.invoice, width=30).place(x=entry_x_margin, y=label_y_margin+5*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.vehicle, width=30).place(x=entry_x_margin, y=label_y_margin+6*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.remarks, width=30).place(x=entry_x_margin, y=label_y_margin+7*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	sl_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:sale_add()).place(x=label_x_margin, y= label_y_margin+8*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:sale_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+8*label_y_gap)
	tk.Entry(cur_frame, textvariable=sl_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+8*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+10*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+10*label_y_gap)

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

	tk.Label(cur_frame, font=label_font, text="Item Code").place(x=label_x_margin, y=label_y_margin)
	tk.Label(cur_frame, font=label_font, text="Quantity").place(x=label_x_margin, y=label_y_margin+label_y_gap)
	tk.Label(cur_frame, font=label_font, text="Date").place(x=label_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="To").place(x=label_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Label(cur_frame, font=label_font, text="From").place(x=label_x_margin, y=label_y_margin+4*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.item_name, width=30).place(x=entry_x_margin, y=label_y_margin)
	tk.Entry(cur_frame, textvariable=ret_item.quantity, width=30).place(x=entry_x_margin, y=label_y_margin+1*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.date, width=30).place(x=entry_x_margin, y=label_y_margin+2*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.to, width=30).place(x=entry_x_margin, y=label_y_margin+3*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.frm, width=30).place(x=entry_x_margin, y=label_y_margin+4*label_y_gap)
	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	ret_item.err_msg = error
	
	# Add button widget
	tk.Button(cur_frame, text="Add", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:return_add()).place(x=label_x_margin, y= label_y_margin+6*label_y_gap)
	# Delete button widget
	tk.Button(cur_frame, text="Delete", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:return_delete()).place(x=label_x_margin + 1*button_gap, y= label_y_margin+6*label_y_gap)
	tk.Entry(cur_frame, textvariable=ret_item.id, width=5, font=("TkMenuFont", 16)).place(x=label_x_margin+1*button_gap+90, y=label_y_margin+6*label_y_gap+10)
	# Show button widget
	tk.Button(cur_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin, y= label_y_margin+8*label_y_gap)
	# Back button widget
	tk.Button(cur_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + button_gap, y= label_y_margin+8*label_y_gap)

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
	tk.Label(cur_frame, text="Old Stock", bg=bg_color, fg="white", font=("TkHeadingFont", 20)).pack(pady=20)

	tk.Label(cur_frame, font=label_font, text="Item Code").place(x=label_x_margin, y=label_y_margin)
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

def load_backup_frame():
	global cur_view
	cur_view = "Backup"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
	cur_frame = backup_frame 
	cur_frame.tkraise()

	# backup_frame widgets
	tk.Label(backup_frame, 
		 text="Backup and Restore", 
		 bg=bg_color, 
		 fg="white", 
		 font=("TkHeadingFont", 20)
	).pack(pady=25)

	error = tk.Message(cur_frame, text="", width=200, bg=bg_color)
	error.place(x = entry_x_margin, y = 70)
	restore_err_msg = error

	# Backup button widget
	tk.Button(backup_frame, text="Backup", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:create_db_backup()).place(x=label_x_margin + 2*button_gap, y= label_y_margin)
	# Restore button widget
	tk.Button(backup_frame, text="Restore", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:restore_db()).place(x=label_x_margin + 2*button_gap, y= label_y_margin+2*label_y_gap)
	# Back button widget
	tk.Button(backup_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + 2*button_gap, y= label_y_margin+4*label_y_gap)

def load_avail_stock_frame():
	global cur_view
	cur_view = "Available_stock"
	clear_widgets(main_frame)
	clear_widgets(view_frame)
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

	# Show button widget
	tk.Button(avail_stock_frame, text="Show", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_view_frame()).place(x=label_x_margin + 2*button_gap, y= label_y_margin)
	# Back button widget
	tk.Button(avail_stock_frame, text="Back", font=("TkMenuFont", 16), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2",
		  activeforeground="black", command=lambda:load_main_frame()).place(x=label_x_margin + 2*button_gap, y= label_y_margin+2*label_y_gap)


def conv_quantity(units, st):
	if units == 'Nos': # int
		return int(st)
	else: # float
		return float(st)

def gen_dict(curs):
	cols = [d[0] for d in curs.description]
	rows=curs.fetchall()
	ret_d = []
	for row in rows:
		ret_d.append(dict(zip(cols, list(row))))
	return ret_d

def sort_dict_arr(c_dict_arr):
	# sort by item_name and date
	items = []
	[items.append(c_dict_arr[i]['item_name']) for i in range(len(c_dict_arr)) if c_dict_arr[i]['item_name'] not in items]
	sorted_dict_arr = []
	for item in items:
		cur_arr = [c_dict_arr[i] for i in range(len(c_dict_arr)) if c_dict_arr[i]['item_name']==item]
		cur_arr = sorted(cur_arr, key=lambda d : d['date'])
		sorted_dict_arr = sorted_dict_arr + cur_arr
	return sorted_dict_arr

def format_date(date):
	d_arr = date.split('/')
	if(len(d_arr[0]) == 4):
		return date
	else:
		d_arr.reverse()
		return '/'.join(d_arr)

def compute_price(qty, date, price_dict):
	# sort price_dict
	date_f = format_date(date)
	price_d = {}
	for d in price_dict:
		price_d[d[1]] = d[0]
	dates = [price_dict[i][1] for i in range(len(price_dict))]
	dates = sorted(dates)
	pick_date = dates[0]
	for d in dates:
		if(date_f < format_date(d)): break
		pick_date = d
	return (qty*price_d[pick_date])


def compute_available_stock():
	# Read inventory and get units and price details
	cursor.execute("select * from inventory")
	inv_dict = gen_dict(cursor)
	stock_init = {}
	stock_cur = {}
	stock_cur_price = {}
	stock_init_date = {}
	price = {}
	tax = {}
	units = {}
	item_code = {}
	qty_t = 0
	for d in inv_dict:
		stock_init[d['item_name']] = 0
		stock_cur[d['item_name']] = 0
		stock_cur_price[d['item_name']] = 0
		stock_init_date[d['item_name']] = '0000/00/00'
		if not d['item_name'] in price:
			price[d['item_name']] = []
		price[d['item_name']].append([float(d['price'])*(1+float(d['tax'])/100), d['date']])
		tax[d['item_name']] = float(d['tax'])
		units[d['item_name']] = d['units']
		item_code[d['item_name']] = d['item_code']
	# Read stock table and get initial stock with dates
	cursor.execute("select * from stock")
	stock_dict = gen_dict(cursor)
	for d in stock_dict:
		stock_init_date[d['item_name']] = format_date(d['date'])
		stock_init[d['item_name']] = conv_quantity(units[d['item_name']], d['quantity'])
		stock_cur[d['item_name']] = stock_init[d['item_name']]
		stock_cur_price[d['item_name']] = compute_price(stock_init[d['item_name']], d['date'], price[d['item_name']])
	# Read purchase table
	cursor.execute("select * from purchase")
	pur_dict = gen_dict(cursor)
	for d in pur_dict:
		if format_date(d['date']) >= stock_init_date[d['item_name']]:
			qty_t = conv_quantity(units[d['item_name']], d['quantity'])
			stock_cur[d['item_name']] = stock_cur[d['item_name']] + qty_t
			stock_cur_price[d['item_name']] = stock_cur_price[d['item_name']] + compute_price(qty_t, d['date'], price[d['item_name']])
	# Read sale table
	cursor.execute("select * from sale")
	sale_dict = gen_dict(cursor)
	for d in sale_dict:
		if format_date(d['date']) >= stock_init_date[d['item_name']]:
			qty_t = conv_quantity(units[d['item_name']], d['quantity'])
			stock_cur[d['item_name']] = stock_cur[d['item_name']] - qty_t
			stock_cur_price[d['item_name']] = stock_cur_price[d['item_name']] - compute_price(qty_t, d['date'], price[d['item_name']])
	# Read return table
	cursor.execute("select * from return")
	ret_dict = gen_dict(cursor)
	for d in ret_dict:
		if format_date(d['date']) >= stock_init_date[d['item_name']]:
			qty_t = conv_quantity(units[d['item_name']], d['quantity'])
			stock_cur[d['item_name']] = stock_cur[d['item_name']] + qty_t
			stock_cur_price[d['item_name']] = stock_cur_price[d['item_name']] + compute_price(qty_t, d['date'], price[d['item_name']])

	# Populate available stock
	cur_stock = []
	id = 1
	total_price = 0
	for item in stock_cur:
		if stock_cur[item]:
			cur_stock.append((id, item, item_code[item], str(stock_cur[item]), "%0.2f"%(compute_price(stock_cur[item], datetime.now().strftime("%d/%m/%Y"), price[item]))))
			id = id + 1
			total_price = total_price + compute_price(stock_cur[item], datetime.now().strftime("%d/%m/%Y"), price[item])
	cur_stock.append((id, 'TOTAL', 'NA', 'NA', "%0.2f"%(total_price)))
	return cur_stock

def write_to_excel_file():
	cursor.execute("select * from inventory")
	inv_dict = gen_dict(cursor)
	price = {}
	units = {}
	item_code = {}
	for d in inv_dict:
		if not d['item_name'] in price:
			price[d['item_name']] = []
		price[d['item_name']].append([float(d['price'])*(1+float(d['tax'])/100), d['date']])
		units[d['item_name']] = d['units']
		item_code[d['item_name']] = d['item_code']
	# Read stock table and get initial stock with dates
	cursor.execute("select * from stock")
	stock_dict = gen_dict(cursor)
	tot_items = len(stock_dict)
	tot_price = 0
	for d in range(tot_items):
		stock_dict[d]['price'] = compute_price(conv_quantity(units[stock_dict[d]['item_name']], stock_dict[d]['quantity']), stock_dict[d]['date'], price[stock_dict[d]['item_name']])
		stock_dict[d]['item_code'] = item_code[stock_dict[d]['item_name']]
		tot_price = tot_price + stock_dict[d]['price']
	stock_dict = sort_dict_arr(stock_dict)
	stock_dict.append({'id':tot_items+1, 'item_name':'TOTAL', 'item_code':'NA', 'quantity':'NA', 'date':'NA', 'price':tot_price})
	# Read purchase table
	cursor.execute("select * from purchase")
	pur_dict = gen_dict(cursor)
	tot_items = len(pur_dict)
	tot_price = 0
	for d in range(tot_items):
		pur_dict[d]['price'] = compute_price(conv_quantity(units[pur_dict[d]['item_name']], pur_dict[d]['quantity']), pur_dict[d]['date'], price[pur_dict[d]['item_name']])
		pur_dict[d]['item_code'] = item_code[pur_dict[d]['item_name']]
		tot_price = tot_price + pur_dict[d]['price']
	pur_dict = sort_dict_arr(pur_dict)
	pur_dict.append({'id':tot_items+1, 'item_name':'TOTAL', 'item_code':'NA', 'quantity':'NA', 'date':'NA', 'company':'NA', 'price':tot_price})
	# Read sale table
	cursor.execute("select * from sale")
	sale_dict = gen_dict(cursor)
	tot_items = len(sale_dict)
	tot_price = 0
	for d in range(tot_items):
		sale_dict[d]['price'] = compute_price(conv_quantity(units[sale_dict[d]['item_name']], sale_dict[d]['quantity']), sale_dict[d]['date'], price[sale_dict[d]['item_name']])
		sale_dict[d]['item_code'] = item_code[sale_dict[d]['item_name']]
		tot_price = tot_price + sale_dict[d]['price']
	sale_dict = sort_dict_arr(sale_dict)
	sale_dict.append({'id':tot_items+1, 'item_name':'TOTAL', 'item_code':'NA', 'quantity':'NA', 'date':'NA', 'to_p':'NA', 'frm':'NA', 'invoice':'NA', 'vehicle':'NA', 'remarks':'NA', 'price':tot_price})
	# Read return table
	cursor.execute("select * from return")
	ret_dict = gen_dict(cursor)
	tot_items = len(ret_dict)
	tot_price = 0
	for d in range(tot_items):
		ret_dict[d]['price'] = compute_price(conv_quantity(units[ret_dict[d]['item_name']], ret_dict[d]['quantity']), ret_dict[d]['date'], price[ret_dict[d]['item_name']])
		ret_dict[d]['item_code'] = item_code[ret_dict[d]['item_name']]
		tot_price = tot_price + ret_dict[d]['price']
	ret_dict = sort_dict_arr(ret_dict)
	ret_dict.append({'id':tot_items+1, 'item_name':'TOTAL', 'item_code':'NA', 'quantity':'NA', 'date':'NA', 'to_p':'NA', 'frm':'NA', 'price':tot_price})

	# Get available stock
	avail_stock_dict = [dict(zip(['id', 'item_name', 'item_code', 'quantity', 'price'], d)) for d in compute_available_stock()]

	xls_name = "Stock_data_%0s.xlsx" % datetime.now().strftime("%d%m%Y_%H%M")
	writer = pd.ExcelWriter(xls_name, engine='xlsxwriter')

	df = pd.DataFrame(inv_dict)
	df.to_excel(writer, sheet_name="Inventory List", index=False)

	df = pd.DataFrame(stock_dict)
	df.to_excel(writer, sheet_name="Old Stock", index=False)

	df = pd.DataFrame(pur_dict)
	df.to_excel(writer, sheet_name="Purchase", index=False)

	df = pd.DataFrame(sale_dict)
	df.to_excel(writer, sheet_name="Sale", index=False)

	df = pd.DataFrame(ret_dict)
	df.to_excel(writer, sheet_name="Return", index=False)

	df = pd.DataFrame(avail_stock_dict)
	df.to_excel(writer, sheet_name="Available Stock", index=False)

	writer.save()



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

backup_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
backup_frame.grid(row=0, column=0, sticky="nesw")

avail_stock_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
avail_stock_frame.grid(row=0, column=0, sticky="nesw")

view_frame = tk.Frame(root, width=500, height=600, bg=bg_color)
view_frame.grid(row=0, column=0, sticky="nesw")

inv_item = inventory_item()
pur_item = purchase_item()
sl_item = sale_item()
ret_item = return_item()
st_item = stock_item()
restore_err_msg = ""

conn =sqlite3.connect("sm.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS inventory(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, date text NOT NULL, item_code text NOT NULL, units text NOT NULL, price text NOT NULL, tax text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS purchase(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, company text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS sale(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, to_p text NOT NULL, frm text NOT NULL, invoice text NOT NULL, vehicle text NOT NULL, remarks text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS return(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL, to_p text NOT NULL, frm text NOT NULL) """);
cursor.execute(""" CREATE TABLE IF NOT EXISTS stock(id integer PRIMARY KEY AUTOINCREMENT, item_name text NOT NULL, quantity text NOT NULL, date text NOT NULL) """);

cur_view = "Inventory"

load_main_frame()

# run app
root.mainloop()
