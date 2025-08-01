# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SCALE_VOLUME_METADATA = Metadata(
    id="6987f91c483f861633afc3be82cefdcfd48e7a50.boutiques",
    name="@ScaleVolume",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VScaleVolumeParameters = typing.TypedDict('VScaleVolumeParameters', {
    "__STYXTYPE__": typing.Literal["@ScaleVolume"],
    "input_dset": InputPathType,
    "prefix": str,
    "val_clip": typing.NotRequired[list[float] | None],
    "perc_clip": typing.NotRequired[list[float] | None],
    "scale_by_mean": bool,
    "scale_by_median": bool,
    "norm": bool,
    "mask": typing.NotRequired[InputPathType | None],
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
        "@ScaleVolume": v__scale_volume_cargs,
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
        "@ScaleVolume": v__scale_volume_outputs,
    }.get(t)


class VScaleVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__scale_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output scaled dataset"""


def v__scale_volume_params(
    input_dset: InputPathType,
    prefix: str,
    val_clip: list[float] | None = None,
    perc_clip: list[float] | None = None,
    scale_by_mean: bool = False,
    scale_by_median: bool = False,
    norm: bool = False,
    mask: InputPathType | None = None,
) -> VScaleVolumeParameters:
    """
    Build parameters.
    
    Args:
        input_dset: Dataset to scale.
        prefix: Prefix of output.
        val_clip: Min and Max of output dataset. Default V0 = 0 and V1 = 255.
        perc_clip: Set lowest P0 percentile to Min and highest P1 percentile to\
            Max. Default P0 = 2 and P1 = 98.
        scale_by_mean: Divide each sub-brick by mean of non-zero voxels.
        scale_by_median: Divide each sub-brick by median of non-zero voxels.
        norm: For each time series T, Tnorm = (T - mean(T)) / stdev(T).
        mask: Restrict to non-zero values of given mask dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ScaleVolume",
        "input_dset": input_dset,
        "prefix": prefix,
        "scale_by_mean": scale_by_mean,
        "scale_by_median": scale_by_median,
        "norm": norm,
    }
    if val_clip is not None:
        params["val_clip"] = val_clip
    if perc_clip is not None:
        params["perc_clip"] = perc_clip
    if mask is not None:
        params["mask"] = mask
    return params


def v__scale_volume_cargs(
    params: VScaleVolumeParameters,
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
    cargs.append("@ScaleVolume")
    cargs.append(execution.input_file(params.get("input_dset")))
    cargs.append(params.get("prefix"))
    if params.get("val_clip") is not None:
        cargs.extend([
            "-val_clip",
            *map(str, params.get("val_clip"))
        ])
    if params.get("perc_clip") is not None:
        cargs.extend([
            "-perc_clip",
            *map(str, params.get("perc_clip"))
        ])
    if params.get("scale_by_mean"):
        cargs.append("-scale_by_mean")
    if params.get("scale_by_median"):
        cargs.append("-scale_by_median")
    if params.get("norm"):
        cargs.append("-norm")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    return cargs


def v__scale_volume_outputs(
    params: VScaleVolumeParameters,
    execution: Execution,
) -> VScaleVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VScaleVolumeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("<-prefix PREFIX>_scaled"),
    )
    return ret


def v__scale_volume_execute(
    params: VScaleVolumeParameters,
    execution: Execution,
) -> VScaleVolumeOutputs:
    """
    A tool to scale the volume of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VScaleVolumeOutputs`).
    """
    params = execution.params(params)
    cargs = v__scale_volume_cargs(params, execution)
    ret = v__scale_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__scale_volume(
    input_dset: InputPathType,
    prefix: str,
    val_clip: list[float] | None = None,
    perc_clip: list[float] | None = None,
    scale_by_mean: bool = False,
    scale_by_median: bool = False,
    norm: bool = False,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> VScaleVolumeOutputs:
    """
    A tool to scale the volume of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dset: Dataset to scale.
        prefix: Prefix of output.
        val_clip: Min and Max of output dataset. Default V0 = 0 and V1 = 255.
        perc_clip: Set lowest P0 percentile to Min and highest P1 percentile to\
            Max. Default P0 = 2 and P1 = 98.
        scale_by_mean: Divide each sub-brick by mean of non-zero voxels.
        scale_by_median: Divide each sub-brick by median of non-zero voxels.
        norm: For each time series T, Tnorm = (T - mean(T)) / stdev(T).
        mask: Restrict to non-zero values of given mask dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VScaleVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SCALE_VOLUME_METADATA)
    params = v__scale_volume_params(
        input_dset=input_dset,
        prefix=prefix,
        val_clip=val_clip,
        perc_clip=perc_clip,
        scale_by_mean=scale_by_mean,
        scale_by_median=scale_by_median,
        norm=norm,
        mask=mask,
    )
    return v__scale_volume_execute(params, execution)


__all__ = [
    "VScaleVolumeOutputs",
    "VScaleVolumeParameters",
    "V__SCALE_VOLUME_METADATA",
    "v__scale_volume",
    "v__scale_volume_params",
]
