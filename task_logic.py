""" The module(Not runnable)  for the Interface class and its methods"""
import tkinter as tk
from typing import Callable

class Interface:
    """
        Summary:
            The interface class for the graphical user interface of the program.
            
        Args:
            root (tkinter): The instance of a tkinter window
            title (str): An optional argument for setting the title of the window
    """
    def __init__(self,
                 root: tk.Tk,
                 title: str | None = None
                ) -> None:
        self.root = root

        #Set the title
        if title is not None:
            self.root.title(title)

        #Set initial window size
        self.root.geometry("300x200")

        self.setup_ui()

    def setup_ui(self) -> None:
        """
            Summary: Set up the user interface
        """
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        title_label = tk.Label(self.root, text="Main Window", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_button("Button 1", 1, 0, self.button1_action)
        self.create_button("Button 2", 1, 1, self.button2_action)

    def create_button(self, text: str, row: int, column: int, command: Callable[[], None]) -> None:
        """
            Summary:
                Create a button with the given parameters
        
            Args:
                text (str): The text to be displayed on the button
                row (int): The row of the button
                column (int): The column of the button
                command (button action/event): The action that will
                                                be performed when a button is clicked
        """
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def button1_action(self) -> None:
        """Action for Button 1"""
        print("Button 1 clicked")

    def button2_action(self) -> None:
        """Action for Button 2"""
        print("Button 2 clicked")

    def run(self) -> None:
        """
            Summary: 
                The method for running the instance of the interface
        """
        self.root.mainloop()

    def factorial(self, number: int) -> int:
        """
        Summary:
            The method for finding the factorial of a given number.

        Args:
            number (int): The number to calculate the factorial of

        Returns:
            int: The result of the n! formula
        """
        pass

    def is_prime(self, number: int) -> bool:
        """
        Summary:
            The method for checking whether a given number is prime.

        Args:
            number (int): The number to check for primality

        Returns:
            bool: True if the number is prime, otherwise false
        """
        pass
