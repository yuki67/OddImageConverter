import Converter_Excel
import Converter_Shell

converters = [
    ["excel", 200, Converter_Excel],
    ["shell script", 75, Converter_Shell],
    ["html", 300, None]
]


def convert(img, filename):
    """ imgを変換する """
    # 画像が大きすぎるときは縮小してから色配列にする
    # 長い方の辺がデフォルトのサイズで一番大きいものになるようにする
    max_len = max(converters, key=lambda x: x[1])[1]
    if max(img.size) > max_len:
        factor = max_len / max(img.size)
        img = img.resize((int(i * factor) for i in img.size))

    # 色配列を作成
    width, height = img.size
    img_array = list(img.getdata())
    img_array = [img_array[i * width:(i + 1) * width] for i in range(height)]
    for _, size, converter in converters:
        converter.convert(img_array, size, filename[:-4])
