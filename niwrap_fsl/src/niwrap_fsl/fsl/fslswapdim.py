# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLSWAPDIM_METADATA = Metadata(
    id="719ac7a26dce0fabfe819da095bdc5f13c6aea42.boutiques",
    name="fslswapdim",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslswapdimParameters = typing.TypedDict('FslswapdimParameters', {
    "__STYXTYPE__": typing.Literal["fslswapdim"],
    "input_file": InputPathType,
    "axis_a": str,
    "axis_b": str,
    "axis_c": str,
    "output_file": typing.NotRequired[str | None],
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
        "fslswapdim": fslswapdim_cargs,
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
        "fslswapdim": fslswapdim_outputs,
    }.get(t)


class FslswapdimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslswapdim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """Output image with swapped dimensions"""


def fslswapdim_params(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: str | None = None,
) -> FslswapdimParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image (e.g. img.nii.gz).
        axis_a: New x-axis dimension (e.g., -x, x, RL, etc.).
        axis_b: New y-axis dimension (e.g., -y, y, PA, etc.).
        axis_c: New z-axis dimension (e.g., -z, z, IS, etc.).
        output_file: Output image (e.g., output.nii.gz). If not specified, the\
            equivalent transformation matrix is written to the standard output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslswapdim",
        "input_file": input_file,
        "axis_a": axis_a,
        "axis_b": axis_b,
        "axis_c": axis_c,
    }
    if output_file is not None:
        params["output_file"] = output_file
    return params


def fslswapdim_cargs(
    params: FslswapdimParameters,
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
    cargs.append("fslswapdim")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("axis_a"))
    cargs.append(params.get("axis_b"))
    cargs.append(params.get("axis_c"))
    if params.get("output_file") is not None:
        cargs.append(params.get("output_file"))
    return cargs


def fslswapdim_outputs(
    params: FslswapdimParameters,
    execution: Execution,
) -> FslswapdimOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslswapdimOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def fslswapdim_execute(
    params: FslswapdimParameters,
    execution: Execution,
) -> FslswapdimOutputs:
    """
    Swap dimensions of an image volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslswapdimOutputs`).
    """
    params = execution.params(params)
    cargs = fslswapdim_cargs(params, execution)
    ret = fslswapdim_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslswapdim(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> FslswapdimOutputs:
    """
    Swap dimensions of an image volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image (e.g. img.nii.gz).
        axis_a: New x-axis dimension (e.g., -x, x, RL, etc.).
        axis_b: New y-axis dimension (e.g., -y, y, PA, etc.).
        axis_c: New z-axis dimension (e.g., -z, z, IS, etc.).
        output_file: Output image (e.g., output.nii.gz). If not specified, the\
            equivalent transformation matrix is written to the standard output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslswapdimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSWAPDIM_METADATA)
    params = fslswapdim_params(
        input_file=input_file,
        axis_a=axis_a,
        axis_b=axis_b,
        axis_c=axis_c,
        output_file=output_file,
    )
    return fslswapdim_execute(params, execution)


__all__ = [
    "FSLSWAPDIM_METADATA",
    "FslswapdimOutputs",
    "FslswapdimParameters",
    "fslswapdim",
    "fslswapdim_params",
]
