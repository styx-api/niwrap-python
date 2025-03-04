# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

REINFLATE_SUBJECT_METADATA = Metadata(
    id="1e08a83747d403bdb6fd509a84d2ca27a452f873.boutiques",
    name="reinflate_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


ReinflateSubjectParameters = typing.TypedDict('ReinflateSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["reinflate_subject"],
    "args": typing.NotRequired[str | None],
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
        "reinflate_subject": reinflate_subject_cargs,
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


class ReinflateSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reinflate_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def reinflate_subject_params(
    args: str | None = None,
) -> ReinflateSubjectParameters:
    """
    Build parameters.
    
    Args:
        args: Arguments for reinflate_subject.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reinflate_subject",
    }
    if args is not None:
        params["args"] = args
    return params


def reinflate_subject_cargs(
    params: ReinflateSubjectParameters,
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
    cargs.append("reinflate_subject")
    if params.get("args") is not None:
        cargs.append(params.get("args"))
    return cargs


def reinflate_subject_outputs(
    params: ReinflateSubjectParameters,
    execution: Execution,
) -> ReinflateSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReinflateSubjectOutputs(
        root=execution.output_file("."),
    )
    return ret


def reinflate_subject_execute(
    params: ReinflateSubjectParameters,
    execution: Execution,
) -> ReinflateSubjectOutputs:
    """
    Tool for reinflating brain surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReinflateSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = reinflate_subject_cargs(params, execution)
    ret = reinflate_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def reinflate_subject(
    args: str | None = None,
    runner: Runner | None = None,
) -> ReinflateSubjectOutputs:
    """
    Tool for reinflating brain surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Arguments for reinflate_subject.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReinflateSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REINFLATE_SUBJECT_METADATA)
    params = reinflate_subject_params(
        args=args,
    )
    return reinflate_subject_execute(params, execution)


__all__ = [
    "REINFLATE_SUBJECT_METADATA",
    "ReinflateSubjectOutputs",
    "ReinflateSubjectParameters",
    "reinflate_subject",
    "reinflate_subject_params",
]
