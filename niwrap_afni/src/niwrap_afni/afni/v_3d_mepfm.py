# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MEPFM_METADATA = Metadata(
    id="44860000dde3dcae9381914d7a939fdce74cff79.boutiques",
    name="3dMEPFM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dMepfmParameters = typing.TypedDict('V3dMepfmParameters', {
    "__STYX_TYPE__": typing.Literal["3dMEPFM"],
    "input_files": list[str],
    "dbgArgs": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "hrf_model": typing.NotRequired[str | None],
    "verbosity": typing.NotRequired[int | None],
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
        "3dMEPFM": v_3d_mepfm_cargs,
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
        "3dMEPFM": v_3d_mepfm_outputs,
    }.get(t)


class V3dMepfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mepfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dr2_output: OutputPathType
    """Changes in R2* parameter, assumed to represent neuronal-related signal
    changes"""
    dr2fit_output: OutputPathType
    """Convolution of DR2 with HRF, one volume per echo"""
    ds0_output: OutputPathType
    """Changes in net magnetization (S0) (if estimated)"""
    lambda_output: OutputPathType
    """Regularization parameter"""
    sigmas_mad_output: OutputPathType
    """Estimate of the noise standard deviation after wavelet decomposition for
    each input dataset"""
    costs_output: OutputPathType
    """Cost function to select the regularization parameter (lambda) according
    to selection criterion"""


def v_3d_mepfm_params(
    input_files: list[str],
    dbg_args: bool = False,
    mask: InputPathType | None = None,
    hrf_model: str | None = None,
    verbosity: int | None = None,
) -> V3dMepfmParameters:
    """
    Build parameters.
    
    Args:
        input_files: Dataset to analyze with Multiecho Paradigm Free Mapping,\
            along with the echo time.
        dbg_args: Enable R to save the parameters in .3dMEPFM.dbg.AFNI.args in\
            the current directory.
        mask: Process voxels inside this mask only. Default is no masking.
        hrf_model: Haemodynamic response function used for deconvolution.
        verbosity: Verbosity level. 0 for quiet, 1 (default) or more:\
            talkative.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMEPFM",
        "input_files": input_files,
        "dbgArgs": dbg_args,
    }
    if mask is not None:
        params["mask"] = mask
    if hrf_model is not None:
        params["hrf_model"] = hrf_model
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def v_3d_mepfm_cargs(
    params: V3dMepfmParameters,
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
    cargs.append("3dMEPFM")
    cargs.extend([
        "-input",
        *params.get("input_files")
    ])
    if params.get("dbgArgs"):
        cargs.append("-dbgArgs")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("hrf_model") is not None:
        cargs.extend([
            "-hrf",
            params.get("hrf_model")
        ])
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    cargs.append("[OTHER_OPTIONS]")
    return cargs


def v_3d_mepfm_outputs(
    params: V3dMepfmParameters,
    execution: Execution,
) -> V3dMepfmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMepfmOutputs(
        root=execution.output_file("."),
        dr2_output=execution.output_file("DR2_[PREFIX]_*.nii.gz"),
        dr2fit_output=execution.output_file("DR2fit_[PREFIX]_*.nii.gz"),
        ds0_output=execution.output_file("DS0_[PREFIX]_*.nii.gz"),
        lambda_output=execution.output_file("lambda_[PREFIX]_*.nii.gz"),
        sigmas_mad_output=execution.output_file("sigmas_MAD_[PREFIX]_*.nii.gz"),
        costs_output=execution.output_file("costs_[PREFIX]_*.nii.gz"),
    )
    return ret


def v_3d_mepfm_execute(
    params: V3dMepfmParameters,
    execution: Execution,
) -> V3dMepfmOutputs:
    """
    Voxelwise deconvolution of Multiecho fMRI data to yield time-varying estimates
    of changes in transverse relaxation (DR2*) and optionally, net magnetization
    (DS0).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMepfmOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_mepfm_cargs(params, execution)
    ret = v_3d_mepfm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mepfm(
    input_files: list[str],
    dbg_args: bool = False,
    mask: InputPathType | None = None,
    hrf_model: str | None = None,
    verbosity: int | None = None,
    runner: Runner | None = None,
) -> V3dMepfmOutputs:
    """
    Voxelwise deconvolution of Multiecho fMRI data to yield time-varying estimates
    of changes in transverse relaxation (DR2*) and optionally, net magnetization
    (DS0).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Dataset to analyze with Multiecho Paradigm Free Mapping,\
            along with the echo time.
        dbg_args: Enable R to save the parameters in .3dMEPFM.dbg.AFNI.args in\
            the current directory.
        mask: Process voxels inside this mask only. Default is no masking.
        hrf_model: Haemodynamic response function used for deconvolution.
        verbosity: Verbosity level. 0 for quiet, 1 (default) or more:\
            talkative.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMepfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MEPFM_METADATA)
    params = v_3d_mepfm_params(
        input_files=input_files,
        dbg_args=dbg_args,
        mask=mask,
        hrf_model=hrf_model,
        verbosity=verbosity,
    )
    return v_3d_mepfm_execute(params, execution)


__all__ = [
    "V3dMepfmOutputs",
    "V3dMepfmParameters",
    "V_3D_MEPFM_METADATA",
    "v_3d_mepfm",
    "v_3d_mepfm_params",
]
