from dataclasses import dataclass
from tkinter import *
from tkinter import ttk

from typing import List

@dataclass
class ListItem:
	box: ttk.Checkbutton
	checked: IntVar

class ItemList(ttk.Frame):
	def __init__(self, root: Tk, names: List[str], *args, **kw) -> None:
		super().__init__(root, *args, **kw)
		canvas = Canvas(self, highlightthickness=0)
		scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
		self.frame = ttk.Frame(canvas)
		self.items: List[ListItem] = []
		
		self.frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

		canvas.create_window((0, 0), window=self.frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.pack(side="left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")
		
		for name in names:
			check: IntVar = IntVar()
			check.set(1)
			listItem: ListItem = ListItem(ttk.Checkbutton(self.frame, text=name, variable=check), check)
			listItem.box.grid(row=len(self.items),column=0, sticky="w")
			self.items.append(listItem)
