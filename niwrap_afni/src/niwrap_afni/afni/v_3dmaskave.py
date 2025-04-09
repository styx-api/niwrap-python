# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMASKAVE_METADATA = Metadata(
    id="c5b975dfce2d2bdf5e26413b56b508d45f7a0ccb.boutiques",
    name="3dmaskave",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dmaskaveParameters = typing.TypedDict('V3dmaskaveParameters', {
    "__STYX_TYPE__": typing.Literal["3dmaskave"],
    "in_file": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "num_threads": typing.NotRequired[int | None],
    "outputtype": typing.NotRequired[typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None],
    "quiet": bool,
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
        "3dmaskave": v_3dmaskave_cargs,
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
        "3dmaskave": v_3dmaskave_outputs,
    }.get(t)


class V3dmaskaveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaskave(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3dmaskave_params(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    quiet: bool = False,
) -> V3dmaskaveParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input file to 3dmaskave.
        mask: Matrix to align input file.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        quiet: Matrix to align input file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmaskave",
        "in_file": in_file,
        "quiet": quiet,
    }
    if mask is not None:
        params["mask"] = mask
    if num_threads is not None:
        params["num_threads"] = num_threads
    if outputtype is not None:
        params["outputtype"] = outputtype
    return params


def v_3dmaskave_cargs(
    params: V3dmaskaveParameters,
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
    cargs.append("3dmaskave")
    cargs.append(execution.input_file(params.get("in_file")))
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("num_threads") is not None:
        cargs.append(str(params.get("num_threads")))
    if params.get("outputtype") is not None:
        cargs.append(params.get("outputtype"))
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3dmaskave_outputs(
    params: V3dmaskaveParameters,
    execution: Execution,
) -> V3dmaskaveOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmaskaveOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(params.get("in_file")).name + "_maskave.1D"),
        out_file_=execution.output_file("out_file"),
    )
    return ret


def v_3dmaskave_execute(
    params: V3dmaskaveParameters,
    execution: Execution,
) -> V3dmaskaveOutputs:
    """
    Computes average of all voxels in the input dataset which satisfy the criterion
    in the options list.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmaskaveOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dmaskave_cargs(params, execution)
    ret = v_3dmaskave_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmaskave(
    in_file: InputPathType,
    mask: InputPathType | None = None,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dmaskaveOutputs:
    """
    Computes average of all voxels in the input dataset which satisfy the criterion
    in the options list.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3dmaskave.
        mask: Matrix to align input file.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        quiet: Matrix to align input file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskaveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASKAVE_METADATA)
    params = v_3dmaskave_params(
        in_file=in_file,
        mask=mask,
        num_threads=num_threads,
        outputtype=outputtype,
        quiet=quiet,
    )
    return v_3dmaskave_execute(params, execution)


__all__ = [
    "V3dmaskaveOutputs",
    "V3dmaskaveParameters",
    "V_3DMASKAVE_METADATA",
    "v_3dmaskave",
    "v_3dmaskave_params",
]
