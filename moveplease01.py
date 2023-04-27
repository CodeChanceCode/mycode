#!/usr/bin/env python3

#library imports
import shutil
import os

def main():
    
    #change into this directory
    os.chdir('/home/student/mycode/')
    
    #move raynor.obj into a new directory
    shutil.move('raynor.obj', 'ceph_storage/')

    #input for new name
    xname = input('What is the new name for kerrigan.obj? ')

    #moving kerrigan.obj to new directory with the new name input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

