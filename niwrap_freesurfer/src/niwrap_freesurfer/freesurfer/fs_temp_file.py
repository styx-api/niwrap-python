# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FS_TEMP_FILE_METADATA = Metadata(
    id="517fdbcd5c110803a94e295435754191461fd4ee.boutiques",
    name="fs_temp_file",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsTempFileParameters = typing.TypedDict('FsTempFileParameters', {
    "__STYX_TYPE__": typing.Literal["fs_temp_file"],
    "base_dir_alt": typing.NotRequired[str | None],
    "suffix_alt": typing.NotRequired[str | None],
    "scratch": bool,
    "help_alt": bool,
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
        "fs_temp_file": fs_temp_file_cargs,
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


class FsTempFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_temp_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fs_temp_file_params(
    base_dir_alt: str | None = None,
    suffix_alt: str | None = None,
    scratch: bool = False,
    help_alt: bool = False,
) -> FsTempFileParameters:
    """
    Build parameters.
    
    Args:
        base_dir_alt: Manually specify base temporary directory.
        suffix_alt: Optional file suffix.
        scratch: Use /scratch directory if available, but FS_TMPDIR takes\
            priority.
        help_alt: Print help text and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_temp_file",
        "scratch": scratch,
        "help_alt": help_alt,
    }
    if base_dir_alt is not None:
        params["base_dir_alt"] = base_dir_alt
    if suffix_alt is not None:
        params["suffix_alt"] = suffix_alt
    return params


def fs_temp_file_cargs(
    params: FsTempFileParameters,
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
    cargs.append("fs_temp_file")
    if params.get("base_dir_alt") is not None:
        cargs.extend([
            "--base",
            params.get("base_dir_alt")
        ])
    if params.get("suffix_alt") is not None:
        cargs.extend([
            "--suffix",
            params.get("suffix_alt")
        ])
    if params.get("scratch"):
        cargs.append("--scratch")
    if params.get("help_alt"):
        cargs.append("--help")
    return cargs


def fs_temp_file_outputs(
    params: FsTempFileParameters,
    execution: Execution,
) -> FsTempFileOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsTempFileOutputs(
        root=execution.output_file("."),
    )
    return ret


def fs_temp_file_execute(
    params: FsTempFileParameters,
    execution: Execution,
) -> FsTempFileOutputs:
    """
    Generates and creates an empty temporary file, printing the resulting path to
    stdout.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsTempFileOutputs`).
    """
    params = execution.params(params)
    cargs = fs_temp_file_cargs(params, execution)
    ret = fs_temp_file_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_temp_file(
    base_dir_alt: str | None = None,
    suffix_alt: str | None = None,
    scratch: bool = False,
    help_alt: bool = False,
    runner: Runner | None = None,
) -> FsTempFileOutputs:
    """
    Generates and creates an empty temporary file, printing the resulting path to
    stdout.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        base_dir_alt: Manually specify base temporary directory.
        suffix_alt: Optional file suffix.
        scratch: Use /scratch directory if available, but FS_TMPDIR takes\
            priority.
        help_alt: Print help text and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsTempFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_TEMP_FILE_METADATA)
    params = fs_temp_file_params(
        base_dir_alt=base_dir_alt,
        suffix_alt=suffix_alt,
        scratch=scratch,
        help_alt=help_alt,
    )
    return fs_temp_file_execute(params, execution)


__all__ = [
    "FS_TEMP_FILE_METADATA",
    "FsTempFileOutputs",
    "FsTempFileParameters",
    "fs_temp_file",
    "fs_temp_file_params",
]
