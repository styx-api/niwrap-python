# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_SKULL_STRIP_METADATA = Metadata(
    id="ab34e8a40a7c57dd3421d932dc0cf51d69472c21.boutiques",
    name="3dSkullStrip",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dSkullStripParameters = typing.TypedDict('V3dSkullStripParameters', {
    "__STYX_TYPE__": typing.Literal["3dSkullStrip"],
    "in_file": InputPathType,
    "num_threads": typing.NotRequired[int | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
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
        "3dSkullStrip": v_3d_skull_strip_cargs,
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
        "3dSkullStrip": v_3d_skull_strip_outputs,
    }.get(t)


class V3dSkullStripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_skull_strip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_skull_strip_params(
    in_file: InputPathType,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
) -> V3dSkullStripParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3dskullstrip.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSkullStrip",
        "in_file": in_file,
    }
    if num_threads is not None:
        params["num_threads"] = num_threads
    if outputtype is not None:
        params["outputtype"] = outputtype
    return params


def v_3d_skull_strip_cargs(
    params: V3dSkullStripParameters,
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
    cargs.append("3dSkullStrip")
    cargs.extend([
        "-input",
        execution.input_file(params.get("in_file"))
    ])
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    return cargs


def v_3d_skull_strip_outputs(
    params: V3dSkullStripParameters,
    execution: Execution,
) -> V3dSkullStripOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSkullStripOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("in_file")).name + "_skullstrip"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def v_3d_skull_strip_execute(
    params: V3dSkullStripParameters,
    execution: Execution,
) -> V3dSkullStripOutputs:
    """
    A program to extract the brain from surrounding tissue from MRI T1-weighted
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSkullStripOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_skull_strip_cargs(params, execution)
    ret = v_3d_skull_strip_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_skull_strip(
    in_file: InputPathType,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner | None = None,
) -> V3dSkullStripOutputs:
    """
    A program to extract the brain from surrounding tissue from MRI T1-weighted
    images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3dskullstrip.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSkullStripOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SKULL_STRIP_METADATA)
    params = v_3d_skull_strip_params(
        in_file=in_file,
        num_threads=num_threads,
        outputtype=outputtype,
    )
    return v_3d_skull_strip_execute(params, execution)


__all__ = [
    "V3dSkullStripOutputs",
    "V3dSkullStripParameters",
    "V_3D_SKULL_STRIP_METADATA",
    "v_3d_skull_strip",
    "v_3d_skull_strip_params",
]
