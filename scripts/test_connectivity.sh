for i in $(cat ip); do
    ((count = 100))                            # Maximum number to try.
    while [[ $count -ne 0 ]] ; do
        ping -c 1  $i                     # Try once.
        rc=$?
        if [[ $rc -eq 0 ]] ; then
            ((count = 1))                      # If okay, flag to exit loop.
        fi
        ((count = count - 1))                  # So we don't go forever.
    done
done

if [[ $rc -eq 0 ]] ; then                  # Make final determination.
    echo `say The internet is back up.`
else
    echo `say Timeout.`
fi
