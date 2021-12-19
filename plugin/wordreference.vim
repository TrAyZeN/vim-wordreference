if exists('g:loaded_wordreference')
    finish
endif
let g:loaded_wordreference = 1

" internal-variables

let s:plugindir = expand("<sfile>:p:h:h")

function! s:translate(lang, word)
    let l:output = systemlist(
        \ "python3 " . s:plugindir . "/wr.py " . a:lang . " " . a:word)

    rightbelow vertical 40new
    setlocal buftype=nofile bufhidden=hide nobuflisted noswapfile
    setfiletype wordreference

    call setline(1, l:output)
endfunction

command -nargs=1 -complete=function Translate :call s:translate("enfr", <q-args>)
