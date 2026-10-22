# Git & GitHub Practice Project — README

## Project Overview

This project documents my beginner-level practical work with Git and GitHub using Windows CMD. I practised creating a repository, tracking changes, working with branches, synchronizing a second local clone, and resolving a merge conflict.

**GitHub repository:** https://github.com/Rishianandd/git_practice

**Main local folder:** `C:\Users\rishi\git_practice`

**Second local clone used for collaboration simulation:** `C:\Users\rishi\collaborator1`

## Learning Objectives

- Understand the difference between Git and GitHub.
- Clone a remote repository to a local computer.
- Stage, commit, and push changes.
- Create and switch between branches.
- Merge a feature branch into `main`.
- Synchronize changes between two local clones through GitHub.
- Create and resolve a merge conflict.
- Inspect commit history and repository status.

## Tools Used

- Git
- GitHub
- Windows Command Prompt (CMD)
- Notepad for editing text files

## Project Files

The exercises introduced the following files:

| File | Purpose |
|---|---|
| `project.txt` | Initial project description exercise |
| `students.txt` | Sample student records |
| `collaborator1.txt` | Demonstration of a collaborator's contribution |
| `conflict.txt` | Demonstration of a merge conflict and its resolution |

## 1. Clone the Repository

I cloned the GitHub repository to my computer:

```cmd
git clone https://github.com/rishianandd/git_practice.git
```

Cloning downloads the repository and its Git history to the local computer and configures a remote, usually named `origin`.

## 2. Create and Commit the Project Description

I created `project.txt` and practised the basic Git workflow:

```cmd
git status
git add project.txt
git commit -m "Add project description"
git push origin main
```

- `git status` displays the current branch and working-tree state.
- `git add` stages changes for the next commit.
- `git commit` records a snapshot in local Git history.
- `git push` uploads local commits to the remote repository.

The associated commit was `c852c63 Add project description`.

## 3. Create a Feature Branch for Student Records

I created a separate branch for student records:

```cmd
git switch -c feature-students
```

I created `students.txt` with sample data:

```text
Student: Alice
Marks: 85
Student: Bob
Marks: 92
```

I staged and committed the file, then pushed the branch:

```cmd
git add students.txt
git commit -m "Add student records"
git push -u origin feature-students
```

The commit was `9bd4bbb Add student records`.

I then merged the feature branch into `main`:

```cmd
git switch main
git merge feature-students
git push origin main
```

This demonstrated how a feature can be developed on a separate branch and merged into the main branch.

## 4. Simulate Collaboration with a Second Clone

I used a second local clone in `C:\Users\rishi\collaborator1` to simulate a collaborator's environment. In that clone, I created `collaborator1.txt` with the following content:

```text
Contribution from Collaborator 1
Learning Git collaboration
```

The related commits shown in the history were:

- `e1b1482 Add collaborator 1 contribution`
- `7382696 Add collaborator contribution text`

After pushing the change to GitHub from the second clone, I returned to the original clone and ran:

```cmd
git pull origin main
```

This demonstrated how one working copy can retrieve changes published to a shared remote repository by another working copy.

**Note:** This was a simulation using two local clones on one computer. It did not by itself verify contributions from an actual teammate using a separate account.

## 5. Create Two Branches with Conflicting Changes

The goal of this exercise was to make two branches edit the same line differently so Git would be unable to merge the changes automatically.

### 5.1 Create the initial status

On `main`, I created `conflict.txt` with:

```text
Project status: Draft
```

Commands:

```cmd
echo Project status: Draft> conflict.txt
git add conflict.txt
git commit -m "Add initial project status"
git push origin main
```

The commit was `d1c0c9e Add initial project status`.

### 5.2 Create `conflict-a`

I created the branch:

```cmd
git switch -c conflict-a
```

I changed the file to:

```text
Project status: Ready
```

Then I committed the change:

```cmd
git add conflict.txt
git commit -m "Set project status to ready"
```

The commit was `c235506 Set project status to ready`.

### 5.3 Create `conflict-b`

I returned to `main` and created the second branch:

```cmd
git switch main
git switch -c conflict-b
```

I changed the same line to:

```text
Project status: In progress
```

Then I committed it:

```cmd
git add conflict.txt
git commit -m "Set project status to in progress"
```

The commit was `60ad65c Set project status to in progress`.

### 5.4 Trigger the merge conflict

While on `conflict-b`, I ran:

```cmd
git merge conflict-a
```

Git reported a content conflict in `conflict.txt`, because both branches changed the same line differently.

The file contained conflict markers similar to:

```text
<<<<<<< HEAD
Project status: In progress
=======
Project status: Ready
>>>>>>> conflict-a
```

- `<<<<<<< HEAD` starts the current branch's version.
- `=======` separates the two versions.
- `>>>>>>> conflict-a` marks the end of the incoming branch's version.

These markers are temporary and must be removed when resolving the file.

### 5.5 Resolve the conflict

I opened the file:

```cmd
notepad conflict.txt
```

I removed the conflict markers and the two competing lines, replacing them with the final decision:

```text
Project status: Ready for review
```

I saved the file, staged the resolution, checked the status, and completed the merge:

```cmd
git add conflict.txt
git status
git commit -m "Resolve project status conflict"
```

The merge commit was `8dde4b6 Resolve project status conflict`.

### 5.6 Push the resolved work and merge into `main`

I pushed the resolved branch and then integrated it into `main`:

```cmd
git push -u origin conflict-b
git switch main
git pull origin main
git merge conflict-b
git push origin main
```

The final history showed the merge commit on `main` and the remote-tracking references `origin/main` and `origin/conflict-b` pointing to `8dde4b6`.

The `conflict-a` branch appeared in the local history; the displayed history did not show an `origin/conflict-a` reference, so it should not be assumed that this branch was pushed.

## 6. Final Commit History

The history observed during the exercise was:

| Commit | Message |
|---|---|
| `c852c63` | Add project description |
| `9bd4bbb` | Add student records |
| `e1b1482` | Add collaborator 1 contribution |
| `7382696` | Add collaborator contribution text |
| `d1c0c9e` | Add initial project status |
| `60ad65c` | Set project status to in progress |
| `c235506` | Set project status to ready |
| `8dde4b6` | Resolve project status conflict |

To inspect the history:

```cmd
git log --oneline --graph --all
```

The merge commit has two parents, so the graph shows the two lines of development joining together.

## 7. Important Git Commands

| Command | Purpose |
|---|---|
| `git clone URL` | Clone a remote repository |
| `git status` | Check branch and working-tree status |
| `git branch` | List local branches |
| `git branch -a` | List local branches and remote-tracking branches |
| `git switch main` | Switch to `main` |
| `git switch -c branch-name` | Create and switch to a branch |
| `git add filename` | Stage a specific file |
| `git add .` | Stage changes in the current directory and its subdirectories |
| `git commit -m "message"` | Record staged changes |
| `git push origin main` | Push `main` to the remote |
| `git push -u origin branch-name` | Push a branch and configure upstream tracking |
| `git pull origin main` | Fetch and integrate remote `main` into the current branch |
| `git merge branch-name` | Merge the named branch into the current branch |
| `git merge --abort` | Abort an in-progress merge when Git can restore the pre-merge state |
| `git log --oneline --graph --all` | View commit history as a graph |
| `type conflict.txt` | Display a text file in Windows CMD |

## 8. Key Concepts Learned

### Git vs. GitHub

- **Git** is the version control system that tracks changes and stores commit history.
- **GitHub** hosts Git repositories online and supports collaboration and code review.

### Working tree, staging area, and commits

- The **working tree** contains the files currently being edited.
- The **staging area** contains changes selected for the next commit.
- A **commit** records a snapshot in the local repository's history.
- A **push** sends commits to the remote repository.

### Branches and merging

A branch provides a separate line of development. Merging integrates changes from another branch into the current branch.

### Pulling and pushing

A push publishes local commits to a remote repository. A pull fetches remote updates and integrates them into the current branch. A local commit in one clone is not automatically available in another clone; the changes normally need to be pushed to the shared remote first.

### Merge conflict

A merge conflict occurs when Git cannot safely combine changes automatically. The developer inspects the competing changes, edits the file to the desired result, stages the resolution, and completes the merge with a commit.

## 9. Final Verification

Run these commands in the main repository:

```cmd
git status
git branch -a
git log --oneline --graph --all
type conflict.txt
```

Expected final file content:

```text
Project status: Ready for review
```

The working tree should report `nothing to commit, working tree clean` when all changes are committed. The branch list shows which branches exist locally and which have remote-tracking references.

On GitHub, open the repository and verify the `main` branch, the `conflict.txt` file, and the commit history. The final merge commit should be visible on `main`.

## 10. What I Completed and What Comes Next

### Completed

- Cloned and worked with a GitHub repository.
- Created files and committed changes.
- Created and merged a feature branch.
- Simulated synchronization between two local clones.
- Created two branches with conflicting edits.
- Resolved a merge conflict manually.
- Committed and pushed the resolution.
- Inspected the commit graph.

### Recommended next steps

- Verify the final files and commits on GitHub.
- Push `conflict-a` if you want that branch to be visible on GitHub.
- Practise with actual teammates using separate accounts and clones.
- Create a feature branch on a teammate's clone and push it.
- Open a pull request, review the changes, and merge it.
- Practise resolving a conflict when both contributors publish their work independently.

## Conclusion

This practical project provided a foundation in Git and GitHub, including version control, branching, commits, remote synchronization, and merge conflict resolution. The main outcome was learning how to handle two different edits to the same line and safely record the chosen result in Git history.

**Final resolved status:** `Project status: Ready for review`
