if [ $UID -eq 0 ]; then NCOLOR="red"; else NCOLOR="green"; fi

PROMPT='[%D{%H:%M:%S}] %{$fg[$NCOLOR]%}%n%{$reset_color%}@%{$fg[cyan]%}%m\
%{$reset_color%}:%{$fg[magenta]%}%~\
$(git_prompt_info) %{$fg[white]%}%(!.#.$)%{$reset_color%} '

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[yellow]%}("
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[green]%}V%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[red]%}X%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$fg[yellow]%})%{$reset_color%}"
