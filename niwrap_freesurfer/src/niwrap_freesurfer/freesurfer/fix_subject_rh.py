# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIX_SUBJECT_RH_METADATA = Metadata(
    id="d6f9654d878ef28530ea8f9531c3a06325244e6b.boutiques",
    name="fix_subject-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FixSubjectRhParameters = typing.TypedDict('FixSubjectRhParameters', {
    "__STYX_TYPE__": typing.Literal["fix_subject-rh"],
    "input_directory": str,
    "help_flag": bool,
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
        "fix_subject-rh": fix_subject_rh_cargs,
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


class FixSubjectRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fix_subject_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fix_subject_rh_params(
    input_directory: str,
    help_flag: bool = False,
) -> FixSubjectRhParameters:
    """
    Build parameters.
    
    Args:
        input_directory: Directory where the subject's right hemisphere data is\
            located.
        help_flag: Displays help information for fix_subject-rh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fix_subject-rh",
        "input_directory": input_directory,
        "help_flag": help_flag,
    }
    return params


def fix_subject_rh_cargs(
    params: FixSubjectRhParameters,
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
    cargs.append("fix_subject-rh")
    cargs.extend([
        "-rh",
        params.get("input_directory")
    ])
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def fix_subject_rh_outputs(
    params: FixSubjectRhParameters,
    execution: Execution,
) -> FixSubjectRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixSubjectRhOutputs(
        root=execution.output_file("."),
    )
    return ret


def fix_subject_rh_execute(
    params: FixSubjectRhParameters,
    execution: Execution,
) -> FixSubjectRhOutputs:
    """
    A tool from FreeSurfer that performs operations on the right hemisphere data
    within a specified directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixSubjectRhOutputs`).
    """
    params = execution.params(params)
    cargs = fix_subject_rh_cargs(params, execution)
    ret = fix_subject_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def fix_subject_rh(
    input_directory: str,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FixSubjectRhOutputs:
    """
    A tool from FreeSurfer that performs operations on the right hemisphere data
    within a specified directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_directory: Directory where the subject's right hemisphere data is\
            located.
        help_flag: Displays help information for fix_subject-rh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixSubjectRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIX_SUBJECT_RH_METADATA)
    params = fix_subject_rh_params(
        input_directory=input_directory,
        help_flag=help_flag,
    )
    return fix_subject_rh_execute(params, execution)


__all__ = [
    "FIX_SUBJECT_RH_METADATA",
    "FixSubjectRhOutputs",
    "FixSubjectRhParameters",
    "fix_subject_rh",
    "fix_subject_rh_params",
]
