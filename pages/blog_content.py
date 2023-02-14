# TODO: AST will be remove when mongodb is added
import ast

import dash
from dash import html

from config import TEST_NEWS

dash.register_page(__name__, path_template="/news_id_<article_id>")


def layout(article_id=None):
    selected_article = TEST_NEWS.iloc[int(article_id), :]
    meta_info = ""
    if selected_article["author"]:
        author = ",".join(ast.literal_eval(selected_article["author"]))
    else:
        author = ""
    update_time = (
        selected_article["update_time"] if selected_article["update_time"] else ""
    )
    meta_info += (
        f"Author: {author} | "
        if author
        else "Author: Please refer to the original link | "
    )
    meta_info += (
        f"{update_time}"
        if update_time
        else "Updated: Please refer to the original link"
    )

    body_content = (
        ast.literal_eval(selected_article["paragraphs"])["content"]
        if selected_article["paragraphs"] is not None
        else ["Article content fail to scrape"]
    )

    img_info = (
        ast.literal_eval(selected_article["image_info"])
        if selected_article["image_info"]
        else None
    )
    if img_info is not None:
        img_src = img_info["src"][0]
        img_cap = img_info["alt"][0]
    else:
        img_src = None
        img_cap = None

    if img_src:
        image_with_caption = html.Div(
            [
                html.Img(
                    src=img_src,
                    style={"display": "block", "margin": "0 auto", "width": "50%"},
                )
                if img_src
                else html.Div(),
                html.Div(
                    style={"text-align": "center", "font-size": "1.0em"},
                    children=[html.P(img_cap, style={"margin": 0})],
                ),
            ]
        )
    else:
        image_with_caption = html.Div([])

    article_list = [html.P(meta_info), image_with_caption]
    for content in body_content:
        article_list.append(html.P(content, style={"margin": "1em 50"}))
    article = html.Div([*article_list])
    return html.Div(children=[html.H1(children=selected_article["title"]), article])
