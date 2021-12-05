Group lab work for code management

Group Information:
1 Sandeep Mantripragada
2 Jyothi Sai Venkata Durga Pavan Kumar Menedi
GITHUB URL:
https://github.com/Pavan0445/spring-cis-5755.git
Group work:
Jyothi Sai Venkata Durga Pavan Kumar had done first python project and word document. (One hour)
Sandeep has done second python project and readme file. (One hour)
Project Introduction:
We had created a project that synchronises the files from GitHub to cloud9 and cloud9 to GitHub. We have created two python files and one readme file in cloud9 and we synchronise the information into GitHub.
Major Steps:
1.Create a stack in aws then create repository in GitHub and create a new environment in aws cloud9.
2.Create SSH key for git to clone the project.
3. Create SSH key for git to clone the project
4. Display the public key using cat command
5. Copy the public key
6. Go to GitHub account settings --> SSH and GPG keys --> New SSH key 
7. Paste the public key and enter a title
8. Click "Add SSH key"
9. Copy the repository URL
10. Go to Cloud9 terminal and clone the repository
  a. Type: git clone + repository URL
  b. Yes

11. Change directory to the new folder
12. Create a project directory (e.g., mkdir Chapter-1)
13. Change to the new directory
14. Create python environment: python3 -m venv env
15. activate the environment: source env/bin/activate
16. Create a python file named ex1-print.py
17. Edit the python file
  a. Open the file
  b. Enter a line of code
  c. Run the file
18. While keeping the current terminal window for project, open a new terminal for git to manage the source code) 
19. git add --all
20. git status
21. git commit -m "first python code"
22. git push
  a. GitHub username.
  b. password: copy and paste the account access token