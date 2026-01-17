# Pj_GetData
A repository for obtaining stock prices for specific stocks and commodity prices (such as Bitcoin and gold prices).

 ① Move to the repository
 cd prompt-knowledge-base

 ② Create a working branch
 git checkout -b "branch name"

 ③ Edit files(Open with VS Code)
 code .
 
     1. Edit some files

     2. Save (⌘ + S)

 ④ Check changes
 git status

     1. Example
         modified: README.md

 ⑤ Stage changes
 git add "file's name"
 (Or use git add . to stage everything)

 ⑥ Commit
 git commit -m "commit massage"

 ⑦Push feature contents to origin(main)
 git push -u origin HEAD
 
 <Spesific case>
 ⑦ Switch to the main branch
 git checkout main
 Update it:
 git pull origin main

 ⑧ Merge
 git merge ""feature/hoge""
 If there are no conflicts, it completes immediately

 ⑨ Push main to the remote
 git push origin main