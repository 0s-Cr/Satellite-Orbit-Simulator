import numpy as np
import plotly.graph_objects as go

from Prototype4Library import *


def graph(parentCoords, satCoords, scale, parentRadius, constants, satMass):
    ellipseCentre = [0, (satCoords[1] + satCoords[3]) / 2]  # Centre of the ellipse, x y
    ellipseRadii = [satCoords[2], (satCoords[3] - ellipseCentre[1])]  # x radius, y radius
    frameNumber = 360  # Number of frames in the animation running at 60fps
    t = np.linspace(0, 2 * math.pi, 100)  # These variables are all calculations performed to plot the coordinates of
    # the circumference of the ellipse for the animation
    s = np.linspace(0, 2 * math.pi, frameNumber)
    x = ellipseRadii[0] * np.cos(t)  #
    y = ellipseCentre[1] + ellipseRadii[1] * np.sin(t)
    xMin = np.min(x) - ellipseRadii[1]
    xMax = np.max(x) + ellipseRadii[1]
    yMin = np.min(y) - ellipseRadii[1]
    yMax = np.max(y) - ellipseRadii[1]
    xx = ellipseRadii[0] * np.cos(s)
    yy = ellipseCentre[1] + ellipseRadii[1] * np.sin(s)

    fig = go.Figure(  # These lines are the ellipse of the satellites orbit
        data=[go.Scatter(x=x, y=y,
                         mode="lines",
                         line=dict(color="purple")),
              go.Scatter(x=x, y=y,
                         name="path",
                         mode="lines",
                         line=dict(color="purple"))
              ],
        layout=go.Layout(
            xaxis=dict(range=[xMin, xMax], autorange=False, zeroline=False),
            yaxis=dict(range=[yMin, yMax], autorange=False, zeroline=False),
            updatemenus=[  # This is used for creating buttons used for controlling the animation
                {
                    "buttons": [  # Buttons used for controlling the speed of the animation
                        {  # Each buttons has parameters for what it does,and how quickly it does it The method
                            # animate tells the program to manipulate the animation as it progresses,
                            # and the duration is used to control the framerate The first two buttons are used to
                            # play the animation at an incredibly slow rate to allow fine control of which frame is
                            # being displayed.
                            "args": [None, {"frame": {"duration": 1000, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 1hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "1 FPS",
                            "method": "animate"
                        },
                        {
                            "args": [None, {"frame": {"duration": 500, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 2hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "2 FPS",
                            "method": "animate"
                        },
                        {
                            "args": [None, {"frame": {"duration": 200 / 3, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 15hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "1/4x Speed",
                            "method": "animate"
                        },
                        {
                            "args": [None, {"frame": {"duration": 100 / 3, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 30hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "1/2x Speed",
                            "method": "animate"
                        },
                        {
                            "args": [None, {"frame": {"duration": 100 / 6, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 60hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "1x Speed",
                            "method": "animate"
                        },
                        {
                            "args": [None, {"frame": {"duration": 25 / 3, "redraw": False},  # Play button
                                            # Duration is measured in milliseconds - 120hz
                                            "fromcurrent": True, "transition": {"duration": 300,
                                                                                "easing": "quadratic-in-out"}}],
                            "label": "2x Speed",
                            "method": "animate"
                        },
                        {
                            "args": [[None], {"frame": {"duration": 0, "redraw": False},  # Pause button
                                              "mode": "immediate",
                                              "transition": {"duration": 0}}],
                            "label": "Pause",
                            "method": "animate"
                        }
                    ],  # Positioning data
                    "direction": "down",
                    "showactive": False,
                    "type": "buttons",
                }
            ],
        ),
        frames=[dict(  # This section is used for animating a marker around the path of the ellipse
            data=[go.Scatter(
                x=xData(xx, k),
                y=yData(yy, k),
                mode="markers",
                name="Satellite",
                marker=dict(color="red", size=10))],
            layout=go.Layout(
                annotations=[  # This section displays all of the information I wish to be displayed which describes
                    # the orbit
                    go.layout.Annotation(  # the text here contains all of the data which gets displayed with the
                        # graph if the data comes from a function it means that the data changes with every frame and
                        # if it is just a variable, it is only calculated once
                        text="Radius: " + str(round(radius(xx, yy, k, scale), 2)) +
                             "m<br>Altitude: " + str(round(radius(xx, yy, k, scale) - parentRadius, 2)) +
                             "m<br>Speed :" + str(speed(xx, yy, k, scale, constants[1], constants[5])) +
                             "ms<sup>-1</sup><br>Centripetal Acceleration: " + str(round(
                            (speed(xx, yy, k, scale, constants[1], constants[5]) ** 2) / radius(xx, yy, k, scale), 5
                        )) + "ms<sup>-2</sup><br>Centripetal Force: " + str(round(
                            (satMass * (speed(xx, yy, k, scale, constants[1], constants[5]) ** 2)) /
                            radius(xx, yy, k, scale), 2)) + "N<br>Period: " + str(round(
                            constants[7], 2)) + "s<br>Eccentricity: " + str(round(constants[6], 15)) +
                             "<br>Semi-major Axis: " + str(round(constants[5], 2)) + "m",
                        align="left",  # This data gives the annotations their positioning and sizing information
                        # which controls where the box with annotations shows up
                        showarrow=False,
                        xanchor="right",
                        yanchor="middle",
                        xshift=275,
                        yshift=273,
                        width=250,
                        opacity=1,
                        bgcolor="white",
                        bordercolor="black",
                        borderwidth=2
                    )
                ]
            )
        )
            for k in range(frameNumber)]
    )
    fig.add_trace(go.Scatter(  # Apoapsis marker
        x=[0],
        y=[satCoords[3]],
        mode="markers",
        name="Apoapsis",
        marker={"color": "orange", "size": 10}
    ))
    fig.add_trace(go.Scatter(  # Periapsis marker
        x=[0],
        y=[satCoords[1]],
        mode="markers",
        name="Periapsis",
        marker={"color": "yellow", "size": 10}
    ))
    fig.update_layout(
        shapes=[
            # Parent body
            dict(
                type="circle",
                fillcolor="Green",
                x0=parentCoords[0][0],
                y0=parentCoords[0][1],
                x1=parentCoords[1][0],
                y1=parentCoords[1][1],
                line_color="Blue",
                name="Parent Body"
            ),
        ])
    fig.update_layout(yaxis=dict(range=[satCoords[1] - 1, satCoords[3] + 1]),
                      xaxis=dict(range=[satCoords[1] - 1, satCoords[3] + 1]),
                      width=6400 / 7, height=800)
    return fig  # returns fig to the main file for displaying


def xData(xx, k):  # data for the x and y coordinates respectively.  These are intended to be edited later for use with
    # recurring calculations within the program and are done as separate functions as the program doesn't like to
    # work with them in the frames data section
    x = xx[k]
    return [x]


# currently the code requires the x and y variables to be separated from the main animation parameters

def yData(yy, k):
    y = yy[k]
    return [y]
