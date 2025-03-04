# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_SUBJECT_METADATA = Metadata(
    id="5ab5fa41476c4d8921b2a5ed52d0505305a8ad2b.boutiques",
    name="segment_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SegmentSubjectParameters = typing.TypedDict('SegmentSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["segment_subject"],
    "input_volume": InputPathType,
    "output_xfm": str,
    "log_file": typing.NotRequired[str | None],
    "help_flag": bool,
    "debug_flag": bool,
    "version_flag": bool,
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
        "segment_subject": segment_subject_cargs,
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
        "segment_subject": segment_subject_outputs,
    }.get(t)


class SegmentSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_xfm_file: OutputPathType
    """Output transformation file"""


def segment_subject_params(
    input_volume: InputPathType,
    output_xfm: str,
    log_file: str | None = None,
    help_flag: bool = False,
    debug_flag: bool = False,
    version_flag: bool = False,
) -> SegmentSubjectParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume.
        output_xfm: Output transformation file.
        log_file: Log file. Default is outdir/talarach.log.
        help_flag: Print help and exit.
        debug_flag: Turn on debugging.
        version_flag: Print version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segment_subject",
        "input_volume": input_volume,
        "output_xfm": output_xfm,
        "help_flag": help_flag,
        "debug_flag": debug_flag,
        "version_flag": version_flag,
    }
    if log_file is not None:
        params["log_file"] = log_file
    return params


def segment_subject_cargs(
    params: SegmentSubjectParameters,
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
    cargs.append("mri_nu_correct.mni")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--xfm",
        params.get("output_xfm")
    ])
    if params.get("log_file") is not None:
        cargs.extend([
            "--log",
            params.get("log_file")
        ])
    if params.get("help_flag"):
        cargs.append("--help")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("version_flag"):
        cargs.append("--version")
    return cargs


def segment_subject_outputs(
    params: SegmentSubjectParameters,
    execution: Execution,
) -> SegmentSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubjectOutputs(
        root=execution.output_file("."),
        output_xfm_file=execution.output_file(params.get("output_xfm")),
    )
    return ret


def segment_subject_execute(
    params: SegmentSubjectParameters,
    execution: Execution,
) -> SegmentSubjectOutputs:
    """
    Front-end for MINCs mritotal to compute the Talairach transform that maps the
    input volume to the MNI305 space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = segment_subject_cargs(params, execution)
    ret = segment_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subject(
    input_volume: InputPathType,
    output_xfm: str,
    log_file: str | None = None,
    help_flag: bool = False,
    debug_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> SegmentSubjectOutputs:
    """
    Front-end for MINCs mritotal to compute the Talairach transform that maps the
    input volume to the MNI305 space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        output_xfm: Output transformation file.
        log_file: Log file. Default is outdir/talarach.log.
        help_flag: Print help and exit.
        debug_flag: Turn on debugging.
        version_flag: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_METADATA)
    params = segment_subject_params(
        input_volume=input_volume,
        output_xfm=output_xfm,
        log_file=log_file,
        help_flag=help_flag,
        debug_flag=debug_flag,
        version_flag=version_flag,
    )
    return segment_subject_execute(params, execution)


__all__ = [
    "SEGMENT_SUBJECT_METADATA",
    "SegmentSubjectOutputs",
    "SegmentSubjectParameters",
    "segment_subject",
    "segment_subject_params",
]
