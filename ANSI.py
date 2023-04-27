#! /usr/bin/env python3

class FG:
  BLACK            = "\u001b[30m"
  RED              = "\u001b[31m"
  GREEN            = "\u001b[32m"
  YELLOW           = "\u001b[33m"
  BLUE             = "\u001b[34m"
  MAGENTA          = "\u001b[35m"
  CYAN             = "\u001b[36m"
  WHITE            = "\u001b[37m"
  
class BG:
  BLACK     = "\u001b[40m"
  RED       = "\u001b[41m"
  GREEN     = "\u001b[42m"
  YELLOW    = "\u001b[43m"
  BLUE      = "\u001b[44m"
  MAGENTA   = "\u001b[45m"
  CYAN      = "\u001b[46m"
  WHITE     = "\u001b[47m"

class UTIL:
  RESET     = "\u001b[0m"
  BOLD      = "\u001b[1m"
  ITALICS   = "\u001b[3m"
  UNDERLINE = "\u001b[4m"
  REVERSE   = "\u001b[7m"

  CLEAR     = "\u001b[2J"
  CLEARLINE = "\u001b[2K"

  UP        = "\u001b[1A"
  DOWN      = "\u001b[1B"
  RIGHT     = "\u001b[1C"
  LEFT      = "\u001b[1D"

  NEXTLINE  = "\u001b[1E"
  LASTLINE  = "\u001b[1F"

  BEGIN     = "\u001b[0F"
  TOP       = "\u001b[0;0H"

  SAVE      = "\u001b[s"
  RESTORE   = "\u001b[u"

  VISIBLE   = "\u001b[?25h"
  INVISIBLE = "\u001b[?25l"

def SetCursor(col, row):
    pos = f"{UTIL.DOWN}" * row + f"{UTIL.RIGHT}" * col
    print(f"{UTIL.TOP}{pos}",end="")

def SaveCursor():
    print(UTIL.SAVE, end="")

def RestoreCursor():
    print(UTIL.RESTORE, end="")

def CursorOff():
  print(UTIL.INVISIBLE, end="")

def CursorOn():
  print(UTIL.VISIBLE, end="")

def Clear():
    print(f"{UTIL.TOP}{UTIL.CLEAR}",end="")
