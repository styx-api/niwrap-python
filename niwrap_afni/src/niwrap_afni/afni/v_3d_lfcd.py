# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_LFCD_METADATA = Metadata(
    id="87de0d819215973cf284e8b6a6ca038b54f23229.boutiques",
    name="3dLFCD",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dLfcdParameters = typing.TypedDict('V3dLfcdParameters', {
    "__STYXTYPE__": typing.Literal["3dLFCD"],
    "in_file": InputPathType,
    "autoclip": bool,
    "automask": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "num_threads": typing.NotRequired[int | None],
    "out_file": typing.NotRequired[str | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "polort": typing.NotRequired[int | None],
    "thresh": typing.NotRequired[float | None],
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
        "3dLFCD": v_3d_lfcd_cargs,
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
        "3dLFCD": v_3d_lfcd_outputs,
    }.get(t)


class V3dLfcdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_lfcd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""


def v_3d_lfcd_params(
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    out_file: str | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    polort: int | None = None,
    thresh: float | None = None,
) -> V3dLfcdParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3dlfcd.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        mask: Mask file to mask input data.
        num_threads: Set number of threads.
        out_file: Output image file name.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        polort: No description provided.
        thresh: Threshold to exclude connections where corr <= thresh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLFCD",
        "in_file": in_file,
        "autoclip": autoclip,
        "automask": automask,
    }
    if mask is not None:
        params["mask"] = mask
    if num_threads is not None:
        params["num_threads"] = num_threads
    if out_file is not None:
        params["out_file"] = out_file
    if outputtype is not None:
        params["outputtype"] = outputtype
    if polort is not None:
        params["polort"] = polort
    if thresh is not None:
        params["thresh"] = thresh
    return params


def v_3d_lfcd_cargs(
    params: V3dLfcdParameters,
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
    cargs.append("3dLFCD")
    cargs.append(execution.input_file(params.get("in_file")))
    if params.get("autoclip"):
        cargs.append("-autoclip")
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    if params.get("out_file") is not None:
        cargs.extend([
            "-prefix",
            params.get("out_file")
        ])
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("thresh") is not None:
        cargs.extend([
            "-thresh",
            str(params.get("thresh"))
        ])
    return cargs


def v_3d_lfcd_outputs(
    params: V3dLfcdParameters,
    execution: Execution,
) -> V3dLfcdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLfcdOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("in_file")).name + "_afni"),
    )
    return ret


def v_3d_lfcd_execute(
    params: V3dLfcdParameters,
    execution: Execution,
) -> V3dLfcdOutputs:
    """
    Performs degree centrality on a dataset using a given maskfile via the 3dLFCD
    command.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLfcdOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_lfcd_cargs(params, execution)
    ret = v_3d_lfcd_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_lfcd(
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    out_file: str | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    polort: int | None = None,
    thresh: float | None = None,
    runner: Runner | None = None,
) -> V3dLfcdOutputs:
    """
    Performs degree centrality on a dataset using a given maskfile via the 3dLFCD
    command.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3dlfcd.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        mask: Mask file to mask input data.
        num_threads: Set number of threads.
        out_file: Output image file name.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        polort: No description provided.
        thresh: Threshold to exclude connections where corr <= thresh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLfcdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LFCD_METADATA)
    params = v_3d_lfcd_params(
        in_file=in_file,
        autoclip=autoclip,
        automask=automask,
        mask=mask,
        num_threads=num_threads,
        out_file=out_file,
        outputtype=outputtype,
        polort=polort,
        thresh=thresh,
    )
    return v_3d_lfcd_execute(params, execution)


__all__ = [
    "V3dLfcdOutputs",
    "V3dLfcdParameters",
    "V_3D_LFCD_METADATA",
    "v_3d_lfcd",
    "v_3d_lfcd_params",
]
