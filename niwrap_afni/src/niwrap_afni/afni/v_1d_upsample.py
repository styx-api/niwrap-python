# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_UPSAMPLE_METADATA = Metadata(
    id="3df755faa433b3cc1a6abb13d23619f453b714fd.boutiques",
    name="1dUpsample",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V1dUpsampleParameters = typing.TypedDict('V1dUpsampleParameters', {
    "__STYXTYPE__": typing.Literal["1dUpsample"],
    "upsample_factor": float,
    "input_file": InputPathType,
    "linear_interpolation": bool,
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
        "1dUpsample": v_1d_upsample_cargs,
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
        "1dUpsample": v_1d_upsample_outputs,
    }.get(t)


class V1dUpsampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_upsample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Upsampled 1D time series output"""


def v_1d_upsample_params(
    upsample_factor: float,
    input_file: InputPathType,
    linear_interpolation: bool = False,
) -> V1dUpsampleParameters:
    """
    Build parameters.
    
    Args:
        upsample_factor: Upsample factor (integer from 2..32).
        input_file: Input 1D time series file.
        linear_interpolation: Use 1st order polynomials (i.e., linear\
            interpolation) instead of 7th order polynomials.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dUpsample",
        "upsample_factor": upsample_factor,
        "input_file": input_file,
        "linear_interpolation": linear_interpolation,
    }
    return params


def v_1d_upsample_cargs(
    params: V1dUpsampleParameters,
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
    cargs.append("1dUpsample")
    cargs.append(str(params.get("upsample_factor")))
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("linear_interpolation"):
        cargs.append("-one")
    return cargs


def v_1d_upsample_outputs(
    params: V1dUpsampleParameters,
    execution: Execution,
) -> V1dUpsampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dUpsampleOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("ethel.1D"),
    )
    return ret


def v_1d_upsample_execute(
    params: V1dUpsampleParameters,
    execution: Execution,
) -> V1dUpsampleOutputs:
    """
    Upsamples a 1D time series to a finer time grid.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dUpsampleOutputs`).
    """
    params = execution.params(params)
    cargs = v_1d_upsample_cargs(params, execution)
    ret = v_1d_upsample_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_upsample(
    upsample_factor: float,
    input_file: InputPathType,
    linear_interpolation: bool = False,
    runner: Runner | None = None,
) -> V1dUpsampleOutputs:
    """
    Upsamples a 1D time series to a finer time grid.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        upsample_factor: Upsample factor (integer from 2..32).
        input_file: Input 1D time series file.
        linear_interpolation: Use 1st order polynomials (i.e., linear\
            interpolation) instead of 7th order polynomials.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dUpsampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_UPSAMPLE_METADATA)
    params = v_1d_upsample_params(
        upsample_factor=upsample_factor,
        input_file=input_file,
        linear_interpolation=linear_interpolation,
    )
    return v_1d_upsample_execute(params, execution)


__all__ = [
    "V1dUpsampleOutputs",
    "V1dUpsampleParameters",
    "V_1D_UPSAMPLE_METADATA",
    "v_1d_upsample",
    "v_1d_upsample_params",
]
