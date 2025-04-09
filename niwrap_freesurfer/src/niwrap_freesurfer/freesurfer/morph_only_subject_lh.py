# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MORPH_ONLY_SUBJECT_LH_METADATA = Metadata(
    id="8e5603f71227f3739180dffce6a4cb9e0e78be9d.boutiques",
    name="morph_only_subject-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MorphOnlySubjectLhParameters = typing.TypedDict('MorphOnlySubjectLhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_only_subject-lh"],
    "subject_dir": str,
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
        "morph_only_subject-lh": morph_only_subject_lh_cargs,
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
        "morph_only_subject-lh": morph_only_subject_lh_outputs,
    }.get(t)


class MorphOnlySubjectLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_only_subject_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    morph_results: OutputPathType
    """Output directory with morphological results."""


def morph_only_subject_lh_params(
    subject_dir: str,
) -> MorphOnlySubjectLhParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory of the subject to process.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_only_subject-lh",
        "subject_dir": subject_dir,
    }
    return params


def morph_only_subject_lh_cargs(
    params: MorphOnlySubjectLhParameters,
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
    cargs.append("morph_only_subject-lh")
    cargs.extend([
        "-lh",
        params.get("subject_dir")
    ])
    return cargs


def morph_only_subject_lh_outputs(
    params: MorphOnlySubjectLhParameters,
    execution: Execution,
) -> MorphOnlySubjectLhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphOnlySubjectLhOutputs(
        root=execution.output_file("."),
        morph_results=execution.output_file(params.get("subject_dir") + "/morph_results"),
    )
    return ret


def morph_only_subject_lh_execute(
    params: MorphOnlySubjectLhParameters,
    execution: Execution,
) -> MorphOnlySubjectLhOutputs:
    """
    A tool for morphological processing for the left hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectLhOutputs`).
    """
    params = execution.params(params)
    cargs = morph_only_subject_lh_cargs(params, execution)
    ret = morph_only_subject_lh_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_only_subject_lh(
    subject_dir: str,
    runner: Runner | None = None,
) -> MorphOnlySubjectLhOutputs:
    """
    A tool for morphological processing for the left hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory of the subject to process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_ONLY_SUBJECT_LH_METADATA)
    params = morph_only_subject_lh_params(
        subject_dir=subject_dir,
    )
    return morph_only_subject_lh_execute(params, execution)


__all__ = [
    "MORPH_ONLY_SUBJECT_LH_METADATA",
    "MorphOnlySubjectLhOutputs",
    "MorphOnlySubjectLhParameters",
    "morph_only_subject_lh",
    "morph_only_subject_lh_params",
]
