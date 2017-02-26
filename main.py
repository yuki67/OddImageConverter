import argparse
from PIL import Image
import OddImageConverter


def prompt():
    """ メイン処理 """
    # 引数を処理
    parser = argparse.ArgumentParser(description="convert image into odd formats.")
    parser.add_argument("-l", action="store_true", help="show the formats into which this program can convert.")
    parser.add_argument(dest="filename", action="store", help="name of the image.", default="", nargs="?")
    args = parser.parse_args()

    # list引数を処理
    if args.l:
        print("formats".center(15), "|", "default size (px)".center(20))
        print("".center(36, "-"))
        for form, size, _ in OddImageConverter.converters:
            print(form.rjust(15), "|", str(size).rjust(15))

    # 変換を実行
    if args.filename:
        img = Image.open(args.filename)
        OddImageConverter.convert(img)

if __name__ == "__main__":
    prompt()
