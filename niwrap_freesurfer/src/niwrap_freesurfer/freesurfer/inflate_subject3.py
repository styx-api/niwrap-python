# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INFLATE_SUBJECT3_METADATA = Metadata(
    id="a274d70311c1a539bade6099eed3c3f3614e2009.boutiques",
    name="inflate_subject3",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


InflateSubject3Parameters = typing.TypedDict('InflateSubject3Parameters', {
    "__STYXTYPE__": typing.Literal["inflate_subject3"],
    "subjects_dir": str,
    "script_name": str,
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
        "inflate_subject3": inflate_subject3_cargs,
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


class InflateSubject3Outputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject3(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inflate_subject3_params(
    subjects_dir: str,
    script_name: str,
) -> InflateSubject3Parameters:
    """
    Build parameters.
    
    Args:
        subjects_dir: The directory where FreeSurfer subjects are stored.
        script_name: The name of the script to be executed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject3",
        "subjects_dir": subjects_dir,
        "script_name": script_name,
    }
    return params


def inflate_subject3_cargs(
    params: InflateSubject3Parameters,
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
    cargs.append("inflate_subject3")
    cargs.append(params.get("subjects_dir"))
    cargs.append(params.get("script_name"))
    return cargs


def inflate_subject3_outputs(
    params: InflateSubject3Parameters,
    execution: Execution,
) -> InflateSubject3Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubject3Outputs(
        root=execution.output_file("."),
    )
    return ret


def inflate_subject3_execute(
    params: InflateSubject3Parameters,
    execution: Execution,
) -> InflateSubject3Outputs:
    """
    A tool related to subject inflation in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubject3Outputs`).
    """
    params = execution.params(params)
    cargs = inflate_subject3_cargs(params, execution)
    ret = inflate_subject3_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject3(
    subjects_dir: str,
    script_name: str,
    runner: Runner | None = None,
) -> InflateSubject3Outputs:
    """
    A tool related to subject inflation in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: The directory where FreeSurfer subjects are stored.
        script_name: The name of the script to be executed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubject3Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT3_METADATA)
    params = inflate_subject3_params(
        subjects_dir=subjects_dir,
        script_name=script_name,
    )
    return inflate_subject3_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT3_METADATA",
    "InflateSubject3Outputs",
    "InflateSubject3Parameters",
    "inflate_subject3",
    "inflate_subject3_params",
]
