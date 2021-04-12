import generator
import json
import os

def createFile(username, name, KPIs, charts):
    f = open('templates/' + username + '\\' + name + '.html', "w")
    f.write('<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"/> <meta http-equiv="X-UA-Compatible" content="IE=edge"/> <meta name="viewport" content="width=device-width, initial-scale=1.0"/> <link rel="stylesheet" type="text/css" href="{{url_for("static", filename="navstyle.css")}}"/> <script src="https://kit.fontawesome.com/64d58efce2.js" crossorigin="anonymous" ></script> <link rel="stylesheet" type="text/css" href="{{url_for("static", filename="dashboard.css")}}"/> <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.0.2/echarts.min.js" integrity="sha512-t9GZbGKCH5MuYUFsq5AdrhllT0kdnc2fNMizKDgLXBBXgHP2dXxjRPOzYJauAXW9OXLlSYELUqWD30k7cb0Mkg==" crossorigin="anonymous" ></script> <script src="{{url_for("static", filename="general.js")}}"></script> <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script> <script src="{{url_for("static", filename="jquery-3.6.0.js")}}"></script> <title>' + name + '</title> </head> <body>{% include "includes/_navbar.html" %}<div class="halfcards" id="halfcards"></div><div class="cards" id="cards"></div><script type="text/javascript">getData(); </script></body></html>')
    os.mkdir('CSV\\' + username + '\\' + name)
    with open('CSV\\' + username + '\\' + name + '\\template.csv', 'w') as fc:
        template = []
        for k in KPIs:
            for column in KPIs[k]['columns']:
                template.append(column)
        for chart in charts:
            for column in charts[chart]['columns']:
                template.append(column)
        uniqueTemplate = list(set(template))
        for i in range(0,len(uniqueTemplate)):
            if(i):
                fc.write(',')    
            fc.write(uniqueTemplate[i])
        fc.close()
    f.close()

def createConfig(username, name ,KPIs, charts):
    f = open('templates/' + username + '\\' + name + '.json', "w")
    template = {}
    template['kpi'] = KPIs
    template['chart'] = charts
    f.write(json.dumps(template))
    f.close()

def generate(username ,name, KPIs, charts):
    createFile(username, name, KPIs, charts)
    createConfig(username, name, KPIs, charts)
    generator.addToSelector(username, name)
    generator.addToUpload(username, name)