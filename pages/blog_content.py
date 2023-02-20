import dash
from bson import ObjectId
from dash import html

from config import COUNTRY_LIST
from global_var import article_database
from util import convert_timezone

dash.register_page(__name__, path_template="<country>/news_id_<article_id>")


def layout(country=None, article_id=None):
    ori_tz = list(filter(lambda x: x[0] == country, COUNTRY_LIST))[0][2]
    selected_article = article_database.retrieve_article(_id=ObjectId(article_id))
    meta_info = ""
    author = ""
    if selected_article["authors"]:
        author = [
            auth["name"]
            for auth in selected_article["authors"]
            if auth["type"] == "author"
        ]
        if author:
            author = ",".join(author)
    update_time = (
        convert_timezone(str(selected_article["dateTimePub"]), ori_timezone=ori_tz)
        if selected_article["dateTimePub"]
        else ""
    )

    if author:
        meta_info += f"Author: {author} | "
    elif "uri" in selected_article:
        meta_info += "Author: {} | ".format(selected_article["uri"])
    else:
        "Author: None | "

    meta_info += (
        f"Published: {update_time}"
        if update_time
        else "Published: Please refer to the original link"
    )
    body_content = (
        selected_article["body"]
        if selected_article["body"] is not None
        else "Article content fail to retrieve"
    )
    img_src = selected_article["image"] if selected_article["image"] else None

    if img_src:
        image_with_caption = html.Div(
            [
                html.Img(
                    src=img_src,
                    style={"display": "block", "margin": "0 auto", "max-width": "100%"},
                ),
                html.Div(
                    style={"text-align": "center", "font-size": "0.5em"},
                    children=[                        html.P(f"reference link: {img_src}", style={"margin": 0})                    ],
                ),
            ],
            style={"max-width": "50em", "margin": "2em auto"},
        )
    else:
        image_with_caption = html.Div([])

    article_sections = [
        
        {
            "content": selected_article["body"] if selected_article["body"] else ""
        }
    ]

    sections = []
    for section in article_sections:
        section_content = html.Div(
            section['content'],
            style={"text-align": "justify", "line-height": "1.5em", "margin-bottom": "2em"}
        )
        if section['content']:
            sections.append(section_content)

    article_list = [
        html.P(meta_info, style={"text-align": "right"}),
        html.H1(selected_article["title"], style={"margin-top": "0.5em"}),
        image_with_caption,
        *sections
    ]
    article = html.Div(article_list, style={"max-width": "50em", "margin": "2em auto"})
    return html.Div(children=[article], style={"text-align": "center"})
