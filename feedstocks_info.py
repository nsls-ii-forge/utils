import glob

import git
import pandas as pd
from tabulate import tabulate

all_feedstocks = sorted(glob.glob("*-feedstock"))

columns = ['Name', 'Branch', 'Changed?']

# header = f'{"#":>5s} | {"Name":^40s} | {"Branch":^20s} | {"Changed?":^10s} |'
# separator = "-" * len(header)
# print(f"\nTotal number of feedstocks: {len(all_feedstocks)}\n")
# print(f"{separator}\n{header}\n{separator}")

info = []
for i, feedstock in enumerate(all_feedstocks):
    repo = git.Repo(feedstock)
    info.append([feedstock, repo.active_branch.name, repo.is_dirty()])
    # print(f"{i:>5d} | {feedstock:40s} | {repo.active_branch.name:^20s} | {str(repo.is_dirty()):^10s} |")  # noqa

# print(separator)

df = pd.DataFrame(info, columns=columns)
print(tabulate(df, headers=df.columns))
