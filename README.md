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
