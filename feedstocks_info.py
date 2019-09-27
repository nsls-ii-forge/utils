import glob
import pandas as pd
import git

df = pd.DataFrame()

all_feedstocks = sorted(glob.glob("*-feedstock"))

header = f'{"#":>5s} | {"Name":^40s} | {"Branch":^20s} | {"Changed?":^10s} |'
separator = "-" * len(header)

print(f"\nTotal number of feedstocks: {len(all_feedstocks)}\n")
print(f"{separator}\n{header}\n{separator}")

for i, feedstock in enumerate(all_feedstocks):
    repo = git.Repo(feedstock)
    print(f"{i:>5d} | {feedstock:40s} | {repo.active_branch.name:^20s} | {str(repo.is_dirty()):^10s} |")  # noqa

print(separator)
