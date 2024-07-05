import sys
from pathlib import Path

args_count = len(sys.argv)

if args_count > 2:
    print(f'One argument expected, {args_count - 1} passed')
    raise SystemExit(2)
elif args_count < 2:
    print(f'You must specify the target directory')
    raise SystemExit(2)

target_dir = Path(sys.argv[1]).resolve()
print(target_dir)

if not target_dir.is_dir():
    print('The target directory does not exist')
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
