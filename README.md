## MacOS
<details><summary>Customize zsh</summary><p>
     
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
</p></details>
<details><summary>How to remove default "Last login" message in MacOS Terminal </summary><p>
     
    ```
    touch ~/.hushlogin
    ```
</p></details>

[Keyboard shortcuts in Terminal on Mac](https://support.apple.com/guide/terminal/keyboard-shortcuts-trmlshtcts/mac)<br>

## Installation
Mounty for NTFS:
```
brew cask install mounty
```
[ngrok - secure introspectable tunnels to localhost](https://ngrok.com/)<br>


## Issue
<details><summary>zsh: permission denied: ./file.bat</summary><p>
     
```
chmod +x ./file.bat
```
</p></details>
<details><summary>xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun</summary><p>
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
</p></details>
<details><summary>SMTP Authentication Error</summary><p>

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
</p></details>

<details><summary>Not installing pip on ubuntu 20.04</summary><p>
https://askubuntu.com/questions/1254309/not-installing-pip-on-ubuntu-20-04
</p></details>

<details><summary>E: Unable to locate package python-pip” on Ubuntu 18.04</summary><p>
     
```
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip
```
</p></details>

[How to use reCAPTCHA on localhost](https://stackoverflow.com/questions/3232904/using-recaptcha-on-localhost)<br>
[How to verify reCAPTCHA - Python](https://techmonger.github.io/5/python-flask-recaptcha/)<br>
[How to Fix Cron Permission Issues in MacOS Catalina & Mojave](https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/)<br>
