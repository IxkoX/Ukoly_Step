# page_generator.py
import json


a_element = """
<a href="{url}">
    <h2>{title}</h2>
    <img src ="{img}" alt="{title}" >
</a>
"""


def gen_list():
    with open ('C:/ŠKOLA ATD/IT_Step/Python/Ukoly_Step/Ukol_09/data.json', encoding='utf-8') as file:
        data = json.load(file)
        
        result = ''
        
        for item in data:
            # PRO TEST PRINTY
            # print(item['title'])
            # print(item['img'])
            # print(item['url'])
            # print()

            link = a_element.format(
                url = item['url'],
                title = item['title'],
                img = item['img']
            )
            result += link
        return result
def safe_list():
    list_html = gen_list()
    #print(list_html)

    with open('Ukoly_Step/Ukol_09/list.html',mode='r', encoding='utf-8') as file:
        html = file.read()
    html= html.replace('<!-- HTML -->',list_html)
        
    with open('Ukoly_Step/Ukol_09/output.html', mode='w', encoding='utf-8') as file:    
        file.write(html)


safe_list()  
