import dataclasses


@dataclasses.dataclass
class Theme:
    BACKGROUND_PRIMARY = '#FFFFFF'
    BACKGROUND_SECONDARY = '#D3D3D3'

    FONT_PRIMARY = '#000000'
    FONT_HINT = '#808080'


@dataclasses.dataclass
class Font:
    SIDEBAR_SEARCH = ('Arial', 13)
    GOALVIEW_NAME = ('Arial', 18, 'bold')
