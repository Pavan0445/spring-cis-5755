Lab: Source Code Management with Github

----------------------------------------------------
Github and Cloud9 setup using Personal Access Token:
----------------------------------------------------- 
1. Login Github and Create a repository
2. get familiar with account profile --> settings -->Developer Settings -->Personal Access Tokens 
3. Click "Generate New Token" 
   a. Provide a Note such as "CIS5755"
   b. Select Expiration Date
   c. Select scopes
4. Click "Generate token", copy and paste the token in a temporary place
5. Create a new cloud9 environment
6. Delete the README.md file
7. git config --global credential.helper store
8. Go to Github and copy the repository URL
8. Go to Cloud9 terminal and clone the repository
  a. Type: git clone + repository URL
  b. enter your github username
  c. Copy and paste teh token for password
9. Change directory to the new folder
10. Create a project directory (e.g. mkdir Chapter-1)
11. Change to the new directory
12. Create python envionrment: python3 -m venv env
13. To activate the envionrment: source env/bin/activate
14. Create a python file named ex1-print.py
15. Edit the python file
  a. Open the file
  b. Enter a line of code
  c. Run the file
16. While keeping the current terminal window for project,  open a new terminal for git to manage the source code) 

18. git add --all
19. git status
20. git commit -m "first python code"
21. git push
  a. github username:
  b. password: copy and paste the account access token
22. check the changes by using: git log
23. Go to Github repository to check the changes
24. Go to Cloud9 and create a second python file: ex2-flask.py
25. Edit the file by copy/paste the basic Flask code
26. Save and Run the file
27. In the terminal, install Flask package (library): python3 -m pip install flask
28. In the terminal, run the file: python3 ex2-flask.py
29. To view the app, go to Tools menu, select Preview --> Preview Running App
30. To stop the service, press Ctrl + C
31. In the git terminal, enter command step 17-21
   a. change commit comment to "First Flask example"

30. Create an instruction markdown file for Chapter 1
   a. Edit the file by copy/paste this lab instructions
   b. Add basic markdown styles
   c. Save the file
31. In the git terminal, enter command step 17-21
   a. change commit comment to "First Instruction File"


---------------------------------------------
Github and Cloud9 setup using SSH
-------------------------------------------
1. Login Github and Create a repository
2. get familiar with account profile --> settings 
3. Create a new cloud9 environment
4. Delete the README.md file
5. Create ssh key for git to clone the project
ssh-keygen -t rsa
6. Display the public key using cat command
7. Copy the public key
8. Go to github account settings --> SSH and GPG keys --> New SSH key 
9. Paste the public key and enter a title
10. Click "Add SSH key"
11. Copy the repository URL
12. Go to Cloud9 terminal and clone the repository
  a. Type: git clone + repository URL
  b. Yes

13. Change directory to the new folder
14. Create a project directory (e.g. mkdir Chapter-1)
15. Change to the new directory
16. Create python envionrment: python3 -m venv env
17. activate the envionrment: source env/bin/activate
18. Create a python file named ex1-print.py
19. Edit the python file
  a. Open the file
  b. Enter a line of code
  c. Run the file
19. While keeping the current terminal window for project,  open a new terminal for git to manage the source code) 
20. git add --all
21. git status
22. git commit -m "first python code"
23. git push
  a. github username:
  b. password: copy and paste the account access token

24. check the changes by using: git log
25. Go to Github repository to check the changes

-----------------------------------------------------------------

Basic Flask Code

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'Hello World'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)



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