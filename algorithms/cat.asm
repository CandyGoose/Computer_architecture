transfer:
    out 1
    in 0
    store *2
    iret

print:
    movh
    store *2
    load 16
    store *3

    ei
    char:
        load *2
        load *3
        dec
        store *3
        jne char
    di
    load *2
    ret

_start:
    func transfer
    store *0
    timer 7

    load 1
    loop:
        call print
        cmp 0
        jne loop

    call print
    halt
