# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSREALPATH_METADATA = Metadata(
    id="ef28f86a2514a0354df33824818f45a5947ff878.boutiques",
    name="fsrealpath",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsrealpathParameters = typing.TypedDict('FsrealpathParameters', {
    "__STYX_TYPE__": typing.Literal["fsrealpath"],
    "path": str,
    "help": bool,
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
        "fsrealpath": fsrealpath_cargs,
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


class FsrealpathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsrealpath(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsrealpath_params(
    path: str,
    help_: bool = False,
) -> FsrealpathParameters:
    """
    Build parameters.
    
    Args:
        path: The path to resolve.
        help_: Show this help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsrealpath",
        "path": path,
        "help": help_,
    }
    return params


def fsrealpath_cargs(
    params: FsrealpathParameters,
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
    cargs.append("fsrealpath")
    cargs.append(params.get("path"))
    if params.get("help"):
        cargs.append("-h")
    return cargs


def fsrealpath_outputs(
    params: FsrealpathParameters,
    execution: Execution,
) -> FsrealpathOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsrealpathOutputs(
        root=execution.output_file("."),
    )
    return ret


def fsrealpath_execute(
    params: FsrealpathParameters,
    execution: Execution,
) -> FsrealpathOutputs:
    """
    Resolve symbolic links in a path.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsrealpathOutputs`).
    """
    params = execution.params(params)
    cargs = fsrealpath_cargs(params, execution)
    ret = fsrealpath_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsrealpath(
    path: str,
    help_: bool = False,
    runner: Runner | None = None,
) -> FsrealpathOutputs:
    """
    Resolve symbolic links in a path.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        path: The path to resolve.
        help_: Show this help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsrealpathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSREALPATH_METADATA)
    params = fsrealpath_params(
        path=path,
        help_=help_,
    )
    return fsrealpath_execute(params, execution)


__all__ = [
    "FSREALPATH_METADATA",
    "FsrealpathOutputs",
    "FsrealpathParameters",
    "fsrealpath",
    "fsrealpath_params",
]
