import dash_bootstrap_components as dbc

from config import COUNTRY_LIST

children = [dbc.DropdownMenuItem("More countries", header=True)]
for country in COUNTRY_LIST:
    children.append(dbc.DropdownMenuItem(country[0], href=country[1]))

nav_bar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("United States", href="#")),
        dbc.DropdownMenu(
            children=children,
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NewsFriend",
    brand_href="#",
    color="primary",
    dark=True,
)

__all__ = ["nav_var"]
