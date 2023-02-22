def gray_encode( bn ):
    assert bn >= 0

    assert type( bn ) in [ int, long ]
    return bn ^ ( bn / 2 )
