import glob
import os

import git
import markdown
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

all_feedstocks = sorted(glob.glob("*-feedstock"))

# header = f'{"#":>5s} | {"Name":^40s} | {"Branch":^20s} | {"Changed?":^10s} |'
# separator = "-" * len(header)
# print(f"\nTotal number of feedstocks: {len(all_feedstocks)}\n")
# print(f"{separator}\n{header}\n{separator}")

info = []
for i, feedstock in enumerate(all_feedstocks):

    # Get version info from README.md's badge via requesting the info from svg:
    try:
        with open(os.path.join(feedstock, 'README.md')) as f:
            html_text = markdown.markdown(f.read())
            html = BeautifulSoup(html_text, features='lxml')
            svg = html.findAll('img', attrs={'alt': 'Conda Version'})[0]
            r = requests.get(svg.attrs['src'])
            svg_html = BeautifulSoup(r.text, features='lxml')
            version_tag = svg_html.findAll('text')[-1]
            version = version_tag.text
    except Exception:
        version = ''

    # Extract info from git:
    repo = git.Repo(feedstock)
    info.append([feedstock, repo.active_branch.name, repo.is_dirty(), version])
    # print(f"{i:>5d} | {feedstock:40s} | {repo.active_branch.name:^20s} | {str(repo.is_dirty()):^10s} |")  # noqa

# print(separator)
columns = ['Name', 'Branch', 'Changed?', 'Version']
df = pd.DataFrame(info, columns=columns)
print(tabulate(df, headers=df.columns))
