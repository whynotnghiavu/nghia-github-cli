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

        # "nghia-auto-microsoft-forms",
        # "nghia-contact-manager",


        # "nghia-work-cv",

        "einvoice-system",



        # "nghia-scrapy-topcv-crawler",

    ]

    list_name = list(set(list_name))

    for name in list_name:
        print(f"🚀 \033[32m{name}\033[0m")

        Create(name, "public")
        # Create(name, "private")

        # Delete(name)
