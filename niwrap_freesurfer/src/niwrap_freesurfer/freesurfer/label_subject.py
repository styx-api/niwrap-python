# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_SUBJECT_METADATA = Metadata(
    id="91f9c5eb131863d4bbc7a95b5adc4b9fd63410f3.boutiques",
    name="label_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


LabelSubjectParameters = typing.TypedDict('LabelSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["label_subject"],
    "nu_file": typing.NotRequired[InputPathType | None],
    "orig_dir": typing.NotRequired[str | None],
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
        "label_subject": label_subject_cargs,
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
        "label_subject": label_subject_outputs,
    }.get(t)


class LabelSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_mnc: OutputPathType
    """Converted MNC file from the original MRI data"""


def label_subject_params(
    nu_file: InputPathType | None = None,
    orig_dir: str | None = "/usr/local/freesurfer/subjects",
) -> LabelSubjectParameters:
    """
    Build parameters.
    
    Args:
        nu_file: Path to the nu.mgz file. If not provided, defaults to nu.mgz.
        orig_dir: The original MRI data directory. If the nu file is not found,\
            it will search in the given directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label_subject",
    }
    if nu_file is not None:
        params["nu_file"] = nu_file
    if orig_dir is not None:
        params["orig_dir"] = orig_dir
    return params


def label_subject_cargs(
    params: LabelSubjectParameters,
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
    cargs.append("label_subject")
    if params.get("nu_file") is not None:
        cargs.append(execution.input_file(params.get("nu_file")))
    if params.get("orig_dir") is not None:
        cargs.append(params.get("orig_dir"))
    return cargs


def label_subject_outputs(
    params: LabelSubjectParameters,
    execution: Execution,
) -> LabelSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelSubjectOutputs(
        root=execution.output_file("."),
        converted_mnc=execution.output_file("/tmp/nu*.mnc"),
    )
    return ret


def label_subject_execute(
    params: LabelSubjectParameters,
    execution: Execution,
) -> LabelSubjectOutputs:
    """
    A tool for labeling subject MRI data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = label_subject_cargs(params, execution)
    ret = label_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_subject(
    nu_file: InputPathType | None = None,
    orig_dir: str | None = "/usr/local/freesurfer/subjects",
    runner: Runner | None = None,
) -> LabelSubjectOutputs:
    """
    A tool for labeling subject MRI data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        nu_file: Path to the nu.mgz file. If not provided, defaults to nu.mgz.
        orig_dir: The original MRI data directory. If the nu file is not found,\
            it will search in the given directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_SUBJECT_METADATA)
    params = label_subject_params(
        nu_file=nu_file,
        orig_dir=orig_dir,
    )
    return label_subject_execute(params, execution)


__all__ = [
    "LABEL_SUBJECT_METADATA",
    "LabelSubjectOutputs",
    "LabelSubjectParameters",
    "label_subject",
    "label_subject_params",
]
