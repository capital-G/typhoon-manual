from typing import Dict, Tuple, List, Optional
from dataclasses import dataclass
import string
from copy import deepcopy

from PIL import Image, ImageDraw, ImageFont

GRANULAR_PANEL: Dict[str, str]= {
    'tune': {
        'pos': (95, 295),
        'text': 'Tune',
    },
    'in_mute': {
        'pos': (281, 101),
        'text': 'In Mute'
    },
    'out_mute': {
        'pos': (672, 101),
        'text': 'Out Mute',
    },
    'hold': {
        'pos': (846, 295),
        'text': 'Hold',
    },
    'in_level': {
        'pos': (95, 598),
        'text': 'In Level',
    },
    'out_level': {
        'pos': (846, 598),
        'text': 'Out Level',
    },
    'position': {
        'pos': (266, 734),
        'text': 'Position',
    },
    'density': {
        'pos': (403, 734),
        'text': 'Density',
    },
    'size': {
        'pos': (545, 734),
        'text': 'Size'
    },
    'texture': {
        'pos': (688, 734),
        'text': 'Texture',
    },
    'wet': {
        'pos': (230, 948),
        'text': 'Wet',
    },
    'stereo': {
        'pos': (396, 948),
        'text': 'Ster',
    },
    'feedback': {
        'pos': (560, 948),
        'text': 'Fbk',
    },
    'reverb': {
        'pos': (726, 948),
        'text': 'Rvb',
    },
    'bank': {
        'pos': (59, 1036),
        'text': 'Bank',
    },
    'time': {
        'pos': (899, 1036),
        'text': 'Time',
    },
    'mod_in_vca': {
        'pos': (54, 1246),
        'text': 'In VCA',
    },
    'mod_aux': {
        'pos': (177, 1246),
        'text': 'Aux',
    },
    'mod_position': {
        'pos': (300, 1246),
        'text': 'Position',
    },
    'mod_density': {
        'pos': (422, 1246),
        'text': 'Density',
    },
    'mod_size': {
        'pos': (544, 1246),
        'text': 'Size',
    },
    'mod_texture': {
        'pos': (666, 1246),
        'text': 'Texture',
    },
    'mod_trigger': {
        'pos': (782, 1246),
        'text': 'Trig',
    },
    'mod_out_vca': {
        'pos': (900, 1246),
        'text': 'Out VCA',
    },
    'mod_in_left': {
        'pos': (54, 1390),
        'text': 'In L',
    },
    'mod_in_right': {
        'pos': (177, 1390),
        'text': 'In R',
    },
    'trigger': {
        'pos': (300, 1390),
        'text': 'Trig',
    },
    'mod_v_oct': {
        'pos': (422, 1390),
        'text': 'V Oct',
    },
    'mod_freq': {
        'pos': (544, 1390),
        'text': 'Freq',
    },
    'mod_hold': {
        'pos': (666,1390),
        'text': 'Hold',
    },
    'mod_out_left': {
        'pos': (782, 1390),
        'text': 'Out L',
        'fill': (255, 0, 0),
    },
    'mod_out_right': {
        'pos': (900, 1390),
        'text': 'Out R',
        'fill': (255, 0, 0),
    }
}

PITCH_SHIFTER_PANEL = deepcopy(GRANULAR_PANEL)
PITCH_SHIFTER_PANEL['position']['text'] = 'Pre-Delay'
PITCH_SHIFTER_PANEL['density']['text'] = 'Diffusion'
PITCH_SHIFTER_PANEL['texture']['text'] = 'LP HP Filter'
PITCH_SHIFTER_PANEL['mod_trigger']['text'] = 'Clock'
PITCH_SHIFTER_PANEL['mod_position']['text'] = 'Pre Delay'
PITCH_SHIFTER_PANEL['mod_density']['text'] = 'Diff'
PITCH_SHIFTER_PANEL['mod_texture']['text'] = 'Filter'

LOOPING_DELAY_PANEL = deepcopy(GRANULAR_PANEL)
LOOPING_DELAY_PANEL['position']['text'] = 'Pre-Delay'
LOOPING_DELAY_PANEL['density']['text'] = 'Diffusion'
LOOPING_DELAY_PANEL['texture']['text'] = 'LP HP Filter'
LOOPING_DELAY_PANEL['mod_trigger']['text'] = 'Clock'
LOOPING_DELAY_PANEL['mod_position']['text'] = 'Pre Delay'
LOOPING_DELAY_PANEL['mod_density']['text'] = 'Diff'
LOOPING_DELAY_PANEL['mod_texture']['text'] = 'Filter'

SPECTRAL_MADNESS_PANEL = deepcopy(GRANULAR_PANEL)
SPECTRAL_MADNESS_PANEL['size']['text'] = 'Spectral Warp'
SPECTRAL_MADNESS_PANEL['density']['text'] = 'TempQ'
SPECTRAL_MADNESS_PANEL['texture']['text'] = 'SpecQ'
SPECTRAL_MADNESS_PANEL['mod_size']['text'] = 'S Warp'
SPECTRAL_MADNESS_PANEL['mod_density']['text'] = 'Time Q'
SPECTRAL_MADNESS_PANEL['mod_texture']['text'] = 'Spec Q'

OLIVERB_PANEL = deepcopy(GRANULAR_PANEL)
OLIVERB_PANEL['position']['text'] = 'Pre-Delay'
OLIVERB_PANEL['size']['text'] = 'Reverb Size'
OLIVERB_PANEL['tune']['text'] = 'Pitch Shift'
OLIVERB_PANEL['density']['text'] = 'Decay'
OLIVERB_PANEL['texture']['text'] = 'Dampening'
OLIVERB_PANEL['mod_position']['text'] = 'Pre-Delay'
OLIVERB_PANEL['mod_size']['text'] = 'R Size'
OLIVERB_PANEL['mod_density']['text'] = 'Decay'
OLIVERB_PANEL['mod_texture']['text'] = 'Diffusion'
OLIVERB_PANEL['stereo']['text'] = 'Dampening'
OLIVERB_PANEL['feedback']['text'] = 'Mod speed'
OLIVERB_PANEL['reverb']['text'] = 'Mod amount'

RESONATOR_PANEL = deepcopy(GRANULAR_PANEL)
RESONATOR_PANEL['position']['text'] = 'Timbre Dur'
RESONATOR_PANEL['size']['text'] = 'Chord'
RESONATOR_PANEL['density']['text'] = 'Decay'
RESONATOR_PANEL['texture']['text'] = 'Dampening'
RESONATOR_PANEL['wet']['text'] = 'Distortion'
RESONATOR_PANEL['mod_trigger']['text'] = 'Burst'
RESONATOR_PANEL['mod_position']['text'] = 'T D'
RESONATOR_PANEL['mod_size']['text'] = 'Chord'
RESONATOR_PANEL['mod_density']['text'] = 'Decay'
RESONATOR_PANEL['mod_texture']['text'] = 'Dampening'
RESONATOR_PANEL['feedback']['text'] = 'Harmonics'
RESONATOR_PANEL['reverb']['text'] = 'Scatter'

BEAT_REPEAT_PANEL = deepcopy(GRANULAR_PANEL)
BEAT_REPEAT_PANEL['position']['text'] = 'Loop Begin'
BEAT_REPEAT_PANEL['size']['text'] = 'Loop Size'
BEAT_REPEAT_PANEL['density']['text'] = 'Size Mod'
BEAT_REPEAT_PANEL['texture']['text'] = 'Slice Step'
BEAT_REPEAT_PANEL['mod_position']['text'] = 'Begin'
BEAT_REPEAT_PANEL['mod_size']['text'] = 'Size'
BEAT_REPEAT_PANEL['mod_density']['text'] = 'Size Mod'
BEAT_REPEAT_PANEL['mod_texture']['text'] = 'Slice Step'
BEAT_REPEAT_PANEL['wet']['text'] = 'Slice Prob'
BEAT_REPEAT_PANEL['stereo']['text'] = 'Clock Div'
BEAT_REPEAT_PANEL['feedback']['text'] = 'Pitch Mod'
BEAT_REPEAT_PANEL['reverb']['text'] = 'Feedback'

SPECTRAL_CLOUDS_PANEL = deepcopy(GRANULAR_PANEL)
SPECTRAL_CLOUDS_PANEL['position']['text'] = 'Band Prob'
SPECTRAL_CLOUDS_PANEL['size']['text'] = 'Band Div'
SPECTRAL_CLOUDS_PANEL['density']['text'] = 'Filter Smoo'
SPECTRAL_CLOUDS_PANEL['texture']['text'] = 'Filter Text'
SPECTRAL_CLOUDS_PANEL['mod_position']['text'] = 'Band Prob'
SPECTRAL_CLOUDS_PANEL['mod_size']['text'] = 'Band Div'
SPECTRAL_CLOUDS_PANEL['mod_density']['text'] = 'Smooth'
SPECTRAL_CLOUDS_PANEL['mod_texture']['text'] = 'Texture'
SPECTRAL_CLOUDS_PANEL['stereo']['text'] = 'Filter Prob'
SPECTRAL_CLOUDS_PANEL['feedback']['text'] = 'Distortion'


PANELS_TO_DRAW: List[Tuple] = [
    ('Granular Processing', GRANULAR_PANEL),
    ('Pitch Shifter', PITCH_SHIFTER_PANEL),
    ('Looping Delay', LOOPING_DELAY_PANEL),
    ('Spectral Madness', SPECTRAL_MADNESS_PANEL),
    ('Oliverb', OLIVERB_PANEL),
    ('Resonator', RESONATOR_PANEL),
    ('Beat Repeat', BEAT_REPEAT_PANEL),
    ('Spectral Clouds', SPECTRAL_CLOUDS_PANEL),
]

class PanelDrawer:
    def __init__(self, base_layout_path: str = 'blank.png'):
        self._base_layout_path = base_layout_path
        self.panel = None
        self.font = ImageFont.truetype('Keyboard.ttf', 25)
        self.draw = None
        self._reload_panel()
    
    def _reload_panel(self) -> Image:
        self.panel = Image.open(self._base_layout_path)
        self.draw = ImageDraw.Draw(self.panel)
    
    def _draw_text(self, pos: Tuple[int, int], text:str, fill: Optional[Tuple]=None, **kwargs):
        if not fill:
            fill = (0, 0, 0)
        w, _ = self.draw.textsize(text, self.font)
        # for height we draw each ascii sign b/c abc would get different height than gjI
        _, h = self.draw.textsize(string.ascii_letters)
        
        self.draw.text(
            xy=(pos[0] - w/2, pos[1] - h/2,),
            text=text,
            font=self.font,
            fill=fill,
            **kwargs,
        )

    def draw_panel(self, name: str, labels: Dict):
        self._reload_panel()
        for _, label in labels.items():
            self._draw_text(**label)
        self.panel.save(f'panels/{name.lower().replace(" ", "_")}.png')

if __name__ == '__main__':
    panel_drawer = PanelDrawer()
    for panel_name, panel_dict in PANELS_TO_DRAW:
        panel_drawer.draw_panel(panel_name, panel_dict)
