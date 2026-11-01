```text

Student B - Evidence

E1 - SSH remotes
origin  git@github.com:karim-adel-soliman/lantern.git (fetch)
origin  git@github.com:karim-adel-soliman/lantern.git (push)


Requirement 1 - Merge commit
2905156

Requirement 2 - Deletion commit
cec6d487490acd56fb07cbbf11eef4ab635e099b

E3 - Commit, tree and blob comparison

git log -2 --format="Commit: %H%nTree: %T%nSubject: %s%n"

Commit: be0fe18fc52f9c116363e3f8e47e5b6b7b042633
Tree: 0808f6c796f600946db47689dff6ed7aa489b342
Subject: docs(usage): explain local task storage

Commit: cec6d487490acd56fb07cbbf11eef4ab635e099b
Tree: c9cdf550541b913f8defb3fa54c77f83184960f1
Subject: chore(scratch): remove practice file

git ls-tree HEAD storage.py docs/usage.md

100644 blob 73fec0fc3a755133f1feed1c17db3b52820f20e8    docs/usage.md
100644 blob fdc392e8c69c1f54b418fed216caee42e4fbb4e7    storage.py

git ls-tree HEAD~1 storage.py docs/usage.md

100644 blob c76c0b7089ab0010c441c56d48215cd47e937da7    docs/usage.md
100644 blob fdc392e8c69c1f54b418fed216caee42e4fbb4e7    storage.py

Requirement 3 - Conflict-resolving merge commit
73534a2

Fast-forward merge output

git merge --ff-only fix/stable-key-order

Updating be0fe18..714b2ae
Fast-forward
 storage.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

E4 - History graph after Requirement 3 merges

git --no-pager log --graph --oneline --decorate -10

*   73534a2 (HEAD -> main) Merge pretty JSON with stable key order
|\
| * 82e0bb6 (feature/pretty-json) feat(storage): format JSON with indentation
* | 714b2ae (fix/stable-key-order) fix(storage): write JSON keys in sorted order
|/
* be0fe18 (origin/main, origin/HEAD) docs(usage): explain local task storage
* cec6d48 chore(scratch): remove practice file
* f29cd49 chore(scratch): add practice file
* d42a630 docs(usage): describe basic commands
*   671cdd5 Merge branch 'main' of github.com:karim-adel-soliman/lantern
|\
| *   6f845ab Merge branch 'main' of https://github.com/karim-adel-soliman/lantern
| |\
| * | e993e47 docs(notes): add CSV export todo item

Requirement 4 - Mistake commit
732ac7f

Requirement 4 - Fix commit
de52280

Files remain on disk after untracking

Test-Path lantern.log
True

Test-Path __pycache__
True

New matching file is ignored

"Ignore test" | Set-Content ignore-test.log

git check-ignore -v ignore-test.log
.gitignore:5:*.log      ignore-test.log

git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


E5(b) - Wrong branch drill

git reset --hard origin/main
HEAD is now at de52280 chore(ignore): untrack generated files

git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

git --no-pager reflog -6
de52280 (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: reset: moving to origin/main
56aa7be (docs/usage-heading) HEAD@{1}: commit: docs(usage): add command examples heading
de52280 (HEAD -> main, origin/main, origin/HEAD) HEAD@{2}: commit: chore(ignore): untrack generated files
732ac7f HEAD@{3}: commit: chore: track generated files for undo drill
73534a2 HEAD@{4}: commit (merge): Merge pretty JSON with stable key order
714b2ae HEAD@{5}: merge fix/stable-key-order: Fast-forward

Requirement 5(b) - Delivery merge
c76096f3eea1d72fa09af48091fa198ac44bd5dc

Requirement 5(d) - Pushed mistake
80b7728

Requirement 5(d) - Revert commit
9957000

Requirement 6 - Fork
https://github.com/Mennzo/lantern

Requirement 6 - Student B Issues
#4 - enhancement
https://github.com/karim-adel-soliman/lantern/issues/4

#5 - bug
https://github.com/karim-adel-soliman/lantern/issues/5

#6 - documentation
https://github.com/karim-adel-soliman/lantern/issues/6

E6 - Named stash

git stash list
stash@{0}: On feature/list-sort: WIP list --sort before empty-list fix

git stash pop
Dropped refs/stash@{0} (763ad9472327ee089b1569ecc72d82bd465abf15)

Requirement 7 - Empty-list PR
https://github.com/karim-adel-soliman/lantern/pull/8
Merge method: Squash and merge
Squash commit: 2b5d313

Requirement 7 - List-sort PR
https://github.com/karim-adel-soliman/lantern/pull/9
Merge method: Create a merge commit
Merge commit: 572efea
Conflict-resolution commit: 4468c5f
Review suggestion applied in: cb050cd

Requirement 7 - Review of Student A's list --done PR
https://github.com/karim-adel-soliman/lantern/pull/3
Requested changes to connect --done to list_tasks() and display results.
Student A addressed the feedback in e1fa484.

Requirement 8 - Contribution from fork

Fork:
https://github.com/Mennzo/lantern

Fork branch:
docs/contributing

Pull request to the original repository:
https://github.com/karim-adel-soliman/lantern/pull/10

Base repository: karim-adel-soliman/lantern
Base branch: main
Head repository: Mennzo/lantern
Head branch: docs/contributing

The fork was 10 commits behind the original repository.
Synced the fork before opening the pull request.

Changes:
- Added CONTRIBUTING.md with branch naming, Conventional Commits,
  pull request reviews, approval requirements, and no force-pushing.
- Added a relative link to CONTRIBUTING.md in README.md.

Commits:
2b915ee - docs(contributing): document team conventions
b850f23 - docs(readme): link contribution guidelines

Closes issue #6:
https://github.com/karim-adel-soliman/lantern/issues/6

Reviewed and approved by: karim-adel-soliman
Review comment: LGTM
Merged by: karim-adel-soliman
Merge commit: 0060449
Status: Merged and closed

```