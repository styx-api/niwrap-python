# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BUGR_METADATA = Metadata(
    id="c59ecc18f09513a64d6c410b4046dd59f641fd90.boutiques",
    name="bugr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


BugrParameters = typing.TypedDict('BugrParameters', {
    "__STYXTYPE__": typing.Literal["bugr"],
    "subject_name": str,
    "command_line": str,
    "error_message": str,
    "log_file": typing.NotRequired[InputPathType | None],
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
        "bugr": bugr_cargs,
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


class BugrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bugr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bugr_params(
    subject_name: str,
    command_line: str,
    error_message: str,
    log_file: InputPathType | None = None,
) -> BugrParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name to include in the bug report.
        command_line: The entire command-line executed.
        error_message: The error message generated.
        log_file: Log file path of the subject's recon-all process.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bugr",
        "subject_name": subject_name,
        "command_line": command_line,
        "error_message": error_message,
    }
    if log_file is not None:
        params["log_file"] = log_file
    return params


def bugr_cargs(
    params: BugrParameters,
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
    cargs.append("bugr")
    cargs.extend([
        "-subject",
        params.get("subject_name")
    ])
    cargs.extend([
        "-command",
        params.get("command_line")
    ])
    cargs.extend([
        "-error",
        params.get("error_message")
    ])
    if params.get("log_file") is not None:
        cargs.extend([
            "-log",
            execution.input_file(params.get("log_file"))
        ])
    return cargs


def bugr_outputs(
    params: BugrParameters,
    execution: Execution,
) -> BugrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BugrOutputs(
        root=execution.output_file("."),
    )
    return ret


def bugr_execute(
    params: BugrParameters,
    execution: Execution,
) -> BugrOutputs:
    """
    Utility for generating and reporting FreeSurfer bugs.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BugrOutputs`).
    """
    params = execution.params(params)
    cargs = bugr_cargs(params, execution)
    ret = bugr_outputs(params, execution)
    execution.run(cargs)
    return ret


def bugr(
    subject_name: str,
    command_line: str,
    error_message: str,
    log_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> BugrOutputs:
    """
    Utility for generating and reporting FreeSurfer bugs.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name to include in the bug report.
        command_line: The entire command-line executed.
        error_message: The error message generated.
        log_file: Log file path of the subject's recon-all process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BugrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BUGR_METADATA)
    params = bugr_params(
        subject_name=subject_name,
        command_line=command_line,
        error_message=error_message,
        log_file=log_file,
    )
    return bugr_execute(params, execution)


__all__ = [
    "BUGR_METADATA",
    "BugrOutputs",
    "BugrParameters",
    "bugr",
    "bugr_params",
]
