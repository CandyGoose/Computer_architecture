start_loop:
    cmp r1, r2
    jge end_loop

    mov r3, r1
    rem r3, 3
    cmp r3, 0
    je add_to_sum

    mov r4, r1
    rem r4, 5
    cmp r4, 0
    je add_to_sum

    jmp next

add_to_sum:
    add r0, r1

end_loop: load *2
    ret

next:
    inc r1
    jmp start_loop

_start:
    mov r0, 0
    mov r1, 0
    mov r2, 1000
    call start_loop
    halt
