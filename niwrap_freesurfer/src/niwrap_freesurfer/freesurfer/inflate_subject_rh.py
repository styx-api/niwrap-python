# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INFLATE_SUBJECT_RH_METADATA = Metadata(
    id="c870a2dd4beffc1dccf8c6c63c1951a8bb440f30.boutiques",
    name="inflate_subject-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


InflateSubjectRhParameters = typing.TypedDict('InflateSubjectRhParameters', {
    "__STYX_TYPE__": typing.Literal["inflate_subject-rh"],
    "arguments": typing.NotRequired[str | None],
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
        "inflate_subject-rh": inflate_subject_rh_cargs,
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


class InflateSubjectRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inflate_subject_rh_params(
    arguments: str | None = None,
) -> InflateSubjectRhParameters:
    """
    Build parameters.
    
    Args:
        arguments: Arguments for the command. Placeholder due to lack of\
            detailed help text.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject-rh",
    }
    if arguments is not None:
        params["arguments"] = arguments
    return params


def inflate_subject_rh_cargs(
    params: InflateSubjectRhParameters,
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
    if params.get("arguments") is not None:
        cargs.extend([
            "-rh",
            "inflate_subject" + params.get("arguments")
        ])
    return cargs


def inflate_subject_rh_outputs(
    params: InflateSubjectRhParameters,
    execution: Execution,
) -> InflateSubjectRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubjectRhOutputs(
        root=execution.output_file("."),
    )
    return ret


def inflate_subject_rh_execute(
    params: InflateSubjectRhParameters,
    execution: Execution,
) -> InflateSubjectRhOutputs:
    """
    Freesurfer command to perform an operation on the right hemisphere of a
    subject's brain image data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectRhOutputs`).
    """
    params = execution.params(params)
    cargs = inflate_subject_rh_cargs(params, execution)
    ret = inflate_subject_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject_rh(
    arguments: str | None = None,
    runner: Runner | None = None,
) -> InflateSubjectRhOutputs:
    """
    Freesurfer command to perform an operation on the right hemisphere of a
    subject's brain image data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        arguments: Arguments for the command. Placeholder due to lack of\
            detailed help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_RH_METADATA)
    params = inflate_subject_rh_params(
        arguments=arguments,
    )
    return inflate_subject_rh_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT_RH_METADATA",
    "InflateSubjectRhOutputs",
    "InflateSubjectRhParameters",
    "inflate_subject_rh",
    "inflate_subject_rh_params",
]
