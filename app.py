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


if __name__=='__main__':
    app.run(debug=False)
