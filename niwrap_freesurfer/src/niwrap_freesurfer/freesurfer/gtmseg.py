# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GTMSEG_METADATA = Metadata(
    id="4ab9659e70272d979f39dad258eeff58c22157fc.boutiques",
    name="gtmseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


GtmsegParameters = typing.TypedDict('GtmsegParameters', {
    "__STYXTYPE__": typing.Literal["gtmseg"],
    "subject": str,
    "outvol": typing.NotRequired[str | None],
    "usf": typing.NotRequired[float | None],
    "subsegwm": bool,
    "keep_hypo": bool,
    "keep_cc": bool,
    "dmax": typing.NotRequired[float | None],
    "ctx_annot": typing.NotRequired[str | None],
    "wm_annot": typing.NotRequired[str | None],
    "output_usf": typing.NotRequired[float | None],
    "head": typing.NotRequired[str | None],
    "subseg_cbwm": bool,
    "no_pons": bool,
    "no_vermis": bool,
    "ctab": typing.NotRequired[InputPathType | None],
    "no_seg_stats": bool,
    "xcerseg": bool,
    "debug": bool,
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
        "gtmseg": gtmseg_cargs,
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
        "gtmseg": gtmseg_outputs,
    }.get(t)


class GtmsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gtmseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType | None
    """Output segmentation volume"""
    output_ctab: OutputPathType
    """Generated color table for the output segmentation"""


def gtmseg_params(
    subject: str,
    outvol: str | None = "gtmseg.mgz",
    usf: float | None = 2,
    subsegwm: bool = False,
    keep_hypo: bool = False,
    keep_cc: bool = False,
    dmax: float | None = 5,
    ctx_annot: str | None = "aparc 1000 2000",
    wm_annot: str | None = "lobes 3200 4200",
    output_usf: float | None = None,
    head: str | None = None,
    subseg_cbwm: bool = False,
    no_pons: bool = False,
    no_vermis: bool = False,
    ctab: InputPathType | None = None,
    no_seg_stats: bool = False,
    xcerseg: bool = False,
    debug: bool = False,
) -> GtmsegParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject to analyze.
        outvol: Output volume relative to subject/mri.
        usf: Upsampling factor for segmentation resolution.
        subsegwm: Subsegment white matter into lobes.
        keep_hypo: Do not relabel hypointensities as white matter when\
            subsegmenting WM.
        keep_cc: Do not relabel corpus callosum as white matter.
        dmax: Distance threshold for subsegmenting WM.
        ctx_annot: Annotation for cortical segmentation.
        wm_annot: Annotation for WM segmentation with --subsegwm.
        output_usf: Set output upsampling factor different from input USF for\
            debugging.
        head: Use alternative head segmentation file.
        subseg_cbwm: Subsegment cerebellum WM into core and gyri.
        no_pons: Do not add pons segmentation when running xcerebralseg.
        no_vermis: Do not add vermis segmentation when running xcerebralseg.
        ctab: Color table for custom segmentation.
        no_seg_stats: Do not compute segmentation statistics.
        xcerseg: Run xcerebralseg to create apas+head.mgz.
        debug: Enable debugging mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gtmseg",
        "subject": subject,
        "subsegwm": subsegwm,
        "keep_hypo": keep_hypo,
        "keep_cc": keep_cc,
        "subseg_cbwm": subseg_cbwm,
        "no_pons": no_pons,
        "no_vermis": no_vermis,
        "no_seg_stats": no_seg_stats,
        "xcerseg": xcerseg,
        "debug": debug,
    }
    if outvol is not None:
        params["outvol"] = outvol
    if usf is not None:
        params["usf"] = usf
    if dmax is not None:
        params["dmax"] = dmax
    if ctx_annot is not None:
        params["ctx_annot"] = ctx_annot
    if wm_annot is not None:
        params["wm_annot"] = wm_annot
    if output_usf is not None:
        params["output_usf"] = output_usf
    if head is not None:
        params["head"] = head
    if ctab is not None:
        params["ctab"] = ctab
    return params


def gtmseg_cargs(
    params: GtmsegParameters,
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
    cargs.append("gtmseg")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("outvol") is not None:
        cargs.extend([
            "--o",
            params.get("outvol")
        ])
    if params.get("usf") is not None:
        cargs.extend([
            "--usf",
            str(params.get("usf"))
        ])
    if params.get("subsegwm"):
        cargs.append("--subsegwm")
    if params.get("keep_hypo"):
        cargs.append("--keep-hypo")
    if params.get("keep_cc"):
        cargs.append("--keep-cc")
    if params.get("dmax") is not None:
        cargs.extend([
            "--dmax",
            str(params.get("dmax"))
        ])
    if params.get("ctx_annot") is not None:
        cargs.extend([
            "--ctx-annot",
            params.get("ctx_annot")
        ])
    if params.get("wm_annot") is not None:
        cargs.extend([
            "--wm-annot",
            params.get("wm_annot")
        ])
    if params.get("output_usf") is not None:
        cargs.extend([
            "--output-usf",
            str(params.get("output_usf"))
        ])
    if params.get("head") is not None:
        cargs.extend([
            "--head",
            params.get("head")
        ])
    if params.get("subseg_cbwm"):
        cargs.append("--subseg-cblum-wm")
    if params.get("no_pons"):
        cargs.append("--no-pons")
    if params.get("no_vermis"):
        cargs.append("--no-vermis")
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    if params.get("no_seg_stats"):
        cargs.append("--no-seg-stats")
    if params.get("xcerseg"):
        cargs.append("--xcerseg")
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def gtmseg_outputs(
    params: GtmsegParameters,
    execution: Execution,
) -> GtmsegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GtmsegOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file("$SUBJECTS_DIR/" + params.get("subject") + "/mri/" + params.get("outvol")) if (params.get("outvol") is not None) else None,
        output_ctab=execution.output_file("$SUBJECTS_DIR/" + params.get("subject") + "/mri/gtmseg+myseg.ctab"),
    )
    return ret


def gtmseg_execute(
    params: GtmsegParameters,
    execution: Execution,
) -> GtmsegOutputs:
    """
    Creates an anatomical segmentation for the geometric transfer matrix (GTM) used
    in PET partial volume correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GtmsegOutputs`).
    """
    params = execution.params(params)
    cargs = gtmseg_cargs(params, execution)
    ret = gtmseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def gtmseg(
    subject: str,
    outvol: str | None = "gtmseg.mgz",
    usf: float | None = 2,
    subsegwm: bool = False,
    keep_hypo: bool = False,
    keep_cc: bool = False,
    dmax: float | None = 5,
    ctx_annot: str | None = "aparc 1000 2000",
    wm_annot: str | None = "lobes 3200 4200",
    output_usf: float | None = None,
    head: str | None = None,
    subseg_cbwm: bool = False,
    no_pons: bool = False,
    no_vermis: bool = False,
    ctab: InputPathType | None = None,
    no_seg_stats: bool = False,
    xcerseg: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> GtmsegOutputs:
    """
    Creates an anatomical segmentation for the geometric transfer matrix (GTM) used
    in PET partial volume correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to analyze.
        outvol: Output volume relative to subject/mri.
        usf: Upsampling factor for segmentation resolution.
        subsegwm: Subsegment white matter into lobes.
        keep_hypo: Do not relabel hypointensities as white matter when\
            subsegmenting WM.
        keep_cc: Do not relabel corpus callosum as white matter.
        dmax: Distance threshold for subsegmenting WM.
        ctx_annot: Annotation for cortical segmentation.
        wm_annot: Annotation for WM segmentation with --subsegwm.
        output_usf: Set output upsampling factor different from input USF for\
            debugging.
        head: Use alternative head segmentation file.
        subseg_cbwm: Subsegment cerebellum WM into core and gyri.
        no_pons: Do not add pons segmentation when running xcerebralseg.
        no_vermis: Do not add vermis segmentation when running xcerebralseg.
        ctab: Color table for custom segmentation.
        no_seg_stats: Do not compute segmentation statistics.
        xcerseg: Run xcerebralseg to create apas+head.mgz.
        debug: Enable debugging mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GtmsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GTMSEG_METADATA)
    params = gtmseg_params(
        subject=subject,
        outvol=outvol,
        usf=usf,
        subsegwm=subsegwm,
        keep_hypo=keep_hypo,
        keep_cc=keep_cc,
        dmax=dmax,
        ctx_annot=ctx_annot,
        wm_annot=wm_annot,
        output_usf=output_usf,
        head=head,
        subseg_cbwm=subseg_cbwm,
        no_pons=no_pons,
        no_vermis=no_vermis,
        ctab=ctab,
        no_seg_stats=no_seg_stats,
        xcerseg=xcerseg,
        debug=debug,
    )
    return gtmseg_execute(params, execution)


__all__ = [
    "GTMSEG_METADATA",
    "GtmsegOutputs",
    "GtmsegParameters",
    "gtmseg",
    "gtmseg_params",
]
