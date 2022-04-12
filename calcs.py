"""
Title block module

An alternate version with different formatting
"""
from IPython.display import display, Markdown
from handcalcs.decorator import handcalc
import datetime

def title_block(proj_name = "", proj_id = "", designer = "", _test=False, **kwargs) -> None:
    """
    Returns None. Displays a simple title block for engineering notes created in Jupyter.
    
    '_test' argument is used for internal testing: returns the markdown as a string instead
    of displaying in Jupyter.
    """
    todays_date = datetime.datetime.now().strftime("%Y-%m-%d")
    md = (
        f"## Design Notes<br>\n"
        f"**Project:** _{proj_name}_<br>\n"
        f"**Project ID:** _{proj_id}_<br>\n"
        f"**Designer:** _{designer}_<br>\n"
        f"**Date:** _{todays_date}_<br>\n"
    )
    extra_md = ""
    for kw, arg in kwargs.items():
        extra_md += f"**{kw}:** {arg}<br>\n"
    display(Markdown(md + extra_md))
    if _test:
        return md
    
    
@handcalc(jupyter_display=True)    
def LC1(DL: float, LL: float, SL: float) -> float:
    """
    Returns a float representing the factored load combination of 
    1.4 DL from NBCC-2015
    """
    fl = 1.4*DL
    return fl


@handcalc(jupyter_display=True)    
def LC2(DL: float, LL: float, SL: float) -> float:
    """
    Returns a float representing the factored load combination of 
    1.25 DL + 1.5 LL + 1.0 SL from NBCC-2015
    """
    fl = 1.25*DL + 1.5*LL + 1.0*SL
    return fl


@handcalc(jupyter_display=True)    
def LC3(DL: float, LL: float, SL: float) -> float:
    """
    Returns a float representing the factored load combination of 
    1.25 DL + 1.5 SL + 1.0 LL from NBCC-2015
    """
    fl = 1.25*DL + 1.5*SL + 1.0*LL
    return fl


def NBCC2015_max(DL: float, LL: float, SL: float) -> float:
    """
    Returns the maximum factored load based on the inputs of 
    'DL', 'LL', 'SL' as per NBCC-2015.
    """
    factored_loads = {
        LC1(DL, LL, SL): "LC1",
        LC2(DL, LL, SL): "LC2",
        LC3(DL, LL, SL): "LC3",
    }
    max_factored_load = max(factored_loads.keys())
    md = Markdown(f"**Max load case:** {factored_loads[max_factored_load]} @ {max_factored_load}")
    display(md)
    return max_factored_load
    