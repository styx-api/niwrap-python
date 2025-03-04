# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TNORM_METADATA = Metadata(
    id="2f017fb0846acaa4d9cf83666f160e4cc99d7998.boutiques",
    name="3dTnorm",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dTnormParameters = typing.TypedDict('V3dTnormParameters', {
    "__STYX_TYPE__": typing.Literal["3dTnorm"],
    "prefix": typing.NotRequired[str | None],
    "norm2": bool,
    "normR": bool,
    "norm1": bool,
    "normx": bool,
    "polort": typing.NotRequired[float | None],
    "L1fit": bool,
    "input_dataset": InputPathType,
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
        "3dTnorm": v_3d_tnorm_cargs,
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
        "3dTnorm": v_3d_tnorm_outputs,
    }.get(t)


class V3dTnormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tnorm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Normalized output dataset"""


def v_3d_tnorm_params(
    input_dataset: InputPathType,
    prefix: str | None = None,
    norm2: bool = False,
    norm_r: bool = False,
    norm1: bool = False,
    normx: bool = False,
    polort: float | None = None,
    l1fit: bool = False,
) -> V3dTnormParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g. data.nii).
        prefix: Prefix for the output dataset.
        norm2: L2 normalize (sum of squares = 1).
        norm_r: Normalize so sum of squares = number of time points.
        norm1: L1 normalize (sum of absolute values = 1).
        normx: Scale so max absolute value = 1 (L_infinity norm).
        polort: Detrend with polynomials of order p before normalizing.
        l1fit: Detrend with L1 regression (L2 is default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTnorm",
        "norm2": norm2,
        "normR": norm_r,
        "norm1": norm1,
        "normx": normx,
        "L1fit": l1fit,
        "input_dataset": input_dataset,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if polort is not None:
        params["polort"] = polort
    return params


def v_3d_tnorm_cargs(
    params: V3dTnormParameters,
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
    cargs.append("3dTnorm")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("norm2"):
        cargs.append("-norm2")
    if params.get("normR"):
        cargs.append("-normR")
    if params.get("norm1"):
        cargs.append("-norm1")
    if params.get("normx"):
        cargs.append("-normx")
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("L1fit"):
        cargs.append("-L1fit")
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v_3d_tnorm_outputs(
    params: V3dTnormParameters,
    execution: Execution,
) -> V3dTnormOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTnormOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + ".nii") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_tnorm_execute(
    params: V3dTnormParameters,
    execution: Execution,
) -> V3dTnormOutputs:
    """
    Normalizes each voxel time series by multiplicative scaling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTnormOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tnorm_cargs(params, execution)
    ret = v_3d_tnorm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tnorm(
    input_dataset: InputPathType,
    prefix: str | None = None,
    norm2: bool = False,
    norm_r: bool = False,
    norm1: bool = False,
    normx: bool = False,
    polort: float | None = None,
    l1fit: bool = False,
    runner: Runner | None = None,
) -> V3dTnormOutputs:
    """
    Normalizes each voxel time series by multiplicative scaling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g. data.nii).
        prefix: Prefix for the output dataset.
        norm2: L2 normalize (sum of squares = 1).
        norm_r: Normalize so sum of squares = number of time points.
        norm1: L1 normalize (sum of absolute values = 1).
        normx: Scale so max absolute value = 1 (L_infinity norm).
        polort: Detrend with polynomials of order p before normalizing.
        l1fit: Detrend with L1 regression (L2 is default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTnormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TNORM_METADATA)
    params = v_3d_tnorm_params(
        prefix=prefix,
        norm2=norm2,
        norm_r=norm_r,
        norm1=norm1,
        normx=normx,
        polort=polort,
        l1fit=l1fit,
        input_dataset=input_dataset,
    )
    return v_3d_tnorm_execute(params, execution)


__all__ = [
    "V3dTnormOutputs",
    "V3dTnormParameters",
    "V_3D_TNORM_METADATA",
    "v_3d_tnorm",
    "v_3d_tnorm_params",
]
