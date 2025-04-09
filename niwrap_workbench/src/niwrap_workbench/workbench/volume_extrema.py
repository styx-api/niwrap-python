# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_EXTREMA_METADATA = Metadata(
    id="344573d42a8895adab1d4ca83bcab182139d58f8.boutiques",
    name="volume-extrema",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


VolumeExtremaPresmoothParameters = typing.TypedDict('VolumeExtremaPresmoothParameters', {
    "__STYX_TYPE__": typing.Literal["presmooth"],
    "kernel": float,
    "opt_fwhm": bool,
})


VolumeExtremaThresholdParameters = typing.TypedDict('VolumeExtremaThresholdParameters', {
    "__STYX_TYPE__": typing.Literal["threshold"],
    "low": float,
    "high": float,
})


VolumeExtremaParameters = typing.TypedDict('VolumeExtremaParameters', {
    "__STYX_TYPE__": typing.Literal["volume-extrema"],
    "volume_in": InputPathType,
    "distance": float,
    "volume_out": str,
    "presmooth": typing.NotRequired[VolumeExtremaPresmoothParameters | None],
    "opt_roi_roi_volume": typing.NotRequired[InputPathType | None],
    "threshold": typing.NotRequired[VolumeExtremaThresholdParameters | None],
    "opt_sum_subvols": bool,
    "opt_consolidate_mode": bool,
    "opt_only_maxima": bool,
    "opt_only_minima": bool,
    "opt_subvolume_subvolume": typing.NotRequired[str | None],
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
        "volume-extrema": volume_extrema_cargs,
        "presmooth": volume_extrema_presmooth_cargs,
        "threshold": volume_extrema_threshold_cargs,
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
        "volume-extrema": volume_extrema_outputs,
    }.get(t)


def volume_extrema_presmooth_params(
    kernel: float,
    opt_fwhm: bool = False,
) -> VolumeExtremaPresmoothParameters:
    """
    Build parameters.
    
    Args:
        kernel: the size of the gaussian smoothing kernel in mm, as sigma by\
            default.
        opt_fwhm: kernel size is FWHM, not sigma.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "presmooth",
        "kernel": kernel,
        "opt_fwhm": opt_fwhm,
    }
    return params


def volume_extrema_presmooth_cargs(
    params: VolumeExtremaPresmoothParameters,
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
    cargs.append("-presmooth")
    cargs.append(str(params.get("kernel")))
    if params.get("opt_fwhm"):
        cargs.append("-fwhm")
    return cargs


def volume_extrema_threshold_params(
    low: float,
    high: float,
) -> VolumeExtremaThresholdParameters:
    """
    Build parameters.
    
    Args:
        low: the largest value to consider for being a minimum.
        high: the smallest value to consider for being a maximum.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "threshold",
        "low": low,
        "high": high,
    }
    return params


def volume_extrema_threshold_cargs(
    params: VolumeExtremaThresholdParameters,
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
    cargs.append("-threshold")
    cargs.append(str(params.get("low")))
    cargs.append(str(params.get("high")))
    return cargs


class VolumeExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output extrema volume"""


def volume_extrema_params(
    volume_in: InputPathType,
    distance: float,
    volume_out: str,
    presmooth: VolumeExtremaPresmoothParameters | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    threshold: VolumeExtremaThresholdParameters | None = None,
    opt_sum_subvols: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    opt_subvolume_subvolume: str | None = None,
) -> VolumeExtremaParameters:
    """
    Build parameters.
    
    Args:
        volume_in: volume file to find the extrema of.
        distance: the minimum distance between identified extrema of the same\
            type.
        volume_out: the output extrema volume.
        presmooth: smooth the volume before finding extrema.
        opt_roi_roi_volume: ignore values outside the selected area: the area\
            to find extrema in.
        threshold: ignore small extrema.
        opt_sum_subvols: output the sum of the extrema subvolumes instead of\
            each subvolume separately.
        opt_consolidate_mode: use consolidation of local minima instead of a\
            large neighborhood.
        opt_only_maxima: only find the maxima.
        opt_only_minima: only find the minima.
        opt_subvolume_subvolume: select a single subvolume to find extrema in:\
            the subvolume number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-extrema",
        "volume_in": volume_in,
        "distance": distance,
        "volume_out": volume_out,
        "opt_sum_subvols": opt_sum_subvols,
        "opt_consolidate_mode": opt_consolidate_mode,
        "opt_only_maxima": opt_only_maxima,
        "opt_only_minima": opt_only_minima,
    }
    if presmooth is not None:
        params["presmooth"] = presmooth
    if opt_roi_roi_volume is not None:
        params["opt_roi_roi_volume"] = opt_roi_roi_volume
    if threshold is not None:
        params["threshold"] = threshold
    if opt_subvolume_subvolume is not None:
        params["opt_subvolume_subvolume"] = opt_subvolume_subvolume
    return params


def volume_extrema_cargs(
    params: VolumeExtremaParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-extrema")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(str(params.get("distance")))
    cargs.append(params.get("volume_out"))
    if params.get("presmooth") is not None:
        cargs.extend(dyn_cargs(params.get("presmooth")["__STYXTYPE__"])(params.get("presmooth"), execution))
    if params.get("opt_roi_roi_volume") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_volume"))
        ])
    if params.get("threshold") is not None:
        cargs.extend(dyn_cargs(params.get("threshold")["__STYXTYPE__"])(params.get("threshold"), execution))
    if params.get("opt_sum_subvols"):
        cargs.append("-sum-subvols")
    if params.get("opt_consolidate_mode"):
        cargs.append("-consolidate-mode")
    if params.get("opt_only_maxima"):
        cargs.append("-only-maxima")
    if params.get("opt_only_minima"):
        cargs.append("-only-minima")
    if params.get("opt_subvolume_subvolume") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvolume")
        ])
    return cargs


def volume_extrema_outputs(
    params: VolumeExtremaParameters,
    execution: Execution,
) -> VolumeExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeExtremaOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_extrema_execute(
    params: VolumeExtremaParameters,
    execution: Execution,
) -> VolumeExtremaOutputs:
    """
    Find extrema in a volume file.
    
    Finds extrema in a volume file, such that no two extrema of the same type
    are within <distance> of each other. The extrema are labeled as -1 for
    minima, 1 for maxima, 0 otherwise. If -only-maxima or -only-minima is
    specified, then it will ignore extrema not of the specified type. These
    options are mutually exclusive.
    
    If -sum-subvols is specified, these extrema subvolumes are summed, and the
    output has a single subvolume with this result.
    
    By default, a datapoint is an extrema only if it is more extreme than every
    other datapoint that is within <distance> from it. If -consolidate-mode is
    used, it instead starts by finding all datapoints that are more extreme than
    their immediate neighbors, then while there are any extrema within
    <distance> of each other, take the two extrema closest to each other and
    merge them into one by a weighted average based on how many original extrema
    have been merged into each.
    
    By default, all input subvolumes are used with no smoothing, use -subvolume
    to specify a single subvolume to use, and -presmooth to smooth the input
    before finding the extrema.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeExtremaOutputs`).
    """
    params = execution.params(params)
    cargs = volume_extrema_cargs(params, execution)
    ret = volume_extrema_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_extrema(
    volume_in: InputPathType,
    distance: float,
    volume_out: str,
    presmooth: VolumeExtremaPresmoothParameters | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    threshold: VolumeExtremaThresholdParameters | None = None,
    opt_sum_subvols: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    opt_subvolume_subvolume: str | None = None,
    runner: Runner | None = None,
) -> VolumeExtremaOutputs:
    """
    Find extrema in a volume file.
    
    Finds extrema in a volume file, such that no two extrema of the same type
    are within <distance> of each other. The extrema are labeled as -1 for
    minima, 1 for maxima, 0 otherwise. If -only-maxima or -only-minima is
    specified, then it will ignore extrema not of the specified type. These
    options are mutually exclusive.
    
    If -sum-subvols is specified, these extrema subvolumes are summed, and the
    output has a single subvolume with this result.
    
    By default, a datapoint is an extrema only if it is more extreme than every
    other datapoint that is within <distance> from it. If -consolidate-mode is
    used, it instead starts by finding all datapoints that are more extreme than
    their immediate neighbors, then while there are any extrema within
    <distance> of each other, take the two extrema closest to each other and
    merge them into one by a weighted average based on how many original extrema
    have been merged into each.
    
    By default, all input subvolumes are used with no smoothing, use -subvolume
    to specify a single subvolume to use, and -presmooth to smooth the input
    before finding the extrema.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: volume file to find the extrema of.
        distance: the minimum distance between identified extrema of the same\
            type.
        volume_out: the output extrema volume.
        presmooth: smooth the volume before finding extrema.
        opt_roi_roi_volume: ignore values outside the selected area: the area\
            to find extrema in.
        threshold: ignore small extrema.
        opt_sum_subvols: output the sum of the extrema subvolumes instead of\
            each subvolume separately.
        opt_consolidate_mode: use consolidation of local minima instead of a\
            large neighborhood.
        opt_only_maxima: only find the maxima.
        opt_only_minima: only find the minima.
        opt_subvolume_subvolume: select a single subvolume to find extrema in:\
            the subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_EXTREMA_METADATA)
    params = volume_extrema_params(
        volume_in=volume_in,
        distance=distance,
        volume_out=volume_out,
        presmooth=presmooth,
        opt_roi_roi_volume=opt_roi_roi_volume,
        threshold=threshold,
        opt_sum_subvols=opt_sum_subvols,
        opt_consolidate_mode=opt_consolidate_mode,
        opt_only_maxima=opt_only_maxima,
        opt_only_minima=opt_only_minima,
        opt_subvolume_subvolume=opt_subvolume_subvolume,
    )
    return volume_extrema_execute(params, execution)


__all__ = [
    "VOLUME_EXTREMA_METADATA",
    "VolumeExtremaOutputs",
    "VolumeExtremaParameters",
    "VolumeExtremaPresmoothParameters",
    "VolumeExtremaThresholdParameters",
    "volume_extrema",
    "volume_extrema_params",
    "volume_extrema_presmooth_params",
    "volume_extrema_threshold_params",
]
