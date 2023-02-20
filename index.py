import dash
import dash_bootstrap_components as dbc

from app import app
from components.navigation_bar import nav_bar

app.layout = dbc.Container(
    [
        nav_bar,
        dash.page_container,
    ],
    className="dbc",
    fluid=True,
    # style={
    #             "background-image": "url('/assets/imgs/newsfriend_banner_v2.png')",
    #             "background-size": "cover",
    #             "background-position": "center",
    #             "height": "400px",
    #             "position": "relative",
    #         },
)

if __name__ == "__main__":
    app.run_server(debug=True)
