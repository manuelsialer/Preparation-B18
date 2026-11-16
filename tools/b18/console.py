# -*- coding: utf-8 -*-
"""Consola UTF-8 para Windows y ayudas de impresión."""
import io
import sys


def setup_console():
    """Reconfigura stdout/stderr a UTF-8 (idempotente)."""
    for stream in ('stdout', 'stderr'):
        s = getattr(sys, stream, None)
        if s is None:
            continue
        try:
            if getattr(s, 'encoding', '').lower() not in ('utf-8', 'utf8'):
                setattr(sys, stream, io.TextIOWrapper(s.buffer, encoding='utf-8'))
        except Exception:  # pragma: no cover - consolas sin buffer
            pass


def banner(text, char='='):
    line = char * 74
    print('\n' + line + '\n' + text + '\n' + line)
