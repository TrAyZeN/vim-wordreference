if exists("b:current_syntax")
  finish
endif

syn match translateFrom /^[^:]*/ contained
syn match translateFromAll /^[^:]*:/ contains=translateFrom
syn match translateTitle /^Translation/ contained
syn match translateTitleColon /^Translation:/ contains=translateTitle

hi def link translateTitle Title
hi def link translateTitleColon NoText
hi def link translateFrom Identifier
hi def link translateFromAll NonText

let b:current_syntax = "wordreference"
