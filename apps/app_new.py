
import os
import dash

from apps.demo import create_layout, demo_callbacks

# for the Local version, import local_layout and local_callbacks
# from local import local_layout, local_callbacks

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

#server = app.server
app.layout = create_layout(app)
demo_callbacks(app)

# Running server
if __name__ == '__main__':
    app.run_server(port=os.getenv("CDSW_APP_PORT"))