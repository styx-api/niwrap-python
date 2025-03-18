# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONCAT_BVARS_METADATA = Metadata(
    id="510347f86dbed1c84a14f18194f7a263598dc7bb.boutiques",
    name="concat_bvars",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ConcatBvarsParameters = typing.TypedDict('ConcatBvarsParameters', {
    "__STYX_TYPE__": typing.Literal["concat_bvars"],
    "output_bvars": str,
    "input_bvars": list[InputPathType],
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
        "concat_bvars": concat_bvars_cargs,
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
        "concat_bvars": concat_bvars_outputs,
    }.get(t)


class ConcatBvarsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `concat_bvars(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Concatenated output .bvars file"""


def concat_bvars_params(
    output_bvars: str,
    input_bvars: list[InputPathType],
) -> ConcatBvarsParameters:
    """
    Build parameters.
    
    Args:
        output_bvars: Output .bvars file.
        input_bvars: List of input .bvars files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "concat_bvars",
        "output_bvars": output_bvars,
        "input_bvars": input_bvars,
    }
    return params


def concat_bvars_cargs(
    params: ConcatBvarsParameters,
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
    cargs.append("concat_bvars")
    cargs.append(params.get("output_bvars"))
    cargs.extend([execution.input_file(f) for f in params.get("input_bvars")])
    return cargs


def concat_bvars_outputs(
    params: ConcatBvarsParameters,
    execution: Execution,
) -> ConcatBvarsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConcatBvarsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_bvars")),
    )
    return ret


def concat_bvars_execute(
    params: ConcatBvarsParameters,
    execution: Execution,
) -> ConcatBvarsOutputs:
    """
    Concatenate multiple .bvars files into a single .bvars file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConcatBvarsOutputs`).
    """
    params = execution.params(params)
    cargs = concat_bvars_cargs(params, execution)
    ret = concat_bvars_outputs(params, execution)
    execution.run(cargs)
    return ret


def concat_bvars(
    output_bvars: str,
    input_bvars: list[InputPathType],
    runner: Runner | None = None,
) -> ConcatBvarsOutputs:
    """
    Concatenate multiple .bvars files into a single .bvars file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_bvars: Output .bvars file.
        input_bvars: List of input .bvars files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConcatBvarsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONCAT_BVARS_METADATA)
    params = concat_bvars_params(
        output_bvars=output_bvars,
        input_bvars=input_bvars,
    )
    return concat_bvars_execute(params, execution)


__all__ = [
    "CONCAT_BVARS_METADATA",
    "ConcatBvarsOutputs",
    "ConcatBvarsParameters",
    "concat_bvars",
    "concat_bvars_params",
]
