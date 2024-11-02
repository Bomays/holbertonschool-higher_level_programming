#!/usr/bin/python3

class Robot:
    """represents a robot, with a name"""
    
    # A class variable counting the number of roots
    population = 0
    
    def __init__(self, name):
        """Initialize the data"""
        self.name = name
        print("(Initializing {})".format(self.name))
        
        # when this person is created, the robot adds to the population
        
        Robot.population += 1
        
    def die(self):
        """i am dying"""
        print("{} is being destroyed!".format(self.name))
        
        Robot.population -= 1

        if Robot.population == 0:
        
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))
            
    def say_hi(self):
        print("Greetings, my masters call me {}".format(self.name))
        
        
    @classmethod # same as > how_many = classmethod(how_many)
    def how_many(cls):
        """prints current population"""
        print("We have {:d} robots".format(cls.population))
        
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")                
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them")
droid1.die()
droid2.die()

Robot.how_many()
