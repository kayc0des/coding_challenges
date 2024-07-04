# Getting Started with CLIs in Python: sys.argv vs argparse

Python comes with a couple of tools that you can use to write command-line interfaces for your programs and apps. If you need to quickly create a minimal CLI for a small program, then you can use the argv attribute from the sys module. This attribute automatically stores the arguments that you pass to a given program at the command line.

`sys.argv` -> The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not).

```Python
import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)

target_dir = Path(sys.argv[1])

if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```