import PySimpleGUI as sg
import textwrap

sg.theme("LightGrey2")

# Defining the left menu
menu = sg.vtop(
    sg.Column(
        layout=[
            [
                sg.Button(
                    button_text="Profile",
                    expand_x=True,
                    disabled=True,
                    key="Button-Profile",
                )
            ],
            [
                sg.Button(
                    button_text="Experience",
                    expand_x=True,
                    disabled=True,
                    key="Button-Experience",
                )
            ],
            [
                sg.Button(
                    button_text="Education",
                    expand_x=True,
                    disabled=True,
                    key="Button-Education",
                )
            ],
            [
                sg.Button(
                    button_text="Hobbies",
                    expand_x=True,
                    disabled=True,
                    key="Button-Hobbies",
                )
            ],
            [
                sg.Button(
                    button_text="Skills",
                    expand_x=True,
                    disabled=True,
                    key="Button-Skills",
                )
            ],
            [
                sg.Button(
                    button_text="Jobs", expand_x=True, disabled=True, key="Button-Jobs"
                )
            ],
            [
                sg.Button(
                    button_text="Interviews",
                    expand_x=True,
                    disabled=True,
                    key="Button-Interviews",
                )
            ],
        ],
        element_justification="left",
    )
)

# PROFILE LAYOUT ------------------------------------------------------------
# Defining the options for profiles combo box
profiles = ["Adrian George Radu", "Profile 2", "Profile 3"]
# Defining the top frame
top_profile = sg.Column(
    [
        [
            sg.Column(
                [
                    [
                        sg.Image(filename="images/icons8-document-writer-50.png"),
                    ]
                ],
                element_justification="left",
            ),
            sg.Column(
                [
                    [
                        sg.Text("Select Profile:"),
                        sg.Combo(profiles, key="Combo-Profiles", readonly=True),
                        sg.Button(button_text="New Profile", key="Button-New-Profile"),
                        sg.Button(
                            button_text="Delete Profile", key="Button-Delete-Profile"
                        ),
                    ]
                ],
                element_justification="right",
                expand_x=True,
            ),
        ],
    ],
    key="Top-Profile",
    visible=True,
)
# Defining the content
content_profile = sg.Column(
    [
        [sg.Text("Name:"), sg.Input(key="-Name-")],
        [sg.Text("Surname:"), sg.Input(key="-Surname-")],
        [sg.Text("Birthday:"), sg.Input(key="-Birthday-")],
        [sg.Text("Sex:"), sg.Input(key="-Sex-")],
        [sg.Text("Phone:"), sg.Input(key="-Phone-")],
        [sg.Text("E-mail:"), sg.Input(key="-Email-")],
        [sg.Text("E-mail pass:"), sg.Input(key="-EmailPass-")],
        [sg.Text("Address:"), sg.Input(key="-Address-")],
        [sg.Text("Language:"), sg.Input(key="-Language-")],
        [sg.Text("Photo:"), sg.Input(size=(33, 1), key="Photo-File"), sg.FileBrowse()],
        [sg.Button(button_text="Save Profile", key="Button-Save-Profile")],
    ],
    element_justification="right",
    expand_x=True,
    key="Content-Profile",
    visible=True,
)

# EXPERIENCE LAYOUT ----------------------------------------------------------
# Defining the top frame
top_experience = sg.Column(
    [
        [
            sg.Column(
                [
                    [
                        sg.Image(filename="images/icons8-populärer-mann-50.png"),
                    ]
                ],
                element_justification="left",
            ),
            sg.Column(
                [[sg.Text("EXPERIENCE - Profile: Adrian George Radu")]],
                element_justification="right",
            ),
        ],
    ],
    key="Top-Experience",
    visible=False,
)

# Defining the content
some_big_text = "Some description goes here in this area with more blah blah... area with more blah blah..."
content_experience = sg.Column(
    [
        [
            sg.Frame(
                layout=[
                    [sg.Text("Name of the experience goes here", justification="left")],
                    [sg.Text("Name of the company", justification="left")],
                    [sg.Text("01.02.2023 - 12.12.2023")],
                    [
                        sg.Text(
                            textwrap.fill(
                                "Some description goes here in this area...", 70
                            ),
                            expand_x=True,
                        )
                    ],
                ],
                title="",
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                layout=[
                    [sg.Text("Other name of the experience writen here")],
                    [sg.Text("Name of the company")],
                    [sg.Text("01.02.2023 - 12.12.2023")],
                    [
                        sg.Text(
                            textwrap.fill(
                                "Some description goes here in this area...", 70
                            ),
                            expand_x=True,
                        )
                    ],
                ],
                title="",
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                layout=[
                    [sg.Text("Name of the experience")],
                    [sg.Text("Name of the company")],
                    [sg.Text("01.02.2023 - 12.12.2023")],
                    [
                        sg.Text(
                            textwrap.fill(
                                "Some description goes here in this area...", 70
                            ),
                            expand_x=True,
                        )
                    ],
                ],
                title="",
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                layout=[
                    [sg.Text("Name of the experience")],
                    [sg.Text("Name of the company")],
                    [sg.Text("01.02.2023 - 12.12.2023")],
                    [sg.Text(textwrap.fill(some_big_text, 70), expand_x=True)],
                    [
                        sg.Button(
                            button_text="Delete Experience",
                            key="Button-Delete-Experience",
                        )
                    ],
                ],
                title="",
                expand_x=True,
            )
        ],
        [
            sg.Frame(
                layout=[
                    [sg.Text("Title:"), sg.Input(key="-Exp-Title-")],
                    [sg.Text("Company:"), sg.Input(key="-Exp-Company-")],
                    [
                        sg.Text("Start:"),
                        sg.Input(key="-Exp-Start-", size=(None, 10)),
                        sg.Text("End:"),
                        sg.Input(key="-Exp-End-", size=(None, 10)),
                    ],
                    [sg.Text("Description:"), sg.Input(key="-Exp-Description-")],
                    [
                        sg.Button(
                            button_text="Save Experience", key="Button-Save-Experience"
                        )
                    ],
                ],
                title="",
                expand_x=True,
                element_justification="right",
            )
        ],
    ],
    element_justification="right",
    expand_x=True,
    expand_y=True,
    key="Content-Experience",
    visible=False,
    scrollable=True,
    vertical_scroll_only=True,
)
