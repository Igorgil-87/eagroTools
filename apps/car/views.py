from django.shortcuts import render
import plotly.express as px
from plotly.offline import plot
import geopandas as gpd

# Create your views here.
def car(request):
    df = px.data.election()
    geo_df = gpd.GeoDataFrame.from_features(
        px.data.election_geojson()["features"]
    ).merge(df, on="district").set_index("district")

    fig = px.choropleth_mapbox(geo_df,
                               geojson=geo_df.geometry,
                               locations=geo_df.index,
                               color="Joly",
                               center={"lat": 45.5517, "lon": -73.7073},
                               mapbox_style="open-street-map",
                               zoom=8.5)




    gantt_plot = plot(fig, output_type = "div")
    context = {'car_div': gantt_plot}
    return render(request, 'main/car.html', context)