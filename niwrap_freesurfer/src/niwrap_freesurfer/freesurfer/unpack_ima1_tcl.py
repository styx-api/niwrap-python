# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNPACK_IMA1_TCL_METADATA = Metadata(
    id="2f44fce6973250c18da864f8fa4ee59aea5aae9d.boutiques",
    name="unpack_ima1.tcl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


UnpackIma1TclParameters = typing.TypedDict('UnpackIma1TclParameters', {
    "__STYXTYPE__": typing.Literal["unpack_ima1.tcl"],
    "input_directory": str,
    "output_directory": str,
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
        "unpack_ima1.tcl": unpack_ima1_tcl_cargs,
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
        "unpack_ima1.tcl": unpack_ima1_tcl_outputs,
    }.get(t)


class UnpackIma1TclOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpack_ima1_tcl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unpacked_files: OutputPathType
    """Unpacked files stored in the output directory"""


def unpack_ima1_tcl_params(
    input_directory: str,
    output_directory: str,
) -> UnpackIma1TclParameters:
    """
    Build parameters.
    
    Args:
        input_directory: The directory containing the input files to be\
            unpacked.
        output_directory: The directory where the unpacked files will be\
            stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "unpack_ima1.tcl",
        "input_directory": input_directory,
        "output_directory": output_directory,
    }
    return params


def unpack_ima1_tcl_cargs(
    params: UnpackIma1TclParameters,
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
    cargs.append("unpack_ima1.tcl")
    cargs.append(params.get("input_directory"))
    cargs.append(params.get("output_directory"))
    return cargs


def unpack_ima1_tcl_outputs(
    params: UnpackIma1TclParameters,
    execution: Execution,
) -> UnpackIma1TclOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UnpackIma1TclOutputs(
        root=execution.output_file("."),
        unpacked_files=execution.output_file(params.get("output_directory") + "/*"),
    )
    return ret


def unpack_ima1_tcl_execute(
    params: UnpackIma1TclParameters,
    execution: Execution,
) -> UnpackIma1TclOutputs:
    """
    A tool for unpacking images using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UnpackIma1TclOutputs`).
    """
    params = execution.params(params)
    cargs = unpack_ima1_tcl_cargs(params, execution)
    ret = unpack_ima1_tcl_outputs(params, execution)
    execution.run(cargs)
    return ret


def unpack_ima1_tcl(
    input_directory: str,
    output_directory: str,
    runner: Runner | None = None,
) -> UnpackIma1TclOutputs:
    """
    A tool for unpacking images using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_directory: The directory containing the input files to be\
            unpacked.
        output_directory: The directory where the unpacked files will be\
            stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackIma1TclOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACK_IMA1_TCL_METADATA)
    params = unpack_ima1_tcl_params(
        input_directory=input_directory,
        output_directory=output_directory,
    )
    return unpack_ima1_tcl_execute(params, execution)


__all__ = [
    "UNPACK_IMA1_TCL_METADATA",
    "UnpackIma1TclOutputs",
    "UnpackIma1TclParameters",
    "unpack_ima1_tcl",
    "unpack_ima1_tcl_params",
]
