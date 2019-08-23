import requests

# Variables
gh_org = 'nsls-ii-forge'
api_url = f'https://api.github.com/orgs/{gh_org}'

all_repos = []

page = 1
while True:
    resp = requests.get(f'{api_url}/repos?page={page}')
    if not resp.json():
        break
    page += 1
    all_repos.extend(resp.json())

# print(f'Number of all repos: {len(all_repos)}')

all_feedstocks = [r for r in all_repos if r['name'].endswith('-feedstock')]
# print(f'Number of all feedstocks: {len(all_feedstocks)}')

for feedstock in all_feedstocks:
    print(feedstock['html_url'])
