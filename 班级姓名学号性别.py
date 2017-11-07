#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class student:
   '所有员工的基类'
   stu_count = 0
   stu_count_wl163 = 0
   stu_count_wl162 = 0
  
 
   def __init__(self,name,stu_number,stu_class,gender):
      self.name = name
      self.stu_number= stu_number
      self.stu_class= stu_class
      self.gender= gender
      student.stu_Count += 1
      if self.stu_class=="wl163":
         student.stu_count_wl163+=1
      elif self.stu_class=="wl162":
              student.stu_count_wl162+=1
            

            
   def displaycount(self):
     print "Total student %d", student.stu_count
 
   def displayCount(self):
      print "Name :   ",self.name,"stu_number:   ",self.stu_number,"stu_class:   ",stu_class,"gender:   ",self.gender
