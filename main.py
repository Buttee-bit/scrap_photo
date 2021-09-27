import requests
import os

GLOBAL_URL = 'https://coop-land.ru/helpguides/top/21427-sekretnye-koncovki-v-igrah-kotorye-vy-mogli-propustit.html'
GlOBAL_PATH = 'case_page_html\\code_html.txt'


def request(url):
    try:
        r = requests.get(url,stream=True)
        if r.status_code == 200:
            return r.text
    except Exception as e:
        print (e)

def create_file_text_page(text_page):
    with open(f'case_page_html\\code_html.txt', 'w', encoding='utf-8') as code_html:
        code_html.write(text_page)


def parse_page_html():
    list_raw_link = []
    with open(GlOBAL_PATH, 'r', encoding='utf-8') as read_html:
        lines = read_html.readlines()
        for line in lines:
            if '.png' in line or 'img' in line:
                list_raw_link.append(line)
    return list_raw_link


def determin(list_mb_link):
    list_link_= []
    str_data_src = ['data-src','src']
    str_endl_link = '"'
    for i in list_mb_link:
        if 'https' in i:
            list_link_.append(i)

    list_link_raw = []
    for bad_link in list_link_:
        count = 0
        FLAG = ''
        for sword in bad_link:
            count += 1
            FLAG += sword
            if str_data_src[0] in FLAG :
                list_link_raw.append(bad_link[count+2:])
                break
    list_links = []
    for j in list_link_raw:
        count = 0
        for sword in j:
            str_end_ = sword
            count += 1
            if str_end_ == str_endl_link:
                list_links.append(j[:count-1])
                break

    return list_links


    



def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name (url):
    try:
        name = url.split('/')[-1]
        print(name)
        return name.replace('"','')
    except Exception as e:
        print (e)

def save_img(name,file_object):
    with open(f'case_jpg/{name}','bw') as f:
        for chunk in file_object.iter_content(2*8192):
            f.write(chunk)


def main():
    text_page = request(GLOBAL_URL)
    #print(text_page)
    create_file_text_page(text_page)
    determin(parse_page_html())
    list_png = determin(parse_page_html())

    for url in list_png:
        try:
            save_img(get_name(url), get_file(url))
        except Exception as e:
            print (e)
main()