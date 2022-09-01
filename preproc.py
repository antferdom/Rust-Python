from typing import Dict, List, Iterable
import os
import gzip
import json

# Globals
ROOT = os.path.dirname(os.path.abspath(__file__))
FILE: str = os.path.join(ROOT, "check_output_logs.jsonl")

# cargo check --message-format json >> check_output_logs.jsonl
# Overwrite file content
if os.path.exists(FILE):
    if(file_size := os.path.getsize(FILE)) >= 0: 
        os.remove(FILE)
        os.system("cargo check --message-format json >> check_output_logs.jsonl")
else:
    os.system("cargo check --message-format json >> check_output_logs.jsonl")

# if(file_size := os.path.getsize(FILE)) >= 0: os.system("rm check_output_logs.jsonl | cargo check --message-format json >> check_output_logs.jsonl")
# os.system("cargo check --message-format json >> check_output_logs.jsonl")


def read_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each jsonl line and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with open(filename, "rb") as gzfp:
            with gzip.open(gzfp, 'rt') as fp:
                for line in fp:
                    if any(not x.isspace() for x in line):
                        yield json.loads(line)
    else:
        with open(filename, "r") as fp:
            for line in fp:
                if any(not x.isspace() for x in line):
                    # print(line)
                    yield json.loads(line)

def read_logs() -> Dict[str, Dict]:
    return {log["reason"]: log for log in read_jsonl(FILE)}


logs: Dict[str, Dict] = read_logs()
print("Rust Cargo build status {}".format(logs["build-finished"]["success"]))
print(logs["compiler-message"]["message"])
print("What logs have?")
