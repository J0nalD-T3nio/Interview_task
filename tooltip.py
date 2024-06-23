""" The module(Not runnable) that contains the tooltip class """

import tkinter as tk
from typing import Optional

class Tooltip:
    """
        Summary:
            A class to create a tooltip for a given widget.

            This tooltip appears when the mouse hovers over the widget and
            disappears when the mouse leaves the widget.

        Attributes:
            widget (tk.Widget): The widget to which the tooltip is attached.
            text (str): The text to be displayed in the tooltip.
            tooltip (Optional[tk.Toplevel]): The toplevel window for the tooltip.
    """

    def __init__(self, widget: tk.Widget, text: str) -> None:
        """
            Summary:
                Initialize the Tooltip instance.

            Args:
                widget (tk.Widget): The widget to which the tooltip will be attached.
                text (str): The text to be displayed in the tooltip.
        """
        self.widget: tk.Widget = widget
        self.text: str = text
        self.tooltip: Optional[tk.Toplevel] = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, _: Optional[tk.Event] = None) -> None:
        """
        Summary:    
            Display the tooltip.

            This method is called when the mouse enters the widget.

        Args:
            event (Optional[tk.Event]): The event that triggered the method.
                                        Defaults to None.
        """
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text,
                         background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, _: Optional[tk.Event] = None) -> None:
        """
            Summary:
                Hide the tooltip.

                This method is called when the mouse leaves the widget.

            Args:
                event (Optional[tk.Event]): The event that triggered the method.
                                            Defaults to None.
        """
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
