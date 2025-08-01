# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TALAIRACH_MGH_METADATA = Metadata(
    id="6b9e2a03c841e63355d5121337160b9481a21d90.boutiques",
    name="talairach_mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TalairachMghParameters = typing.TypedDict('TalairachMghParameters', {
    "__STYXTYPE__": typing.Literal["talairach_mgh"],
    "input_volume": InputPathType,
    "output_volume": str,
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
        "talairach_mgh": talairach_mgh_cargs,
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
        "talairach_mgh": talairach_mgh_outputs,
    }.get(t)


class TalairachMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `talairach_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output: OutputPathType
    """Transformed output volume aligned with Talairach reference brain"""


def talairach_mgh_params(
    input_volume: InputPathType,
    output_volume: str,
) -> TalairachMghParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume file for the talairach transformation.
        output_volume: Output volume file for the talairach transformation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "talairach_mgh",
        "input_volume": input_volume,
        "output_volume": output_volume,
    }
    return params


def talairach_mgh_cargs(
    params: TalairachMghParameters,
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
    cargs.append("talairach_mgh")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(params.get("output_volume"))
    return cargs


def talairach_mgh_outputs(
    params: TalairachMghParameters,
    execution: Execution,
) -> TalairachMghOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TalairachMghOutputs(
        root=execution.output_file("."),
        transformed_output=execution.output_file(params.get("output_volume")),
    )
    return ret


def talairach_mgh_execute(
    params: TalairachMghParameters,
    execution: Execution,
) -> TalairachMghOutputs:
    """
    A tool for aligning brain volume with Talairach reference brain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TalairachMghOutputs`).
    """
    params = execution.params(params)
    cargs = talairach_mgh_cargs(params, execution)
    ret = talairach_mgh_outputs(params, execution)
    execution.run(cargs)
    return ret


def talairach_mgh(
    input_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> TalairachMghOutputs:
    """
    A tool for aligning brain volume with Talairach reference brain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file for the talairach transformation.
        output_volume: Output volume file for the talairach transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalairachMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALAIRACH_MGH_METADATA)
    params = talairach_mgh_params(
        input_volume=input_volume,
        output_volume=output_volume,
    )
    return talairach_mgh_execute(params, execution)


__all__ = [
    "TALAIRACH_MGH_METADATA",
    "TalairachMghOutputs",
    "TalairachMghParameters",
    "talairach_mgh",
    "talairach_mgh_params",
]
