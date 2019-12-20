
import os, sys
print "KIDNUMBER"
print
print "[01] positive    "
print "[02] delete  "
print "[03] multiply "
print "[04] divide  "

print "[00] Exit "
print
A = raw_input("Skip : ")

if A == "1" or A == "01":
  print
  A = input("Number : ")
  B = input("Number : ")

print (A + B)

