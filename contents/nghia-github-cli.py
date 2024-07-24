import os
import shutil
import subprocess


def Create(name, type):

    if type not in ["public", "private"]:
        raise ValueError("type là 'công khai' hoặc 'riêng tư'")

    subprocess.run(
        f" gh repo create --{type} {name} ",
        shell=True
    )


# def Delete(name):
#     subprocess.run(
#         f" gh repo delete --yes {name} ",
#         shell=True
#     )


if __name__ == "__main__":
    author = "vuvannghia452002"
    author = "vuvannghia452002"
    author = "vuvannghia452002"
    author = "whynotnghiavu"


# gh auth login
# gh auth refresh -h github.com -s delete_repo

    list_name = [
        # "nghia-format-gui",
        # "nghia-learn-nestjs",
        # "nghia-vscode",
        "nghia-windows",
        "nghia-ubuntu",





        # "nghia-chrome-passwords",

        # "nghia-windows-unikey",
        # "nghia-windows-unikey",
        # "nghia-github-push",



        # "nghia-windows-unikey",
        # "nghia-windows-unikey",
        # "nghia-windows-unikey",

        # "nghia-push",
        # "nghia-test-tikz",

        # "nghia-delete-empty-folder",
        # "nghia-rename-time",
        # "nghia-ubuntu-link",
        # "nghia-ubuntu",

        # "nghia-google-map",
        # "nghia-scrapy-topcv-crawler",

        # "nghia-note",
        # "nghia-step-recorder",
    ]

    list_name = list(set(list_name))

    for name in list_name:
        print(f"🚀 \033[32m{name}\033[0m")

        Create(name, "public")
        # Create(name, "private")

        # Delete(name)
