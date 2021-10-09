import json
from plotly import offline
from plotly.graph_objs import Scattergeo,Layout



def get_data(Json_file):



    infile= open(Json_file,'r')
    #outfile= open('readable_eq_data.json','w')

    eq_data = json.load(infile)
#json.dump(eq_data,outfile,intent=4)

    brightness=[]
    lons=[]
    lats=[]

    for eq in eq_data:
        if float(eq['brightness'])>450:
            bright=float(eq['brightness'])
            lon=float(eq['longitude'])
            lat=float(eq['latitude'])
            brightness.append(bright)
            lons.append(lon)
            lats.append(lat)
    return (brightness,lons,lats)

def Plot_data(csv,Title1):

    brightness,lons,lats=get_data(csv)
    data = [{
        'type': 'scattergeo',
        'locationmode' : 'USA-states',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [1/30* bright for bright in brightness],
            'color': brightness,
            'colorscale': 'Inferno',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'},
        },
    }]

    my_layout = Layout(title=Title1
         )
    fig = {'data': data, 'layout': my_layout}

    offline.plot(fig, filename=Title1+'.html')
     


Plot_data('US_fires_9_1.json','US_fires_9_1_To_13')
Plot_data('US_fires_9_14.json','US_fires_9_14_To_20')



