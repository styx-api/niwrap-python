# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPUTE_SEG_OVERLAP_METADATA = Metadata(
    id="28002ed71580b05451b3cd31d91e0b05078efaf6.boutiques",
    name="mri_compute_seg_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriComputeSegOverlapParameters = typing.TypedDict('MriComputeSegOverlapParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compute_seg_overlap"],
    "segvol1": InputPathType,
    "segvol2": InputPathType,
    "log_file": typing.NotRequired[str | None],
    "mean_log_file": typing.NotRequired[str | None],
    "std_log_file": typing.NotRequired[str | None],
    "overall_log_flag": bool,
    "exclude_cortex_flag": bool,
    "exclude_wm_flag": bool,
    "all_labels_flag": bool,
    "dice_params": typing.NotRequired[str | None],
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
        "mri_compute_seg_overlap": mri_compute_seg_overlap_cargs,
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


class MriComputeSegOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_seg_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_compute_seg_overlap_params(
    segvol1: InputPathType,
    segvol2: InputPathType,
    log_file: str | None = None,
    mean_log_file: str | None = None,
    std_log_file: str | None = None,
    overall_log_flag: bool = False,
    exclude_cortex_flag: bool = False,
    exclude_wm_flag: bool = False,
    all_labels_flag: bool = False,
    dice_params: str | None = None,
) -> MriComputeSegOverlapParameters:
    """
    Build parameters.
    
    Args:
        segvol1: First segmentation volume.
        segvol2: Second segmentation volume.
        log_file: Log file for individual Dice coefficients for 12 structure\
            pairs, plus mean, std, and 'overall'.
        mean_log_file: Log file for mean Dice.
        std_log_file: Log file for std Dice.
        overall_log_flag: Log file for 'overall' Dice (mean excluding wm, gm,\
            and accumbens).
        exclude_cortex_flag: Exclude cerebral cortex labels from all\
            calculation. (0/1 flag, if nonzero).
        exclude_wm_flag: Exclude cerebral white matter labels from all\
            calculation. (0/1 flag, if nonzero).
        all_labels_flag: Check all labels, not just the predefined main\
            structures.
        dice_params: Standalone way to compute Dice coefficients, using seg1,\
            seg2, ctab, ReportEmpty01, ExcludeId, datfile, and tablefile as\
            additional parameters.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_seg_overlap",
        "segvol1": segvol1,
        "segvol2": segvol2,
        "overall_log_flag": overall_log_flag,
        "exclude_cortex_flag": exclude_cortex_flag,
        "exclude_wm_flag": exclude_wm_flag,
        "all_labels_flag": all_labels_flag,
    }
    if log_file is not None:
        params["log_file"] = log_file
    if mean_log_file is not None:
        params["mean_log_file"] = mean_log_file
    if std_log_file is not None:
        params["std_log_file"] = std_log_file
    if dice_params is not None:
        params["dice_params"] = dice_params
    return params


def mri_compute_seg_overlap_cargs(
    params: MriComputeSegOverlapParameters,
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
    cargs.append("mri_compute_seg_overlap")
    cargs.append(execution.input_file(params.get("segvol1")))
    cargs.append(execution.input_file(params.get("segvol2")))
    if params.get("log_file") is not None:
        cargs.extend([
            "-log",
            params.get("log_file")
        ])
    if params.get("mean_log_file") is not None:
        cargs.extend([
            "-mlog",
            params.get("mean_log_file")
        ])
    if params.get("std_log_file") is not None:
        cargs.extend([
            "-slog",
            params.get("std_log_file")
        ])
    if params.get("overall_log_flag"):
        cargs.append("-olog")
    if params.get("exclude_cortex_flag"):
        cargs.append("-cortex")
    if params.get("exclude_wm_flag"):
        cargs.append("-wm")
    if params.get("all_labels_flag"):
        cargs.append("-all_labels")
    if params.get("dice_params") is not None:
        cargs.extend([
            "-dice",
            params.get("dice_params")
        ])
    return cargs


def mri_compute_seg_overlap_outputs(
    params: MriComputeSegOverlapParameters,
    execution: Execution,
) -> MriComputeSegOverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeSegOverlapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_compute_seg_overlap_execute(
    params: MriComputeSegOverlapParameters,
    execution: Execution,
) -> MriComputeSegOverlapOutputs:
    """
    Compute coefficients of overlap between segmentation volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeSegOverlapOutputs`).
    """
    params = execution.params(params)
    cargs = mri_compute_seg_overlap_cargs(params, execution)
    ret = mri_compute_seg_overlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_seg_overlap(
    segvol1: InputPathType,
    segvol2: InputPathType,
    log_file: str | None = None,
    mean_log_file: str | None = None,
    std_log_file: str | None = None,
    overall_log_flag: bool = False,
    exclude_cortex_flag: bool = False,
    exclude_wm_flag: bool = False,
    all_labels_flag: bool = False,
    dice_params: str | None = None,
    runner: Runner | None = None,
) -> MriComputeSegOverlapOutputs:
    """
    Compute coefficients of overlap between segmentation volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segvol1: First segmentation volume.
        segvol2: Second segmentation volume.
        log_file: Log file for individual Dice coefficients for 12 structure\
            pairs, plus mean, std, and 'overall'.
        mean_log_file: Log file for mean Dice.
        std_log_file: Log file for std Dice.
        overall_log_flag: Log file for 'overall' Dice (mean excluding wm, gm,\
            and accumbens).
        exclude_cortex_flag: Exclude cerebral cortex labels from all\
            calculation. (0/1 flag, if nonzero).
        exclude_wm_flag: Exclude cerebral white matter labels from all\
            calculation. (0/1 flag, if nonzero).
        all_labels_flag: Check all labels, not just the predefined main\
            structures.
        dice_params: Standalone way to compute Dice coefficients, using seg1,\
            seg2, ctab, ReportEmpty01, ExcludeId, datfile, and tablefile as\
            additional parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeSegOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_SEG_OVERLAP_METADATA)
    params = mri_compute_seg_overlap_params(
        segvol1=segvol1,
        segvol2=segvol2,
        log_file=log_file,
        mean_log_file=mean_log_file,
        std_log_file=std_log_file,
        overall_log_flag=overall_log_flag,
        exclude_cortex_flag=exclude_cortex_flag,
        exclude_wm_flag=exclude_wm_flag,
        all_labels_flag=all_labels_flag,
        dice_params=dice_params,
    )
    return mri_compute_seg_overlap_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_SEG_OVERLAP_METADATA",
    "MriComputeSegOverlapOutputs",
    "MriComputeSegOverlapParameters",
    "mri_compute_seg_overlap",
    "mri_compute_seg_overlap_params",
]
