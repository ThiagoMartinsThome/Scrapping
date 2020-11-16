Git commands:

- git init: initialize a repository

- git status: see the status of our repository (files added to staging area, files commited...)

- git add <file_name> or git add . (add all files) : add files to the staging area

- git rm --cached <file_name>: unstage file

- git commit -m "message": to commit

- git log: see the commit history full version

- git log --oneline: see the commit history condensed

- git checkout <unique_number>: checkout commit

- git revert <unique_number>: revert commit (wq to leave the screen)

- git reset <unique_number>: reset commit (don't erase the lines on the editor)

- git reset <unique_number> --hard: reset commit (erase the lines on the editor)

- git branch <name>: create a branch

- git branch -a: list all branches

- git checkout <branch_name>: switch to another branch

- git branch -D: delete a branch

- git checkout -b <branch_name>: switch from branch and create a new one

- git merge <branch_name>: to merge branches. First ensure we are on the branch to be merged

- ssh-keygen -t rsa -C 'tthome3@hotmail.com'. Generate a private and public key to share with others collaborators

- git remote add origin <githubRepositoryUrl>. To add the repository to our project
