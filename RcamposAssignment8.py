# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:24:20 2022

@author: ronal
"""

class University:
def __init__(self, university_name, location, undergraduate_students, graduate_students):
self.university_name = university_name
self.location = location
self.undergraduate_students = undergraduate_students
self.graduate_students = graduate_students

def print_university_size(self):
total = self.undergraduate_students + self.graduate_students
print('University Size:',total)

def is_undergraduate_greater(self):
if self.undergraduate_students > self.graduate_students:
print('There are more undergraduate students than graduate students')
else:
print('There are more graduate students than undergraduate students')

SPU = University('Sardar Patel University', 'Gujarath', 3536, 2562)
SPU.print_university_size()
SPU.is_undergraduate_greater()