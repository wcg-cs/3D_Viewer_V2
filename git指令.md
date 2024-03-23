|                           命令名称                           |                             作用                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|             git config --global user.name 用户名             |                         设置用户签名                         |
|             git config --global user.email 邮箱              |                         设置用户密码                         |
|                      git config --list                       |                   查看所有配置（是否登录）                   |
|                           git init                           |                         初始化本地库                         |
|                          git status                          |                        查看本地库状态                        |
|                       git add 文件名字                       |                      将文件添加到暂存区                      |
|                          git add .                           |                    将全部文件添加到暂存区                    |
|                         git ls-files                         |                        查看暂存区文件                        |
|                 git rm -r --cached <文件名>                  |                       删除暂存区的文件                       |
|                  git commit -m <"日志信息">                  |                         提交到本地库                         |
|                          git reflog                          |                         查看历史记录                         |
|                   git reset --hard 版本号                    |                           版本穿梭                           |
|                      git branch 分支名                       |                           创建分支                           |
|                        git branch -v                         |                           查看分支                           |
|                     git checkout 分支名                      |                           切换分支                           |
|                      git switch 分支名                       |                           切换分支                           |
|                       git merge 分支名                       |                 把指定的分支合并到当前分支上                 |
|                        git remote -v                         |                    查看所有远程仓库的别名                    |
|                git remote add 别名 远程库网站                |                         给远程库取名                         |
|                       git fetch origin                       | 从远程仓库获取远程跟踪分支的变更到本地。<br />该命令将从远程仓库获取所有更新，并将其保存在本地 |
|        git branch --set-upstream-to origin 远程分支名        |                   设置本地分支追踪远程分支                   |
| git push 别名 master<br />git push origin master/hcg:master/hcg |                将本地分支推送至远程库对应分支                |
|          git push --set-upstream origin 远程分支名           |                推送并设置本地分支追踪远程分支                |
|                           git push                           |                       追踪后可直接推送                       |
|                 git pull 别名/origin master                  |                          拉取远程库                          |
|          git pull --set-upstream origin 远程分支名           |                拉取并设置本地分支追踪远程分支                |
|                        git clone 网址                        |                      下载远程仓库的内容                      |
|                  git push origin 远程分支名                  |                        提交到远程分支                        |
|               git remote set-url origin [URL]                |                       关联远程仓库地址                       |
|     git push <远程主机别名名> <本地分支名>:<远程分支名>      |                         推送至远程库                         |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |

## git报错解决

* ```
  input: git push origin hcg
  error: fatal: unable to access 'https://github.com/Cg-Hu/bysj-remote.git/': Failed to connect to github.com port 443: Connection timed out
  ===解决方法===
  $ git config --global  --unset http.https://github.com.proxy 
  $ git config --global  --unset http.https://github.com.proxy 
  ```

* 
