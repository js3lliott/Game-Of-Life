# For the board we need:
# - To define the rows and columns to set the size (constructor will handle this)
# - A method to draw the board
# - A method to check all the neighbours of all the cells
# - A method which updates the board based on the neighbour statuses

from cell import Cell
from random import randint

class Board:

    def __init__(self, rows, columns):
        """
        Initialize the vairables to hold the values of the rows and columns
        as well as the grid that will be used to display the statuses
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]

        self.generate_board()

    def draw_board(self):
        print('\n'*10)
        print('Printing board...')

        for row in self.grid:
            for column in row:
                print(column.get_print_character(), end='')
            print()

    def generate_board(self):
        for row in self.grid:
            for column in row:
                # There is a 33% chance the cells spawn alive
                chance_number = randint(0, 2)
                if chance_number == 1:
                    column.set_alive()

    def update_board(self):
        print('Updating board...')
        # Cells list for living cells to kill and cells to resurrect or keep alive

        goes_alive = []
        gets_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):

                # Check neighbour square
                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # Check live status for neighbour_cell
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self.grid[row][column]
                status_main_cell = cell_object.is_alive()

                # If the cell is alive, check the neighbour status
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # Set cell statuses
        for cell_items in goes_alive:
            cell_items.is_alive()
            
        for cell_items in gets_killed:
            cell_items.set_dead()


    def check_neighbour(self, check_row, check_column):
        # How deep the search is
        search_min = -1
        search_max = 2

        # Empty list to append neighbours into
        neighbour_list = []

        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column
                
                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_column:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self.rows:
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self.columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])

        return neighbour_list