import dash
from dash import html

from global_var import article_database
from util import convert_timezone
from config import COUNTRY_LIST
from bson import ObjectId
dash.register_page(__name__, path_template="<country>/news_id_<article_id>")

def layout(country=None, article_id=None):
    ori_tz = list(filter(lambda x: x[0] == country, COUNTRY_LIST))[0][2]
    selected_article = article_database.retrieve_article(_id=ObjectId(article_id))
    meta_info = ""
    author = ""
    if selected_article["authors"]:
        author = [auth["name"] for auth in selected_article["authors"] if auth["type"]=="author"]
        if author: author = ",".join(author)
    update_time = (
        convert_timezone(str(selected_article["dateTimePub"]), ori_timezone=ori_tz) if selected_article["dateTimePub"] else ""
    )
    meta_info += (
        f"Author: {author} | "
        if author
        else "Author: Please refer to the original link | "
    )
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
    img_src = (
        selected_article["image"]
        if selected_article["image"]
        else None
    )

    if img_src:
        image_with_caption = html.Div(
            [
                html.Img(
                    src=img_src,
                    style={"display": "block", "margin": "0 auto", "width": "50%"},
                ),
                html.Div(
                    style={"text-align": "center", "font-size": "0.5em"},
                    children=[html.P(f"reference link: {img_src}", style={"margin": 0})],
                )
            ]
        )
    else:
        image_with_caption = html.Div([])

    article_list = [html.P(meta_info), image_with_caption, body_content]
    # for content in body_content:
    #     article_list.append(html.P(content, style={"margin": "1em 50"}))
    article = html.Div([*article_list])
    return html.Div(children=[html.H1(children=selected_article["title"]), article])
