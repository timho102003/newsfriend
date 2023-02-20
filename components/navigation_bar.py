import dash
import dash_bootstrap_components as dbc

# from config import COUNTRY_LIST

children = [dbc.DropdownMenuItem("More countries", header=True)]

children += [
    dbc.DropdownMenuItem(page["name"], href=page["path"])
    for page in dash.page_registry.values()
    if page["module"]
    not in ["pages.not_found_404", "pages.main_page", "pages.blog_content"]
]

nav_bar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("United State", href="/")),
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
    style={
            "height": "80px",
            # "object-fit": "cover",
            "borderBottomLeftRadius": "40px",
            "borderBottomRightRadius": "40px",
            "margin-left": "50px",
            "margin-right": "50px",
            "font-size": "20px"
    }
)

__all__ = ["nav_var"]
