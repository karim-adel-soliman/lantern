## E1
origin	https://github.com/karim-adel-soliman/lantern.git (fetch)
origin	https://github.com/karim-adel-soliman/lantern.git (push)

## E2
### git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   tasks.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   tasks.py

### git diff (unstaged)
diff --git a/tasks.py b/tasks.py
index f88d2f3..c4be29c 100644
--- a/tasks.py
+++ b/tasks.py
@@ -4,3 +4,6 @@ def add_task(title):
     task = {"title": title}
     TASKS.append(task)
     return task
+
+def list_tasks():
+    return TASKS
### git diff --staged (staged)
diff --git a/tasks.py b/tasks.py
new file mode 100644
index 0000000..f88d2f3
--- /dev/null
+++ b/tasks.py
@@ -0,0 +1,6 @@
+TASKS = []
+
+def add_task(title):
+    task = {"title": title}
+    TASKS.append(task)
+    return task

## E4
*   cad46ea (HEAD -> main) Merge branch 'feature/done-flag'
|\  
| * 817f95f feat(tasks): add done flag to new tasks
* | 6812381 fix(tasks): strip whitespace from task title
|/  
* f0e9e0c chore(notes): rename draft.txt to notes.txt
* a890f7f docs(notes): add draft placeholder file
* aef7261 feat(cli): add argparse entry point for add and list

## E5
### (c)
e993e47 HEAD@{0}: reset: moving to HEAD@{1}
d85c479 HEAD@{1}: reset: moving to HEAd~1
e993e47 HEAD@{2}: commit: docs(notes): add CSV export todo item
### (a)
d85c479 HEAD@{3}: commit (amend): docs(notes): add CLI todo item
f7adafc HEAD@{4}: commit: dcos(notes): add CLI todo item
2fce7eb HEAD@{5}: commit: fix(git): untrack .env and ignore env files

## E7
remote: error: GH013: Repository rule violations found for refs/heads/main.        
remote: Review all repository rules at https://github.com/karim-adel-soliman/lantern/rules?ref=refs%2Fheads%2Fmain        
remote: 
remote: - Changes must be made through a pull request.        
remote: 
To https://github.com/karim-adel-soliman/lantern.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/karim-adel-soliman/lantern.git'
