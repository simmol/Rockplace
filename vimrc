" Use spaces instead of tabs
set shiftwidth=2
set tabstop=2
set softtabstop=2
set expandtab

"Enabled auto-indenting
set autoindent
set smartindent
filetype plugin indent on

" Automatically set current directory to file's location
set autochdir

" Show tabs and trailing spaces so I can remove them
set list
set listchars=tab:»·,trail:·

function! RemoveTrailingSpaces()
  %s/\s\+$//e
endfunction

function! ConvertTabsToSpaces()
  %retab
endfunction

function! CleanFile()
  call ConvertTabsToSpaces()
  call RemoveTrailingSpaces()
endfunction

" Key binding F5 to clean up file
nnoremap <silent> <F5> :let _s=@/<Bar>:call CleanFile()<CR>

" Show the cursor position and line numbers
"set number
"set ruler

let php_sql_query=1
let php_htmlInStrings=1
let php_parent_error_close=1
let php_parent_error_open=1
let php_folding=1

if has("autocmd")
    " Drupal *.module and *.install files.
      augroup module
          autocmd BufRead,BufNewFile *.module set filetype=php
          autocmd BufRead,BufNewFile *.install set filetype=php
          autocmd BufRead,BufNewFile *.test set filetype=php
      augroup END
endif
syntax on

colorscheme wombat

let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1

filetype plugin on
set completeopt=menu
" Undo in Insert mode (CTRL+Z)
map <c-z> <c-o>u

" Remap omni-completion to CTRL+SPACE
inoremap <expr> <C-Space> pumvisible() \|\| &omnifunc == '' ?
\ "\<lt>C-n>" :
\ "\<lt>C-x>\<lt>C-o><c-r>=pumvisible() ?" .
\ "\"\\<lt>c-n>\\<lt>c-p>\\<lt>c-n>\" :" .
\ "\" \\<lt>bs>\\<lt>C-n>\"\<CR>"
imap <C-@> <C-Space>
