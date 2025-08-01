# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMMV_METADATA = Metadata(
    id="44ec8b1b3324cc2a5621203b5bcc839d1c6cbcd8.boutiques",
    name="immv",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ImmvParameters = typing.TypedDict('ImmvParameters', {
    "__STYXTYPE__": typing.Literal["immv"],
    "source_files": list[InputPathType],
    "destination": str,
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
        "immv": immv_cargs,
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
    }.get(t)


class ImmvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `immv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def immv_params(
    source_files: list[InputPathType],
    destination: str,
) -> ImmvParameters:
    """
    Build parameters.
    
    Args:
        source_files: Source files to be moved. Recognized file extensions:\
            .nii.gz, .nii, .img, .hdr, .img.gz, .hdr.gz.
        destination: Destination file or directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "immv",
        "source_files": source_files,
        "destination": destination,
    }
    return params


def immv_cargs(
    params: ImmvParameters,
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
    cargs.append("immv")
    cargs.extend([execution.input_file(f) for f in params.get("source_files")])
    cargs.append(params.get("destination"))
    return cargs


def immv_outputs(
    params: ImmvParameters,
    execution: Execution,
) -> ImmvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImmvOutputs(
        root=execution.output_file("."),
    )
    return ret


def immv_execute(
    params: ImmvParameters,
    execution: Execution,
) -> ImmvOutputs:
    """
    Moves images from one file or directory to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImmvOutputs`).
    """
    params = execution.params(params)
    cargs = immv_cargs(params, execution)
    ret = immv_outputs(params, execution)
    execution.run(cargs)
    return ret


def immv(
    source_files: list[InputPathType],
    destination: str,
    runner: Runner | None = None,
) -> ImmvOutputs:
    """
    Moves images from one file or directory to another.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        source_files: Source files to be moved. Recognized file extensions:\
            .nii.gz, .nii, .img, .hdr, .img.gz, .hdr.gz.
        destination: Destination file or directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImmvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMMV_METADATA)
    params = immv_params(
        source_files=source_files,
        destination=destination,
    )
    return immv_execute(params, execution)


__all__ = [
    "IMMV_METADATA",
    "ImmvOutputs",
    "ImmvParameters",
    "immv",
    "immv_params",
]
