# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FREEVIEW_METADATA = Metadata(
    id="c7a33420dcdb44d944cc751c512e7e743300b534.boutiques",
    name="freeview",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FreeviewParameters = typing.TypedDict('FreeviewParameters', {
    "__STYX_TYPE__": typing.Literal["freeview"],
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
        "freeview": freeview_cargs,
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


class FreeviewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `freeview(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def freeview_params(
    args: str | None = None,
) -> FreeviewParameters:
    """
    Build parameters.
    
    Args:
        args: Arguments for freeview.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "freeview",
    }
    if args is not None:
        params["args"] = args
    return params


def freeview_cargs(
    params: FreeviewParameters,
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
    cargs.append("freeview")
    if params.get("args") is not None:
        cargs.append(params.get("args"))
    return cargs


def freeview_outputs(
    params: FreeviewParameters,
    execution: Execution,
) -> FreeviewOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FreeviewOutputs(
        root=execution.output_file("."),
    )
    return ret


def freeview_execute(
    params: FreeviewParameters,
    execution: Execution,
) -> FreeviewOutputs:
    """
    Freeview is a 3D/2D brain visualization tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FreeviewOutputs`).
    """
    params = execution.params(params)
    cargs = freeview_cargs(params, execution)
    ret = freeview_outputs(params, execution)
    execution.run(cargs)
    return ret


def freeview(
    args: str | None = None,
    runner: Runner | None = None,
) -> FreeviewOutputs:
    """
    Freeview is a 3D/2D brain visualization tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Arguments for freeview.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FreeviewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FREEVIEW_METADATA)
    params = freeview_params(
        args=args,
    )
    return freeview_execute(params, execution)


__all__ = [
    "FREEVIEW_METADATA",
    "FreeviewOutputs",
    "FreeviewParameters",
    "freeview",
    "freeview_params",
]
