global _start

section .text
match: 
		push ebp
		mov ebp, esp
		sub esp, 4
		
		push esi
		push edi
		mov esi, [ebp+8]
		mov edi, [ebp+12]
.again: 
		
		
		cmp byte [edi], 0
		jne .not_end
		cmp byte [esi], 0
		jne near .false
		jmp .true 
.not_end:
		cmp byte [edi], '*'
		jne .not_star
		mov dword [ebp-4], 0 ; I := 0
.star_loop:
	
		mov eax, edi
		inc eax
		push eax
		mov eax, esi
		add eax, [ebp-4]
		push eax
		call match
		
		add esp, 8
		test eax, eax
		jnz .true
		
		
		
		add eax, [ebp-4]
		
		
		
		cmp byte [esi+eax], 0
		
		je .false 
		inc dword [ebp-4]
		jmp .star_loop

.not_star: 
		mov al, [edi]
		cmp al, '?'
		je .quest
		cmp al, [esi]
		
		
		
		
		jne .false
		
		jmp .goon
		
.quest:
		cmp byte [esi], 0
		jz .false
		
.goon:	
		inc esi
		inc edi
		jmp .again
.true:
		mov eax, 1
		jmp .quit
.false:
		xor eax, eax
.quit:
		pop edi
		pop esi
		mov esp, ebp
		pop ebp
		ret
		
;main part
_start:
		pop eax 
		cmp eax, 3
		jne wrong_args
		pop esi
		pop esi
		pop edi
		mov [string], esi
		mov [pattern], edi
		
		push edi
		push esi 
		call match
		add esp, 8
		test eax, eax
		jz print_no
		
		mov edx, 4	;print yes
		mov ecx, m_yes
		mov ebx, 1
		mov eax, 4
		int 80h
		jmp quit
		
print_no:			;print no
		mov edx, 4
		mov ecx, m_no
		mov ebx, 1
		mov eax, 4
		int 80h
		jmp quit
		
quit:
		mov ebx, 0
		mov eax, 1
		int 80h
section .bss

string		resd	1
pattern	resd	1

section .data

m_yes		db	"YES", 10
m_no		db	"NO", 10
m_wrong	db	"wrong arguments count, must be 2", 10
m_wrong_len	equ	$-m_wrong
		
