
    
  
from pathlib import Path
from html import escape
from turtle import width
from urllib.parse import quote

DEFAULT_OWNER = "vividblueprint"
STYLE = "flat"
IMG_SIZE = 500

def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def main() -> None:
    print("=" * 45)
    print("       GitHub README Badge Generator")
    print("=" * 45)

    owner = ask("GitHub owner", DEFAULT_OWNER)
    repo = ask("Repository name")
    
    while not repo:
        print("Repository name is required.")
        repo = ask("Repository name")
    
    image_url = ask("Image URL (optional, Enter to skip)")
    if image_url:
        img_width = ask("Image width ", IMG_SIZE)
            
    repo_title = ask("Repository Title (optional, Enter to skip)")

    base = f"{quote(owner, safe='')}/{quote(repo, safe='')}"
    owner_url = f"https://github.com/{quote(owner, safe='')}"
    url = f"https://github.com/{base}"

    badges = {
        "GitHub": f"[![GitHub](https://img.shields.io/badge/GitHub-{quote(owner, safe='')}-181717?logo=github&logoColor=white)]({owner_url})",
        # "Profile Views": f"[![Profile Views](https://komarev.com/ghpvc/?username={quote(owner, safe='')}&label=Profile%20Views&color=blueviolet&style={STYLE})]({owner_url})",
        "Issues": f"[![Issues](https://img.shields.io/github/issues/{base}?style={STYLE})]({url}/issues)",
        "Pull Requests": f"[![Pull Requests](https://img.shields.io/github/issues-pr/{base}?style={STYLE})]({url}/pulls)",
        "Contributors": f"[![Contributors](https://img.shields.io/github/contributors/{base}?style={STYLE})]({url}/graphs/contributors)",
        "Stars": f"[![Stars](https://img.shields.io/github/stars/{base}?style={STYLE})]({url}/stargazers)",
        "Forks": f"[![Forks](https://img.shields.io/github/forks/{base}?style={STYLE})]({url}/forks)",
        "Watchers": f"[![Watchers](https://img.shields.io/github/watchers/{base}?style={STYLE})]({url}/watchers)",
        "Last Commit": f"[![Last Commit](https://img.shields.io/github/last-commit/{base}?style={STYLE})]({url}/commits)",
        "Monthly Commits": f"[![Monthly Commits](https://img.shields.io/github/commit-activity/m/{base}?style={STYLE})]({url}/commits)",
        "Languages": f"[![Languages](https://img.shields.io/github/languages/count/{base}?style={STYLE})]({url})",
        "Code Size": f"[![Code Size](https://img.shields.io/github/languages/code-size/{base}?style={STYLE})]({url})",
        "Repo Size": f"[![Repo Size](https://img.shields.io/github/repo-size/{base}?style={STYLE})]({url})",
        "Total Commits": f"[![Total Commits](https://img.shields.io/github/commit-activity/t/{base}?style={STYLE}&label=Total%20Commits)]({url}/commits)",
        "Files": f"[![Files](https://img.shields.io/github/directory-file-count/{base}?type=file&style={STYLE})]({url}/tree/HEAD)",
        "License": f"[![License](https://img.shields.io/github/license/{base}?style={STYLE})]({url}/blob/HEAD/LICENSE)",
    }

    parts = ['<div align="center">', '']
    if image_url:
        image_url="./assets/"+image_url
        parts.extend([f'<img src="{escape(image_url, quote=True)}" alt="Repository Banner" width="{img_width}">', ''])
    
    if repo_title:
        parts.extend([
            '<h1 align="center" >\n',
            *['<img width="25px" src="https://em-content.zobj.net/source/microsoft-teams/337/heart-with-ribbon_1f49d.png"/>' for _ in range(3)],
            f"<b>{repo_title}</b>",
            *['<img width="25px" src="https://em-content.zobj.net/source/microsoft-teams/337/heart-with-ribbon_1f49d.png"/>' for _ in range(3)],
            '\n</h1>\n',
        ])
    parts.extend(badges.values())
    parts.extend(['', '</div>', ''])

    output = Path('BADGES.md')
    output.write_text('\n'.join(parts), encoding='utf-8')
    print(f"\nGenerated {len(badges)} clickable badges!")
    print(f"Repository: {url}")
    print(f"Saved to: {output.resolve()}")
    print("\n" + output.read_text(encoding='utf-8'))
    print("Note: Shields.io's directory-file-count endpoint may be unsupported.")


if __name__ == '__main__':
    main()


