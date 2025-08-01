# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_NWARP_ADJUST_METADATA = Metadata(
    id="01d507ebaf57c706c49cc3bf6e04158f3b035085.boutiques",
    name="3dNwarpAdjust",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dNwarpAdjustParameters = typing.TypedDict('V3dNwarpAdjustParameters', {
    "__STYXTYPE__": typing.Literal["3dNwarpAdjust"],
    "input_warps": list[InputPathType],
    "source_datasets": typing.NotRequired[list[InputPathType] | None],
    "output_prefix": typing.NotRequired[str | None],
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
        "3dNwarpAdjust": v_3d_nwarp_adjust_cargs,
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
        "3dNwarpAdjust": v_3d_nwarp_adjust_outputs,
    }.get(t)


class V3dNwarpAdjustOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_nwarp_adjust(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Output mean dataset BRIK file"""
    output_head: OutputPathType | None
    """Output mean dataset HEAD file"""


def v_3d_nwarp_adjust_params(
    input_warps: list[InputPathType],
    source_datasets: list[InputPathType] | None = None,
    output_prefix: str | None = None,
) -> V3dNwarpAdjustParameters:
    """
    Build parameters.
    
    Args:
        input_warps: List of input 3D warp datasets (at least 5).
        source_datasets: List of input 3D datasets to be warped by the adjusted\
            warp datasets. There must be exactly as many of these datasets as there\
            are input warps.
        output_prefix: Prefix for the output mean dataset (only needed if the\
            '-source' option is also given).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNwarpAdjust",
        "input_warps": input_warps,
    }
    if source_datasets is not None:
        params["source_datasets"] = source_datasets
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    return params


def v_3d_nwarp_adjust_cargs(
    params: V3dNwarpAdjustParameters,
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
    cargs.append("3dNwarpAdjust")
    cargs.extend([
        "-nwarp",
        *[execution.input_file(f) for f in params.get("input_warps")]
    ])
    if params.get("source_datasets") is not None:
        cargs.extend([
            "-source",
            *[execution.input_file(f) for f in params.get("source_datasets")]
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    return cargs


def v_3d_nwarp_adjust_outputs(
    params: V3dNwarpAdjustParameters,
    execution: Execution,
) -> V3dNwarpAdjustOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNwarpAdjustOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(params.get("output_prefix") + "+tlrc.BRIK") if (params.get("output_prefix") is not None) else None,
        output_head=execution.output_file(params.get("output_prefix") + "+tlrc.HEAD") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_nwarp_adjust_execute(
    params: V3dNwarpAdjustParameters,
    execution: Execution,
) -> V3dNwarpAdjustOutputs:
    """
    Program to adjust 3D warp datasets by composing them with the inverse of their
    average, optionally warping input datasets and generating an output mean
    dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNwarpAdjustOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_nwarp_adjust_cargs(params, execution)
    ret = v_3d_nwarp_adjust_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_nwarp_adjust(
    input_warps: list[InputPathType],
    source_datasets: list[InputPathType] | None = None,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dNwarpAdjustOutputs:
    """
    Program to adjust 3D warp datasets by composing them with the inverse of their
    average, optionally warping input datasets and generating an output mean
    dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_warps: List of input 3D warp datasets (at least 5).
        source_datasets: List of input 3D datasets to be warped by the adjusted\
            warp datasets. There must be exactly as many of these datasets as there\
            are input warps.
        output_prefix: Prefix for the output mean dataset (only needed if the\
            '-source' option is also given).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNwarpAdjustOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NWARP_ADJUST_METADATA)
    params = v_3d_nwarp_adjust_params(
        input_warps=input_warps,
        source_datasets=source_datasets,
        output_prefix=output_prefix,
    )
    return v_3d_nwarp_adjust_execute(params, execution)


__all__ = [
    "V3dNwarpAdjustOutputs",
    "V3dNwarpAdjustParameters",
    "V_3D_NWARP_ADJUST_METADATA",
    "v_3d_nwarp_adjust",
    "v_3d_nwarp_adjust_params",
]
