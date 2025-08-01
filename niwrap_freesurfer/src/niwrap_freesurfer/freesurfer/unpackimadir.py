# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNPACKIMADIR_METADATA = Metadata(
    id="6a27f64ee58627da90e1a875d70fa5b839c021e5.boutiques",
    name="unpackimadir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


UnpackimadirParameters = typing.TypedDict('UnpackimadirParameters', {
    "__STYXTYPE__": typing.Literal["unpackimadir"],
    "source_directory": str,
    "target_directory": str,
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
        "unpackimadir": unpackimadir_cargs,
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


class UnpackimadirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpackimadir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def unpackimadir_params(
    source_directory: str,
    target_directory: str,
) -> UnpackimadirParameters:
    """
    Build parameters.
    
    Args:
        source_directory: Source directory containing the images to be unpacked.
        target_directory: Target directory where the unpacked images will be\
            stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "unpackimadir",
        "source_directory": source_directory,
        "target_directory": target_directory,
    }
    return params


def unpackimadir_cargs(
    params: UnpackimadirParameters,
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
    cargs.append("unpackimadir")
    cargs.extend([
        "-src",
        params.get("source_directory")
    ])
    cargs.extend([
        "-targ",
        params.get("target_directory")
    ])
    return cargs


def unpackimadir_outputs(
    params: UnpackimadirParameters,
    execution: Execution,
) -> UnpackimadirOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UnpackimadirOutputs(
        root=execution.output_file("."),
    )
    return ret


def unpackimadir_execute(
    params: UnpackimadirParameters,
    execution: Execution,
) -> UnpackimadirOutputs:
    """
    Unpack image directories.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UnpackimadirOutputs`).
    """
    params = execution.params(params)
    cargs = unpackimadir_cargs(params, execution)
    ret = unpackimadir_outputs(params, execution)
    execution.run(cargs)
    return ret


def unpackimadir(
    source_directory: str,
    target_directory: str,
    runner: Runner | None = None,
) -> UnpackimadirOutputs:
    """
    Unpack image directories.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_directory: Source directory containing the images to be unpacked.
        target_directory: Target directory where the unpacked images will be\
            stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackimadirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACKIMADIR_METADATA)
    params = unpackimadir_params(
        source_directory=source_directory,
        target_directory=target_directory,
    )
    return unpackimadir_execute(params, execution)


__all__ = [
    "UNPACKIMADIR_METADATA",
    "UnpackimadirOutputs",
    "UnpackimadirParameters",
    "unpackimadir",
    "unpackimadir_params",
]
