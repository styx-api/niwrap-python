# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GET_AFNI_MODEL_PRF_6_BAD_METADATA = Metadata(
    id="f7614b8ced72773ab9bfd46ff569ff9a092b84e3.boutiques",
    name="get_afni_model_PRF_6_BAD",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


GetAfniModelPrf6BadParameters = typing.TypedDict('GetAfniModelPrf6BadParameters', {
    "__STYXTYPE__": typing.Literal["get_afni_model_PRF_6_BAD"],
    "amplitude": float,
    "x_coord": float,
    "y_coord": float,
    "sigma": float,
    "sigrat": float,
    "theta": float,
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
        "get_afni_model_PRF_6_BAD": get_afni_model_prf_6_bad_cargs,
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


class GetAfniModelPrf6BadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_afni_model_prf_6_bad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def get_afni_model_prf_6_bad_params(
    amplitude: float,
    x_coord: float,
    y_coord: float,
    sigma: float,
    sigrat: float,
    theta: float,
) -> GetAfniModelPrf6BadParameters:
    """
    Build parameters.
    
    Args:
        amplitude: Amplitude parameter A.
        x_coord: X coordinate parameter x.
        y_coord: Y coordinate parameter y.
        sigma: Sigma parameter sigma.
        sigrat: Sigma ratio parameter sigrat.
        theta: Theta parameter theta (in radians).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "get_afni_model_PRF_6_BAD",
        "amplitude": amplitude,
        "x_coord": x_coord,
        "y_coord": y_coord,
        "sigma": sigma,
        "sigrat": sigrat,
        "theta": theta,
    }
    return params


def get_afni_model_prf_6_bad_cargs(
    params: GetAfniModelPrf6BadParameters,
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
    cargs.append("get_afni_model_PRF_6_BAD")
    cargs.append(str(params.get("amplitude")))
    cargs.append(str(params.get("x_coord")))
    cargs.append(str(params.get("y_coord")))
    cargs.append(str(params.get("sigma")))
    cargs.append(str(params.get("sigrat")))
    cargs.append(str(params.get("theta")))
    return cargs


def get_afni_model_prf_6_bad_outputs(
    params: GetAfniModelPrf6BadParameters,
    execution: Execution,
) -> GetAfniModelPrf6BadOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GetAfniModelPrf6BadOutputs(
        root=execution.output_file("."),
    )
    return ret


def get_afni_model_prf_6_bad_execute(
    params: GetAfniModelPrf6BadParameters,
    execution: Execution,
) -> GetAfniModelPrf6BadOutputs:
    """
    Command line tool for obtaining AFNI pRF model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrf6BadOutputs`).
    """
    params = execution.params(params)
    cargs = get_afni_model_prf_6_bad_cargs(params, execution)
    ret = get_afni_model_prf_6_bad_outputs(params, execution)
    execution.run(cargs)
    return ret


def get_afni_model_prf_6_bad(
    amplitude: float,
    x_coord: float,
    y_coord: float,
    sigma: float,
    sigrat: float,
    theta: float,
    runner: Runner | None = None,
) -> GetAfniModelPrf6BadOutputs:
    """
    Command line tool for obtaining AFNI pRF model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        amplitude: Amplitude parameter A.
        x_coord: X coordinate parameter x.
        y_coord: Y coordinate parameter y.
        sigma: Sigma parameter sigma.
        sigrat: Sigma ratio parameter sigrat.
        theta: Theta parameter theta (in radians).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrf6BadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_AFNI_MODEL_PRF_6_BAD_METADATA)
    params = get_afni_model_prf_6_bad_params(
        amplitude=amplitude,
        x_coord=x_coord,
        y_coord=y_coord,
        sigma=sigma,
        sigrat=sigrat,
        theta=theta,
    )
    return get_afni_model_prf_6_bad_execute(params, execution)


__all__ = [
    "GET_AFNI_MODEL_PRF_6_BAD_METADATA",
    "GetAfniModelPrf6BadOutputs",
    "GetAfniModelPrf6BadParameters",
    "get_afni_model_prf_6_bad",
    "get_afni_model_prf_6_bad_params",
]
