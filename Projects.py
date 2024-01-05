import datetime
import json
# helper functions


# function for project name validation

def namevalidation():
    projectname = input("enter your project name : ").strip().lower()
    while True:
        if projectname.isalpha():
            break
        else:
            print("enter your project name without spaces or digits")
            projectname = input("enter your project name : ").strip().lower()
    return projectname

# function for project description validation

def descvalidation():
    projectdescription = input("enter project decription : ").strip().lower()
    while True:
        if projectdescription.isalpha():
            break
        elif projectdescription == " ":
            print("cannot be empty")
            projectdescription = input(
                "enter project decription : ").strip().lower()
        else:
            print("enter project decription without symbols or number , just use ','")
            projectdescription = input(
                "enter project decription : ").strip().lower()
    return projectdescription

# function for project total target validation

def targetnumvalidation():
    while True:
        target = int(input("please enter your total target : "))
        if target >= 2500:
            break
        else:
            print("please enter target number above 1000")
            target = input("please enter your total target : ")
    return target

# function for project start and end date validation

def datevalidation():
    while True:
        try:
            projectendDate = input("enter project end date in '%d-%m-%y' format : ").split('-')
            projectendDate = datetime.datetime(int(projectendDate[2]), int(projectendDate[1]), int(projectendDate[0]))
            return projectendDate
        except ValueError:
            print("Invalid date format. Please enter a valid date in '%d-%m-%y' format.")
        except IndexError:
            print("Invalid date format. Please enter a valid date in '%d-%m-%y' format.")

# function for project editing fields validation

def fieldvalidation(id, line):
    editedline = []
    fields = ["name", "description",
              "target", "startdate", "enddate"]
    editedfield = input(
        "enter the field name to be edited from [ 'name', 'description','target', 'startdate', 'enddate'] :").strip().lower()
    if editedfield in fields:
        if editedfield == "name":
            projectname = namevalidation()
            line[1] = projectname
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "description":
            projectdescription = descvalidation()
            line[2] = projectdescription
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "target":
            target = str(targetnumvalidation())
            line[3] = target
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "startdate" or editedfield == "enddate":
            projectstartDate = str(datevalidation()[0])
            projectendDate = str(datevalidation()[1])
            line[4] = projectstartDate
            line[7] = projectendDate
            editedline.append(line)
            print("editing field")
            return editedline[0]
    else:
        print("no available field")

# main functions

# function creating a project

# def createproject(id):
#
#     projectname = namevalidation()
#
#     projectdescription = descvalidation()
#
#     target = targetnumvalidation()
#
#     projectstartDate =datetime.datetime.now().strftime("%d-%m-%y")
#
#     projectendDate = datevalidation()
#
#     print("creating project")
#
#     print(
#         f" project name : {projectname} \n project description : {projectdescription} \n project total target : {target} \n project start date : {projectstartDate} \n project end date : {projectendDate} ")
#
#     with open("projects.txt", 'a') as projectsfile:
#         projectsfile.writelines(
#             [f"{id}:{projectname}:{projectdescription}:{target}:{projectstartDate}:{projectendDate} \n"]
#         )

        def createproject(id):
            # ... existing code ...

            project_data = {
                "id": id,
                "name": projectname,
                "description": projectdescription,
                "target": target,
                "start_date": projectstartDate,
                "end_date": projectendDate.strftime("%d-%m-%y")
            }

            try:
                with open("projects.json", 'r+') as file:
                    projects = json.load(file)
                    projects.append(project_data)
                    file.seek(0)
                    json.dump(projects, file)
            except FileNotFoundError:
                with open("projects.json", 'w') as file:
                    json.dump([project_data], file)

            print("Project created successfully")
            # rest of the function...


# function deleteing a project

# def deleteproject(id):
#     while True:
#         projectsfile = open("projects.txt", 'r')
#         restfile = ""
#         projectname = input(
#             "enter your project name to be deleted : ").strip().lower()
#         for line in projectsfile.readlines():
#             if id in line:
#                 if line.split(":")[1] == projectname:
#                     print("deleting project")
#                 else:
#                     restfile += line
#             else:
#                 print("you don't have any projects to be deleted ")
#                 restfile += line
#                 break
#         return restfile
def deleteproject(id):
    try:
        with open("projects.json", 'r') as file:
            projects = json.load(file)

        projectname = input("enter your project name to be deleted: ").strip().lower()
        projects = [project for project in projects if not (project['id'] == id and project['name'] == projectname)]

        with open("projects.json", 'w') as file:
            json.dump(projects, file)

        print("Project deleted successfully.")

    except FileNotFoundError:
        print("No project data found.")

# function viewing projects

# def viewproject():
#     projectsfile = open("projects.txt", 'r')
#     for line in projectsfile:
#         print(line)

def viewproject():
    try:
        with open("projects.json", 'r') as file:
            projects = json.load(file)

        for project in projects:
            print(f"ID: {project['id']}, Name: {project['name']}, Description: {project['description']}, Target: {project['target']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")

    except FileNotFoundError:
        print("No project data found.")

# function edit a project

# def editproject(id):
#     while True:
#         projectsfile = open("projects.txt", 'r')
#         restfile = ""
#         projectname = input(
#             "enter your project name to be edited : ").strip().lower()
#         for line in projectsfile.readlines():
#             if id in line:
#                 if line.split(":")[1] == projectname:
#                     editedline = fieldvalidation(id, line.split(":"))
#                     editedline = ":".join(editedline)
#                     restfile += editedline
#                     #print("editing file")
#                 else:
#                     restfile += line
#             else:
#                 print("you don't have any projects to be edited ")
#                 restfile += line
#         return restfile
def editproject(id):
    try:
        with open("projects.json", 'r') as file:
            projects = json.load(file)

        projectname = input("enter your project name to be edited: ").strip().lower()
        for project in projects:
            if project['id'] == id and project
                if ['name'] == projectname:
                editedline = fieldvalidation(id, [project['name'], project['description'], project['target'], project['start_date'], project['end_date']])
                project.update({
                    "name": editedline[0],
                    "description": editedline[1],
                    "target": editedline[2],
                    "start_date": editedline[3],
                    "end_date": editedline[4]
                })
                print("Project edited successfully.")
                break

        with open("projects.json", 'w') as file:
            json.dump(projects, file)

    except FileNotFoundError:
        print("No project data found.")

# function to handle all the above

def projects(id):
    while True:
        choice = int(input(
            "for create projects enter 1       \n       for edit projects enter 2    \n      for delete projects enter 3     \n      for view projects enter 4     \n      for exit 5  : "))
        try:
            choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5
        except:
            print("something went wrong")
        else:
            if choice == 1:
                try:
                    createproject(id)
                except:
                    print("something went wrong")
            elif choice == 2:
                try:
                    edit = editproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(edit)
            elif choice == 3:
                try:
                    delete = deleteproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(delete)
            elif choice == 4:
                print("viewing projects")
                try:
                    viewproject()
                except:
                    print("something went wrong")
            elif choice == 5:
                print("ok bye bye , hope to see you soon")
                break
            else:
                print("invalid choice")