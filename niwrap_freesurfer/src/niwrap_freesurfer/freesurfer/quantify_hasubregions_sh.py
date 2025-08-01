# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUANTIFY_HASUBREGIONS_SH_METADATA = Metadata(
    id="2c2579fdfb34fa03272c566e729ceed9f991aef2.boutiques",
    name="quantifyHAsubregions.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


QuantifyHasubregionsShParameters = typing.TypedDict('QuantifyHasubregionsShParameters', {
    "__STYXTYPE__": typing.Literal["quantifyHAsubregions.sh"],
    "prefix": str,
    "suffix": str,
    "output_file": str,
    "subjects_directory": typing.NotRequired[str | None],
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
        "quantifyHAsubregions.sh": quantify_hasubregions_sh_cargs,
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
        "quantifyHAsubregions.sh": quantify_hasubregions_sh_outputs,
    }.get(t)


class QuantifyHasubregionsShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quantify_hasubregions_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """File containing the quantification results of hippocampal subregions."""


def quantify_hasubregions_sh_params(
    prefix: str,
    suffix: str,
    output_file: str,
    subjects_directory: str | None = None,
) -> QuantifyHasubregionsShParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for the files to be processed.
        suffix: Suffix for the files to be processed.
        output_file: Output file name to store the results.
        subjects_directory: Directory containing the subject data. If not\
            provided, the current directory is used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quantifyHAsubregions.sh",
        "prefix": prefix,
        "suffix": suffix,
        "output_file": output_file,
    }
    if subjects_directory is not None:
        params["subjects_directory"] = subjects_directory
    return params


def quantify_hasubregions_sh_cargs(
    params: QuantifyHasubregionsShParameters,
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
    cargs.append("quantifyHAsubregions.sh")
    cargs.append(params.get("prefix"))
    cargs.append(params.get("suffix"))
    cargs.append(params.get("output_file"))
    if params.get("subjects_directory") is not None:
        cargs.append(params.get("subjects_directory"))
    return cargs


def quantify_hasubregions_sh_outputs(
    params: QuantifyHasubregionsShParameters,
    execution: Execution,
) -> QuantifyHasubregionsShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuantifyHasubregionsShOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def quantify_hasubregions_sh_execute(
    params: QuantifyHasubregionsShParameters,
    execution: Execution,
) -> QuantifyHasubregionsShOutputs:
    """
    Tool to quantify hippocampal subregions using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuantifyHasubregionsShOutputs`).
    """
    params = execution.params(params)
    cargs = quantify_hasubregions_sh_cargs(params, execution)
    ret = quantify_hasubregions_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def quantify_hasubregions_sh(
    prefix: str,
    suffix: str,
    output_file: str,
    subjects_directory: str | None = None,
    runner: Runner | None = None,
) -> QuantifyHasubregionsShOutputs:
    """
    Tool to quantify hippocampal subregions using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        prefix: Prefix for the files to be processed.
        suffix: Suffix for the files to be processed.
        output_file: Output file name to store the results.
        subjects_directory: Directory containing the subject data. If not\
            provided, the current directory is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuantifyHasubregionsShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUANTIFY_HASUBREGIONS_SH_METADATA)
    params = quantify_hasubregions_sh_params(
        prefix=prefix,
        suffix=suffix,
        output_file=output_file,
        subjects_directory=subjects_directory,
    )
    return quantify_hasubregions_sh_execute(params, execution)


__all__ = [
    "QUANTIFY_HASUBREGIONS_SH_METADATA",
    "QuantifyHasubregionsShOutputs",
    "QuantifyHasubregionsShParameters",
    "quantify_hasubregions_sh",
    "quantify_hasubregions_sh_params",
]
