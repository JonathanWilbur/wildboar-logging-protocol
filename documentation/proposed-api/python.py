#!/usr/bin/python

wl = WELP.WelpLog()
wl.log(
    containsPasswords=True,
    severity=WELP.MEDIUM,
    urgency=WELP.PATIENT,
    concerns=[ WELP.CONFIDENTIALITY, WELP.LEGALITY ],
    message={
        client: "test-client.domain.local",
        authFailureReason: "PASSWORD",
        username: "bob",
        password: "example"
    })