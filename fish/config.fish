#set theme_color_scheme terminal2-dark

#set PATH ~/.mutt $PATH

alias fuck="eval sudo \$history[1]"
alias sm="sm -i"
alias smc="sm -n mono"
alias l="ls -lah"
alias ldir="ls -al | grep \^d"
alias python="python3"
alias wetter="curl wttr.in/~Dresden"
alias wifi="nmcli dev wifi list"
alias wifi-con="nmcli con up id"
alias wifi-new="nmcli --ask con up id"
alias sizeof="du -sh"
alias swt="cd ~/Dokumente/Studium/03_Wintersemester_2017_2018/SWT/swt17w3/"
alias copy="xclip -sel clip <"
alias mutt="neomutt"
alias fsr-nummer="sm '+49 351 4638226'"
alias x="exa --header --long --git"
alias vim="mvim"
alias wpm-de="wpm --stats-file ~/.wpm/de"
alias wpm-neo="wpm --stats-file ~/.wpm/neo"
