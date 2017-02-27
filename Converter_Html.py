import Converter


def convert(array, size, filename):
    ConverterHtml().convert(array, size, filename)


class ConverterHtml(Converter.Converter):
    """ HTMLでお絵かきするためのクラス """

    def __init__(self):
        super().__init__()
        self.filename = None
        self.str = ""

    def open(self, color_array, size, filename):
        """ 初期設定を行う """
        self.filename = filename + ".html"
        d = max(1, max(len(color_array), len(color_array[0])) / size)
        width, height = len(color_array[0]) * d, len(color_array) * d
        self.str += "<html>\n" + \
                    "<head><title>" + self.filename[:-5] + "</title></head>\n" + \
                    "<body><table border=\"0px\" cellspacing=\"0px\" width=\"%d\" height=\"%d\">\n" % (width, height) + \
                    "<tr>\n"

    def put_pixel(self, color):
        """ pointを描画する """
        self.str += "<th bgcolor=\"%s\"/>" % (self.color_code_from_rgb(color))

    def new_line(self):
        """ 行を改める """
        self.str += "</tr>\n<tr>"

    def close(self):
        """ ファイルを閉じる """
        self.str += "</body></html>"
        file = open(self.filename, "w")
        file.write(self.str)
        file.close()

    @staticmethod
    def color_code_from_rgb(rgb):
        """ 色のRGB表記(R, G, B)を#RGBに直す """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str
