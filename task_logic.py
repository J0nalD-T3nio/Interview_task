""" The module(Not runnable)  for the Interface class and its methods """

import math
import tkinter as tk
from tkinter import messagebox
from functools import lru_cache
from typing import Callable
from tooltip import Tooltip

class Interface:
    """
        Summary:
            The interface class for the graphical user interface of the program.
            
        Attributes:
            root (tkinter): The instance of a tkinter window.
            window_title (str or None): An optional argument for setting the title of the .
            main_title (str): The text label of the main window.
                              Default value is Main Window.
            button1_text (str): The text inside the first button.
                                Default value is Button 1.
            button2_text (str): The text inside the second button.
                                Default value is Button 1.
            button1_description (str): Description of button 1's functionality
                                       A default value is present. 
            button2_description (str): Description of button 2's functionality
                                       A default value is present.
    """
    def __init__(self,
                 root: tk.Tk,
                 window_title: str | None = None,
                 main_title: str = "Main Window",
                 button1_text: str = "Button 1",
                 button2_text: str = "Button 2",
                 button1_description: str = "Calculates the factorial of n.",
                 button2_description: str = "Checks if the number is prime."
                 ) -> None:
        self.root: tk.Tk = root
        self.main_title_var: tk.StringVar = tk.StringVar(self.root, main_title)
        self.button1_text_var: tk.StringVar = tk.StringVar(self.root, button1_text)
        self.button2_text_var: tk.StringVar = tk.StringVar(self.root, button2_text)
        self.button1_description: str = button1_description
        self.button2_description: str = button2_description

        if window_title is not None:
            self.root.title(window_title)

        # Set initial window size
        self.root.geometry("300x200")

        # Set initial font size
        self.title_font_size: int = 16
        self.button_font_size: int = 12

        # Setup for the user interface to be dynamic
        self.setup_ui()
        self.root.bind("<Configure>", self.on_resize)


    def setup_ui(self) -> None:
        """
            Summary: Set up the user interface
        """
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.title_label: tk.Label = tk.Label(self.root,
                                    textvariable=self.main_title_var,
                                    font=("Arial", self.title_font_size)
                                    )

        self.title_label.grid(row=0, column=0,
                              columnspan=2, pady=10,
                              sticky="nsew"
                              )

        # Button 1 is for the factorial operation
        self.button1: tk.Button = self.create_button(self.button1_text_var,
                                          1, 0,
                                          self.button1_action,
                                          self.button1_description
                                          )

        # Button 2 is for the Prime checker operation
        self.button2: tk.Button = self.create_button(self.button2_text_var,
                                          1, 1,
                                          self.button2_action,
                                          self.button2_description
                                          )

    def create_button(self, text_var: tk.StringVar,
                      row: int, column: int,
                      command: Callable[[], None],
                      description: str
                      ) -> tk.Button:
        """
            Summary:
                Create a button with the given parameters.
        
            Args:
                text (str): The text to be displayed on the button.
                row (int): The row of the button.
                column (int): The column of the button.
                command (button action/event): The action that will
                                                be performed when a button is clicked.
                description (str): The description to be shown on the tooltip.

            Returns:
                tk.Button: Returns a dynamic and scalable tkinter button widget
        """
        button: tk.Button = tk.Button(self.root,
                           textvariable=text_var,
                           command=command,
                           font=("Arial", self.button_font_size)
                           )

        button.grid(row=row, column=column,
                    padx=10, pady=10,
                    sticky="nsew")

        # Add tooltip to the button
        Tooltip(button, description)

        return button

    def button1_action(self) -> None:
        """
            Summary: 
                Action for Factorial Button
        """
        self.create_input_window("Factorial Calculator", self.calculate_factorial)

    def button2_action(self) -> None:
        """
            Summary: 
                Action for Prime Check Button
        """
        self.create_input_window("Prime Number Checker", self.check_prime)

    def create_input_window(self, title: str, action_function: callable) -> None:
        """
            Summary: 
                Create a new window for input and result display
            
            Args:
                title (str): The title of the window
                action_function (callable): The functionality the window will do
        """
        # Hide the main window
        self.root.withdraw()

        input_window = tk.Toplevel(self.root)
        input_window.title(title)
        input_window.geometry("300x200")
        input_window.protocol("WM_DELETE_WINDOW", lambda: self.close_input_window(input_window))

        label = tk.Label(input_window, text="Enter a number:")
        label.pack(pady=5)

        entry = tk.Entry(input_window)
        entry.insert(0, "Enter number here")
        entry.pack(pady=5)
        entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))

        result_var = tk.StringVar()
        result_label = tk.Label(input_window, textvariable=result_var, wraplength=250)
        result_label.pack(pady=10)

        def process_input():
            try:
                number = int(entry.get())
                result = action_function(number)
                result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer")

        calculate_button = tk.Button(input_window, text="Calculate", command=process_input)
        calculate_button.pack(pady=5)

        entry.bind("<Return>", lambda event: process_input())

    def close_input_window(self, window: tk.Toplevel) -> None:
        """
            Summary:
                Close the input window and show the main window
            
            Args:
                window (tk.Toplevel): The current window that will be closed
        """
        window.destroy()

        # Show the main window
        self.root.deiconify()

    def on_resize(self, event: tk.Event) -> None:
        """
            Summary:
                Adjust font sizes based on window size.
                
            Args:
                event (tk.Event): 
                    represents event that occurs in the GUI,
                    such as a mouse click, key press, or 
                    window resize. This is binded so that
                    when the window resizes the texts also
                    resizes.
        """
        # Adjust title font size
        new_title_size = max(16, min(32, event.width // 20, event.height // 10))
        self.title_label.config(font=("Arial", new_title_size))

        # Adjust button font size
        new_button_size = max(10, min(24, event.width // 30, event.height // 15))
        self.button1.config(font=("Arial", new_button_size))
        self.button2.config(font=("Arial", new_button_size))

    def run(self) -> None:
        """
            Summary: 
                The method for running the instance of the interface.
        """
        self.root.mainloop()

    def calculate_factorial(self, number: int) -> str:
        """
            Summary: 
                Calculate factorial and return result string

            Args:
                number (int): The given number
        """
        try:
            result = Interface.factorial(number)  # Use class name instead of self
            return f"The factorial of {number} is {result}"
        except ValueError as e:
            return str(e)

    def check_prime(self, number: int) -> str:
        """
            Summary: 
                Check if number is prime and return result string

            Args:
                number (int): The given number
        """
        try:
            is_prime = Interface.is_prime(number)  # Use class name instead of self
            prime_status = "a Prime" if is_prime else "Not a Prime"
            return f"{number} is {prime_status} Number"
        except ValueError as e:
            return str(e)

    @staticmethod
    @lru_cache(maxsize=None)
    def factorial(number: int) -> int:
        """
        Summary:
            The method for finding the factorial of a given number.

        Args:
            number (int): The number to calculate the factorial.

        Returns:
            int: The result of the n! formula.
        """
        if number < 0:
            raise ValueError("Factorial only works with none negative numbers")

        if number in (0, 1):
            return 1
        return number * Interface.factorial(number - 1)

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Summary:
            The method for checking whether a given number is prime.

        Args:
            number (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, otherwise false.
        """
        if number < 0:
            raise ValueError(
                "Prime number checking is not traditionaly used in none negative numbers"
                )

        if number in (0, 1):
            return False

        if number in (2, 3):
            return True

        if number%2 == 0 or number%3 == 0:
            return False

        # Check up to the square root of the number
        for i in range(5, int(math.sqrt(number)) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True
