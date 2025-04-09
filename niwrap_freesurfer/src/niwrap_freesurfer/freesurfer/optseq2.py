# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

OPTSEQ2_METADATA = Metadata(
    id="7c0799dd0a1ffd018ca41b11e7c2ba518f9578e8.boutiques",
    name="optseq2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Optseq2Parameters = typing.TypedDict('Optseq2Parameters', {
    "__STYX_TYPE__": typing.Literal["optseq2"],
    "ntp": float,
    "tr": float,
    "tprescan": float,
    "psdwin": list[float],
    "event": typing.NotRequired[list[str] | None],
    "repvar": typing.NotRequired[str | None],
    "polyfit": typing.NotRequired[float | None],
    "tnullmin": typing.NotRequired[float | None],
    "tnullmax": typing.NotRequired[float | None],
    "nsearch": typing.NotRequired[float | None],
    "tsearch": typing.NotRequired[float | None],
    "first_order_cb": typing.NotRequired[float | None],
    "ar1": typing.NotRequired[float | None],
    "penalize": typing.NotRequired[list[float] | None],
    "evc": typing.NotRequired[list[float] | None],
    "cmtx": typing.NotRequired[InputPathType | None],
    "cost": typing.NotRequired[str | None],
    "sumdelays": bool,
    "seed": typing.NotRequired[float | None],
    "nkeep": typing.NotRequired[float | None],
    "outstem": typing.NotRequired[str | None],
    "mtxstem": typing.NotRequired[str | None],
    "cmtxfile": typing.NotRequired[str | None],
    "summaryfile": typing.NotRequired[str | None],
    "logfile": typing.NotRequired[str | None],
    "pctupdate": typing.NotRequired[float | None],
    "sviterfile": typing.NotRequired[str | None],
    "instem": typing.NotRequired[str | None],
    "input_schedule": typing.NotRequired[list[str] | None],
    "nosearch": bool,
    "help": bool,
    "version": bool,
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
        "optseq2": optseq2_cargs,
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
        "optseq2": optseq2_outputs,
    }.get(t)


class Optseq2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `optseq2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_schedules: OutputPathType | None
    """Output schedules"""
    output_design_matrices: OutputPathType | None
    """Output FIR design matrices"""
    output_contrast_matrix: OutputPathType | None
    """Output contrast matrix"""
    output_summary: OutputPathType | None
    """Output search summary"""
    output_log: OutputPathType | None
    """Output log file"""
    output_sviter: OutputPathType | None
    """Output per-iteration information"""


def optseq2_params(
    ntp: float,
    tr: float,
    tprescan: float,
    psdwin: list[float],
    event: list[str] | None = None,
    repvar: str | None = None,
    polyfit: float | None = None,
    tnullmin: float | None = None,
    tnullmax: float | None = None,
    nsearch: float | None = None,
    tsearch: float | None = None,
    first_order_cb: float | None = None,
    ar1: float | None = None,
    penalize: list[float] | None = None,
    evc: list[float] | None = None,
    cmtx: InputPathType | None = None,
    cost: str | None = None,
    sumdelays: bool = False,
    seed: float | None = None,
    nkeep: float | None = None,
    outstem: str | None = None,
    mtxstem: str | None = None,
    cmtxfile: str | None = None,
    summaryfile: str | None = None,
    logfile: str | None = None,
    pctupdate: float | None = None,
    sviterfile: str | None = None,
    instem: str | None = None,
    input_schedule: list[str] | None = None,
    nosearch: bool = False,
    help_: bool = False,
    version: bool = False,
) -> Optseq2Parameters:
    """
    Build parameters.
    
    Args:
        ntp: Number of time points to be acquired during the scan.
        tr: Temporal resolution of acquisition in seconds.
        tprescan: Start events t seconds before first acquisition.
        psdwin: Post-stimulus window specifications: minimum PSD, maximum PSD,\
            and optional dPSD.
        event: Event type specification with label, duration, and number of\
            repetitions.
        repvar: Allow number of repetitions of event types to vary by\
            percentage, optionally per event.
        polyfit: Add polynomial regressors as nuisance variables of specified\
            order.
        tnullmin: Minimum duration of null time between stimuli in seconds.
        tnullmax: Maximum duration of null time between stimuli in seconds.
        nsearch: Search over a specified number of iterations for schedules.
        tsearch: Search for schedules over a specified number of hours.
        first_order_cb: Pre-optimize first order counter-balancing.
        ar1: Optimize assuming whitening with AR1 parameter.
        penalize: Penalize for presentations being too close with parameters\
            alpha, T, and dtmin.
        evc: Contrast of event types with weights.
        cmtx: Load contrast from ASCII matrix file.
        cost: Specify cost function and its parameters.
        sumdelays: Sum delays when forming contrast matrix.
        seed: Initialize random number generator with seed value.
        nkeep: Number of best schedules to keep.
        outstem: Output stem for saved schedules.
        mtxstem: Output stem for saved design matrices.
        cmtxfile: File for saving contrast matrix.
        summaryfile: File for saving search summary.
        logfile: File for saving log information.
        pctupdate: Percentage interval after which progress is logged.
        sviterfile: File to save information from each iteration.
        instem: Initialize with input schedules that match instem-RRR.par.
        input_schedule: Input schedule files.
        nosearch: Do not perform search for optimal schedules.
        help_: Print help page.
        version: Print version string.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "optseq2",
        "ntp": ntp,
        "tr": tr,
        "tprescan": tprescan,
        "psdwin": psdwin,
        "sumdelays": sumdelays,
        "nosearch": nosearch,
        "help": help_,
        "version": version,
    }
    if event is not None:
        params["event"] = event
    if repvar is not None:
        params["repvar"] = repvar
    if polyfit is not None:
        params["polyfit"] = polyfit
    if tnullmin is not None:
        params["tnullmin"] = tnullmin
    if tnullmax is not None:
        params["tnullmax"] = tnullmax
    if nsearch is not None:
        params["nsearch"] = nsearch
    if tsearch is not None:
        params["tsearch"] = tsearch
    if first_order_cb is not None:
        params["first_order_cb"] = first_order_cb
    if ar1 is not None:
        params["ar1"] = ar1
    if penalize is not None:
        params["penalize"] = penalize
    if evc is not None:
        params["evc"] = evc
    if cmtx is not None:
        params["cmtx"] = cmtx
    if cost is not None:
        params["cost"] = cost
    if seed is not None:
        params["seed"] = seed
    if nkeep is not None:
        params["nkeep"] = nkeep
    if outstem is not None:
        params["outstem"] = outstem
    if mtxstem is not None:
        params["mtxstem"] = mtxstem
    if cmtxfile is not None:
        params["cmtxfile"] = cmtxfile
    if summaryfile is not None:
        params["summaryfile"] = summaryfile
    if logfile is not None:
        params["logfile"] = logfile
    if pctupdate is not None:
        params["pctupdate"] = pctupdate
    if sviterfile is not None:
        params["sviterfile"] = sviterfile
    if instem is not None:
        params["instem"] = instem
    if input_schedule is not None:
        params["input_schedule"] = input_schedule
    return params


def optseq2_cargs(
    params: Optseq2Parameters,
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
    cargs.append("optseq2")
    cargs.extend([
        "--ntp",
        str(params.get("ntp"))
    ])
    cargs.extend([
        "--tr",
        str(params.get("tr"))
    ])
    cargs.extend([
        "--tprescan",
        str(params.get("tprescan"))
    ])
    cargs.extend([
        "--psdwin",
        *map(str, params.get("psdwin"))
    ])
    if params.get("event") is not None:
        cargs.extend([
            "--ev",
            *params.get("event")
        ])
    if params.get("repvar") is not None:
        cargs.extend([
            "--repvar",
            params.get("repvar")
        ])
    if params.get("polyfit") is not None:
        cargs.extend([
            "--polyfit",
            str(params.get("polyfit"))
        ])
    if params.get("tnullmin") is not None:
        cargs.extend([
            "--tnullmin",
            str(params.get("tnullmin"))
        ])
    if params.get("tnullmax") is not None:
        cargs.extend([
            "--tnullmax",
            str(params.get("tnullmax"))
        ])
    if params.get("nsearch") is not None:
        cargs.extend([
            "--nsearch",
            str(params.get("nsearch"))
        ])
    if params.get("tsearch") is not None:
        cargs.extend([
            "--tsearch",
            str(params.get("tsearch"))
        ])
    if params.get("first_order_cb") is not None:
        cargs.extend([
            "--focb",
            str(params.get("first_order_cb"))
        ])
    if params.get("ar1") is not None:
        cargs.extend([
            "--ar1",
            str(params.get("ar1"))
        ])
    if params.get("penalize") is not None:
        cargs.extend([
            "--pen",
            *map(str, params.get("penalize"))
        ])
    if params.get("evc") is not None:
        cargs.extend([
            "--evc",
            *map(str, params.get("evc"))
        ])
    if params.get("cmtx") is not None:
        cargs.extend([
            "--C",
            execution.input_file(params.get("cmtx"))
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "--cost",
            params.get("cost")
        ])
    if params.get("sumdelays"):
        cargs.append("--sumdelays")
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("nkeep") is not None:
        cargs.extend([
            "--nkeep",
            str(params.get("nkeep"))
        ])
    if params.get("outstem") is not None:
        cargs.extend([
            "--o",
            params.get("outstem")
        ])
    if params.get("mtxstem") is not None:
        cargs.extend([
            "--mtx",
            params.get("mtxstem")
        ])
    if params.get("cmtxfile") is not None:
        cargs.extend([
            "--cmtx",
            params.get("cmtxfile")
        ])
    if params.get("summaryfile") is not None:
        cargs.extend([
            "--sum",
            params.get("summaryfile")
        ])
    if params.get("logfile") is not None:
        cargs.extend([
            "--log",
            params.get("logfile")
        ])
    if params.get("pctupdate") is not None:
        cargs.extend([
            "--pctupdate",
            str(params.get("pctupdate"))
        ])
    if params.get("sviterfile") is not None:
        cargs.extend([
            "--sviter",
            params.get("sviterfile")
        ])
    if params.get("instem") is not None:
        cargs.extend([
            "--i",
            params.get("instem")
        ])
    if params.get("input_schedule") is not None:
        cargs.extend([
            "--in",
            *params.get("input_schedule")
        ])
    if params.get("nosearch"):
        cargs.append("--nosearch")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def optseq2_outputs(
    params: Optseq2Parameters,
    execution: Execution,
) -> Optseq2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Optseq2Outputs(
        root=execution.output_file("."),
        output_schedules=execution.output_file(params.get("outstem") + "-RRR.par") if (params.get("outstem") is not None) else None,
        output_design_matrices=execution.output_file(params.get("mtxstem") + "_RRR.mat") if (params.get("mtxstem") is not None) else None,
        output_contrast_matrix=execution.output_file(params.get("cmtxfile")) if (params.get("cmtxfile") is not None) else None,
        output_summary=execution.output_file(params.get("summaryfile")) if (params.get("summaryfile") is not None) else None,
        output_log=execution.output_file(params.get("logfile")) if (params.get("logfile") is not None) else None,
        output_sviter=execution.output_file(params.get("sviterfile")) if (params.get("sviterfile") is not None) else None,
    )
    return ret


def optseq2_execute(
    params: Optseq2Parameters,
    execution: Execution,
) -> Optseq2Outputs:
    """
    Optseq2 is a tool for automatically scheduling events for rapid-presentation
    event-related (RPER) fMRI experiments.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Optseq2Outputs`).
    """
    params = execution.params(params)
    cargs = optseq2_cargs(params, execution)
    ret = optseq2_outputs(params, execution)
    execution.run(cargs)
    return ret


def optseq2(
    ntp: float,
    tr: float,
    tprescan: float,
    psdwin: list[float],
    event: list[str] | None = None,
    repvar: str | None = None,
    polyfit: float | None = None,
    tnullmin: float | None = None,
    tnullmax: float | None = None,
    nsearch: float | None = None,
    tsearch: float | None = None,
    first_order_cb: float | None = None,
    ar1: float | None = None,
    penalize: list[float] | None = None,
    evc: list[float] | None = None,
    cmtx: InputPathType | None = None,
    cost: str | None = None,
    sumdelays: bool = False,
    seed: float | None = None,
    nkeep: float | None = None,
    outstem: str | None = None,
    mtxstem: str | None = None,
    cmtxfile: str | None = None,
    summaryfile: str | None = None,
    logfile: str | None = None,
    pctupdate: float | None = None,
    sviterfile: str | None = None,
    instem: str | None = None,
    input_schedule: list[str] | None = None,
    nosearch: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Optseq2Outputs:
    """
    Optseq2 is a tool for automatically scheduling events for rapid-presentation
    event-related (RPER) fMRI experiments.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        ntp: Number of time points to be acquired during the scan.
        tr: Temporal resolution of acquisition in seconds.
        tprescan: Start events t seconds before first acquisition.
        psdwin: Post-stimulus window specifications: minimum PSD, maximum PSD,\
            and optional dPSD.
        event: Event type specification with label, duration, and number of\
            repetitions.
        repvar: Allow number of repetitions of event types to vary by\
            percentage, optionally per event.
        polyfit: Add polynomial regressors as nuisance variables of specified\
            order.
        tnullmin: Minimum duration of null time between stimuli in seconds.
        tnullmax: Maximum duration of null time between stimuli in seconds.
        nsearch: Search over a specified number of iterations for schedules.
        tsearch: Search for schedules over a specified number of hours.
        first_order_cb: Pre-optimize first order counter-balancing.
        ar1: Optimize assuming whitening with AR1 parameter.
        penalize: Penalize for presentations being too close with parameters\
            alpha, T, and dtmin.
        evc: Contrast of event types with weights.
        cmtx: Load contrast from ASCII matrix file.
        cost: Specify cost function and its parameters.
        sumdelays: Sum delays when forming contrast matrix.
        seed: Initialize random number generator with seed value.
        nkeep: Number of best schedules to keep.
        outstem: Output stem for saved schedules.
        mtxstem: Output stem for saved design matrices.
        cmtxfile: File for saving contrast matrix.
        summaryfile: File for saving search summary.
        logfile: File for saving log information.
        pctupdate: Percentage interval after which progress is logged.
        sviterfile: File to save information from each iteration.
        instem: Initialize with input schedules that match instem-RRR.par.
        input_schedule: Input schedule files.
        nosearch: Do not perform search for optimal schedules.
        help_: Print help page.
        version: Print version string.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Optseq2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OPTSEQ2_METADATA)
    params = optseq2_params(
        ntp=ntp,
        tr=tr,
        tprescan=tprescan,
        psdwin=psdwin,
        event=event,
        repvar=repvar,
        polyfit=polyfit,
        tnullmin=tnullmin,
        tnullmax=tnullmax,
        nsearch=nsearch,
        tsearch=tsearch,
        first_order_cb=first_order_cb,
        ar1=ar1,
        penalize=penalize,
        evc=evc,
        cmtx=cmtx,
        cost=cost,
        sumdelays=sumdelays,
        seed=seed,
        nkeep=nkeep,
        outstem=outstem,
        mtxstem=mtxstem,
        cmtxfile=cmtxfile,
        summaryfile=summaryfile,
        logfile=logfile,
        pctupdate=pctupdate,
        sviterfile=sviterfile,
        instem=instem,
        input_schedule=input_schedule,
        nosearch=nosearch,
        help_=help_,
        version=version,
    )
    return optseq2_execute(params, execution)


__all__ = [
    "OPTSEQ2_METADATA",
    "Optseq2Outputs",
    "Optseq2Parameters",
    "optseq2",
    "optseq2_params",
]
