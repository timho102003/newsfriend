import dash
import dash_auth

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
    use_pages=True,
)
VALID_USERNAME_PASSWORD_PAIRS = {"hello": "world"}
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

server = app.server
