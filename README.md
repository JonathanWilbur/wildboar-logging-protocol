# Wildboar Logging Protocol (WELP)

* Author: [Jonathan M. Wilbur](https://jonathan.wilbur.space) <[jonathan@wilbur.space](mailto:jonathan@wilbur.space)>
* Copyright Year: 2019
* License: [MIT License](https://mit-license.org/)

This is currently abandoned, but I might come back to it.

## The Problems of Existing Logging Protocols

1. Existing logging protocols don't specify, as a part of the protocols
   themselves, the person or team to whose attention the log event should
   be brought.
2. Existing logging protocols do not have a concept of urgency; they only use
   the naively simple system of log levels, which are typically "debug,"
   "info," "warning," and "error." Not all severe log events warrant immediate
   attention, and not all log events that warrant immediate attention are
   severe.
3. Existing logging protocols only have a system of negative severity, which is
   to say that log levels vary from "neutral" to "extremely bad", rather than
   ranging from "unimportant" to "important".
4. Existing logging protocols, such as rsyslog, are susceptible to log
   splitting, because they use newlines as delimiters for log messages.
5. Many logging protocols do not use any compression in transit, and use simple
   text-based protocols, or computationally-expensive textual protocols, such
   as XML or JSON over HTTP.

## See Also

* [Protocol Buffers](https://developers.google.com/protocol-buffers)

## Contact Me

If you would like to suggest fixes or improvements on this library, please just
[leave an issue on this GitHub page](https://github.com/JonathanWilbur/wildboar-logging-protocol/issues). If you would like to contact me for other reasons,
please email me at [jonathan@wilbur.space](mailto:jonathan@wilbur.space)
([My GPG Key](https://jonathan.wilbur.space/downloads/jonathan@wilbur.space.gpg.pub))
([My TLS Certificate](https://jonathan.wilbur.space/downloads/jonathan@wilbur.space.chain.pem)). :boar: