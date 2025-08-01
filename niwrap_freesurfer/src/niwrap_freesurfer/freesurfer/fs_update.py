# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FS_UPDATE_METADATA = Metadata(
    id="7559054caea5811a27d56eadbc3ee13035050ade.boutiques",
    name="fs_update",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsUpdateParameters = typing.TypedDict('FsUpdateParameters', {
    "__STYXTYPE__": typing.Literal["fs_update"],
    "update_path": typing.NotRequired[str | None],
    "help_short": bool,
    "help_medium": bool,
    "help_long": bool,
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
        "fs_update": fs_update_cargs,
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


class FsUpdateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_update(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fs_update_params(
    update_path: str | None = None,
    help_short: bool = False,
    help_medium: bool = False,
    help_long: bool = False,
) -> FsUpdateParameters:
    """
    Build parameters.
    
    Args:
        update_path: Path to specific files or directories to update, copied\
            recursively.
        help_short: Show help.
        help_medium:.
        help_long:.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_update",
        "help_short": help_short,
        "help_medium": help_medium,
        "help_long": help_long,
    }
    if update_path is not None:
        params["update_path"] = update_path
    return params


def fs_update_cargs(
    params: FsUpdateParameters,
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
    cargs.append("fs_update")
    if params.get("update_path") is not None:
        cargs.append(params.get("update_path"))
    if params.get("help_short"):
        cargs.append("-h")
    if params.get("help_medium"):
        cargs.append("-help")
    if params.get("help_long"):
        cargs.append("--help")
    return cargs


def fs_update_outputs(
    params: FsUpdateParameters,
    execution: Execution,
) -> FsUpdateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsUpdateOutputs(
        root=execution.output_file("."),
    )
    return ret


def fs_update_execute(
    params: FsUpdateParameters,
    execution: Execution,
) -> FsUpdateOutputs:
    """
    Utility to update the FreeSurfer installation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsUpdateOutputs`).
    """
    params = execution.params(params)
    cargs = fs_update_cargs(params, execution)
    ret = fs_update_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_update(
    update_path: str | None = None,
    help_short: bool = False,
    help_medium: bool = False,
    help_long: bool = False,
    runner: Runner | None = None,
) -> FsUpdateOutputs:
    """
    Utility to update the FreeSurfer installation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        update_path: Path to specific files or directories to update, copied\
            recursively.
        help_short: Show help.
        help_medium:.
        help_long:.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsUpdateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_UPDATE_METADATA)
    params = fs_update_params(
        update_path=update_path,
        help_short=help_short,
        help_medium=help_medium,
        help_long=help_long,
    )
    return fs_update_execute(params, execution)


__all__ = [
    "FS_UPDATE_METADATA",
    "FsUpdateOutputs",
    "FsUpdateParameters",
    "fs_update",
    "fs_update_params",
]
