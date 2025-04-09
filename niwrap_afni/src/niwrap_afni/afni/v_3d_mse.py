# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MSE_METADATA = Metadata(
    id="f6ca026af1cb73e73646daceebece681cda8d8dc.boutiques",
    name="3dMSE",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dMseParameters = typing.TypedDict('V3dMseParameters', {
    "__STYX_TYPE__": typing.Literal["3dMSE"],
    "polynomial_order": typing.NotRequired[int | None],
    "autoclip": bool,
    "automask": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "scales": typing.NotRequired[float | None],
    "entwin": typing.NotRequired[float | None],
    "rthresh": typing.NotRequired[float | None],
    "dset": InputPathType,
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
        "3dMSE": v_3d_mse_cargs,
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
        "3dMSE": v_3d_mse_outputs,
    }.get(t)


class V3dMseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mse(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brik: OutputPathType | None
    """Output dataset in BRIK format."""
    out_head: OutputPathType | None
    """Output dataset in HEAD format."""


def v_3d_mse_params(
    dset: InputPathType,
    polynomial_order: int | None = None,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    scales: float | None = None,
    entwin: float | None = None,
    rthresh: float | None = None,
) -> V3dMseParameters:
    """
    Build parameters.
    
    Args:
        dset: Input dataset (e.g., dset.nii.gz).
        polynomial_order: Remove polynomial trend of order 'm' (default is m=1;\
            m=-1 means no detrending).
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Use automask to clip low-intensity regions.
        mask: Mask to define 'in-brain' voxels.
        prefix: Prefix for the output dataset (default is 'MSE').
        scales: The number of scales to be used in the calculation (default is\
            5).
        entwin: The window size used in the calculation (default is 2).
        rthresh: The radius threshold for determining if values are the same in\
            the SampleEn calculation, in fractions of the standard deviation\
            (default is 0.5).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMSE",
        "autoclip": autoclip,
        "automask": automask,
        "dset": dset,
    }
    if polynomial_order is not None:
        params["polynomial_order"] = polynomial_order
    if mask is not None:
        params["mask"] = mask
    if prefix is not None:
        params["prefix"] = prefix
    if scales is not None:
        params["scales"] = scales
    if entwin is not None:
        params["entwin"] = entwin
    if rthresh is not None:
        params["rthresh"] = rthresh
    return params


def v_3d_mse_cargs(
    params: V3dMseParameters,
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
    cargs.append("3dMSE")
    if params.get("polynomial_order") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polynomial_order"))
        ])
    if params.get("autoclip"):
        cargs.append("-autoclip")
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("scales") is not None:
        cargs.extend([
            "-scales",
            str(params.get("scales"))
        ])
    if params.get("entwin") is not None:
        cargs.extend([
            "-entwin",
            str(params.get("entwin"))
        ])
    if params.get("rthresh") is not None:
        cargs.extend([
            "-rthresh",
            str(params.get("rthresh"))
        ])
    cargs.append(execution.input_file(params.get("dset")))
    return cargs


def v_3d_mse_outputs(
    params: V3dMseParameters,
    execution: Execution,
) -> V3dMseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMseOutputs(
        root=execution.output_file("."),
        out_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
        out_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_mse_execute(
    params: V3dMseParameters,
    execution: Execution,
) -> V3dMseOutputs:
    """
    Computes voxelwise multi-scale entropy.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMseOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_mse_cargs(params, execution)
    ret = v_3d_mse_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mse(
    dset: InputPathType,
    polynomial_order: int | None = None,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    scales: float | None = None,
    entwin: float | None = None,
    rthresh: float | None = None,
    runner: Runner | None = None,
) -> V3dMseOutputs:
    """
    Computes voxelwise multi-scale entropy.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input dataset (e.g., dset.nii.gz).
        polynomial_order: Remove polynomial trend of order 'm' (default is m=1;\
            m=-1 means no detrending).
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Use automask to clip low-intensity regions.
        mask: Mask to define 'in-brain' voxels.
        prefix: Prefix for the output dataset (default is 'MSE').
        scales: The number of scales to be used in the calculation (default is\
            5).
        entwin: The window size used in the calculation (default is 2).
        rthresh: The radius threshold for determining if values are the same in\
            the SampleEn calculation, in fractions of the standard deviation\
            (default is 0.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MSE_METADATA)
    params = v_3d_mse_params(
        polynomial_order=polynomial_order,
        autoclip=autoclip,
        automask=automask,
        mask=mask,
        prefix=prefix,
        scales=scales,
        entwin=entwin,
        rthresh=rthresh,
        dset=dset,
    )
    return v_3d_mse_execute(params, execution)


__all__ = [
    "V3dMseOutputs",
    "V3dMseParameters",
    "V_3D_MSE_METADATA",
    "v_3d_mse",
    "v_3d_mse_params",
]
