from global_var import article_database
import dash_bootstrap_components as dbc
from dash import html
from config import COUNTRY_LIST, NO_IMG_URL

MAX_COLS = 4


def form_card(title, imgsrc, ori_link, lang, id):
    country = list(filter(lambda x: x[1] == lang, COUNTRY_LIST))[0][0]
    card_img = dbc.CardImg(src=imgsrc, top=True, style={
        "width": "100%",
        "height": "100%",
        "object-fit": "hidden"
    })
    card_body = dbc.CardBody(
        [
            html.H6(title, className="card-title"),
        ]
    )
    ori_article = dbc.Button(
        "Original Article",
        color="secondary",
        external_link=True,
        href=ori_link,
        target="_blank",
        class_name="p-2 me-2",
    )
    read_more = dbc.Button(
        "Read More",
        color="primary",
        external_link=True,
        href=f"{country}/news_id_{id}",
        target="_blank",
        class_name="p-2 me-2",
    )
    card_footer = dbc.CardFooter(children=[ori_article, read_more])
    return card_img, card_body, card_footer


def form_layout(row_style="p-2", lang=""):
    card_list = []
    articles = article_database.retrieve_article(lang=lang)
    # print(f"length: {len(articles)}")
    for article in articles:
        # print(article)
        card_img, card_body, card_footer = form_card(
            title=article["title"],
            imgsrc=article["image"] if article["image"] is not None else NO_IMG_URL,
            ori_link=article["url"],
            lang=lang,
            id=article["_id"],
        )
        card = dbc.Card(
            [card_img, card_body, card_footer], style={
                "width": "600",
                "height": "400",
                "overflow": "hidden"
            }
        )
        card_list.append(card)

    card_layout = []
    row_ = []
    article_idx = 0
    while article_idx < len(card_list):
        if article_idx % MAX_COLS == 0 and article_idx != 0:
            card_layout.append(
                dbc.Row(
                    row_,
                    align="center",
                    justify="center",
                    class_name=row_style,
                )
            )
            row_ = []
        row_.append(dbc.Col(card_list[article_idx]))
        article_idx += 1
    card_layout.append(
        dbc.Row(row_, align="center", justify="center", class_name=row_style)
    )
    return card_layout


__all__ = ["card_layout", "form_layout"]
