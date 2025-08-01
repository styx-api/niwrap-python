# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMLN_METADATA = Metadata(
    id="8b01d07542dbd623ad758acd765f26736fdf23cd.boutiques",
    name="imln",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ImlnParameters = typing.TypedDict('ImlnParameters', {
    "__STYXTYPE__": typing.Literal["imln"],
    "input_file": InputPathType,
    "link_name": str,
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
        "imln": imln_cargs,
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
        "imln": imln_outputs,
    }.get(t)


class ImlnOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imln(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_link: OutputPathType
    """The created link to the input file"""


def imln_params(
    input_file: InputPathType,
    link_name: str,
) -> ImlnParameters:
    """
    Build parameters.
    
    Args:
        input_file: The source file (file1) to create a link to.
        link_name: The name for the link (file2).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imln",
        "input_file": input_file,
        "link_name": link_name,
    }
    return params


def imln_cargs(
    params: ImlnParameters,
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
    cargs.append("imln")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("link_name"))
    return cargs


def imln_outputs(
    params: ImlnParameters,
    execution: Execution,
) -> ImlnOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImlnOutputs(
        root=execution.output_file("."),
        output_link=execution.output_file(params.get("link_name")),
    )
    return ret


def imln_execute(
    params: ImlnParameters,
    execution: Execution,
) -> ImlnOutputs:
    """
    Creates a link (called file2) to file1.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImlnOutputs`).
    """
    params = execution.params(params)
    cargs = imln_cargs(params, execution)
    ret = imln_outputs(params, execution)
    execution.run(cargs)
    return ret


def imln(
    input_file: InputPathType,
    link_name: str,
    runner: Runner | None = None,
) -> ImlnOutputs:
    """
    Creates a link (called file2) to file1.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: The source file (file1) to create a link to.
        link_name: The name for the link (file2).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImlnOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMLN_METADATA)
    params = imln_params(
        input_file=input_file,
        link_name=link_name,
    )
    return imln_execute(params, execution)


__all__ = [
    "IMLN_METADATA",
    "ImlnOutputs",
    "ImlnParameters",
    "imln",
    "imln_params",
]
