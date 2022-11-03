"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730561311"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, another_d: Point) -> float:
        """Returns distance between point's object."""
        d: float = sqrt((self.x - another_d.x)**2 + (self.y - another_d.y)**2)
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates constant movement of dot's location."""
        self.location = self.location.add(self.direction)

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() == True:
            return "gray"
        if self.is_infected() == True:
            return "deep pink"
    
    def contract_disease(self) -> None:
        """Changes if in contact with sick cell to a sick cell, if infected long enough changes to immune."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool: 
        """If dot has never been infected return true for vulnerability to sickness."""   
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """If infected return true for sick."""
        if self.sickness == constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, another: Cell) -> None:
        """When two dots come into contact and one is infected, spread infection to both dots."""
        if Cell.is_infected(self) == True and Cell.is_vulnerable(another) == True or Cell.is_infected(another) == True and Cell.is_vulnerable(self):
            if Cell.is_vulnerable(self) == True:
                Cell.contract_disease(self)
            if Cell.is_vulnerable(another) == True:
                Cell.contract_disease(another)


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    infected_num: int = constants.BEGININF
    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if self.infected_num >= cells or self.infected_num <= 0:
            return ValueError
        for _ in range(Model.infected_num):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cel: Cell = Cell(start_location, start_direction)
            Cell.contract_disease(cel)
            self.population.append(cel)
        for _ in range(Model.infected_num, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population: 
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts(self)
    
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self, another_cell: Cell) -> None:
        """Checks to see if two dots come into contact."""
        a: int = 0
        b: int = 1
        another_cell == self.population[b]
        for index in self.population:
            for dot in index:
                if Point.distance(dot[a], dot[b]) < constants.CELL_RADIUS:
                    Cell.contact_with(self.population[a], another_cell)
            a += 2
            b += 2

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False