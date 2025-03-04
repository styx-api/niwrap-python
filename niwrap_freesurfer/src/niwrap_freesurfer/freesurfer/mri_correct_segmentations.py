# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CORRECT_SEGMENTATIONS_METADATA = Metadata(
    id="bc3ea4572fe4ebef8155dbeace0ea841cbc2a21c.boutiques",
    name="mri_correct_segmentations",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCorrectSegmentationsParameters = typing.TypedDict('MriCorrectSegmentationsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_correct_segmentations"],
    "input_file_1": InputPathType,
    "input_file_2": InputPathType,
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
        "mri_correct_segmentations": mri_correct_segmentations_cargs,
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


class MriCorrectSegmentationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_correct_segmentations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_correct_segmentations_params(
    input_file_1: InputPathType,
    input_file_2: InputPathType,
) -> MriCorrectSegmentationsParameters:
    """
    Build parameters.
    
    Args:
        input_file_1: First input file for correction (e.g. segmentation file).
        input_file_2: Second input file for correction (e.g. reference file).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_correct_segmentations",
        "input_file_1": input_file_1,
        "input_file_2": input_file_2,
    }
    return params


def mri_correct_segmentations_cargs(
    params: MriCorrectSegmentationsParameters,
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
    cargs.append("mri_correct_segmentations")
    cargs.append(execution.input_file(params.get("input_file_1")))
    cargs.append(execution.input_file(params.get("input_file_2")))
    return cargs


def mri_correct_segmentations_outputs(
    params: MriCorrectSegmentationsParameters,
    execution: Execution,
) -> MriCorrectSegmentationsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCorrectSegmentationsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_correct_segmentations_execute(
    params: MriCorrectSegmentationsParameters,
    execution: Execution,
) -> MriCorrectSegmentationsOutputs:
    """
    Tool for correcting automated infant segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCorrectSegmentationsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_correct_segmentations_cargs(params, execution)
    ret = mri_correct_segmentations_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_correct_segmentations(
    input_file_1: InputPathType,
    input_file_2: InputPathType,
    runner: Runner | None = None,
) -> MriCorrectSegmentationsOutputs:
    """
    Tool for correcting automated infant segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file_1: First input file for correction (e.g. segmentation file).
        input_file_2: Second input file for correction (e.g. reference file).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCorrectSegmentationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CORRECT_SEGMENTATIONS_METADATA)
    params = mri_correct_segmentations_params(
        input_file_1=input_file_1,
        input_file_2=input_file_2,
    )
    return mri_correct_segmentations_execute(params, execution)


__all__ = [
    "MRI_CORRECT_SEGMENTATIONS_METADATA",
    "MriCorrectSegmentationsOutputs",
    "MriCorrectSegmentationsParameters",
    "mri_correct_segmentations",
    "mri_correct_segmentations_params",
]
