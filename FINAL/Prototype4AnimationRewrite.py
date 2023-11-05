import plotly.graph_objects as go  # Importing libraries which will be used in this file
import numpy as np
from Prototype4Library import *


def graphData(parentCoords, satCoords, scale, parentRadius, constants, satMass):
    # This function creates vital information which is used by the figure for displaying an orbit
    ellipseCentre = [0, (satCoords[1] + satCoords[3]) / 2]  # Centre of the ellipse, x y
    ellipseRadii = [satCoords[2], (satCoords[3] - ellipseCentre[1])]  # x radius, y radius
    frameNumber = 360  # Number of frames in the animation running at 60fps
    t = np.linspace(0, 2 * math.pi, 100)  # These variables are all calculations performed to plot the coordinates of
    # the circumference of the ellipse for the animation
    s = np.linspace(0, 2 * math.pi, frameNumber)
    x = ellipseRadii[0] * np.cos(t)  # x and y are used here to represent points along the x and y axis where
    # calculations take place and the elliptical path itself
    y = ellipseCentre[1] + ellipseRadii[1] * np.sin(t)
    xMin = np.min(x) - ellipseRadii[1]
    xMax = np.max(x) + ellipseRadii[1]
    yMin = np.min(y) - ellipseRadii[1]
    yMax = np.max(y) - ellipseRadii[1]
    xx = ellipseRadii[0] * np.cos(s)  # xx and yy are operations performed which determines the position around an
    # ellipse which the animation used to display the orbit
    yy = ellipseCentre[1] + ellipseRadii[1] * np.sin(s)

    figure = {  # Creating the initial dictionary which contains the figure data
        "layout": {},
        "frames": [],
        "data": [go.Scatter(x=x, y=y,
                            mode="lines",
                            line=dict(color="purple")),
                 go.Scatter(x=x, y=y,
                            name="path",
                            mode="lines",
                            line=dict(color="purple"))]
    }
    # The layout information controls the size of the graph and where it is positioned
    figure["layout"]["xaxis"] = dict(range=[xMin, xMax], autorange=False, zeroline=False)
    figure["layout"]["yaxis"] = dict(range=[yMin, yMax], autorange=False, zeroline=False)
    figure["layout"]["updatemenus"] = [  # This is used for creating buttons used for controlling the animation
        {
            "buttons": [  # Buttons used for controlling the speed of the animation
                {
                    # Each buttons has parameters for what it does,and how quickly
                    # it does it The method animate tells the program to manipulate
                    # the animation as it progresses, and the duration is used to
                    # control the frame rate

                    "args": [None, {"frame": {"duration": 200 / 3, "redraw": False},
                                    # 1/4 speed button
                                    # Duration is measured in milliseconds - 15hz
                                    "fromcurrent": True,
                                    "transition": {"duration": 300,
                                                   "easing": "quadratic-in-out"}}],
                    "label": "1/4x Speed",
                    "method": "animate"
                },
                {
                    "args": [None, {"frame": {"duration": 100 / 3, "redraw": False},
                                    # 1/2 speed button
                                    # Duration is measured in milliseconds - 30hz
                                    "fromcurrent": True,
                                    "transition": {"duration": 300,
                                                   "easing": "quadratic-in-out"}}],
                    "label": "1/2x Speed",
                    "method": "animate"
                },
                {
                    "args": [None, {"frame": {"duration": 100 / 6, "redraw": False},
                                    # 1 speed button
                                    # Duration is measured in milliseconds - 60hz
                                    "fromcurrent": True,
                                    "transition": {"duration": 300,
                                                   "easing": "quadratic-in-out"}}],
                    "label": "1x Speed",
                    "method": "animate"
                },
                {
                    "args": [None, {"frame": {"duration": 25 / 3, "redraw": False},
                                    # 2 speed
                                    # Duration is measured in milliseconds - 120hz
                                    "fromcurrent": True,
                                    "transition": {"duration": 300,
                                                   "easing": "quadratic-in-out"}}],
                    "label": "2x Speed",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                      # Pause button
                                      "mode": "immediate",
                                      "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],  # Positioning and other data
            "direction": "down",
            "showactive": False,
            "type": "buttons",
        }
    ]

    slider = [dict(
        active=0,
        yanchor="top",
        xanchor="left",
        currentvalue={
            "font": {"size": 20},
            "prefix": "Frame Number ",
            "visible": True,
            "xanchor": "right"
        },
        transition={"duration": 300, "easing": "cubic-in-out"},
        len=1,
        steps=[]
    )]

    for n in range(frameNumber):  # Frame number is the total number of frames in the animation and n is the current
        # frame
        frame = {"data": [], "layout": go.Layout(
            annotations=[go.layout.Annotation(  # the text here contains all of the data which gets displayed with the
                # graph if the data comes from a function it means that the data changes with every frame and
                # if it is just a variable, it is only calculated once
                text="Radius: " + str(round(radius(xx, yy, n, scale), 2)) +
                     "m<br>Altitude: " + str(round(radius(xx, yy, n, scale) - parentRadius, 2)) +
                     "m<br>Speed :" + str(speed(xx, yy, n, scale, constants[1], constants[5])) +
                     "ms<sup>-1</sup><br>Centripetal Acceleration: " + str(round(
                    (speed(xx, yy, n, scale, constants[1], constants[5]) ** 2) / radius(xx, yy, n, scale), 5
                )) + "ms<sup>-2</sup><br>Centripetal Force: " + str(round(
                    (satMass * (speed(xx, yy, n, scale, constants[1], constants[5]) ** 2)) /
                    radius(xx, yy, n, scale), 2)) + "N<br>Period: " + str(round(
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
            )])}
        newData = {
            "x": list(xData(xx, n)),
            "y": list(yData(yy, n)),
            "traces": [0],
            "mode": "markers",
            "name": "Satellite",
            "marker": {
                "color": "red",
                "size": 10}
        }
        frame["data"].append(newData)
        figure["frames"].append(frame)
        sliderStep = {"args": [
            [n],
            {"frame": {"duration": 300, "redraw": False},
             "mode": "immediate",
             "transition": {"duration": 300}}
        ],
            "label": n,
            "method": "animate"}
        slider[0]["steps"].append(sliderStep)

    figure["layout"]["sliders"] = slider
    figure = go.Figure(figure)
    figure.update_layout(
        shapes=[dict(
            type="circle",
            fillcolor="Green",
            name="Planet",
            x0=parentCoords[0][0],
            y0=parentCoords[0][1],
            x1=parentCoords[1][0],
            y1=parentCoords[1][1],
            line_color="Blue"
        )],
        yaxis=dict(range=[satCoords[1] - 1, satCoords[3] + 1]),
        xaxis=dict(range=[satCoords[1] - 1, satCoords[3] + 1]),
        width=6400 / 7, height=800)

    return figure


def xData(xx, k):  # data for the x and y coordinates respectively.  These are intended to be edited later for use with
    # recurring calculations within the program and are done as separate functions as the program doesn't like to
    # work with them in the frames data section
    x = xx[k]
    return [x]


# currently the code requires the x and y variables to be separated from the main animation parameters
def yData(yy, k):
    y = yy[k]
    return [y]
