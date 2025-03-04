# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

OXFORD_ASL_METADATA = Metadata(
    id="eadb081312f49bbddc149e22fee8be8a141e4596.boutiques",
    name="oxford_asl",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


OxfordAslParameters = typing.TypedDict('OxfordAslParameters', {
    "__STYX_TYPE__": typing.Literal["oxford_asl"],
    "asl_data": InputPathType,
    "output_dir_name": str,
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
        "oxford_asl": oxford_asl_cargs,
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
        "oxford_asl": oxford_asl_outputs,
    }.get(t)


class OxfordAslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `oxford_asl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Directory containing the output files"""


def oxford_asl_params(
    asl_data: InputPathType,
    output_dir_name: str,
) -> OxfordAslParameters:
    """
    Build parameters.
    
    Args:
        asl_data: Input ASL data.
        output_dir_name: Output directory name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "oxford_asl",
        "asl_data": asl_data,
        "output_dir_name": output_dir_name,
    }
    return params


def oxford_asl_cargs(
    params: OxfordAslParameters,
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
    cargs.append("oxford_asl")
    cargs.extend([
        "-i",
        execution.input_file(params.get("asl_data"))
    ])
    cargs.extend([
        "-o",
        params.get("output_dir_name")
    ])
    cargs.append("[options]")
    return cargs


def oxford_asl_outputs(
    params: OxfordAslParameters,
    execution: Execution,
) -> OxfordAslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = OxfordAslOutputs(
        root=execution.output_file("."),
        output_dir=execution.output_file(params.get("output_dir_name")),
    )
    return ret


def oxford_asl_execute(
    params: OxfordAslParameters,
    execution: Execution,
) -> OxfordAslOutputs:
    """
    Calculate perfusion maps from ASL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `OxfordAslOutputs`).
    """
    params = execution.params(params)
    cargs = oxford_asl_cargs(params, execution)
    ret = oxford_asl_outputs(params, execution)
    execution.run(cargs)
    return ret


def oxford_asl(
    asl_data: InputPathType,
    output_dir_name: str,
    runner: Runner | None = None,
) -> OxfordAslOutputs:
    """
    Calculate perfusion maps from ASL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        asl_data: Input ASL data.
        output_dir_name: Output directory name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OxfordAslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OXFORD_ASL_METADATA)
    params = oxford_asl_params(
        asl_data=asl_data,
        output_dir_name=output_dir_name,
    )
    return oxford_asl_execute(params, execution)


__all__ = [
    "OXFORD_ASL_METADATA",
    "OxfordAslOutputs",
    "OxfordAslParameters",
    "oxford_asl",
    "oxford_asl_params",
]
