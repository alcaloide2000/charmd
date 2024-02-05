# These first 3 lines of code are needed when running the app in https://wasmdash.vercel.app/
# import micropip
# await micropip.install('dash-mantine-components')
# await micropip.install('dash-iconify')
import dash_mantine_components as dmc
from dash import Dash, html, dcc
from dash_iconify import DashIconify

card1 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/02/04/bJxU60.thomasdash.png",
                    alt="BASIC MULTIPAGE APP STRUCTURE",
                ),
                href="https://ultrabasicdash.onrender.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("BASIC MULTIPAGE APP STRUCTURE", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/alcaloide2000/ultrabasicdash',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "basisc multipage structure on DASH, cheatsheet explaining all",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card2 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/01/27/bF8YKP.thomasprobab.png",
                    alt="dash-app",
                ),
                href="https://probab3.onrender.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("RATE OF RETURN PROBABILITY", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/alcaloide2000/probab3',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Calculate the probability of an invesment in some indexes.",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

card3 = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Anchor(
                dmc.Image(
                    src="https://i.im.ge/2024/01/23/YVJpED.thomas.png",
                    alt="dash-app",
                ),
                href="https://theec5.onrender.com/",
                target="_blank"
            ),
        ),
        dmc.Group(
            [
                dmc.Text("TRANSLATION ESP/ENG GAME", weight=500, size='xl'),
                html.A(
                    DashIconify(icon="ion:logo-github", width=30),
                    href='https://github.com/alcaloide2000/theec5',
                    target="_blank"
                )
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "basic translation game from Spanish to English sentences",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

all_cards = [
    dmc.Header(
        height=80,
        children=[dmc.Text("Data Analysis and AI Projects",
                           style={"fontSize": 40})],
    ),
    dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        breakpoints=[
            {"maxWidth": 1240, "cols": 2, "spacing": "md"},
            {"maxWidth": 950, "cols": 1, "spacing": "sm"},
        ],
        children=[
            html.Div(card1),
            html.Div(card2),
            html.Div(card3),
        ],
    )
]

reference_card = html.Div([
    dmc.Card(
        children=[
            dmc.Text("ALCALOIDE", weight=500, size='xl'),
            dmc.Text(
                "Basic apps in Dash/Python",
                size="md",
                mb="xs",
            ),
            html.A(
                DashIconify(icon="bi:twitter", width=30),
                href='https://twitter.com/alcaloide',
                target="_blank"
            ),
            html.A(
                DashIconify(icon="ion:logo-github", width=30),
                href='https://github.com/alcaloide2000',
                target="_blank"
            ),
            html.A(
                    DashIconify(icon="bi:discord", width=30),
                    href='https://discord.com/',
                    target="_blank"
                )

        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 350})
    ],
    style={"paddingTop": 40}
)

resume_div = html.Div([
    html.Iframe(src="https://www.dropbox.com/scl/fi/199571mr76sse93cwr8q5/dashmultipagecheatsheet.pdf?rlkey=ekhlp6c2h82ewy5og41k4v657&dl=0",
                width="800", height="480")
    ],
    style={"paddingTop": 40}
)


app = Dash()
server = app.server
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    children=[
            dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.Tab("Projects", value="projects"),
                    dmc.Tab("Cheatsheets", value="resume"),
                    dmc.Tab("Links", value="references"),
                ], style={"paddingRight": 50, "paddingTop": 15}
            ),
            dmc.TabsPanel(children=all_cards, value="projects", pb="xs"),
            dmc.TabsPanel(resume_div, value="resume", pb="xs"),
            dmc.TabsPanel(reference_card, value="references", pb="xs"),
        ],
        value="projects",
        orientation='vertical',
        variant='pills',
    )
])


if __name__=='__main__':
    app.run(debug=False)
