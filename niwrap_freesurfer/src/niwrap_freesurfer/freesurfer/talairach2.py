# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TALAIRACH2_METADATA = Metadata(
    id="200a3bdd395b88d5b03ecdc9cf8d79338e29d2f2.boutiques",
    name="talairach2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Talairach2Parameters = typing.TypedDict('Talairach2Parameters', {
    "__STYX_TYPE__": typing.Literal["talairach2"],
    "subject_id": str,
    "mgz_flag": typing.NotRequired[str | None],
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
        "talairach2": talairach2_cargs,
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


class Talairach2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `talairach2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def talairach2_params(
    subject_id: str,
    mgz_flag: str | None = None,
) -> Talairach2Parameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject identifier for the talairach transformation.
        mgz_flag: Flag to indicate whether mgz format is used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "talairach2",
        "subject_id": subject_id,
    }
    if mgz_flag is not None:
        params["mgz_flag"] = mgz_flag
    return params


def talairach2_cargs(
    params: Talairach2Parameters,
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
    cargs.append("talairach2")
    cargs.append(params.get("subject_id"))
    if params.get("mgz_flag") is not None:
        cargs.append(params.get("mgz_flag"))
    return cargs


def talairach2_outputs(
    params: Talairach2Parameters,
    execution: Execution,
) -> Talairach2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Talairach2Outputs(
        root=execution.output_file("."),
    )
    return ret


def talairach2_execute(
    params: Talairach2Parameters,
    execution: Execution,
) -> Talairach2Outputs:
    """
    Tool for processing and converting talairach transformation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Talairach2Outputs`).
    """
    params = execution.params(params)
    cargs = talairach2_cargs(params, execution)
    ret = talairach2_outputs(params, execution)
    execution.run(cargs)
    return ret


def talairach2(
    subject_id: str,
    mgz_flag: str | None = None,
    runner: Runner | None = None,
) -> Talairach2Outputs:
    """
    Tool for processing and converting talairach transformation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject identifier for the talairach transformation.
        mgz_flag: Flag to indicate whether mgz format is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Talairach2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALAIRACH2_METADATA)
    params = talairach2_params(
        subject_id=subject_id,
        mgz_flag=mgz_flag,
    )
    return talairach2_execute(params, execution)


__all__ = [
    "TALAIRACH2_METADATA",
    "Talairach2Outputs",
    "Talairach2Parameters",
    "talairach2",
    "talairach2_params",
]
