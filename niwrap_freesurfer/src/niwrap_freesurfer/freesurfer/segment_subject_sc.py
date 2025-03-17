# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_SUBJECT_SC_METADATA = Metadata(
    id="fa16d65c7df23bac2f3fce0055543daf1ef20f51.boutiques",
    name="segment_subject_sc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SegmentSubjectScParameters = typing.TypedDict('SegmentSubjectScParameters', {
    "__STYX_TYPE__": typing.Literal["segment_subject_sc"],
    "invol": InputPathType,
    "outxfm": InputPathType,
    "log": typing.NotRequired[str | None],
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
        "segment_subject_sc": segment_subject_sc_cargs,
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
        "segment_subject_sc": segment_subject_sc_outputs,
    }.get(t)


class SegmentSubjectScOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_sc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_xfm_file: OutputPathType
    """Output transform file (xfm)"""


def segment_subject_sc_params(
    invol: InputPathType,
    outxfm: InputPathType,
    log: str | None = "outdir/talarach.log",
    debug: bool = False,
) -> SegmentSubjectScParameters:
    """
    Build parameters.
    
    Args:
        invol: Input volume.
        outxfm: Output xfm file.
        log: Log file. Default is outdir/talarach.log.
        debug: Turn on debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segment_subject_sc",
        "invol": invol,
        "outxfm": outxfm,
        "debug": debug,
    }
    if log is not None:
        params["log"] = log
    return params


def segment_subject_sc_cargs(
    params: SegmentSubjectScParameters,
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
    cargs.append("segment_subject_sc")
    cargs.extend([
        "-i",
        execution.input_file(params.get("invol"))
    ])
    cargs.extend([
        "-xfm",
        execution.input_file(params.get("outxfm"))
    ])
    if params.get("log") is not None:
        cargs.extend([
            "--log",
            params.get("log")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def segment_subject_sc_outputs(
    params: SegmentSubjectScParameters,
    execution: Execution,
) -> SegmentSubjectScOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectScOutputs(
        root=execution.output_file("."),
        output_xfm_file=execution.output_file(pathlib.Path(params.get("outxfm")).name),
    )
    return ret


def segment_subject_sc_execute(
    params: SegmentSubjectScParameters,
    execution: Execution,
) -> SegmentSubjectScOutputs:
    """
    Front-end for MINC's mritotal. Computes the Talairach transform for mapping the
    input volume to the MNI305 space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectScOutputs`).
    """
    params = execution.params(params)
    cargs = segment_subject_sc_cargs(params, execution)
    ret = segment_subject_sc_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject_sc(
    invol: InputPathType,
    outxfm: InputPathType,
    log: str | None = "outdir/talarach.log",
    debug: bool = False,
    runner: Runner | None = None,
) -> SegmentSubjectScOutputs:
    """
    Front-end for MINC's mritotal. Computes the Talairach transform for mapping the
    input volume to the MNI305 space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        invol: Input volume.
        outxfm: Output xfm file.
        log: Log file. Default is outdir/talarach.log.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectScOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_SC_METADATA)
    params = segment_subject_sc_params(
        invol=invol,
        outxfm=outxfm,
        log=log,
        debug=debug,
    )
    return segment_subject_sc_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_SC_METADATA",
    "SegmentSubjectScOutputs",
    "SegmentSubjectScParameters",
    "segment_subject_sc",
    "segment_subject_sc_params",
]
