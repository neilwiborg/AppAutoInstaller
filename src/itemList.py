from tkinter import *
from tkinter import ttk

from typing import List

class ItemList:
	def __init__(self, root, items: List[str]) -> None:
		self.frame = ttk.Frame(root)
		for item in items:
			listItem = ttk.Checkbutton(self.frame, text=item)
			listItem.pack(side=TOP)

	def pack(self) -> None:
		self.frame.pack()