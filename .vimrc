" --------------------------------------------
" vimrc 
" Christopher Folmar  10/30/2013
" --------------------------------------------

" First we are going to change the default color scheme to solarized
syntax enable
set background=dark
"let g:solarized_termcolors=256
colorscheme ir_black 

" We are going to try ',' as our mapleader, cause \ doesn't seem to want to work for vim-latex"
let mapleader = ","

" Turn numbering on, our default nubmering is absolute"
set number 

" Now we want to be able to switch between absolute numbering and relative numbering
" We will map abs numbering to F1 and relative numbering to F2. 
" First we deal with F1
imap <F1> <Esc>:set number<CR>a
nmap <F1> :set number<CR>

" Now we deal with F2
imap <F2> <Esc>:set relativenumber<CR>a
nmap <F2> :set relativenumber<CR>

" Now we need to set up vim-Latex
" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
filetype plugin on

" IMPORTANT: grep will sometimes skip displaying the file name if you
" search in a singe file. This will confuse Latex-Suite. Set your grep
" program to always generate a file-name.
set

" OPTIONAL: This enables automatic indentation as you type.
filetype indent on

" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'


set runtimepath+=~/.vim_runtime

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
"source ~/.vim_runtime/vimrcs/extended.vim

"try
"source ~/.vim_runtime/my_configs.vim
"catch
"endtry


