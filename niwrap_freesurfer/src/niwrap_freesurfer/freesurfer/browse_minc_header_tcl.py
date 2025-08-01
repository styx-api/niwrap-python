# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BROWSE_MINC_HEADER_TCL_METADATA = Metadata(
    id="22e391d58621f276bcf2d734a8c66b008bb55ba4.boutiques",
    name="browse-minc-header.tcl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


BrowseMincHeaderTclParameters = typing.TypedDict('BrowseMincHeaderTclParameters', {
    "__STYXTYPE__": typing.Literal["browse-minc-header.tcl"],
    "infile": InputPathType,
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
        "browse-minc-header.tcl": browse_minc_header_tcl_cargs,
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


class BrowseMincHeaderTclOutputs(typing.NamedTuple):
    """
    Output object returned when calling `browse_minc_header_tcl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def browse_minc_header_tcl_params(
    infile: InputPathType,
) -> BrowseMincHeaderTclParameters:
    """
    Build parameters.
    
    Args:
        infile: MINC file for which the header is to be browsed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "browse-minc-header.tcl",
        "infile": infile,
    }
    return params


def browse_minc_header_tcl_cargs(
    params: BrowseMincHeaderTclParameters,
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
    cargs.append("browse-minc-header.tcl")
    cargs.append(execution.input_file(params.get("infile")))
    return cargs


def browse_minc_header_tcl_outputs(
    params: BrowseMincHeaderTclParameters,
    execution: Execution,
) -> BrowseMincHeaderTclOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BrowseMincHeaderTclOutputs(
        root=execution.output_file("."),
    )
    return ret


def browse_minc_header_tcl_execute(
    params: BrowseMincHeaderTclParameters,
    execution: Execution,
) -> BrowseMincHeaderTclOutputs:
    """
    A tool for browsing MINC file headers, likely part of the FreeSurfer package.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BrowseMincHeaderTclOutputs`).
    """
    params = execution.params(params)
    cargs = browse_minc_header_tcl_cargs(params, execution)
    ret = browse_minc_header_tcl_outputs(params, execution)
    execution.run(cargs)
    return ret


def browse_minc_header_tcl(
    infile: InputPathType,
    runner: Runner | None = None,
) -> BrowseMincHeaderTclOutputs:
    """
    A tool for browsing MINC file headers, likely part of the FreeSurfer package.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: MINC file for which the header is to be browsed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BrowseMincHeaderTclOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BROWSE_MINC_HEADER_TCL_METADATA)
    params = browse_minc_header_tcl_params(
        infile=infile,
    )
    return browse_minc_header_tcl_execute(params, execution)


__all__ = [
    "BROWSE_MINC_HEADER_TCL_METADATA",
    "BrowseMincHeaderTclOutputs",
    "BrowseMincHeaderTclParameters",
    "browse_minc_header_tcl",
    "browse_minc_header_tcl_params",
]
