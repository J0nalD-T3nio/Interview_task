""" The main script(Runnable) for the assessment"""
import tkinter as tk
from typing import TypeAlias
from task_logic import Interface

def main() -> None:
    """
        Summary:
            The main instance of using the Interface class
    """
    Gui: TypeAlias = Interface
    root = tk.Tk()
    window: Gui = Interface(root,title="User Interface")

    window.run()

if __name__ == "__main__":
    main()
