# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ROI_CORR_MAT_METADATA = Metadata(
    id="5904d2e01ec13ad3edfd3292a0db082f6bbac4d2.boutiques",
    name="@ROI_Corr_Mat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VRoiCorrMatParameters = typing.TypedDict('VRoiCorrMatParameters', {
    "__STYXTYPE__": typing.Literal["@ROI_Corr_Mat"],
    "ts_vol": InputPathType,
    "roi_vol": InputPathType,
    "prefix": str,
    "roisel": typing.NotRequired[InputPathType | None],
    "zval": bool,
    "mat_opt": typing.NotRequired[str | None],
    "dirty": bool,
    "keep_tmp": bool,
    "echo": bool,
    "verb": bool,
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
        "@ROI_Corr_Mat": v__roi_corr_mat_cargs,
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
        "@ROI_Corr_Mat": v__roi_corr_mat_outputs,
    }.get(t)


class VRoiCorrMatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__roi_corr_mat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix_1d: OutputPathType
    """Correlation matrix in .1D format"""
    matrix_brick: OutputPathType
    """Correlation matrix in .BRIK format"""


def v__roi_corr_mat_params(
    ts_vol: InputPathType,
    roi_vol: InputPathType,
    prefix: str,
    roisel: InputPathType | None = None,
    zval: bool = False,
    mat_opt: str | None = None,
    dirty: bool = False,
    keep_tmp: bool = False,
    echo: bool = False,
    verb: bool = False,
) -> VRoiCorrMatParameters:
    """
    Build parameters.
    
    Args:
        ts_vol: Time series volume.
        roi_vol: ROI volume.
        prefix: Use output for a prefix.
        roisel: Force processing of ROI label (integers) listed in ROISEL 1D\
            file.
        zval: Output a zscore version of the correlation matrix.
        mat_opt: Output matrix in different manners.
        dirty: Keep temporary files.
        keep_tmp: Keep temporary files.
        echo: Set echo (echo all commands to screen).
        verb: Verbose flag.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ROI_Corr_Mat",
        "ts_vol": ts_vol,
        "roi_vol": roi_vol,
        "prefix": prefix,
        "zval": zval,
        "dirty": dirty,
        "keep_tmp": keep_tmp,
        "echo": echo,
        "verb": verb,
    }
    if roisel is not None:
        params["roisel"] = roisel
    if mat_opt is not None:
        params["mat_opt"] = mat_opt
    return params


def v__roi_corr_mat_cargs(
    params: VRoiCorrMatParameters,
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
    cargs.append("@ROI_Corr_Mat")
    cargs.extend([
        "-ts",
        execution.input_file(params.get("ts_vol"))
    ])
    cargs.extend([
        "-roi",
        execution.input_file(params.get("roi_vol"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("roisel") is not None:
        cargs.extend([
            "-roisel",
            execution.input_file(params.get("roisel"))
        ])
    if params.get("zval"):
        cargs.append("-zval")
    if params.get("mat_opt") is not None:
        cargs.extend([
            "-mat",
            params.get("mat_opt")
        ])
    if params.get("dirty"):
        cargs.append("-dirty")
    if params.get("keep_tmp"):
        cargs.append("-keep_tmp")
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("verb"):
        cargs.append("-verb")
    return cargs


def v__roi_corr_mat_outputs(
    params: VRoiCorrMatParameters,
    execution: Execution,
) -> VRoiCorrMatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VRoiCorrMatOutputs(
        root=execution.output_file("."),
        matrix_1d=execution.output_file(params.get("prefix") + "_matrix.1D"),
        matrix_brick=execution.output_file(params.get("prefix") + "_matrix.BRIK"),
    )
    return ret


def v__roi_corr_mat_execute(
    params: VRoiCorrMatParameters,
    execution: Execution,
) -> VRoiCorrMatOutputs:
    """
    Script to produce an NxN ROI correlation matrix of N ROIs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VRoiCorrMatOutputs`).
    """
    params = execution.params(params)
    cargs = v__roi_corr_mat_cargs(params, execution)
    ret = v__roi_corr_mat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__roi_corr_mat(
    ts_vol: InputPathType,
    roi_vol: InputPathType,
    prefix: str,
    roisel: InputPathType | None = None,
    zval: bool = False,
    mat_opt: str | None = None,
    dirty: bool = False,
    keep_tmp: bool = False,
    echo: bool = False,
    verb: bool = False,
    runner: Runner | None = None,
) -> VRoiCorrMatOutputs:
    """
    Script to produce an NxN ROI correlation matrix of N ROIs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ts_vol: Time series volume.
        roi_vol: ROI volume.
        prefix: Use output for a prefix.
        roisel: Force processing of ROI label (integers) listed in ROISEL 1D\
            file.
        zval: Output a zscore version of the correlation matrix.
        mat_opt: Output matrix in different manners.
        dirty: Keep temporary files.
        keep_tmp: Keep temporary files.
        echo: Set echo (echo all commands to screen).
        verb: Verbose flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRoiCorrMatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ROI_CORR_MAT_METADATA)
    params = v__roi_corr_mat_params(
        ts_vol=ts_vol,
        roi_vol=roi_vol,
        prefix=prefix,
        roisel=roisel,
        zval=zval,
        mat_opt=mat_opt,
        dirty=dirty,
        keep_tmp=keep_tmp,
        echo=echo,
        verb=verb,
    )
    return v__roi_corr_mat_execute(params, execution)


__all__ = [
    "VRoiCorrMatOutputs",
    "VRoiCorrMatParameters",
    "V__ROI_CORR_MAT_METADATA",
    "v__roi_corr_mat",
    "v__roi_corr_mat_params",
]
