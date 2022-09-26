from struct import pack
from tkinter import *
from tkinter import ttk

from itemList import ItemList

class AppAutoInstaller:
	def __init__(self, root: Tk) -> None:
		root.title("App Auto Installer")
		root.minsize(700, 700)
		root.option_add('*tearOff', False)

		menubar = Menu(root)
		root.config(menu = menubar)
		file = Menu(menubar)
		edit = Menu(menubar)
		help_ = Menu(menubar)
		menubar.add_cascade(menu = file, label = "File")
		menubar.add_cascade(menu = edit, label = "Edit")
		menubar.add_cascade(menu = help_, label = "Help")
		file.add_command(label = "Import")
		file.add_command(label = "Export")

		itemsFrame = ttk.Frame(root)
		ttk.Label(itemsFrame, text="Programs to install:").grid(row=0,column=0, sticky="nw")
		myList = ItemList(itemsFrame, ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20", "s21", "s22", "s23", "s24"])
		myList.grid(row=1, column=0)
		itemsFrame.grid(row=0,column=0, sticky="nw")

		packageManagerFrame = ttk.Frame(root)
		ttk.Label(packageManagerFrame, text="Package manager:").grid(row=0, column=0, sticky="nw")
		packageManagerOptions = [
			"winget",
			"scoop",
			"apt-get"
		]
		dropdownSelection = StringVar()
		dropdownSelection.set(packageManagerOptions[0])
		dropdown = ttk.OptionMenu(packageManagerFrame, dropdownSelection, *packageManagerOptions)
		dropdown.grid(row=1, column=0, sticky="nw")
		installButton = ttk.Button(packageManagerFrame, text="Install selected packages")
		installButton.grid(row=2, column=0, sticky="nw")
		packageManagerFrame.grid(row=0, column=1, sticky="nw")
		
		itemButtonsFrame = ttk.Frame(root)
		importButton = ttk.Button(itemButtonsFrame, text="Import")
		exportButton = ttk.Button(itemButtonsFrame, text="Export")
		importButton.grid(row=0, column=0)
		exportButton.grid(row=0, column=1)
		itemButtonsFrame.grid(row=1, column=0, sticky="nw")

def main() -> None:
	root = Tk()
	AppAutoInstaller(root)
	root.mainloop()

if __name__ == "__main__":
	main()