# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MAKE_SURFACES_METADATA = Metadata(
    id="e96557d2a5fb1819382e59922a58f1b8b9878284.boutiques",
    name="mris_make_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisMakeSurfacesParameters = typing.TypedDict('MrisMakeSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_make_surfaces"],
    "subject_name": str,
    "hemisphere": str,
    "white": typing.NotRequired[str | None],
    "pial": typing.NotRequired[str | None],
    "whiteonly": bool,
    "nowhite": bool,
    "orig_white": typing.NotRequired[str | None],
    "orig_pial": typing.NotRequired[str | None],
    "q": bool,
    "max_gray_scale": typing.NotRequired[float | None],
    "c": bool,
    "cortex": typing.NotRequired[float | None],
    "w": typing.NotRequired[float | None],
    "first_wm_peak": bool,
    "a_avgs": typing.NotRequired[float | None],
    "pa_avgs": typing.NotRequired[float | None],
    "wa_avgs": typing.NotRequired[float | None],
    "t1_vol": typing.NotRequired[str | None],
    "w_vol": typing.NotRequired[str | None],
    "long": bool,
    "dura_thresh": typing.NotRequired[float | None],
    "sdir": typing.NotRequired[str | None],
    "erase_cerebellum": bool,
    "wm_weight": typing.NotRequired[float | None],
    "nsigma_above": typing.NotRequired[float | None],
    "nsigma_below": typing.NotRequired[float | None],
    "t2_min_inside": typing.NotRequired[float | None],
    "t2_max_inside": typing.NotRequired[float | None],
    "t2_outside_min": typing.NotRequired[float | None],
    "t2_outside_max": typing.NotRequired[float | None],
    "min_peak_pct": typing.NotRequired[float | None],
    "border_vals_hires": bool,
    "no_unitize": bool,
    "intensity": typing.NotRequired[float | None],
    "curv": typing.NotRequired[float | None],
    "tspring": typing.NotRequired[float | None],
    "nspring": typing.NotRequired[float | None],
    "repulse": typing.NotRequired[float | None],
    "save_target": bool,
    "save_res": bool,
    "v_vertexno": typing.NotRequired[float | None],
    "diag_vertex": typing.NotRequired[float | None],
    "rip": typing.NotRequired[str | None],
    "sigma_white": typing.NotRequired[str | None],
    "sigma_pial": typing.NotRequired[str | None],
    "output": typing.NotRequired[str | None],
    "min_border_white": typing.NotRequired[float | None],
    "max_border_white": typing.NotRequired[float | None],
    "min_gray_white_border": typing.NotRequired[float | None],
    "max_gray": typing.NotRequired[float | None],
    "max_gray_csf_border": typing.NotRequired[float | None],
    "min_gray_csf_border": typing.NotRequired[float | None],
    "max_csf": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mris_make_surfaces": mris_make_surfaces_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class MrisMakeSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_make_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_make_surfaces_params(
    subject_name: str,
    hemisphere: str,
    white: str | None = None,
    pial: str | None = None,
    whiteonly: bool = False,
    nowhite: bool = False,
    orig_white: str | None = None,
    orig_pial: str | None = None,
    q: bool = False,
    max_gray_scale: float | None = None,
    c: bool = False,
    cortex: float | None = None,
    w: float | None = None,
    first_wm_peak: bool = False,
    a_avgs: float | None = None,
    pa_avgs: float | None = None,
    wa_avgs: float | None = None,
    t1_vol: str | None = None,
    w_vol: str | None = None,
    long: bool = False,
    dura_thresh: float | None = None,
    sdir: str | None = None,
    erase_cerebellum: bool = False,
    wm_weight: float | None = None,
    nsigma_above: float | None = None,
    nsigma_below: float | None = None,
    t2_min_inside: float | None = None,
    t2_max_inside: float | None = None,
    t2_outside_min: float | None = None,
    t2_outside_max: float | None = None,
    min_peak_pct: float | None = None,
    border_vals_hires: bool = False,
    no_unitize: bool = False,
    intensity: float | None = None,
    curv: float | None = None,
    tspring: float | None = None,
    nspring: float | None = None,
    repulse: float | None = None,
    save_target: bool = False,
    save_res: bool = False,
    v_vertexno: float | None = None,
    diag_vertex: float | None = None,
    rip: str | None = None,
    sigma_white: str | None = None,
    sigma_pial: str | None = None,
    output: str | None = None,
    min_border_white: float | None = None,
    max_border_white: float | None = None,
    min_gray_white_border: float | None = None,
    max_gray: float | None = None,
    max_gray_csf_border: float | None = None,
    min_gray_csf_border: float | None = None,
    max_csf: float | None = None,
) -> MrisMakeSurfacesParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Brain hemisphere (r or l).
        white: Output name for white surface (default is 'white'). Set to\
            NOWHITE to generate but not save white surface.
        pial: Output name for pial surface (default is 'pial').
        whiteonly: Only generate white matter surface.
        nowhite: Only generate pial surface.
        orig_white: Specify a white surface to start with.
        orig_pial: Specify a pial surface to start with.
        q: Omit self-intersection and only generate gray/white surface.
        max_gray_scale: Set maximum gray scale value.
        c: Do not create curvature and area files from white matter surface.
        cortex: Set to 0 to turn off creation of cortex label file.
        w: Unused argument.
        first_wm_peak: Settle WM surface at first peak in intensity profile\
            instead of highest.
        a_avgs: Average curvature values a number of times (default=10).
        pa_avgs: Average pial curvature values a max of a number of times\
            (default=16).
        wa_avgs: Average white curvature values a max of a number of times\
            (default=4).
        t1_vol: Specify T1 volume (default is brain).
        w_vol: Specify white volume and <hires> option.
        long: Run longitudinal analysis.
        dura_thresh: Set a threshold for the multi-echo mprage dura avoidance.
        sdir: Specify SUBJECTS_DIR.
        erase_cerebellum: Erase cerebellar labeled voxels if aseg is loaded.
        wm_weight: Weighting of WM mean in calculating T2 threshold of\
            disallowed GM values, default=3.
        nsigma_above: # of sigmas above the mean to allow gray matter T2\
            intensities.
        nsigma_below: # of sigmas below the mean to allow gray matter T2\
            intensities.
        t2_min_inside: Specify threshold for min T2 value allowed to be\
            interior to the cortical ribbon.
        t2_max_inside: Specify threshold for max T2 value allowed to be\
            interior to the cortical ribbon.
        t2_outside_min: Specify threshold for min T2 value outside of pial\
            surface that will cause surface to deform outwards.
        t2_outside_max: Specify threshold for max T2 value outside of pial\
            surface that will cause surface to deform outwards.
        min_peak_pct: Specify the pct of the histo peak in the local gm\
            histogram to use as threshold for finding the local inside and outside\
            gm thresholds.
        border_vals_hires: Turn on hires options in\
            MRIScomputeBorderValues_new(). May not be helpful.
        no_unitize: Turn off face normal unitization.
        intensity: Set weight of intensity cost.
        curv: Set weight of curvature cost.
        tspring: Set weight of tangential spring cost.
        nspring: Set weight of normal spring cost.
        repulse: Set weight of repulsion force.
        save_target: Save target surface for debugging.
        save_res: Save residual for debugging.
        v_vertexno: Set Gdiag_no to vertex number.
        diag_vertex: Set Gdiag_no to vertex number and turn off writing of\
            cortex label or curvature files.
        rip: Save ripflag as overlay. Specify full path including hemi, suffix,\
            etc.
        sigma_white: Save white surface sigma as overlay. Specify full path\
            including hemi, suffix, etc.
        sigma_pial: Save pial surface sigma as overlay. Specify full path\
            including hemi, suffix, etc.
        output: Append suffix to all outputs to prevent over-writing.
        min_border_white: Minimum border white.
        max_border_white: Maximum border white.
        min_gray_white_border: Minimum gray at white border.
        max_gray: Maximum gray value.
        max_gray_csf_border: Maximum gray at CSF border.
        min_gray_csf_border: Minimum gray at CSF border.
        max_csf: Maximum CSF value.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_make_surfaces",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "whiteonly": whiteonly,
        "nowhite": nowhite,
        "q": q,
        "c": c,
        "first_wm_peak": first_wm_peak,
        "long": long,
        "erase_cerebellum": erase_cerebellum,
        "border_vals_hires": border_vals_hires,
        "no_unitize": no_unitize,
        "save_target": save_target,
        "save_res": save_res,
    }
    if white is not None:
        params["white"] = white
    if pial is not None:
        params["pial"] = pial
    if orig_white is not None:
        params["orig_white"] = orig_white
    if orig_pial is not None:
        params["orig_pial"] = orig_pial
    if max_gray_scale is not None:
        params["max_gray_scale"] = max_gray_scale
    if cortex is not None:
        params["cortex"] = cortex
    if w is not None:
        params["w"] = w
    if a_avgs is not None:
        params["a_avgs"] = a_avgs
    if pa_avgs is not None:
        params["pa_avgs"] = pa_avgs
    if wa_avgs is not None:
        params["wa_avgs"] = wa_avgs
    if t1_vol is not None:
        params["t1_vol"] = t1_vol
    if w_vol is not None:
        params["w_vol"] = w_vol
    if dura_thresh is not None:
        params["dura_thresh"] = dura_thresh
    if sdir is not None:
        params["sdir"] = sdir
    if wm_weight is not None:
        params["wm_weight"] = wm_weight
    if nsigma_above is not None:
        params["nsigma_above"] = nsigma_above
    if nsigma_below is not None:
        params["nsigma_below"] = nsigma_below
    if t2_min_inside is not None:
        params["t2_min_inside"] = t2_min_inside
    if t2_max_inside is not None:
        params["t2_max_inside"] = t2_max_inside
    if t2_outside_min is not None:
        params["t2_outside_min"] = t2_outside_min
    if t2_outside_max is not None:
        params["t2_outside_max"] = t2_outside_max
    if min_peak_pct is not None:
        params["min_peak_pct"] = min_peak_pct
    if intensity is not None:
        params["intensity"] = intensity
    if curv is not None:
        params["curv"] = curv
    if tspring is not None:
        params["tspring"] = tspring
    if nspring is not None:
        params["nspring"] = nspring
    if repulse is not None:
        params["repulse"] = repulse
    if v_vertexno is not None:
        params["v_vertexno"] = v_vertexno
    if diag_vertex is not None:
        params["diag_vertex"] = diag_vertex
    if rip is not None:
        params["rip"] = rip
    if sigma_white is not None:
        params["sigma_white"] = sigma_white
    if sigma_pial is not None:
        params["sigma_pial"] = sigma_pial
    if output is not None:
        params["output"] = output
    if min_border_white is not None:
        params["min_border_white"] = min_border_white
    if max_border_white is not None:
        params["max_border_white"] = max_border_white
    if min_gray_white_border is not None:
        params["min_gray_white_border"] = min_gray_white_border
    if max_gray is not None:
        params["max_gray"] = max_gray
    if max_gray_csf_border is not None:
        params["max_gray_csf_border"] = max_gray_csf_border
    if min_gray_csf_border is not None:
        params["min_gray_csf_border"] = min_gray_csf_border
    if max_csf is not None:
        params["max_csf"] = max_csf
    return params


def mris_make_surfaces_cargs(
    params: MrisMakeSurfacesParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mris_make_surfaces")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    if params.get("white") is not None:
        cargs.extend([
            "-white",
            params.get("white")
        ])
    if params.get("pial") is not None:
        cargs.extend([
            "-pial",
            params.get("pial")
        ])
    if params.get("whiteonly"):
        cargs.append("-whiteonly")
    if params.get("nowhite"):
        cargs.append("-nowhite")
    if params.get("orig_white") is not None:
        cargs.extend([
            "-orig_white",
            params.get("orig_white")
        ])
    if params.get("orig_pial") is not None:
        cargs.extend([
            "-orig_pial",
            params.get("orig_pial")
        ])
    if params.get("q"):
        cargs.append("-q")
    if params.get("max_gray_scale") is not None:
        cargs.extend([
            "-max_gray_scale",
            str(params.get("max_gray_scale"))
        ])
    if params.get("c"):
        cargs.append("-c")
    if params.get("cortex") is not None:
        cargs.extend([
            "-cortex",
            str(params.get("cortex"))
        ])
    if params.get("w") is not None:
        cargs.extend([
            "-w",
            str(params.get("w"))
        ])
    if params.get("first_wm_peak"):
        cargs.append("-first_wm_peak")
    if params.get("a_avgs") is not None:
        cargs.extend([
            "-a",
            str(params.get("a_avgs"))
        ])
    if params.get("pa_avgs") is not None:
        cargs.extend([
            "-pa",
            str(params.get("pa_avgs"))
        ])
    if params.get("wa_avgs") is not None:
        cargs.extend([
            "-wa",
            str(params.get("wa_avgs"))
        ])
    if params.get("t1_vol") is not None:
        cargs.extend([
            "-T1",
            params.get("t1_vol")
        ])
    if params.get("w_vol") is not None:
        cargs.extend([
            "-wvol",
            params.get("w_vol")
        ])
    if params.get("long"):
        cargs.append("-long")
    if params.get("dura_thresh") is not None:
        cargs.extend([
            "-dura_thresh",
            str(params.get("dura_thresh"))
        ])
    if params.get("sdir") is not None:
        cargs.extend([
            "-SDIR",
            params.get("sdir")
        ])
    if params.get("erase_cerebellum"):
        cargs.append("-erase_cerebellum")
    if params.get("wm_weight") is not None:
        cargs.extend([
            "-wm_weight",
            str(params.get("wm_weight"))
        ])
    if params.get("nsigma_above") is not None:
        cargs.extend([
            "-nsigma_above",
            str(params.get("nsigma_above"))
        ])
    if params.get("nsigma_below") is not None:
        cargs.extend([
            "-nsigma_below",
            str(params.get("nsigma_below"))
        ])
    if params.get("t2_min_inside") is not None:
        cargs.extend([
            "-T2_min_inside",
            str(params.get("t2_min_inside"))
        ])
    if params.get("t2_max_inside") is not None:
        cargs.extend([
            "-T2_max_inside",
            str(params.get("t2_max_inside"))
        ])
    if params.get("t2_outside_min") is not None:
        cargs.extend([
            "-T2_outside_min",
            str(params.get("t2_outside_min"))
        ])
    if params.get("t2_outside_max") is not None:
        cargs.extend([
            "-T2_outside_max",
            str(params.get("t2_outside_max"))
        ])
    if params.get("min_peak_pct") is not None:
        cargs.extend([
            "-min_peak_pct",
            str(params.get("min_peak_pct"))
        ])
    if params.get("border_vals_hires"):
        cargs.append("-border-vals-hires")
    if params.get("no_unitize"):
        cargs.append("-no-unitize")
    if params.get("intensity") is not None:
        cargs.extend([
            "-intensity",
            str(params.get("intensity"))
        ])
    if params.get("curv") is not None:
        cargs.extend([
            "-curv",
            str(params.get("curv"))
        ])
    if params.get("tspring") is not None:
        cargs.extend([
            "-tspring",
            str(params.get("tspring"))
        ])
    if params.get("nspring") is not None:
        cargs.extend([
            "-nspring",
            str(params.get("nspring"))
        ])
    if params.get("repulse") is not None:
        cargs.extend([
            "-repulse",
            str(params.get("repulse"))
        ])
    if params.get("save_target"):
        cargs.append("-save-target")
    if params.get("save_res"):
        cargs.append("-save-res")
    if params.get("v_vertexno") is not None:
        cargs.extend([
            "-v",
            str(params.get("v_vertexno"))
        ])
    if params.get("diag_vertex") is not None:
        cargs.extend([
            "-diag-vertex",
            str(params.get("diag_vertex"))
        ])
    if params.get("rip") is not None:
        cargs.extend([
            "-rip",
            params.get("rip")
        ])
    if params.get("sigma_white") is not None:
        cargs.extend([
            "-sigma-white",
            params.get("sigma_white")
        ])
    if params.get("sigma_pial") is not None:
        cargs.extend([
            "-sigma-pial",
            params.get("sigma_pial")
        ])
    if params.get("output") is not None:
        cargs.extend([
            "-output",
            params.get("output")
        ])
    if params.get("min_border_white") is not None:
        cargs.extend([
            "-min_border_white",
            str(params.get("min_border_white"))
        ])
    if params.get("max_border_white") is not None:
        cargs.extend([
            "-max_border_white",
            str(params.get("max_border_white"))
        ])
    if params.get("min_gray_white_border") is not None:
        cargs.extend([
            "-min_gray_at_white_border",
            str(params.get("min_gray_white_border"))
        ])
    if params.get("max_gray") is not None:
        cargs.extend([
            "-max_gray",
            str(params.get("max_gray"))
        ])
    if params.get("max_gray_csf_border") is not None:
        cargs.extend([
            "-max_gray_at_csf_border",
            str(params.get("max_gray_csf_border"))
        ])
    if params.get("min_gray_csf_border") is not None:
        cargs.extend([
            "-min_gray_at_csf_border",
            str(params.get("min_gray_csf_border"))
        ])
    if params.get("max_csf") is not None:
        cargs.extend([
            "-max_csf",
            str(params.get("max_csf"))
        ])
    return cargs


def mris_make_surfaces_outputs(
    params: MrisMakeSurfacesParameters,
    execution: Execution,
) -> MrisMakeSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMakeSurfacesOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_make_surfaces_execute(
    params: MrisMakeSurfacesParameters,
    execution: Execution,
) -> MrisMakeSurfacesOutputs:
    """
    Positions the tessellation of the cortical surface at the white matter surface,
    then the gray matter surface, generating surface files along with a curvature
    file and a surface file for cortical thickness.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMakeSurfacesOutputs`).
    """
    params = execution.params(params)
    cargs = mris_make_surfaces_cargs(params, execution)
    ret = mris_make_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_make_surfaces(
    subject_name: str,
    hemisphere: str,
    white: str | None = None,
    pial: str | None = None,
    whiteonly: bool = False,
    nowhite: bool = False,
    orig_white: str | None = None,
    orig_pial: str | None = None,
    q: bool = False,
    max_gray_scale: float | None = None,
    c: bool = False,
    cortex: float | None = None,
    w: float | None = None,
    first_wm_peak: bool = False,
    a_avgs: float | None = None,
    pa_avgs: float | None = None,
    wa_avgs: float | None = None,
    t1_vol: str | None = None,
    w_vol: str | None = None,
    long: bool = False,
    dura_thresh: float | None = None,
    sdir: str | None = None,
    erase_cerebellum: bool = False,
    wm_weight: float | None = None,
    nsigma_above: float | None = None,
    nsigma_below: float | None = None,
    t2_min_inside: float | None = None,
    t2_max_inside: float | None = None,
    t2_outside_min: float | None = None,
    t2_outside_max: float | None = None,
    min_peak_pct: float | None = None,
    border_vals_hires: bool = False,
    no_unitize: bool = False,
    intensity: float | None = None,
    curv: float | None = None,
    tspring: float | None = None,
    nspring: float | None = None,
    repulse: float | None = None,
    save_target: bool = False,
    save_res: bool = False,
    v_vertexno: float | None = None,
    diag_vertex: float | None = None,
    rip: str | None = None,
    sigma_white: str | None = None,
    sigma_pial: str | None = None,
    output: str | None = None,
    min_border_white: float | None = None,
    max_border_white: float | None = None,
    min_gray_white_border: float | None = None,
    max_gray: float | None = None,
    max_gray_csf_border: float | None = None,
    min_gray_csf_border: float | None = None,
    max_csf: float | None = None,
    runner: Runner | None = None,
) -> MrisMakeSurfacesOutputs:
    """
    Positions the tessellation of the cortical surface at the white matter surface,
    then the gray matter surface, generating surface files along with a curvature
    file and a surface file for cortical thickness.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Brain hemisphere (r or l).
        white: Output name for white surface (default is 'white'). Set to\
            NOWHITE to generate but not save white surface.
        pial: Output name for pial surface (default is 'pial').
        whiteonly: Only generate white matter surface.
        nowhite: Only generate pial surface.
        orig_white: Specify a white surface to start with.
        orig_pial: Specify a pial surface to start with.
        q: Omit self-intersection and only generate gray/white surface.
        max_gray_scale: Set maximum gray scale value.
        c: Do not create curvature and area files from white matter surface.
        cortex: Set to 0 to turn off creation of cortex label file.
        w: Unused argument.
        first_wm_peak: Settle WM surface at first peak in intensity profile\
            instead of highest.
        a_avgs: Average curvature values a number of times (default=10).
        pa_avgs: Average pial curvature values a max of a number of times\
            (default=16).
        wa_avgs: Average white curvature values a max of a number of times\
            (default=4).
        t1_vol: Specify T1 volume (default is brain).
        w_vol: Specify white volume and <hires> option.
        long: Run longitudinal analysis.
        dura_thresh: Set a threshold for the multi-echo mprage dura avoidance.
        sdir: Specify SUBJECTS_DIR.
        erase_cerebellum: Erase cerebellar labeled voxels if aseg is loaded.
        wm_weight: Weighting of WM mean in calculating T2 threshold of\
            disallowed GM values, default=3.
        nsigma_above: # of sigmas above the mean to allow gray matter T2\
            intensities.
        nsigma_below: # of sigmas below the mean to allow gray matter T2\
            intensities.
        t2_min_inside: Specify threshold for min T2 value allowed to be\
            interior to the cortical ribbon.
        t2_max_inside: Specify threshold for max T2 value allowed to be\
            interior to the cortical ribbon.
        t2_outside_min: Specify threshold for min T2 value outside of pial\
            surface that will cause surface to deform outwards.
        t2_outside_max: Specify threshold for max T2 value outside of pial\
            surface that will cause surface to deform outwards.
        min_peak_pct: Specify the pct of the histo peak in the local gm\
            histogram to use as threshold for finding the local inside and outside\
            gm thresholds.
        border_vals_hires: Turn on hires options in\
            MRIScomputeBorderValues_new(). May not be helpful.
        no_unitize: Turn off face normal unitization.
        intensity: Set weight of intensity cost.
        curv: Set weight of curvature cost.
        tspring: Set weight of tangential spring cost.
        nspring: Set weight of normal spring cost.
        repulse: Set weight of repulsion force.
        save_target: Save target surface for debugging.
        save_res: Save residual for debugging.
        v_vertexno: Set Gdiag_no to vertex number.
        diag_vertex: Set Gdiag_no to vertex number and turn off writing of\
            cortex label or curvature files.
        rip: Save ripflag as overlay. Specify full path including hemi, suffix,\
            etc.
        sigma_white: Save white surface sigma as overlay. Specify full path\
            including hemi, suffix, etc.
        sigma_pial: Save pial surface sigma as overlay. Specify full path\
            including hemi, suffix, etc.
        output: Append suffix to all outputs to prevent over-writing.
        min_border_white: Minimum border white.
        max_border_white: Maximum border white.
        min_gray_white_border: Minimum gray at white border.
        max_gray: Maximum gray value.
        max_gray_csf_border: Maximum gray at CSF border.
        min_gray_csf_border: Minimum gray at CSF border.
        max_csf: Maximum CSF value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMakeSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MAKE_SURFACES_METADATA)
    params = mris_make_surfaces_params(
        subject_name=subject_name,
        hemisphere=hemisphere,
        white=white,
        pial=pial,
        whiteonly=whiteonly,
        nowhite=nowhite,
        orig_white=orig_white,
        orig_pial=orig_pial,
        q=q,
        max_gray_scale=max_gray_scale,
        c=c,
        cortex=cortex,
        w=w,
        first_wm_peak=first_wm_peak,
        a_avgs=a_avgs,
        pa_avgs=pa_avgs,
        wa_avgs=wa_avgs,
        t1_vol=t1_vol,
        w_vol=w_vol,
        long=long,
        dura_thresh=dura_thresh,
        sdir=sdir,
        erase_cerebellum=erase_cerebellum,
        wm_weight=wm_weight,
        nsigma_above=nsigma_above,
        nsigma_below=nsigma_below,
        t2_min_inside=t2_min_inside,
        t2_max_inside=t2_max_inside,
        t2_outside_min=t2_outside_min,
        t2_outside_max=t2_outside_max,
        min_peak_pct=min_peak_pct,
        border_vals_hires=border_vals_hires,
        no_unitize=no_unitize,
        intensity=intensity,
        curv=curv,
        tspring=tspring,
        nspring=nspring,
        repulse=repulse,
        save_target=save_target,
        save_res=save_res,
        v_vertexno=v_vertexno,
        diag_vertex=diag_vertex,
        rip=rip,
        sigma_white=sigma_white,
        sigma_pial=sigma_pial,
        output=output,
        min_border_white=min_border_white,
        max_border_white=max_border_white,
        min_gray_white_border=min_gray_white_border,
        max_gray=max_gray,
        max_gray_csf_border=max_gray_csf_border,
        min_gray_csf_border=min_gray_csf_border,
        max_csf=max_csf,
    )
    return mris_make_surfaces_execute(params, execution)


__all__ = [
    "MRIS_MAKE_SURFACES_METADATA",
    "MrisMakeSurfacesOutputs",
    "MrisMakeSurfacesParameters",
    "mris_make_surfaces",
    "mris_make_surfaces_params",
]
