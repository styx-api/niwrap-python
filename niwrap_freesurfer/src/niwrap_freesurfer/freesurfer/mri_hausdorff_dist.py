# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_HAUSDORFF_DIST_METADATA = Metadata(
    id="bdcef721bb6481f0dd0eb1df21b37c8534448bd6.boutiques",
    name="mri_hausdorff_dist",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriHausdorffDistParameters = typing.TypedDict('MriHausdorffDistParameters', {
    "__STYXTYPE__": typing.Literal["mri_hausdorff_dist"],
    "vol1": InputPathType,
    "vol2": InputPathType,
    "output_text_file": str,
    "threshold": typing.NotRequired[float | None],
    "input_file_flag": bool,
    "blur_sigma": typing.NotRequired[float | None],
    "max_flag": bool,
    "label_index": typing.NotRequired[float | None],
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
        "mri_hausdorff_dist": mri_hausdorff_dist_cargs,
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
        "mri_hausdorff_dist": mri_hausdorff_dist_outputs,
    }.get(t)


class MriHausdorffDistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_hausdorff_dist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_text: OutputPathType
    """Output text file containing the results of Hausdorff distance
    calculation"""


def mri_hausdorff_dist_params(
    vol1: InputPathType,
    vol2: InputPathType,
    output_text_file: str,
    threshold: float | None = None,
    input_file_flag: bool = False,
    blur_sigma: float | None = None,
    max_flag: bool = False,
    label_index: float | None = None,
) -> MriHausdorffDistParameters:
    """
    Build parameters.
    
    Args:
        vol1: First input volume.
        vol2: Second input volume.
        output_text_file: Output text file.
        threshold: Binarize input volumes with given threshold.
        input_file_flag: Read volumes from an input file (first argument is the\
            input filename).
        blur_sigma: Blur the input image with Gaussian of specified sigma.
        max_flag: Compute the maximum of the minimum distances instead of the\
            mean.
        label_index: Use specified label index as the target label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_hausdorff_dist",
        "vol1": vol1,
        "vol2": vol2,
        "output_text_file": output_text_file,
        "input_file_flag": input_file_flag,
        "max_flag": max_flag,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if blur_sigma is not None:
        params["blur_sigma"] = blur_sigma
    if label_index is not None:
        params["label_index"] = label_index
    return params


def mri_hausdorff_dist_cargs(
    params: MriHausdorffDistParameters,
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
    cargs.append("mri_hausdorff_dist")
    cargs.append(execution.input_file(params.get("vol1")))
    cargs.append(execution.input_file(params.get("vol2")))
    cargs.append(params.get("output_text_file"))
    if params.get("threshold") is not None:
        cargs.extend([
            "-b",
            str(params.get("threshold"))
        ])
    if params.get("input_file_flag"):
        cargs.append("-F")
    if params.get("blur_sigma") is not None:
        cargs.extend([
            "-g",
            str(params.get("blur_sigma"))
        ])
    if params.get("max_flag"):
        cargs.append("-max")
    if params.get("label_index") is not None:
        cargs.extend([
            "-l",
            str(params.get("label_index"))
        ])
    return cargs


def mri_hausdorff_dist_outputs(
    params: MriHausdorffDistParameters,
    execution: Execution,
) -> MriHausdorffDistOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriHausdorffDistOutputs(
        root=execution.output_file("."),
        output_text=execution.output_file(params.get("output_text_file")),
    )
    return ret


def mri_hausdorff_dist_execute(
    params: MriHausdorffDistParameters,
    execution: Execution,
) -> MriHausdorffDistOutputs:
    """
    Tool for computing the mean or max of the minimum distances between point sets
    in 3D volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriHausdorffDistOutputs`).
    """
    params = execution.params(params)
    cargs = mri_hausdorff_dist_cargs(params, execution)
    ret = mri_hausdorff_dist_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_hausdorff_dist(
    vol1: InputPathType,
    vol2: InputPathType,
    output_text_file: str,
    threshold: float | None = None,
    input_file_flag: bool = False,
    blur_sigma: float | None = None,
    max_flag: bool = False,
    label_index: float | None = None,
    runner: Runner | None = None,
) -> MriHausdorffDistOutputs:
    """
    Tool for computing the mean or max of the minimum distances between point sets
    in 3D volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol1: First input volume.
        vol2: Second input volume.
        output_text_file: Output text file.
        threshold: Binarize input volumes with given threshold.
        input_file_flag: Read volumes from an input file (first argument is the\
            input filename).
        blur_sigma: Blur the input image with Gaussian of specified sigma.
        max_flag: Compute the maximum of the minimum distances instead of the\
            mean.
        label_index: Use specified label index as the target label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriHausdorffDistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_HAUSDORFF_DIST_METADATA)
    params = mri_hausdorff_dist_params(
        vol1=vol1,
        vol2=vol2,
        output_text_file=output_text_file,
        threshold=threshold,
        input_file_flag=input_file_flag,
        blur_sigma=blur_sigma,
        max_flag=max_flag,
        label_index=label_index,
    )
    return mri_hausdorff_dist_execute(params, execution)


__all__ = [
    "MRI_HAUSDORFF_DIST_METADATA",
    "MriHausdorffDistOutputs",
    "MriHausdorffDistParameters",
    "mri_hausdorff_dist",
    "mri_hausdorff_dist_params",
]
