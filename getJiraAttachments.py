# Retrieve and store attachments from Jira server
#
# AVOU 06.11.2019 v1
# AVOU 25.06.2020 v2
# AVOU 28.12.2020 v3
#
# This script connects to a jira_server (given the jira_user/jira_password) and retrieves the attachments
# of all the tickets of the defined projects. Attachments are stored in a directory named with the key of the
# ticket.

from jira import JIRA
import os
import configparser

# read properties
config = configparser.ConfigParser()
config.read('jira.properties')

# Get JIRA details and connect to Jira
jira_server = config.get("JiraDetails", "jira_server")
jira_user = config.get("JiraDetails", "jira_user")
jira_password = config.get("JiraDetails", "jira_password")

jira_server = {'server': jira_server}
jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))

# get projects
projects = config.get("ProjectsSection", "projects")
print(projects)

projectsList = projects.split(',')
print(projectsList)
    
# Get path where the folder with the attachments will be placed
path = config.get("PathSection", "path")
print(path)


# Iterate through the projects
for project in projectsList:
    print(project)

    # Iterate through tickets and store their attachments in a directory named as ticket's key number
    try:
        issues_in_proj = jira.search_issues('project='+project, maxResults=250)
    except:
        print("Project does not exist")
        input("Press enter to exit")   
    for issue in issues_in_proj:
        print ('ticket-no=',issue.key)
    
        jira_issue = jira.issue(issue.key, expand="attachment")

        for attachment in jira_issue.fields.attachment :    
            attach = attachment.get()
            jira_filename = attachment.filename    

            # make a dir for the project
            dir = os.path.join(path,project)
            if not os.path.exists(dir):
                os.mkdir(dir)        

            # make a dir for the ticket
            dir = os.path.join(path,project,jira_issue.key)

            if not os.path.exists(dir):
                os.mkdir(dir)

            # store the attachement    
            os.chdir(dir)
            with open(jira_filename, 'wb') as f:        
                f.write(attach)

input("Press enter to exit")

        

