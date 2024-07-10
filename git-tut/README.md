# Git Crash Course

## Introduction to Git
Git is a distributed version control system used for tracking changes in source code during software development. It allows multiple developers to collaborate on a project efficiently.

## Installation
To install Git on your machine, follow these steps:
- **Windows**: Download the installer from the [official Git website](https://git-scm.com/) and follow the installation instructions.
- **macOS**: You can install Git using Homebrew by running `brew install git` in the terminal.
- **Linux**: Use your distribution's package manager to install Git. For example, on Ubuntu, you can run `sudo apt-get install git`.

## Configuration
After installing Git, configure your name and email address using the following commands:
```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Initializing a Repository
To start tracking changes in a project, navigate to its directory in the terminal and initialize a Git repository using the command:
```sh
git init
```

## Basic Workflow
The basic workflow in Git involves three main steps:
- **Adding Files**: Add files to the staging area using `git add <file>`.
- **Committing Changes**: Commit changes to the repository with a message using `git commit -m "Commit message"`.
- **Viewing Changes**: Check the status of your repository and view commit history using `git status` and `git log`.

## Branching and Merging
Git allows you to create branches to work on new features or fixes independently. You can switch between branches and merge changes using commands like `git branch`, `git checkout`, and `git merge`.

## Remote Repositories
You can link your local repository to a remote repository (e.g., GitHub) and push your changes using commands like `git remote add origin <remote-url>` and `git push -u origin <branch-name>`.

## Collaboration
Collaborating with others in Git involves actions like cloning repositories, forking repositories, and creating pull requests. These actions enable seamless collaboration and code review.

## Undoing Changes
If you need to undo changes in Git, you can discard changes in the working directory or reset the repository to a previous commit using commands like `git checkout -- <file>` and `git reset --hard <commit-hash>`.

## Conclusion
This crash course covers the essential concepts of Git version control. By mastering these fundamentals, you'll be well-equipped to manage your projects effectively with Git.

## Resources
For further learning and reference, check out the official [Git documentation](https://git-scm.com/doc).
