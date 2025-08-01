# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GET_AFNI_MODEL_PRF_6_METADATA = Metadata(
    id="a1644a25504c74d6961d86251212dfc9c7f6fb99.boutiques",
    name="get_afni_model_PRF_6",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


GetAfniModelPrf6Parameters = typing.TypedDict('GetAfniModelPrf6Parameters', {
    "__STYXTYPE__": typing.Literal["get_afni_model_PRF_6"],
    "NT": float,
    "AMP": float,
    "X": float,
    "Y": float,
    "SIGMA": float,
    "SIGRAT": float,
    "THETA": float,
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
        "get_afni_model_PRF_6": get_afni_model_prf_6_cargs,
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


class GetAfniModelPrf6Outputs(typing.NamedTuple):
    """
    Output object returned when calling `get_afni_model_prf_6(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def get_afni_model_prf_6_params(
    nt_: float,
    amp: float,
    x: float,
    y: float,
    sigma: float,
    sigrat: float,
    theta: float,
) -> GetAfniModelPrf6Parameters:
    """
    Build parameters.
    
    Args:
        nt_: Number of time points of the stimulus dataset.
        amp: Amplitude of the pRF model.
        x: X coordinate of the pRF center.
        y: Y coordinate of the pRF center.
        sigma: Standard deviation of the Gaussian pRF.
        sigrat: Ratio of standard deviations (sigma_x/sigma_y) of the Gaussian\
            pRF.
        theta: Rotation angle theta of the Gaussian pRF.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "get_afni_model_PRF_6",
        "NT": nt_,
        "AMP": amp,
        "X": x,
        "Y": y,
        "SIGMA": sigma,
        "SIGRAT": sigrat,
        "THETA": theta,
    }
    return params


def get_afni_model_prf_6_cargs(
    params: GetAfniModelPrf6Parameters,
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
    cargs.append("get_afni_model_PRF_6")
    cargs.append(str(params.get("NT")))
    cargs.append(str(params.get("AMP")))
    cargs.append(str(params.get("X")))
    cargs.append(str(params.get("Y")))
    cargs.append(str(params.get("SIGMA")))
    cargs.append(str(params.get("SIGRAT")))
    cargs.append(str(params.get("THETA")))
    return cargs


def get_afni_model_prf_6_outputs(
    params: GetAfniModelPrf6Parameters,
    execution: Execution,
) -> GetAfniModelPrf6Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GetAfniModelPrf6Outputs(
        root=execution.output_file("."),
    )
    return ret


def get_afni_model_prf_6_execute(
    params: GetAfniModelPrf6Parameters,
    execution: Execution,
) -> GetAfniModelPrf6Outputs:
    """
    A command to invoke AFNI's population receptive field (pRF) model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrf6Outputs`).
    """
    params = execution.params(params)
    cargs = get_afni_model_prf_6_cargs(params, execution)
    ret = get_afni_model_prf_6_outputs(params, execution)
    execution.run(cargs)
    return ret


def get_afni_model_prf_6(
    nt_: float,
    amp: float,
    x: float,
    y: float,
    sigma: float,
    sigrat: float,
    theta: float,
    runner: Runner | None = None,
) -> GetAfniModelPrf6Outputs:
    """
    A command to invoke AFNI's population receptive field (pRF) model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        nt_: Number of time points of the stimulus dataset.
        amp: Amplitude of the pRF model.
        x: X coordinate of the pRF center.
        y: Y coordinate of the pRF center.
        sigma: Standard deviation of the Gaussian pRF.
        sigrat: Ratio of standard deviations (sigma_x/sigma_y) of the Gaussian\
            pRF.
        theta: Rotation angle theta of the Gaussian pRF.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrf6Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_AFNI_MODEL_PRF_6_METADATA)
    params = get_afni_model_prf_6_params(
        nt_=nt_,
        amp=amp,
        x=x,
        y=y,
        sigma=sigma,
        sigrat=sigrat,
        theta=theta,
    )
    return get_afni_model_prf_6_execute(params, execution)


__all__ = [
    "GET_AFNI_MODEL_PRF_6_METADATA",
    "GetAfniModelPrf6Outputs",
    "GetAfniModelPrf6Parameters",
    "get_afni_model_prf_6",
    "get_afni_model_prf_6_params",
]
