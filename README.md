# CS Lab Management
This is the description of the project. Maybe getting it to be more than one line would be nice.
## Source for git information
The resource used for the following information on using git was found at https://guides.github.com/introduction/git-handbook/, so please visit that guide if you want a better understanding of using git.
## General git setup
You will want to setup an SSH key for your github account for each of your computers that you use. This makes it easier to authenticate yourself with the remote repository. Be sure to set your global/local username and email to whatever you want to be used on the project. There are two ways to to this, `git config --global` and `git config --local`, local being for the local repository in which you are working. Here is a resource to help with setting up git with github. https://docs.github.com/en/get-started/quickstart/set-up-git
## git commands
- **cloning the project:**  
`git clone git@github.com:CS-LAB-MGMT/CS_LAB_MGMT.git`
- **setting remote repo for push/pull:**  
`git remote add origin git@github.com:CS-LAB-MGMT/CS_LAB_MGMT.git`  
This is only needed for new repositories that you want to connect to a remote server. This was already done. Cloning this project will already have the remote repo set.
- **checking your git configuration:**  
`git config --list`  
See what is your current username and user email and if you have origin set among other things. Read the set-up-git link for how to set these if you don't already have them set.
- **checking out an existing branch:**  
`git checkout <branch>`  
`git checkout main` will switch you to `main` branch  
Where `<branch>` can be `main`, `development`, or `feature123`  
Any development work you do must be on a feature branch that you created after checking out the most up-to-date development branch. For a branching architecture that looks like this:  
->main  
->development  
|  
---->feature_123 (working here)  
For that you will need the next command..
- **creating a new branch:**  
`git checkout -b feature123`  
Creates a new branch named feature123 and checks it out. You can also use `git branch feature123` but this will leave you in the parent branch you were in, which should always be `development` and ideally we don't make our changes to that branch except with through a pull request and merge. More on that later.
- **pushing a local branch to the remote repository:**  
`git push origin feature123`  
This will make your local branch and its commits available on the remote repository. This step is where we will start using the GitHub web interface to create pull requests, review, and finally merge changes into the development branch, and eventually the main branch.
- **pulling latest changes of a branch:**  
`git checkout development`  
`git pull origin development`  
*or*  
`git checkout development`  
`git pull`  
If the upstream is already set. Which you will know because `git pull` won't work. You can also see if it is set with the `git config --list` command.  
This is how you will use this command most often. First you checkout the branch you want to update to the latest remote version. Then you use the `git pull` command to get the latest changes. In 99.9% of cases for this project you will only be pulling updates to the development branch on your local machine. This command will be used to apply the most recent changes to your feature branch using the `merge` command. But be careful to checkout your feature branch and use `git merge development` to bring changes to development INTO your feature branch, and not the other way around. See **merging branches** for more information.
- **adding new or modified files to the repository:**  
`git add file.txt`  
*or*  
`git add file1.txt file2.txt`  
*or*  
`git add .`  
This will add a single file or a list of files to a commit for a branch. This is will occur locally. We will have a .gitignore file where we will specify all the files, file types, and directories that should not be in the repository. This makes it possible to use the more convenient `git add .` command that will add any new or modified files in the directory/sub-directories within your local repo to the commit, except those that meet the specifications within the .gitignore file(s) throughout the project.
- **committing changes to your local branch:**  
`git commit -m "this is the message that tells people what this change IS."`  
This will take all the new and modified files added with `git add` and commit them to the branch.
- **merging branches:**  
`git checkout feature123`  
`git merge development`  
When working on your feature branch or hotfix, things may change upstream on the development branch as other people complete features, submit pull requests, and have them merged to development. When working on a branch, you might want to try something crazy or that is likely to screw up all the hard work you did for branch feature123, so you make a branch off feature123 called feature123_try_quantum_computing. On this branch you test out some idea you had, and if it doesn't work, you can switch back to feature123 and delete the feature123_try_quantum_computing branch. But what if it does work? Then make sure your changes are committed to that branch, checkout feature123, and use the `git merge feature123_try_quantum_computing` command to start the process of merging it back into the feature123 branch. This will compare the two and attempt to merge them automatically, if there are changes to both branches, however, you will need to manually review and decide what to keep from each branch. We will be trying to avoid merging any branch with development without doing a pull request, first, and will generally do the merging within GitHub itself rather than from the command line.


### An example workflow by git commands
Clone once:  
`git clone git@github.com:CS-LAB-MGMT/CS_LAB_MGMT.git`  
`git checkout development`  
`git checkout -b feature123`  
Make some changes.
`git add .`  
`git commit -m "I changed something."`  
Make some more changes.
`git add .`  
`git commit -m "Did more stuff"`  
Decide to try a cool library out.  
`git checkout -b "feature123_libtest"`  
Try out library, go crazy, its horrible! Maybe later.  
`git checkout feature123`  
Finish the feature, and learn more about that cool library. Maybe you can make it work?  
`git add .`  
`git commit -m "Finished feature"`  

