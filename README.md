# web_crawler
A prototype of web crawler

## 安装过程   
1. 确认已经安装conda, 安装详情请参考之前的教程：https://www.jiuzhang.com/tutorial/ai-camp/477
2. 打开一个terminal，windows用户建议打开Anaconda Prompt.
3. 输入命令行: conda create --name web_crawler python=3.5
3. 输入命令行: conda activate web_crawler        
如果激活环境遇到了问题，conda会自己提示解决方案，比如：   
、、、
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
If your shell is Bash or a Bourne variant, enable conda for the current user with

    $ echo ". /Users/Andrew/anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile
、、、         
NOTE： 注意Andrew是我的用户名，请根据自己的提示信息进行修改
6. 输入命令行: git clone https://github.com/jiuzhangjiangzuo/web_crawler.git 或直接下载压缩包[link](https://github.com/jiuzhangjiangzuo/web_crawler/archive/master.zip)
7. 输入命令行: cd web_crawler
8. 输入命令行: pip install -r requirements.txt
