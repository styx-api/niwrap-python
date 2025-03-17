# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IS_SURFACE_METADATA = Metadata(
    id="86c411bc39041a8b3eae45962259ad09e76de3b1.boutiques",
    name="is-surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


IsSurfaceParameters = typing.TypedDict('IsSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["is-surface"],
    "infile": InputPathType,
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
        "is-surface": is_surface_cargs,
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


class IsSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `is_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def is_surface_params(
    infile: InputPathType,
) -> IsSurfaceParameters:
    """
    Build parameters.
    
    Args:
        infile: Input file to check if it's a surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "is-surface",
        "infile": infile,
    }
    return params


def is_surface_cargs(
    params: IsSurfaceParameters,
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
    cargs.append("is-surface")
    cargs.extend([
        "-surface",
        execution.input_file(params.get("infile"))
    ])
    return cargs


def is_surface_outputs(
    params: IsSurfaceParameters,
    execution: Execution,
) -> IsSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsSurfaceOutputs(
        root=execution.output_file("."),
    )
    return ret


def is_surface_execute(
    params: IsSurfaceParameters,
    execution: Execution,
) -> IsSurfaceOutputs:
    """
    Determines whether a file is a volume-encoded surface file by examining its
    dimensions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsSurfaceOutputs`).
    """
    params = execution.params(params)
    cargs = is_surface_cargs(params, execution)
    ret = is_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def is_surface(
    infile: InputPathType,
    runner: Runner | None = None,
) -> IsSurfaceOutputs:
    """
    Determines whether a file is a volume-encoded surface file by examining its
    dimensions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file to check if it's a surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IS_SURFACE_METADATA)
    params = is_surface_params(
        infile=infile,
    )
    return is_surface_execute(params, execution)


__all__ = [
    "IS_SURFACE_METADATA",
    "IsSurfaceOutputs",
    "IsSurfaceParameters",
    "is_surface",
    "is_surface_params",
]
