transfer:
    out 2
    sign 0
    in 1
    store *2
    iret

print:
    movh
    store *2
    load 16
    store *3

    sign 3
    ei
    char:
        load *2
        load *3
        dec
        store *3
        jne char
    di
    sign 3
    ret

_start:
    vec
    func transfer
    store *0
    timer 7

    sign 3

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
