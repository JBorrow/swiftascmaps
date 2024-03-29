"""
Colors (defined as RGB values) for the Taylor Swift albums.
"""

from swiftascmaps.make_cmap import hex_to_rgb

red = [
    [40, 37, 62],
    [175, 30, 73],
    [235, 233, 220],
]

nineteen_eighty_nine = [
    [58, 64, 84],
    [139, 112, 156],
    [203, 152, 123],
    [215, 197, 162],
    [229, 231, 220],
]

reputation = [
    [26, 26, 26],
    [140, 140, 140],
    [230, 230, 230],
    [255, 255, 255],
]

lover = [
    [93, 174, 218],
    [254, 166, 184],
    [255, 244, 208],
]

folklore = [
    [69, 60, 46],
    [106, 103, 88],
    [158, 134, 108],
    [223, 222, 220],
]

evermore = [
    [241, 149, 91],
    [142, 52, 38],
    [33, 21, 49],
    [154, 112, 82],
    [241, 149, 91],
]

evermore_shifted = [
    [33, 21, 49],
    [154, 112, 82],
    [241, 149, 91],
    [142, 52, 38],
    [33, 21, 49],
]

fearless_tv = [
    [77, 51, 33],
    [132, 99, 60],
    #    [117, 84, 45],
    #    [202, 165, 98],
    [186, 151, 88],
    [232, 206, 148],
    [250, 241, 200],
]

red_tv = hex_to_rgb(
    reversed(
        [
            "#E7DDD5",
            "#C5AD9A",
            "#BA704B",
            "#8F4C3A",
            "#6F2019",
            "#480200",
        ]
    )
)

midnights = hex_to_rgb(
    [
        "#2A1828",
        "#4F5D87",
        "#83A5BA",
        "#E8E7E3",
    ]
)

speak_now_tv = hex_to_rgb(
    [
        "#0E0E0E",
        "#693C83",
        "#B58CB5",
        "#EEE6DC",
    ]
)

nineteen_eighty_nine_tv = hex_to_rgb(
    ["#3A1F16", "#C13C25", "#D7AB8A", "#FBFAF8", "#7EA7C5", "#446D8D", "#1F2D3B"]
)
