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


def Delete(name):
    subprocess.run(
        f" gh repo delete --yes {name} ",
        shell=True
    )


if __name__ == "__main__":
    author = "vuvannghia452002"
    author = "vuvannghia452002"
    author = "vuvannghia452002"
    author = "whynotnghiavu"


# gh auth login
# gh auth refresh -h github.com -s delete_repo

    list_name = [

        # "nghia-auto-microsoft-forms",
        #         "nghia-contact-manager",
        #         "nghia-python-requirements",

        # "nghia-oop-adapter-round-square",

        # "nghia-work-cv",

        # "einvoice-system",

        # "nghia-internship",


        #         "nghia-einvoice-system",



        # "nghia-scrapy-topcv-crawler",




        #  "nghia-contact-manager",

        #  "nghia-crawl-data-scrapy-topcv-crawler",

        #  "nghia-einvoice-system",

        #  "nghia-oop-adapter-round-square",
        #  "nghia-extensions-create-file",
        #  "nghia-extensions-create-folder",




        #  "nghia-extensions-create-folder",

        # nghia-delete-empty-folder
        # nghia-delete-empty-folder
        # nghia-delete-empty-folder
        # nghia-delete-empty-folder
        # nghia-delete-empty-folder



        # "nghia-extensions-rename-time",
        # "nghia-extensions-delete-empty-folder",
        # "nghia-extensions-video-VN",
        # "nghia-extensions-convert-text-pascal",


        # "nghia-extensions-filter-file",


        # "20241",
        # "nghia-extensions-xem-video",

        # "nghia-extensions-find-text",
        # "nghia-extensions-shutdown-computer",







        "nghia-work-backend",

    ]

    list_name = list(set(list_name))

    for name in list_name:
        print(f"🚀 \033[32m{name}\033[0m")

        Create(name, "public")
        # Create(name, "private")

        # Delete(name)
