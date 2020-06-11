# Rules:
# If a cell is alive it will: 
# - Die if there are less than two living neighbours
# - Continue living if there are exactly two or three living neighbours
# - Die if there are more than three living neighbours
# 
# If a cell is dead it will:
# - Resurrect if there are exactly three living neighbours 


# All cells will be dead initially. We will randomly generate the dead or alive status for the first
# generation. For the next generation the rules above apply.
# We need the ability to check whether ther cell is alive and we wil create a method funciton to tell
# the board what to print depending on the cell status.

class Cell:

    def __init__(self):
        """
        Class holding init status of cell (dead).
        Ability to set and fetch new statuses with other functions
        """
        self.status = 'Dead'

    def set_dead(self):
        """
        Method sets the cell status to Dead.
        """
        self.status = 'Dead'
        
    def set_alive(self):
        """
        Method to set status to Alive.
        """
        self.status = 'Alive'

    def is_alive(self):
        """
        Checks whether the cell is Alive.
        Returns True if it is, returns False if it is not.
        """
        if self.status == 'Alive':
            return True
        return False

    def get_print_character(self):
        """
        Method for returning a status character to print to the board.
        """
        if self.is_alive():
            return 'O'
        return '*'