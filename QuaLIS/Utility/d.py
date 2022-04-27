import os
def projectDirectory():

    projectDirectory=""

    fileDirectory=os.path.abspath(__file__)

    fileDirectoryArray=fileDirectory.split("\\")

    for i in fileDirectoryArray:

        projectDirectory=projectDirectory+"\\"+i
        if i=="QuaLIS":
             break

    print(projectDirectory)

    projectDirectory=projectDirectory[1:]

    print(projectDirectory)

    return projectDirectory

projectDirectory()