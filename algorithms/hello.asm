transfer:
    out 2
    in 1
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
    ret

_start:
    func transfer
    store *0
    timer 7

    load 'H'
    call print
    load 'e'
    call print
    load 'l'
    call print
    load 'l'
    call print
    load 'o'
    call print
    load ' '
    call print
    load 'w'
    call print
    load 'o'
    call print
    load 'r'
    call print
    load 'l'
    call print
    load 'd'
    call print
    load '!'
    call print
    load 0
    call print

    halt
