# A collection of useful Coding Notes 

## Assembly
[Creating your own operating system](http://createyourownos.blogspot.com/)<br>
[16 colors for background in MCGA BIOS text mode (AL = 03h)](https://stackoverflow.com/questions/28790368/16-colors-for-background-in-mcga-bios-text-mode-al-03h)<br>

## About MacOS Terminal
1. Customize zsh:<br>

|Shell  |zsh         | bash              |
|-------|------------|-------------------|
|Command|vim ~/.zshrc|vim ~/.bash_profile|

Change default directory:<br>
```
cd ~/Desktop
```
Change color:<br>
```
PROMPT='[%F{red}%*%f] %F{red}%~%f >> '
```
<img width="548" alt="Screen Shot 2020-11-24 at 11 23 17 AM" src="https://user-images.githubusercontent.com/24274444/100129721-84c52380-2e47-11eb-94cf-a41134a2cd01.png">

[Customize the MacOS Terminal](https://medium.com/dev-genius/customize-the-macos-terminal-zsh-4cb387e4f447)<br>
[zsh Prompt Expansion](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Prompt-Expansion)<br>
[oh my zsh](https://ohmyz.sh/#install)

3. How to remove default "Last login" message in MacOS Terminal
```
touch ~/.hushlogin
```
4. [Keyboard shortcuts in Terminal on Mac](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac)


## Installation
Mounty for NTFS:
```
brew cask install mounty
```
[Install Node.js on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04)<br>
[Homebrew](https://brew.sh/)<br>
[VirtualBox Ubuntu](https://blog.csdn.net/u012732259/article/details/70172704)<br>
[ngrok - secure introspectable tunnels to localhost](https://ngrok.com/)<br>

## Other
Press Windows + R and type shell:startup, then move the shortcut of a software which you want automatically start up to this folder.

## Issue
1. zsh: permission denied: ./file.bat
```
chmod +x ./file.bat
```

2. xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun

After upgrade to Mac Catalina I faced the same issue, I had to run couple of commands to get this fixed.

First started with:
```

xcode-select --install
```

It didn't fix the problem, had to run the following in sudo
```
sudo xcode-select --reset
```

Then, finally got fixed after I switched and set the path explicitly for active developer directory:
```

sudo xcode-select -s /Library/Developer/CommandLineTools
```

Note: In case you have Xcode installed, you may need to specify Xcode directory in this case, it should be something like this
```

xcode-select -s /Applications/Xcode.app
```
[Stack Overflow solution](https://stackoverflow.com/questions/52522565/git-is-not-working-after-macos-update-xcrun-error-invalid-active-developer-pa)<br>
[Download CommandLineTool from Apple Developer](https://developer.apple.com/download/more/)<br>

3. [How to use reCAPTCHA on localhost](https://stackoverflow.com/questions/3232904/using-recaptcha-on-localhost)<br>
4. [How to verify reCAPTCHA - Python](https://techmonger.github.io/5/python-flask-recaptcha/)<br>
5. SMTP Authentication Error
```
Traceback (most recent call last):
  File "gmail.py", line 22, in <module>
    server.login(gmail_user, gmail_password)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/smtplib.py", line 734, in login
    raise last_exception
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/smtplib.py", line 723, in login
    (code, resp) = self.auth(
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/smtplib.py", line 646, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials n72sm18791391pfd.202 - gsmtp')
```
Log in to your Google account, and use these links:<br>
Step 1 [Link of Disabling 2-step verification](https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin)<br>
Step 2: [Link for Allowing less secure apps](https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none)<br>
[Login credentials not working with Gmail SMTP](https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp)<br>

## Related Link
[极客学院](https://www.jikexueyuan.com/)<br>
[牛客网](https://www.nowcoder.com/)<br>
[计算机网络知识](https://www.cnblogs.com/maybe2030/p/4781555.html)<br>
[HTTPS原理](https://mp.weixin.qq.com/s/5zcpyKxuyib5gxMe3mqrhw)<br>
[15 张图，了解一下 TCP/IP 必知也必会的 10 个问题](https://mp.weixin.qq.com/s/qf8L52VtGTzWcF0NB5Filg)<br>
[免费在线云盘](https://mp.weixin.qq.com/s/CVT6z9yFWjs4PUp9eBYyPg)<br>
[CodeGym](https://codegym.cc/zh/)<br>
[w3schools](https://www.w3schools.com/)<br>
[Stack Overflow](https://stackoverflow.com/)<br>
[Snap](https://snap.berkeley.edu/snap/snap.html)<br>
[Create Your Own Certificate and CA](https://sites.google.com/site/ddmwsst/create-your-own-certificate-and-ca)<br>
[App inventor Mole Mash project](http://appinventor.mit.edu/explore/ai2/molemash.html)<br>
[App inventor: How do you record information in a list?](http://www.appinventor.org/content/howDoYou/RecordingInfo/notes)<br>
[How do you record items in a list in App Inventor?](https://www.youtube.com/watch?v=aiFrwX7M4vc)<br>
[App Inventor 2 Tutorial Canvas image HD](https://www.youtube.com/watch?v=TE-1mzvvk40)<br>
[Create google reCAPTCHA](https://www.google.com/recaptcha/admin/create)<br>

### Tool
[Jdoodle - Online Compiler](https://www.jdoodle.com/online-java-compiler/)<br>
[Repl.it - Online Compiler](https://repl.it/)<br>
[Diagrams - Online diagrams tool](https://app.diagrams.net/)<br>
[Creately - Online diagrams tool](https://app.creately.com/)<br>

### Algorithm
[动态规划解决扔鸡蛋问题](https://mp.weixin.qq.com/s/R3aQ7m1HdHwt50ELX7Kn2g)<br>
[LRU算法](https://mp.weixin.qq.com/s/YhJ9dkhh7Uw1RMt8Yn-O4A)<br>
[经典排序算法 JAVA实现](https://www.cnblogs.com/guoyaohua/p/8600214.html)<br>


### Github
[Github formatting syntax](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax)<br>
[Github add README images](https://www.youtube.com/watch?v=nvPOUdz5PL4)<br>
[Github Online IDE](https://github.com/features/codespaces)<br>
[怎么在 GitHub上面找项目](https://mp.weixin.qq.com/s/_DJPf6L9XViT_siyShwvMQ)<br>

## Course Material
[Discrete Structures](http://web.stanford.edu/class/cs103x/cs103x-notes.pdf)<br>
[Discrete Mathematics](https://books.google.com/books?id=6cMSAAAAQBAJ&pg=PA43&lpg=PA43&dq=if+s+is+a+tautology+and+R+is+a+contradiction+what+is+the+truth+value+of+following&source=bl&ots=7LWfF8dGpP&sig=u9V166ISijvcvSfhRIxZ-OPn-iI&hl=en&sa=X&ved=0ahUKEwirvLOevIDLAhVD4CYKHcbWBmAQ6AEIQjAG#v=onepage&q=if%20s%20is%20a%20tautology%20and%20R%20is%20a%20contradiction%20what%20is%20the%20truth%20value%20of%20following&f=false)<br>
[Solutions Manual for Languages and Machines: An Introduction to the Theory of Computer Science Third Edition](https://cdn.manesht.ir/3252___Sudkamp-Solutions-3rd.pdf)<br>
[Processing Unit](http://web.cecs.pdx.edu/~zeshan/ece341_lecture10a.pdf)<br>
[Interface circuits](http://www.idc-online.com/technical_references/pdfs/information_technology/Interface_circuits_%20i.pdf)<br>
