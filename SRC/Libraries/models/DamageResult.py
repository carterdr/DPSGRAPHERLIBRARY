import numpy as np
from Libraries.utils.Excel import print_to_sheet
from Libraries.utils.config import print_when_adding
from Libraries.database import Database

class DamageResult():
    """
    Represents a damage over time result across the simulation timeline.

    Attributes:
        name (str): The name of the source (e.g., weapon/ability name).
        dot (np.ndarray): An array representing damage dealt at each 0.1-second interval (length 1001).
        last_time (float): The last time (in seconds) that damage was recorded.
        category (str): Optional category label for grouping (e.g., "primary", "mw").

    Methods:
        add(other): Adds another DamageResult to this one, sets the last_time to the higher one, and changes the category to "mw".
        __add__(other): Similar to add() but returns a new damage result object.
        __str__(): Returns a human-readable string representation.
        save(): Saves this result to the database with its current category.
    """
    def __init__(self, name = "", dot = None, last_time = 0, category = None):
        """
        Initializes a DamageResult object.

        Args:
            name (str): Name of the source of damage.
            dot (np.ndarray): Optional custom damage over time array (length 1001).
            last_time (float): Timestamp of the last damage applied.
            category (str): Optional category for database tagging.
        """
        self.name = name
        self.dot = dot if dot is not None else np.zeros(1001, dtype=int)
        self.last_time = last_time
        self.category = category
    def add(self, second):
        """
        Adds another DamageResult into this one (modifies in place).

        Args:
            second (DamageResult): Another damage result to add.

        Returns:
            DamageResult: The modified current instance.
        """
        if second.name != "":
            if self.name == "":
                self.name = second.name
            else:
                self.name += " + " + second.name
        self.dot += second.dot
        if second.last_time > self.last_time:
            self.last_time = second.last_time
        if self.category != None:
            self.category = "mw"
        if print_when_adding:
            print_to_sheet(self)
        return self
    def __str__(self):
        return f"name: {self.name}\nlast time:{self.last_time}\ndot:{self.dot}\ncategory:{self.category}"
    def __add__(self, second):
        """
        Combines two DamageResult objects and returns a new one.

        Args:
            second (DamageResult): The other damage result to combine.

        Returns:
            DamageResult: A new instance with combined damage.
        """
        if second.name != "":
            if self.name == "":
                name = second.name
            else:
                name = self.name + " + " + second.name
        else:
            name = self.name
        if second.last_time > self.last_time:
            last_time = second.last_time
        if self.category != None:
            category = "mw"
        output = DamageResult(dot = self.dot + second.dot, last_time = last_time, name = name, category= category)
        if print_when_adding:
            print_to_sheet(output)
        return output
    def save(self, custom_name=None, custom_category=None):
        """
        Saves this DamageResult to the database using the current category or a custom name and category.
        Args:
            custom_name (str): New name for this result.
            custom_category (str): New category label.
        """
        category = custom_category if custom_category else self.category
        if custom_name:
            self.name = custom_name
        Database.save_to_database(self, category)
