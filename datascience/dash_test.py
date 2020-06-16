import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)
df = pd.read_csv("country_profile_variables.csv")

app.layout = html.Div(
    [
        dcc.Graph(
            id='gdp',
            figure={
                'data': [
                    dict(
                        x=df[df['country'] == i]['Population density (per km2, 2017)'],
                        y=df[df['country'] == i]['GDP per capita (current US$)'],
                        text=df[df['country'] == i]['country'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in df.country.unique()
                ],
                'layout': dict(
                    xaxis={'type': 'linear', 'title': 'Population density (per km2, 2017)'},
                    yaxis={'title': 'GDP per capita (current US$)'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
