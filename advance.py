import os
from shutil import move
from time import sleep

dir = ""

def main():
    if dir:
        os.chdir(dir)
    try:
        os.mkdir("documents")
    except:
        pass
    try:
        os.mkdir("videos")
    except:
        pass
    try:
        os.mkdir("music")
    except:
        pass
    try:
        os.mkdir("pictures")
    except:
        pass
    try:
        os.mkdir("executables")
    except:
        pass
    try:
        os.mkdir("other")
    except:
        pass
    while True:
        filenames = GetNames()
        for i in filenames:
            if i and i != "main.py":
                Cdir = os.path.join(os.getcwd(), i)
                if os.path.exists(Cdir):
                    extinsion = i.split(".")[-1]
                    if i.find(".") > 0:
                        try:
                            Move(i, extinsion, os.getcwd())
                        except:
                            pass
        sleep(20)


def Move(filename, extension, Cdir):
    extension = extension.lower()
    document_extensions = [
        "doc",
        "docx",
        "txt",
        "pdf",
        "rtf",
        "odt",
        "csv",
        "xlsx",
        "xls",
        "pptx",
        "ppt",
        "odp",
        "html",
    ]

    video_extensions = [
        "mp4",
        "avi",
        "mkv",
        "mov",
        "wmv",
        "flv",
        "webm",
        "m4v",
        "mpeg",
        "mpg",
        "3gp",
        "3g2",
    ]

    music_extensions = [
        "mp3",
        "wav",
        "ogg",
        "flac",
        "aac",
        "wma",
        "m4a",
        "alac",
        "aiff",
        "mid",
        "midi",
    ]

    picture_extensions = [
        "jpg",
        "jpeg",
        "png",
        "gif",
        "bmp",
        "tiff",
        "webp",
        "svg",
        "ico",
        "jfif",
        "heif",
        "raw",
    ]

    executable_extensions = [
        "exe",
        "dmg",
        "app",
        "apk",
        "msi",
        "bat",
        "sh",
    ]
    if extension in document_extensions:
        document(filename, Cdir)
    elif extension in video_extensions:
        video(filename, Cdir)
    elif extension in music_extensions:
        music(filename, Cdir)
    elif extension in picture_extensions:
        picture(filename, Cdir)
    elif extension in executable_extensions:
        executable(filename, Cdir)
    else:
        other(filename, Cdir)


def document(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "documents"), filename),
        )


def video(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "videos"), filename),
        )


def music(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "music"), filename),
        )


def picture(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "pictures"), filename),
        )


def executable(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "executables"), filename),
        )


def other(filename, Cdir):
    if filename and Cdir:
        move(
            os.path.join(Cdir, filename),
            os.path.join(os.path.join(Cdir, "other"), filename),
        )


def GetNames():
    directory_path = os.getcwd()
    os.chdir(directory_path)
    return os.listdir()


if __name__ == "__main__":
    main()
