## git常用命令

### 重要概念
1. 远程库  一般远程为裸库 
2. 本地库  可以理解为被.git文件包含 
3. 暂存区
4. 工作区
5. 贮藏区
6. 分支
7. HEAD 

### help 
```bash 
## 显示所有命令
git help -a 
## 使用手册
git help -t  
## 显示具体的命令帮忙F、B键翻页
git help add 
```

### config

git config有三个空间
系统空间  
全局空间   
项目空间  

```bash
git config --help
git config --list
## 全局设置
git config --global user.name 'abc'
## 重置选项
git config --unset --global user.name 
## 为命令添加别名
git config --global alias.co checkout
```

### init 
```bash
## 创建一个祼库 
git init --bare one.git
```

### clone 
```bash
## 克隆库到two文件夹
git clone one.git two
## 克隆库到three文件夹
git clone one.git three
## 克隆库到four文件夹
```

### add 
```bash
## 将修改添加到暂存区
git add .

```

### status
```bash 
## 显示工作区状态
git status
```

### commit 
```bash
## 将暂存区提交到本地库
git commit -m atxt
## 添加并提交 相当于add再commit 
git commit -a -m 'threeatxtadd2line'
```

### push 

```bash 
## 将本地库提交到远程库 
git push
## 将本地dev分支提交到远程库 
git push origin dev
## 强制以HEAD版本提交远程库
git push --force
## 删除远程分支
git push origin --delete dev
## 推送tag:mergedev1到远程 
git push origin mergedev1
## 将所有tag推送到远程
git push origin --tags
## 删除远程的tag
git push origin :refs/tags/mergedev1
```

### pull 
```bash 
## 从远程库fetch并merge到工作区
git pull
```

### checkout 
```bash
## 创建并切换分支到dev
git checkout -b dev
## 切换分支 
git checkout master
## 将远程分支剪出到本地dev分支 
git checkout -b dev remotes/origin/dev
## 将文件恢复到历史某一版本 
git checkout b1f2bab -- a.txt
## 创建游离分支，切换到tag:createatxt
git checkout createatxt
```

### branch 
```bash 
## 查看所有分支
git branch -a
## 删除dev分支
git branch -d dev
## 重命名分支
git branch -m dev dev1
## 将本地分支关联到远程分支
git branch --set-upstream-to=origin/dev dev
```

### log 
```bash 
## 以简要方式查看当前分支提交记录 
git log --oneline 
## 以简要方式查看所有分支提交记录 
git log --oneline --decorate --all 
## 以提交树的方式查看所有提交记录 
git log --oneline --decorate --all --graph
## 通过作者筛选提交记录
git log --author zeimao77 -n 2
## 通过某一段时间筛选提交记录
git log --after '2020-08-22 19:10:00' --before '2020-08-22 20:00:00'
## 查看某一提交具体修改内容
git log -p -n 1
```

### diff
```bash 
## 查看dev分支master分支区别
git diff dev..master
## 如果暂存区为空比较本地库和工作区 否则比较工作区与暂存区
git diff b.txt 
## 比较本地库与暂存区 
git diff --cached b.txt 
## 如果工作区不为空，将比较本地库(HEAD)和工作区，否则比较本地库HEAD与暂存区 
git diff HEAD b.txt 
## 和上一命令一样，和历史某一版本比较 
git diff b1f2bab a.txt
## 指定两个版本比较 
git diff b1f2bab 58574a5 a.txt

```

### merge
```bash 
## 将dev分支合并到当前分支 
git merge dev 
## 当merge操作冲突时，我们可以选择取消merge 
git merge --abort

```

### rebase 
```bash 
## 将dev分支变基到当前分支 
git rebase dev
## 取消变基操作
git rebase --abort
## 丢弃掉此提交
git rebase --skip
```

### stash
```bash 
## 查看贮藏区列表
git stash list
## 将当前快照添加到贮藏区 
git stash save -q b6line btxtadd6line
## 恢复合并贮藏
git stash pop stash@{0}
## 丢弃贮藏 
git stash drop stash@{0}
## 显示区别 
git stash show -p 123
``` 

### fetch 
```bash 
## 将远程库更新到本地库 但不执行合并操作
git fetch 
## 创建一个本地dev1分支，关联远程dev分支
git fetch origin dev:dev1
```

### reset 
```bash 
## 重置HEAD到某一版本,hard将影响到工作区、暂存区
git reset --hard b1f2bab
## 重置HEAD到某一版本,soft只影响本地库 
git reset --soft b1f2bab
## 重置HEAD到某一版本，mixed影响本地库和暂存区 
git reset --mixed b1f2bab
## 同理
git reset --hard HEAD

```

### remote 
```bash 
## 查看远程库
git remote --verbose
## 添加一个远程库
git remote add origin /home/zeimao77/桌面/gitdir/one.git
## 删除远程库关联 
git remote rm origin
```

### rm 
```bash 
## 删除某个文件
git rm c.txt
## 删除某个文件夹 
git rm -r assets/css/
```

### mv
```bash
## 重命名文件
git mv a.txt aa.txt
## 移动文件
git mv aa.txt txt/
## 移动文件夹及子文件
git mv css assets/
```

### tag
```bash
## 列出以merge开头的tag  
git tag -l merge*
## 删除某个tag  
git tag -d mergedev1
## 创建一个带有备注信息的tag 
git tag -a mergedev1 -m 'mrege-updataatxt'
## 显示tag详细信息
git show mergedev1
## 为某一次提交创建tag 
git tag -a createatxt -m "create_file_atxt" 7351f52
```

### update-index 
```bash 
## 临时性决定忽略某个文件 
git update-index --assume-unchanged b.txt
## 取消以上操作
git update-index --no-assume-unchanged b.txt
## 重置所有文件状态
git update-index --really-refresh
```