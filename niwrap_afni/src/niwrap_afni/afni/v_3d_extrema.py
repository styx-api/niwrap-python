# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_EXTREMA_METADATA = Metadata(
    id="a99e42a29322557d96803717af2d04aa40a35929.boutiques",
    name="3dExtrema",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dExtremaParameters = typing.TypedDict('V3dExtremaParameters', {
    "__STYXTYPE__": typing.Literal["3dExtrema"],
    "input_dataset": InputPathType,
    "output_prefix": typing.NotRequired[str | None],
    "output_session": typing.NotRequired[str | None],
    "quiet": bool,
    "mask_file": typing.NotRequired[InputPathType | None],
    "mask_threshold": typing.NotRequired[float | None],
    "data_threshold": typing.NotRequired[float | None],
    "n_best": typing.NotRequired[float | None],
    "separation_distance": typing.NotRequired[float | None],
    "minima": bool,
    "maxima": bool,
    "strict": bool,
    "partial": bool,
    "interior": bool,
    "closure": bool,
    "slice": bool,
    "volume": bool,
    "remove": bool,
    "average": bool,
    "weight": bool,
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
        "3dExtrema": v_3d_extrema_cargs,
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
        "3dExtrema": v_3d_extrema_outputs,
    }.get(t)


class V3dExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head_file: OutputPathType | None
    """Output HEAD file"""
    output_brik_file: OutputPathType | None
    """Output BRIK file"""


def v_3d_extrema_params(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    output_session: str | None = None,
    quiet: bool = False,
    mask_file: InputPathType | None = None,
    mask_threshold: float | None = None,
    data_threshold: float | None = None,
    n_best: float | None = None,
    separation_distance: float | None = None,
    minima: bool = False,
    maxima: bool = False,
    strict: bool = False,
    partial: bool = False,
    interior: bool = False,
    closure: bool = False,
    slice_: bool = False,
    volume: bool = False,
    remove: bool = False,
    average: bool = False,
    weight: bool = False,
) -> V3dExtremaParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g. dataset+tlrc'[sub-brick]').
        output_prefix: Prefix for the output dataset name.
        output_session: Directory for the output dataset session.
        quiet: Suppress screen output.
        mask_file: Mask statistic from file.
        mask_threshold: Only voxels whose mask statistic is >= m in absolute\
            value will be considered.
        data_threshold: Only voxels whose value (intensity) is greater than d\
            in absolute value will be considered.
        n_best: Only print the first N extrema.
        separation_distance: Minimum separation distance (in mm) for distinct\
            extrema.
        minima: Find local minima.
        maxima: Find local maxima (default).
        strict: Use strict inequality for extrema (default).
        partial: Use partial inequality for extrema.
        interior: Extrema must be interior points (default).
        closure: Extrema may be boundary points.
        slice_: Consider each slice separately (default).
        volume: Consider the volume as a whole.
        remove: Remove all but strongest of neighboring extrema (default).
        average: Replace neighboring extrema by average.
        weight: Replace neighboring extrema by weighted average.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dExtrema",
        "input_dataset": input_dataset,
        "quiet": quiet,
        "minima": minima,
        "maxima": maxima,
        "strict": strict,
        "partial": partial,
        "interior": interior,
        "closure": closure,
        "slice": slice_,
        "volume": volume,
        "remove": remove,
        "average": average,
        "weight": weight,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if output_session is not None:
        params["output_session"] = output_session
    if mask_file is not None:
        params["mask_file"] = mask_file
    if mask_threshold is not None:
        params["mask_threshold"] = mask_threshold
    if data_threshold is not None:
        params["data_threshold"] = data_threshold
    if n_best is not None:
        params["n_best"] = n_best
    if separation_distance is not None:
        params["separation_distance"] = separation_distance
    return params


def v_3d_extrema_cargs(
    params: V3dExtremaParameters,
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
    cargs.append("3dExtrema")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("output_session") is not None:
        cargs.extend([
            "-session",
            params.get("output_session")
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("mask_file") is not None:
        cargs.extend([
            "-mask_file",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("mask_threshold") is not None:
        cargs.extend([
            "-mask_thr",
            str(params.get("mask_threshold"))
        ])
    if params.get("data_threshold") is not None:
        cargs.extend([
            "-data_thr",
            str(params.get("data_threshold"))
        ])
    if params.get("n_best") is not None:
        cargs.extend([
            "-nbest",
            str(params.get("n_best"))
        ])
    if params.get("separation_distance") is not None:
        cargs.extend([
            "-sep_dist",
            str(params.get("separation_distance"))
        ])
    if params.get("minima"):
        cargs.append("-minima")
    if params.get("maxima"):
        cargs.append("-maxima")
    if params.get("strict"):
        cargs.append("-strict")
    if params.get("partial"):
        cargs.append("-partial")
    if params.get("interior"):
        cargs.append("-interior")
    if params.get("closure"):
        cargs.append("-closure")
    if params.get("slice"):
        cargs.append("-slice")
    if params.get("volume"):
        cargs.append("-volume")
    if params.get("remove"):
        cargs.append("-remove")
    if params.get("average"):
        cargs.append("-average")
    if params.get("weight"):
        cargs.append("-weight")
    return cargs


def v_3d_extrema_outputs(
    params: V3dExtremaParameters,
    execution: Execution,
) -> V3dExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dExtremaOutputs(
        root=execution.output_file("."),
        output_head_file=execution.output_file(params.get("output_prefix") + ".HEAD") if (params.get("output_prefix") is not None) else None,
        output_brik_file=execution.output_file(params.get("output_prefix") + ".BRIK") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_extrema_execute(
    params: V3dExtremaParameters,
    execution: Execution,
) -> V3dExtremaOutputs:
    """
    Find local extrema (minima or maxima) in 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dExtremaOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_extrema_cargs(params, execution)
    ret = v_3d_extrema_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_extrema(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    output_session: str | None = None,
    quiet: bool = False,
    mask_file: InputPathType | None = None,
    mask_threshold: float | None = None,
    data_threshold: float | None = None,
    n_best: float | None = None,
    separation_distance: float | None = None,
    minima: bool = False,
    maxima: bool = False,
    strict: bool = False,
    partial: bool = False,
    interior: bool = False,
    closure: bool = False,
    slice_: bool = False,
    volume: bool = False,
    remove: bool = False,
    average: bool = False,
    weight: bool = False,
    runner: Runner | None = None,
) -> V3dExtremaOutputs:
    """
    Find local extrema (minima or maxima) in 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g. dataset+tlrc'[sub-brick]').
        output_prefix: Prefix for the output dataset name.
        output_session: Directory for the output dataset session.
        quiet: Suppress screen output.
        mask_file: Mask statistic from file.
        mask_threshold: Only voxels whose mask statistic is >= m in absolute\
            value will be considered.
        data_threshold: Only voxels whose value (intensity) is greater than d\
            in absolute value will be considered.
        n_best: Only print the first N extrema.
        separation_distance: Minimum separation distance (in mm) for distinct\
            extrema.
        minima: Find local minima.
        maxima: Find local maxima (default).
        strict: Use strict inequality for extrema (default).
        partial: Use partial inequality for extrema.
        interior: Extrema must be interior points (default).
        closure: Extrema may be boundary points.
        slice_: Consider each slice separately (default).
        volume: Consider the volume as a whole.
        remove: Remove all but strongest of neighboring extrema (default).
        average: Replace neighboring extrema by average.
        weight: Replace neighboring extrema by weighted average.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EXTREMA_METADATA)
    params = v_3d_extrema_params(
        input_dataset=input_dataset,
        output_prefix=output_prefix,
        output_session=output_session,
        quiet=quiet,
        mask_file=mask_file,
        mask_threshold=mask_threshold,
        data_threshold=data_threshold,
        n_best=n_best,
        separation_distance=separation_distance,
        minima=minima,
        maxima=maxima,
        strict=strict,
        partial=partial,
        interior=interior,
        closure=closure,
        slice_=slice_,
        volume=volume,
        remove=remove,
        average=average,
        weight=weight,
    )
    return v_3d_extrema_execute(params, execution)


__all__ = [
    "V3dExtremaOutputs",
    "V3dExtremaParameters",
    "V_3D_EXTREMA_METADATA",
    "v_3d_extrema",
    "v_3d_extrema_params",
]
