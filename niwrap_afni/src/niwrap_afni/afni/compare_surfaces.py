# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

COMPARE_SURFACES_METADATA = Metadata(
    id="653d6f831efb2cdba11144f083f4857fcc5112b4.boutiques",
    name="CompareSurfaces",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


CompareSurfacesParameters = typing.TypedDict('CompareSurfacesParameters', {
    "__STYXTYPE__": typing.Literal["CompareSurfaces"],
    "spec_file": InputPathType,
    "hemisphere": typing.Literal["L", "R"],
    "volume_parent_1": InputPathType,
    "volume_parent_2": InputPathType,
    "file_prefix": typing.NotRequired[str | None],
    "one_node": typing.NotRequired[float | None],
    "node_range": typing.NotRequired[list[float] | None],
    "no_consistency_check": bool,
    "no_volreg": bool,
    "no_transform": bool,
    "set_environment_variable": typing.NotRequired[str | None],
    "trace": bool,
    "extreme_trace": bool,
    "no_memory_trace": bool,
    "yes_memory_trace": bool,
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
        "CompareSurfaces": compare_surfaces_cargs,
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
        "CompareSurfaces": compare_surfaces_outputs,
    }.get(t)


class CompareSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compare_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    distance_output_file: OutputPathType | None
    """Distance output file."""
    color_output_file: OutputPathType | None
    """Node color output file."""


def compare_surfaces_params(
    spec_file: InputPathType,
    hemisphere: typing.Literal["L", "R"],
    volume_parent_1: InputPathType,
    volume_parent_2: InputPathType,
    file_prefix: str | None = None,
    one_node: float | None = None,
    node_range: list[float] | None = None,
    no_consistency_check: bool = False,
    no_volreg: bool = False,
    no_transform: bool = False,
    set_environment_variable: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    no_memory_trace: bool = False,
    yes_memory_trace: bool = False,
) -> CompareSurfacesParameters:
    """
    Build parameters.
    
    Args:
        spec_file: File containing surface specification.
        hemisphere: Specify the hemisphere being processed (left or right).
        volume_parent_1: Volume parent BRIK for first surface.
        volume_parent_2: Volume parent BRIK for second surface.
        file_prefix: Prefix for distance and node color output files. Existing\
            file will not be overwritten.
        one_node: Output results for node index only. This option is for\
            debugging.
        node_range: Output results from node istart to node istop only. This\
            option is for debugging.
        no_consistency_check: Skip mesh orientation consistency check. This\
            speeds up the start time so it is useful for debugging runs.
        no_volreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        no_transform: Same as -novolreg.
        set_environment_variable: Set environment variable ENVname to be\
            ENVvalue. Quotes are necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        no_memory_trace: Turn off memory tracing.
        yes_memory_trace: Turn on memory tracing (default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "CompareSurfaces",
        "spec_file": spec_file,
        "hemisphere": hemisphere,
        "volume_parent_1": volume_parent_1,
        "volume_parent_2": volume_parent_2,
        "no_consistency_check": no_consistency_check,
        "no_volreg": no_volreg,
        "no_transform": no_transform,
        "trace": trace_,
        "extreme_trace": extreme_trace,
        "no_memory_trace": no_memory_trace,
        "yes_memory_trace": yes_memory_trace,
    }
    if file_prefix is not None:
        params["file_prefix"] = file_prefix
    if one_node is not None:
        params["one_node"] = one_node
    if node_range is not None:
        params["node_range"] = node_range
    if set_environment_variable is not None:
        params["set_environment_variable"] = set_environment_variable
    return params


def compare_surfaces_cargs(
    params: CompareSurfacesParameters,
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
    cargs.append("CompareSurfaces")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("spec_file"))
    ])
    cargs.extend([
        "-hemi",
        params.get("hemisphere")
    ])
    cargs.extend([
        "-sv1",
        execution.input_file(params.get("volume_parent_1"))
    ])
    cargs.extend([
        "-sv2",
        execution.input_file(params.get("volume_parent_2"))
    ])
    if params.get("file_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("file_prefix")
        ])
    if params.get("one_node") is not None:
        cargs.extend([
            "-onenode",
            str(params.get("one_node"))
        ])
    if params.get("node_range") is not None:
        cargs.extend([
            "-noderange",
            *map(str, params.get("node_range"))
        ])
    if params.get("no_consistency_check"):
        cargs.append("-nocons")
    if params.get("no_volreg"):
        cargs.append("-novolreg")
    if params.get("no_transform"):
        cargs.append("-noxform")
    if params.get("set_environment_variable") is not None:
        cargs.extend([
            "-setenv",
            params.get("set_environment_variable")
        ])
    if params.get("trace"):
        cargs.append("-trace")
    if params.get("extreme_trace"):
        cargs.append("-TRACE")
    if params.get("no_memory_trace"):
        cargs.append("-nomall")
    if params.get("yes_memory_trace"):
        cargs.append("-yesmall")
    return cargs


def compare_surfaces_outputs(
    params: CompareSurfacesParameters,
    execution: Execution,
) -> CompareSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CompareSurfacesOutputs(
        root=execution.output_file("."),
        distance_output_file=execution.output_file(params.get("file_prefix") + "_distance.txt") if (params.get("file_prefix") is not None) else None,
        color_output_file=execution.output_file(params.get("file_prefix") + "_color.txt") if (params.get("file_prefix") is not None) else None,
    )
    return ret


def compare_surfaces_execute(
    params: CompareSurfacesParameters,
    execution: Execution,
) -> CompareSurfacesOutputs:
    """
    Calculates distance at each node in Surface 1 (S1) to Surface 2 (S2) along the
    local surface normal at each node in S1. Superseded by SurfToSurf.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CompareSurfacesOutputs`).
    """
    params = execution.params(params)
    cargs = compare_surfaces_cargs(params, execution)
    ret = compare_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def compare_surfaces(
    spec_file: InputPathType,
    hemisphere: typing.Literal["L", "R"],
    volume_parent_1: InputPathType,
    volume_parent_2: InputPathType,
    file_prefix: str | None = None,
    one_node: float | None = None,
    node_range: list[float] | None = None,
    no_consistency_check: bool = False,
    no_volreg: bool = False,
    no_transform: bool = False,
    set_environment_variable: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    no_memory_trace: bool = False,
    yes_memory_trace: bool = False,
    runner: Runner | None = None,
) -> CompareSurfacesOutputs:
    """
    Calculates distance at each node in Surface 1 (S1) to Surface 2 (S2) along the
    local surface normal at each node in S1. Superseded by SurfToSurf.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: File containing surface specification.
        hemisphere: Specify the hemisphere being processed (left or right).
        volume_parent_1: Volume parent BRIK for first surface.
        volume_parent_2: Volume parent BRIK for second surface.
        file_prefix: Prefix for distance and node color output files. Existing\
            file will not be overwritten.
        one_node: Output results for node index only. This option is for\
            debugging.
        node_range: Output results from node istart to node istop only. This\
            option is for debugging.
        no_consistency_check: Skip mesh orientation consistency check. This\
            speeds up the start time so it is useful for debugging runs.
        no_volreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        no_transform: Same as -novolreg.
        set_environment_variable: Set environment variable ENVname to be\
            ENVvalue. Quotes are necessary.
        trace_: Turns on In/Out debug and Memory tracing.
        extreme_trace: Turns on extreme tracing.
        no_memory_trace: Turn off memory tracing.
        yes_memory_trace: Turn on memory tracing (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CompareSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPARE_SURFACES_METADATA)
    params = compare_surfaces_params(
        spec_file=spec_file,
        hemisphere=hemisphere,
        volume_parent_1=volume_parent_1,
        volume_parent_2=volume_parent_2,
        file_prefix=file_prefix,
        one_node=one_node,
        node_range=node_range,
        no_consistency_check=no_consistency_check,
        no_volreg=no_volreg,
        no_transform=no_transform,
        set_environment_variable=set_environment_variable,
        trace_=trace_,
        extreme_trace=extreme_trace,
        no_memory_trace=no_memory_trace,
        yes_memory_trace=yes_memory_trace,
    )
    return compare_surfaces_execute(params, execution)


__all__ = [
    "COMPARE_SURFACES_METADATA",
    "CompareSurfacesOutputs",
    "CompareSurfacesParameters",
    "compare_surfaces",
    "compare_surfaces_params",
]
