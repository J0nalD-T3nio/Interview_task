""" The main script(Runnable) for the assessment """
import tkinter as tk
from typing import TypeAlias
from task_logic import Interface

def main() -> None:
    """
        Summary:
            The main instance of using the Interface class.
    """
    Gui: TypeAlias = Interface
    root = tk.Tk()
    window: Gui = Interface(root,
                            window_title="User Interface",
                            main_title="Technical Assessment",
                            button1_text="Factorial",
                            button2_text="Prime Check"
                            )

    window.run()

if __name__ == "__main__":
    main()
