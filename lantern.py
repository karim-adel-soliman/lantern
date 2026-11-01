import argparse
from export import export_csv
from tasks import list_tasks

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="cmd")
sub.add_parser("add")

list_parser = sub.add_parser("list")
list_parser.add_argument("--done", action="store_true", help="Show only completed tasks")

export_parser = sub.add_parser("export")
export_parser.add_argument("--csv", action="store_true", help="Export tasks as CSV")

args = parser.parse_args()

if args.cmd == "list":
    tasks = list_tasks(only_done=args.done)
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task["title"])
elif args.cmd == "export" and args.csv:
    print(export_csv(list_tasks()))
else:
    print(f"Running {args.cmd}")