# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:49:06 2016

@author: marco
"""

'''
Programmer: Marco Arceo
Class: CptS 111-01, Fall 2016
Programming Assignment #8
12/12/16

Description: "Carpet Fishing"
'''

import random
import time

class Coordinate:
    '''
    Gathers coordinates from the user
    '''
    def __init__(self, row, col):
        '''
        '''
        self.row = row
        self.col = col
        
    def __str__(self):
        '''
        '''
        return ("(row: %d, col: %d)" %(self.row, self.col))
        
        
class Cell:
    '''
    Adds inputs to the cells of the grid
    '''
    def __init__(self, row, col,):
        '''
        '''
        self.location_coords = Coordinate(row, col)
        self.contains_line = False
        self.fish = " "
        
    def __str__(self):
        '''
        '''
        cell_str = ""
        
        if self.fish != "":
            cell_str += self.fish[0]
        else:
            cell_str += " "
            
        if self.contains_line == True:
            cell_str += "*"
        else:
            cell_str += " "
            
        return cell_str
    
class CarpetSea:
    '''
    Constructs the grid structure and displays it
    '''
    def __init__(self, N):
        '''

        '''
        self.N = N
        self.grid = []
        for i in range(self.N):
            row = []
            for j in range(0, self.N):
                cell = Cell(i, j)
                row.append(cell)
            self.grid.append(row)

        self.available_fish = ["Salmon", "Marlin", "Tuna", "Halibut"]
        
    def __str__(self):
        '''
        Creates the grid display for Carpet Sea
        '''
        curr_cell = " "
        for x in range(self.N):
           curr_cell += str(x)
           curr_cell += "\n--" + "---" * self.N + "\n"
           for j in range(self.N):
                curr_cell += " " + str(j) + "|"
                for i in range(self.N):
                    curr_cell += self.grid[j][i].__str__() + "|"
                curr_cell += "\n--" + "---" * self.N + "\n"

        return curr_cell      
                
    def randomly_place_fish(self):
        '''
        randomly selects coordinates of a cell and randomly selects a fish from the available_fish list attribute. 
        Marks the cell as containing the fish.
        '''
        i = random.choice(list(self.available_fish))
        rand1 = random.randrange(0, self.N)
        rand2 = random.randrange(0, self.N)
        self.grid[rand1][rand2].fish = i
        return rand1, rand2, i
    
    def drop_fishing_line(self, coords):
        '''
        accepts the location of the user's fishing line (a Coordinate object). 
        Marks the cell as containing the line.
        '''
        self.grid[coords.row][coords.col].contains_line = True
        
        
    def check_fish_caught(self, coords, rand1, rand2, i):
        '''
        If the cell containing the fishing line also contains a fish, returns the fish. 
        Otherwise, return False.
        '''

        if rand1 == coords.row and rand2 == coords.col:
            print("Congrats!, (%d, %d) contained a fish! It was a %s!\n" %(coords.row, coords.col, i))
            caught = True
        else:
            print("Sorry! There was no fish at your lines location\n")
            caught = False
        return caught
    
    
class GameStats:
    '''
    Keeps track of the amount of times a fish was caught, how many hours passed, and the total average
    when it comes to amount of fish caught in relation to time
    '''
    def __init__(self, fish_caught, hours, average):
        '''
        
        '''
        self.fish_caught = fish_caught
        self.hours = hours
        self.average = average
        
    def __str__(self):
        '''
        
        '''
        return \
        "%d fish caught in %.2f hours\n" \
        "On avarage, you caught %.2f fish per hour" %(self.fish_caught, self.hours, self.average)
        
def calculate_stats(hours, fish_caught):
    average = fish_caught / hours
    return GameStats(fish_caught, hours, average)
    
    
def validate_menu(cont, stats):
    '''
    Checks to make sure that the user menu option are valid
    '''
    correct = False
    while not correct:
        if cont == "y":
            correct = True
            cont = True
        elif cont == "q":
            correct = False
            cont = False
            print(stats)
            break
        else:
            print("Your menu option is not supported")
            cont = input("Would you like to keep playing? Enter 'y' to play or 'q' to quit: ")
            print("")
    return cont
    
def validate_user_coordinates(row, col, N):
    '''
    Makes sure the user inputed valid coordinates
    '''
    correct = False
    while not correct:
        if (row < N and row >= 0) and (col < N and col >= 0):
            correct = True
        else: 
            print("Your coordinates have to be below %d and equal or greater than 0" %(N))
            line = input("Please enter the coordinate (x,y) of the cell in which you want to drop your line: ")
            x = line.split(' ')
            row = int(x[0])
            col = int(x[1])
    return row, col


def main():
    #display instructions
    print("Welcome to Dilbert's Carpet Fishing Game!")
    print("To play, you will cast your fishing line into a location in the Carpet Sea.")
    print("After a certain amount of time, you will reel in your line and find out if you caught a fish!")
    print("You can keep re-casting and re-reeling until you want to quit.\n")
    print("The fish in Carpet Sea include: \nM: Marlin \nS: Salmon \nT: Tuna \nH: Halibut \n")
    print("Note: One hour (60 minutes) will be simulated as one second.\n\n")
    
    #set timer
    m = 60
    s = m * (1/60)
    
    #Hard code N
    N = 2
    
    #Apply a while loop
    hours = 0
    fish_caught = 0
    
    cont = True
    while cont == True:
        hours += 1
        
        #Gathers row and col
        line = input("Please enter the coordinate (x,y) of the cell in which you want to drop your line: ")
        x = line.split(' ')
        row = int(x[0])
        col = int(x[1])
        print("")
        (row, col) = validate_user_coordinates(row, col, N)
        
        #Sleep timer
        print("*One hour later...*\n")
        time.sleep(s)
        
        #Runs through  Objects
        CarpSea = CarpetSea(N)
        coords = Coordinate(row, col)
        (rand1, rand2, i) = CarpSea.randomly_place_fish()
        CarpSea.drop_fishing_line(coords)
        caught = CarpSea.check_fish_caught(coords, rand1, rand2, i)
        print(CarpSea)
        print("")
        
        #Starts to gather statistic information
        if caught == True:
            fish_caught += 1
        else:
            fish_caught = fish_caught
            
        stats = calculate_stats(hours, fish_caught)
        cont = input("Would you like to keep playing? Enter 'y' to play or 'q' to quit: ")
        print("\n")
        cont = validate_menu(cont, stats)
        
        
main()