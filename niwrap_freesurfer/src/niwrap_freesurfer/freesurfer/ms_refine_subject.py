# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MS_REFINE_SUBJECT_METADATA = Metadata(
    id="f721290b4f615b29593a88005b00f64f24e7ebf7.boutiques",
    name="ms_refine_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MsRefineSubjectParameters = typing.TypedDict('MsRefineSubjectParameters', {
    "__STYXTYPE__": typing.Literal["ms_refine_subject"],
    "subjects_dir": str,
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
        "ms_refine_subject": ms_refine_subject_cargs,
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


class MsRefineSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ms_refine_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ms_refine_subject_params(
    subjects_dir: str,
) -> MsRefineSubjectParameters:
    """
    Build parameters.
    
    Args:
        subjects_dir: Directory containing the subject data (e.g.\
            /usr/local/freesurfer/subjects).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ms_refine_subject",
        "subjects_dir": subjects_dir,
    }
    return params


def ms_refine_subject_cargs(
    params: MsRefineSubjectParameters,
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
    cargs.append("ms_refine_subject")
    cargs.append(params.get("subjects_dir"))
    return cargs


def ms_refine_subject_outputs(
    params: MsRefineSubjectParameters,
    execution: Execution,
) -> MsRefineSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MsRefineSubjectOutputs(
        root=execution.output_file("."),
    )
    return ret


def ms_refine_subject_execute(
    params: MsRefineSubjectParameters,
    execution: Execution,
) -> MsRefineSubjectOutputs:
    """
    Unknown.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MsRefineSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = ms_refine_subject_cargs(params, execution)
    ret = ms_refine_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def ms_refine_subject(
    subjects_dir: str,
    runner: Runner | None = None,
) -> MsRefineSubjectOutputs:
    """
    Unknown.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Directory containing the subject data (e.g.\
            /usr/local/freesurfer/subjects).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MsRefineSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MS_REFINE_SUBJECT_METADATA)
    params = ms_refine_subject_params(
        subjects_dir=subjects_dir,
    )
    return ms_refine_subject_execute(params, execution)


__all__ = [
    "MS_REFINE_SUBJECT_METADATA",
    "MsRefineSubjectOutputs",
    "MsRefineSubjectParameters",
    "ms_refine_subject",
    "ms_refine_subject_params",
]
