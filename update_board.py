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