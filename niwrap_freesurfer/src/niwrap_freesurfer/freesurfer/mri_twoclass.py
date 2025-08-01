# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_TWOCLASS_METADATA = Metadata(
    id="a4bd1f841f3834d6bee43f67f3cc687cf2b8aec8.boutiques",
    name="mri_twoclass",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriTwoclassParameters = typing.TypedDict('MriTwoclassParameters', {
    "__STYXTYPE__": typing.Literal["mri_twoclass"],
    "segmentation_volume": InputPathType,
    "output_subject": str,
    "output_volume": str,
    "c1_subjects": list[str],
    "c2_subjects": list[str],
    "f_threshold": typing.NotRequired[float | None],
    "bonferroni_correction": bool,
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
        "mri_twoclass": mri_twoclass_cargs,
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
        "mri_twoclass": mri_twoclass_outputs,
    }.get(t)


class MriTwoclassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_twoclass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_volume: OutputPathType
    """Output volume storing the results"""


def mri_twoclass_params(
    segmentation_volume: InputPathType,
    output_subject: str,
    output_volume: str,
    c1_subjects: list[str],
    c2_subjects: list[str],
    f_threshold: float | None = None,
    bonferroni_correction: bool = False,
) -> MriTwoclassParameters:
    """
    Build parameters.
    
    Args:
        segmentation_volume: Input segmentation volume.
        output_subject: Output subject name.
        output_volume: Output volume.
        c1_subjects: List of subjects from class 1.
        c2_subjects: List of subjects from class 2.
        f_threshold: Specify F threshold.
        bonferroni_correction: Perform Bonferroni correction.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_twoclass",
        "segmentation_volume": segmentation_volume,
        "output_subject": output_subject,
        "output_volume": output_volume,
        "c1_subjects": c1_subjects,
        "c2_subjects": c2_subjects,
        "bonferroni_correction": bonferroni_correction,
    }
    if f_threshold is not None:
        params["f_threshold"] = f_threshold
    return params


def mri_twoclass_cargs(
    params: MriTwoclassParameters,
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
    cargs.append("mri_twoclass")
    cargs.append(execution.input_file(params.get("segmentation_volume")))
    cargs.append(params.get("output_subject"))
    cargs.append(params.get("output_volume"))
    cargs.extend(params.get("c1_subjects"))
    cargs.extend(params.get("c2_subjects"))
    if params.get("f_threshold") is not None:
        cargs.extend([
            "-t",
            str(params.get("f_threshold"))
        ])
    if params.get("bonferroni_correction"):
        cargs.append("-b")
    return cargs


def mri_twoclass_outputs(
    params: MriTwoclassParameters,
    execution: Execution,
) -> MriTwoclassOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriTwoclassOutputs(
        root=execution.output_file("."),
        result_volume=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_twoclass_execute(
    params: MriTwoclassParameters,
    execution: Execution,
) -> MriTwoclassOutputs:
    """
    Compute cross-subject statistics of two sets of labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriTwoclassOutputs`).
    """
    params = execution.params(params)
    cargs = mri_twoclass_cargs(params, execution)
    ret = mri_twoclass_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_twoclass(
    segmentation_volume: InputPathType,
    output_subject: str,
    output_volume: str,
    c1_subjects: list[str],
    c2_subjects: list[str],
    f_threshold: float | None = None,
    bonferroni_correction: bool = False,
    runner: Runner | None = None,
) -> MriTwoclassOutputs:
    """
    Compute cross-subject statistics of two sets of labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segmentation_volume: Input segmentation volume.
        output_subject: Output subject name.
        output_volume: Output volume.
        c1_subjects: List of subjects from class 1.
        c2_subjects: List of subjects from class 2.
        f_threshold: Specify F threshold.
        bonferroni_correction: Perform Bonferroni correction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTwoclassOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TWOCLASS_METADATA)
    params = mri_twoclass_params(
        segmentation_volume=segmentation_volume,
        output_subject=output_subject,
        output_volume=output_volume,
        c1_subjects=c1_subjects,
        c2_subjects=c2_subjects,
        f_threshold=f_threshold,
        bonferroni_correction=bonferroni_correction,
    )
    return mri_twoclass_execute(params, execution)


__all__ = [
    "MRI_TWOCLASS_METADATA",
    "MriTwoclassOutputs",
    "MriTwoclassParameters",
    "mri_twoclass",
    "mri_twoclass_params",
]
