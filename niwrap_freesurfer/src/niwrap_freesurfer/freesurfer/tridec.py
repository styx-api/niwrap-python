# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TRIDEC_METADATA = Metadata(
    id="b02273ae065ddda351360aefaa95dc302ac759eb.boutiques",
    name="tridec",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TridecParameters = typing.TypedDict('TridecParameters', {
    "__STYXTYPE__": typing.Literal["tridec"],
    "subject_name": str,
    "fine_file": InputPathType,
    "ico_file": InputPathType,
    "out_file": str,
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
        "tridec": tridec_cargs,
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
        "tridec": tridec_outputs,
    }.get(t)


class TridecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tridec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file from tridec processing."""


def tridec_params(
    subject_name: str,
    fine_file: InputPathType,
    ico_file: InputPathType,
    out_file: str,
) -> TridecParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject being processed.
        fine_file: Fine file input for tridec.
        ico_file: ICO file input for tridec.
        out_file: Output file for tridec processing result.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tridec",
        "subject_name": subject_name,
        "fine_file": fine_file,
        "ico_file": ico_file,
        "out_file": out_file,
    }
    return params


def tridec_cargs(
    params: TridecParameters,
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
    cargs.append("tridec")
    cargs.append(params.get("subject_name"))
    cargs.append(execution.input_file(params.get("fine_file")))
    cargs.append(execution.input_file(params.get("ico_file")))
    cargs.append(params.get("out_file"))
    return cargs


def tridec_outputs(
    params: TridecParameters,
    execution: Execution,
) -> TridecOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TridecOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("out_file")),
    )
    return ret


def tridec_execute(
    params: TridecParameters,
    execution: Execution,
) -> TridecOutputs:
    """
    Tridec tool for processing brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TridecOutputs`).
    """
    params = execution.params(params)
    cargs = tridec_cargs(params, execution)
    ret = tridec_outputs(params, execution)
    execution.run(cargs)
    return ret


def tridec(
    subject_name: str,
    fine_file: InputPathType,
    ico_file: InputPathType,
    out_file: str,
    runner: Runner | None = None,
) -> TridecOutputs:
    """
    Tridec tool for processing brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject being processed.
        fine_file: Fine file input for tridec.
        ico_file: ICO file input for tridec.
        out_file: Output file for tridec processing result.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TridecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRIDEC_METADATA)
    params = tridec_params(
        subject_name=subject_name,
        fine_file=fine_file,
        ico_file=ico_file,
        out_file=out_file,
    )
    return tridec_execute(params, execution)


__all__ = [
    "TRIDEC_METADATA",
    "TridecOutputs",
    "TridecParameters",
    "tridec",
    "tridec_params",
]
