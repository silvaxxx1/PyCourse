
# 🚀 Lesson 4 — **Introduction to Git and GitHub**

---

## 🧠 1. What is Git?

**Git** is a version control system that helps you track changes in your code. It allows you to revert to previous versions of your project, collaborate with other developers, and manage code effectively.

### Key Concepts:
- **Version Control**: The process of tracking and managing changes to code over time.
- **Repository**: A collection of files and the history of changes to them.
- **Commit**: A snapshot of your project at a specific point in time.
- **Branch**: A separate line of development within a project.
- **Merge**: The process of combining different branches.

---

## 🧩 2. What is GitHub?

**GitHub** is a platform for hosting Git repositories online. It provides a user-friendly interface to manage your repositories, collaborate with others, and share your work.

### Why GitHub?
- **Collaboration**: Easily work with other developers by pushing and pulling changes.
- **Backup**: Your code is stored online, making it safe from local machine failures.
- **Open-source Projects**: Contribute to and access a vast number of open-source projects.

---

## 🔥 3. Basic Git Commands

### Initialize a Git Repository
To start tracking a project, navigate to the project folder and run:
```bash
git init
```

### Check Git Status
See the status of your repository (changes, untracked files, etc.):
```bash
git status
```

### Stage Changes
Before committing changes, you need to stage the files:
```bash
git add filename
```
To stage all changes:
```bash
git add .
```

### Commit Changes
Once you've staged your files, you can commit your changes with a message:
```bash
git commit -m "Your commit message"
```

### View Commit History
To view the history of commits in your repository:
```bash
git log
```

---

## 🛠️ 4. Working with Branches

### Create a New Branch
To create a new branch:
```bash
git branch branch_name
```

### Switch to a Branch
To switch to another branch:
```bash
git checkout branch_name
```

### Merge Branches
To merge a branch into your current branch:
```bash
git merge branch_name
```

---

## 🌐 5. Pushing Changes to GitHub

### Create a GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository.
2. Follow the instructions to push your local repository to GitHub.

### Link Local Repository to GitHub
After initializing the Git repository, link it to your GitHub repository:
```bash
git remote add origin https://github.com/yourusername/repository_name.git
```

### Push Changes
To push your changes to GitHub:
```bash
git push origin main
```

---

## 🧪 6. Cloning a Repository

If you want to copy an existing repository from GitHub to your local machine, you can clone it:
```bash
git clone https://github.com/username/repository_name.git
```

---

## 📝 7. Pulling Changes from GitHub

To pull the latest changes from GitHub to your local machine:
```bash
git pull origin main
```

---

## 💡 8. GitHub Workflow

1. **Clone a repository** to work on it locally.
2. **Create a branch** for new features or fixes.
3. **Stage and commit changes** regularly.
4. **Push your changes** to GitHub.
5. **Create a pull request** on GitHub to propose merging your changes into the main branch.

---

## 🔥 Quick Git Recap

| Command | Purpose |
|:--------|:--------|
| `git init` | Initialize a new Git repository |
| `git status` | Check the status of the repository |
| `git add` | Stage changes for commit |
| `git commit -m` | Commit staged changes with a message |
| `git log` | View the commit history |
| `git branch` | Create a new branch |
| `git checkout` | Switch to another branch |
| `git merge` | Merge a branch into your current branch |
| `git push` | Push changes to GitHub |
| `git pull` | Pull the latest changes from GitHub |
| `git clone` | Clone a repository from GitHub |

---

## 🌱 Mini Challenges (Optional)

1. **Set up a new repository** on GitHub and push a project to it.
2. **Create a new branch**, make some changes, and then merge it into the main branch.
3. **Fork an open-source repository** on GitHub, clone it, and make a pull request with your changes.

---

## 🎯 Summary

Git and GitHub are powerful tools for version control and collaboration. Understanding how to use them effectively will make managing your code easier, especially as your projects grow. By following Git workflows, you can collaborate with others, track the evolution of your code, and avoid mistakes that come with managing files manually.
```

