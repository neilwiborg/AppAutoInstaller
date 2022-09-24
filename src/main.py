from tkinter import *
from tkinter import ttk

from itemList import ItemList

class AppAutoInstaller:
	def __init__(self, root) -> None:
		root.title("App Auto Installer")
		root.minsize(700, 700)
		myList = ItemList(root, ["s1", "s2", "s3"])
		myList.pack()


def main() -> None:
	root = Tk()
	AppAutoInstaller(root)
	root.mainloop()

if __name__ == "__main__":
	main()