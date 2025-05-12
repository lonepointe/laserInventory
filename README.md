# laserInventory
a python project to track and value laser engraver projects.


#  Git: Local Repo & Remote Repo Out of Sync (Unrelated Histories Fix)

##  Problem:
- You initialized a local repo (`git init`).
- You also created files directly on GitHub.
- Now when you try to pull, Git says:
  > "refusing to merge unrelated histories."

##  Solution:
Merge the histories explicitly:
```bash
git pull --no-rebase --allow-unrelated-histories

then:
git add .
git commit -m "Merged unrelated histories"
git push
