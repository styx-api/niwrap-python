# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TTO1_D_METADATA = Metadata(
    id="ce8e76b7df50a297f638920b54ead13d47c43d94.boutiques",
    name="3dTto1D",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dTto1DParameters = typing.TypedDict('V3dTto1DParameters', {
    "__STYXTYPE__": typing.Literal["3dTto1D"],
    "input_dataset": InputPathType,
    "method": str,
    "automask": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "verbose": typing.NotRequired[float | None],
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
        "3dTto1D": v_3d_tto1_d_cargs,
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
        "3dTto1D": v_3d_tto1_d_outputs,
    }.get(t)


class V3dTto1DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tto1_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output 1D time series file"""


def v_3d_tto1_d_params(
    input_dataset: InputPathType,
    method: str,
    automask: bool = False,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    verbose: float | None = None,
) -> V3dTto1DParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Specify input dataset. This should be a set of 3D time\
            series. If the input is in 1D format, a transpose operator will\
            typically be required.
        method: Specify 4D to 1D conversion method. Methods include: enorm,\
            dvars, srms, shift_srms, mdiff, smdiff, 4095_count, 4095_frac,\
            4095_warn.
        automask: Restrict computation to automask.
        mask: Restrict computation to given mask.
        prefix: Specify output file. Default is stdout.
        verbose: Specify verbose level. Default is 1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTto1D",
        "input_dataset": input_dataset,
        "method": method,
        "automask": automask,
    }
    if mask is not None:
        params["mask"] = mask
    if prefix is not None:
        params["prefix"] = prefix
    if verbose is not None:
        params["verbose"] = verbose
    return params


def v_3d_tto1_d_cargs(
    params: V3dTto1DParameters,
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
    cargs.append("3dTto1D")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    cargs.extend([
        "-method",
        params.get("method")
    ])
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
    if params.get("verbose") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbose"))
        ])
    return cargs


def v_3d_tto1_d_outputs(
    params: V3dTto1DParameters,
    execution: Execution,
) -> V3dTto1DOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTto1DOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_tto1_d_execute(
    params: V3dTto1DParameters,
    execution: Execution,
) -> V3dTto1DOutputs:
    """
    Collapse a 4D time series to a 1D time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTto1DOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tto1_d_cargs(params, execution)
    ret = v_3d_tto1_d_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tto1_d(
    input_dataset: InputPathType,
    method: str,
    automask: bool = False,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    verbose: float | None = None,
    runner: Runner | None = None,
) -> V3dTto1DOutputs:
    """
    Collapse a 4D time series to a 1D time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Specify input dataset. This should be a set of 3D time\
            series. If the input is in 1D format, a transpose operator will\
            typically be required.
        method: Specify 4D to 1D conversion method. Methods include: enorm,\
            dvars, srms, shift_srms, mdiff, smdiff, 4095_count, 4095_frac,\
            4095_warn.
        automask: Restrict computation to automask.
        mask: Restrict computation to given mask.
        prefix: Specify output file. Default is stdout.
        verbose: Specify verbose level. Default is 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTto1DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TTO1_D_METADATA)
    params = v_3d_tto1_d_params(
        input_dataset=input_dataset,
        method=method,
        automask=automask,
        mask=mask,
        prefix=prefix,
        verbose=verbose,
    )
    return v_3d_tto1_d_execute(params, execution)


__all__ = [
    "V3dTto1DOutputs",
    "V3dTto1DParameters",
    "V_3D_TTO1_D_METADATA",
    "v_3d_tto1_d",
    "v_3d_tto1_d_params",
]
