transfer:
    out 2
    sign 0
    in 1
    store *3
    iret

print:
    movh
    store *3
    load 16
    store *4

    sign 3
    ei
    char:
        load *3
        load *4
        dec
        store *4
        jne char
    di
    sign 3
    load *3
    cmp 0
    je skip
    store **2+

    skip: ret

_start:
    vec
    func transfer
    store *0
    timer 7
    sign 3

    call hello

    load 5
    store *1
    load 12
    store *2

    call name_req
    waiting_for_chars:
        load 1
        call print
        cmp 0
        je waiting_for_chars

    load **1+
    loop:
        call print
        load **1+
        cmp 0
        jne loop

    load '!'
    call print
    load 0
    call print
    halt

name_req:
    load 'W'
    call print
    load 'h'
    call print
    load 'a'
    call print
    load 't'
    call print
    load ' '
    call print

    load 'i'
    call print
    load 's'
    call print
    load ' '
    call print

    load 'y'
    call print
    load 'o'
    call print
    load 'u'
    call print
    load 'r'
    call print
    load ' '
    call print

    load 'n'
    call print
    load 'a'
    call print
    load 'm'
    call print
    load 'e'
    call print
    load '?'
    call print
    load 0
    call print
    load 10
    call print

    ret

hello:
    load 'H'
    store *5
    load 'e'
    store *6
    load 'l'
    store *7
    load 'l'
    store *8
    load 'o'
    store *9
    load ','
    store *10
    load ' '
    store *11

    ret
