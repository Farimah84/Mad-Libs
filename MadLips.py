"""
Description: This program generates a Mad Libs story by asking the user for various inputs such as adjectives, nouns, and verbs.
Author: Farimah Nourpanah
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s s ruled the world."
print "Mad Libs has started"
#Asking the user name
name = raw_input("Enter a name: ")
#Asking user for three adjective
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter a second adjective: ")
adj3 = raw_input("Enter a third adjective: ")
#Asking user for a verb
verb = raw_input("Enter a verb: ")
#Asking for two nouns
noun1 = raw_input("Enter an noun: ")
noun2 = raw_input("Enter a second noun: ")

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

#printing the final text
print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
