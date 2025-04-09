# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EXTRACTTXT_METADATA = Metadata(
    id="4a3bed1da6981adbde061512034e1d96efc6c5c8.boutiques",
    name="extracttxt",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ExtracttxtParameters = typing.TypedDict('ExtracttxtParameters', {
    "__STYX_TYPE__": typing.Literal["extracttxt"],
    "search_word": str,
    "file": InputPathType,
    "num_trailing_lines": typing.NotRequired[float | None],
    "relative_start": typing.NotRequired[float | None],
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
        "extracttxt": extracttxt_cargs,
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
        "extracttxt": extracttxt_outputs,
    }.get(t)


class ExtracttxtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `extracttxt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Extracted text output file"""


def extracttxt_params(
    search_word: str,
    file: InputPathType,
    num_trailing_lines: float | None = 0,
    relative_start: float | None = 0,
) -> ExtracttxtParameters:
    """
    Build parameters.
    
    Args:
        search_word: The word to search for in the file.
        file: Path to the file where text is to be extracted.
        num_trailing_lines: Number of trailing lines to include after the\
            search word.
        relative_start: Relative start position to begin the search.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "extracttxt",
        "search_word": search_word,
        "file": file,
    }
    if num_trailing_lines is not None:
        params["num_trailing_lines"] = num_trailing_lines
    if relative_start is not None:
        params["relative_start"] = relative_start
    return params


def extracttxt_cargs(
    params: ExtracttxtParameters,
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
    cargs.append("extracttxt")
    cargs.append(params.get("search_word"))
    cargs.append(execution.input_file(params.get("file")))
    if params.get("num_trailing_lines") is not None:
        cargs.append(str(params.get("num_trailing_lines")))
    if params.get("relative_start") is not None:
        cargs.append(str(params.get("relative_start")))
    return cargs


def extracttxt_outputs(
    params: ExtracttxtParameters,
    execution: Execution,
) -> ExtracttxtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ExtracttxtOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    return ret


def extracttxt_execute(
    params: ExtracttxtParameters,
    execution: Execution,
) -> ExtracttxtOutputs:
    """
    Extracts text from a file based on a search word.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ExtracttxtOutputs`).
    """
    params = execution.params(params)
    cargs = extracttxt_cargs(params, execution)
    ret = extracttxt_outputs(params, execution)
    execution.run(cargs)
    return ret


def extracttxt(
    search_word: str,
    file: InputPathType,
    num_trailing_lines: float | None = 0,
    relative_start: float | None = 0,
    runner: Runner | None = None,
) -> ExtracttxtOutputs:
    """
    Extracts text from a file based on a search word.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        search_word: The word to search for in the file.
        file: Path to the file where text is to be extracted.
        num_trailing_lines: Number of trailing lines to include after the\
            search word.
        relative_start: Relative start position to begin the search.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExtracttxtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXTRACTTXT_METADATA)
    params = extracttxt_params(
        search_word=search_word,
        file=file,
        num_trailing_lines=num_trailing_lines,
        relative_start=relative_start,
    )
    return extracttxt_execute(params, execution)


__all__ = [
    "EXTRACTTXT_METADATA",
    "ExtracttxtOutputs",
    "ExtracttxtParameters",
    "extracttxt",
    "extracttxt_params",
]
