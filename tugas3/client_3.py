import logging
import requests
import os
import threading

def download_gambar(url=None):
    if url is None:
        return False
    ff = requests.get(url)
    types = dict()
    types['image/png']='png'
    types['image/jpg']='jpg'
    types['image/jpg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if content_type in list(types.keys()):
        fileName = os.path.basename(url)
        extension = types[content_type]
        logging.warning(f"writing {fileName}.{extension}")
        fp = open(f"{fileName}.{extension}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':

    image_list = [
        "https://i.graphicmama.com/blog/wp-content/uploads/2019/10/07142805/graphic-design-trends-2020-breaking-the-rules.jpg",
        "https://uptown.id/wp-content/uploads/2019/12/20-Bisnis-Online-di-Indonesia-Yang-Akan-Booming-di-Tahun-2020-960x528.jpg",
        "https://www.mandreel.com/indonesia/wp-content/uploads/2018/12/logo-design-services-newstarship.jpg"
    ]

    thread_list = []
    for i in range(len(image_list)):
        t = threading.Thread( target=download_gambar, args=(image_list[i],) )
        thread_list.append(t)

    for each_thread in thread_list:
        each_thread.start()