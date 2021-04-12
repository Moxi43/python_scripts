section .data
buf   resb 1024

       xor al, al
       mov edi, buf
       mov ecx, 1024
       cld
lp:    stosb
       loop lp
       xor al, al
       mov edi, buf
       mov ecx, 1024
       cld
       rep stosb
