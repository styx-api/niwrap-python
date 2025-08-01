# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PERFUSION_SUBTRACT_METADATA = Metadata(
    id="9feeea7d168f906886e7d401e5314a26027ab52e.boutiques",
    name="perfusion_subtract",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PerfusionSubtractParameters = typing.TypedDict('PerfusionSubtractParameters', {
    "__STYXTYPE__": typing.Literal["perfusion_subtract"],
    "four_d_input": InputPathType,
    "four_d_output": str,
    "control_first_flag": bool,
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
        "perfusion_subtract": perfusion_subtract_cargs,
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
        "perfusion_subtract": perfusion_subtract_outputs,
    }.get(t)


class PerfusionSubtractOutputs(typing.NamedTuple):
    """
    Output object returned when calling `perfusion_subtract(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output 4D image with subtraction results"""


def perfusion_subtract_params(
    four_d_input: InputPathType,
    four_d_output: str,
    control_first_flag: bool = False,
) -> PerfusionSubtractParameters:
    """
    Build parameters.
    
    Args:
        four_d_input: Input 4D perfusion image (e.g. perfusion.nii.gz).
        four_d_output: Output 4D image with subtraction results (e.g.\
            perfusion_subtracted.nii.gz).
        control_first_flag: First timepoint is control instead of tag. Default\
            is tag first.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "perfusion_subtract",
        "four_d_input": four_d_input,
        "four_d_output": four_d_output,
        "control_first_flag": control_first_flag,
    }
    return params


def perfusion_subtract_cargs(
    params: PerfusionSubtractParameters,
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
    cargs.append("perfusion_subtract")
    cargs.append(execution.input_file(params.get("four_d_input")))
    cargs.append(params.get("four_d_output"))
    if params.get("control_first_flag"):
        cargs.append("-c")
    return cargs


def perfusion_subtract_outputs(
    params: PerfusionSubtractParameters,
    execution: Execution,
) -> PerfusionSubtractOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PerfusionSubtractOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("four_d_output") + ".nii.gz"),
    )
    return ret


def perfusion_subtract_execute(
    params: PerfusionSubtractParameters,
    execution: Execution,
) -> PerfusionSubtractOutputs:
    """
    Subtract control images from tag images in 4D perfusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PerfusionSubtractOutputs`).
    """
    params = execution.params(params)
    cargs = perfusion_subtract_cargs(params, execution)
    ret = perfusion_subtract_outputs(params, execution)
    execution.run(cargs)
    return ret


def perfusion_subtract(
    four_d_input: InputPathType,
    four_d_output: str,
    control_first_flag: bool = False,
    runner: Runner | None = None,
) -> PerfusionSubtractOutputs:
    """
    Subtract control images from tag images in 4D perfusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        four_d_input: Input 4D perfusion image (e.g. perfusion.nii.gz).
        four_d_output: Output 4D image with subtraction results (e.g.\
            perfusion_subtracted.nii.gz).
        control_first_flag: First timepoint is control instead of tag. Default\
            is tag first.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PerfusionSubtractOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PERFUSION_SUBTRACT_METADATA)
    params = perfusion_subtract_params(
        four_d_input=four_d_input,
        four_d_output=four_d_output,
        control_first_flag=control_first_flag,
    )
    return perfusion_subtract_execute(params, execution)


__all__ = [
    "PERFUSION_SUBTRACT_METADATA",
    "PerfusionSubtractOutputs",
    "PerfusionSubtractParameters",
    "perfusion_subtract",
    "perfusion_subtract_params",
]
