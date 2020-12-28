# Jira Ticket Attachments
Extracts attachments from Jira tickets

This script connects to a jira server and retrieves the attachments of all the tickets of the defined projects. Attachments are stored in a directory named with the key of the
ticket. E.g. for a project ABC, all the attachments from the ABC tickets will be downloaded under ABC/ABC-X where X is the number of the ticket.

## Setup (using the source code)
The script is written in python 3. To execute the script follow the steps below:
* Update the jira.properties file with the Jira server, credentials, path to store the attachments and the Jira projects
* Install python 3
* Install Jira library: `pip install Jira`
* Execute getJiraAttachments.py file

## Run executable file 
You may use directly the executable file for Windows 10. You will need to just update the jira.properties file:
* Place the executable file and jira.properties under the same directory
* Update the jira.properties file with the Jira server, credentials, path to store the attachments and the Jira projects
* Execute the getJiraAttachments.exe file

[Buy me a coffee! ☕](https://www.buymeacoffee.com/avoupavou)
