# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TCORR1_D_METADATA = Metadata(
    id="a49b25e122306e3daa45adb2052372c71e881198.boutiques",
    name="3dTcorr1D",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dTcorr1DParameters = typing.TypedDict('V3dTcorr1DParameters', {
    "__STYX_TYPE__": typing.Literal["3dTcorr1D"],
    "ktaub": bool,
    "num_threads": typing.NotRequired[int | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "pearson": bool,
    "quadrant": bool,
    "spearman": bool,
    "xset": InputPathType,
    "y_1d": InputPathType,
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
        "3dTcorr1D": v_3d_tcorr1_d_cargs,
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
        "3dTcorr1D": v_3d_tcorr1_d_outputs,
    }.get(t)


class V3dTcorr1DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcorr1_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output filename prefix."""
    out_file_: OutputPathType
    """Output file containing correlations."""


def v_3d_tcorr1_d_params(
    xset: InputPathType,
    y_1d: InputPathType,
    ktaub: bool = False,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    pearson: bool = False,
    quadrant: bool = False,
    spearman: bool = False,
) -> V3dTcorr1DParameters:
    """
    Build parameters.
    
    Args:
        xset: 3d+time dataset input.
        y_1d: 1d time series file input.
        ktaub: Correlation is the kendall's tau_b correlation coefficient.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        pearson: Correlation is the normal pearson correlation coefficient.
        quadrant: Correlation is the quadrant correlation coefficient.
        spearman: Correlation is the spearman (rank) correlation coefficient.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTcorr1D",
        "ktaub": ktaub,
        "pearson": pearson,
        "quadrant": quadrant,
        "spearman": spearman,
        "xset": xset,
        "y_1d": y_1d,
    }
    if num_threads is not None:
        params["num_threads"] = num_threads
    if outputtype is not None:
        params["outputtype"] = outputtype
    return params


def v_3d_tcorr1_d_cargs(
    params: V3dTcorr1DParameters,
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
    cargs.append("3dTcorr1D")
    if params.get("ktaub"):
        cargs.append("-ktaub")
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("pearson"):
        cargs.append("-pearson")
    if params.get("quadrant"):
        cargs.append("-quadrant")
    if params.get("spearman"):
        cargs.append("-spearman" + execution.input_file(params.get("xset")) + execution.input_file(params.get("y_1d")))
    return cargs


def v_3d_tcorr1_d_outputs(
    params: V3dTcorr1DParameters,
    execution: Execution,
) -> V3dTcorr1DOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTcorr1DOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("xset")).name + "_correlation.nii.gz"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def v_3d_tcorr1_d_execute(
    params: V3dTcorr1DParameters,
    execution: Execution,
) -> V3dTcorr1DOutputs:
    """
    Computes the correlation coefficient between each voxel time series in the input
    3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTcorr1DOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tcorr1_d_cargs(params, execution)
    ret = v_3d_tcorr1_d_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tcorr1_d(
    xset: InputPathType,
    y_1d: InputPathType,
    ktaub: bool = False,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    pearson: bool = False,
    quadrant: bool = False,
    spearman: bool = False,
    runner: Runner | None = None,
) -> V3dTcorr1DOutputs:
    """
    Computes the correlation coefficient between each voxel time series in the input
    3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        xset: 3d+time dataset input.
        y_1d: 1d time series file input.
        ktaub: Correlation is the kendall's tau_b correlation coefficient.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        pearson: Correlation is the normal pearson correlation coefficient.
        quadrant: Correlation is the quadrant correlation coefficient.
        spearman: Correlation is the spearman (rank) correlation coefficient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcorr1DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCORR1_D_METADATA)
    params = v_3d_tcorr1_d_params(
        ktaub=ktaub,
        num_threads=num_threads,
        outputtype=outputtype,
        pearson=pearson,
        quadrant=quadrant,
        spearman=spearman,
        xset=xset,
        y_1d=y_1d,
    )
    return v_3d_tcorr1_d_execute(params, execution)


__all__ = [
    "V3dTcorr1DOutputs",
    "V3dTcorr1DParameters",
    "V_3D_TCORR1_D_METADATA",
    "v_3d_tcorr1_d",
    "v_3d_tcorr1_d_params",
]
