# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_TO_SURF_METADATA = Metadata(
    id="af80d3026cea586c9cddcde8e039ab19779b80fa.boutiques",
    name="SurfToSurf",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SurfToSurfParameters = typing.TypedDict('SurfToSurfParameters', {
    "__STYXTYPE__": typing.Literal["SurfToSurf"],
    "input_surface_1": InputPathType,
    "input_surface_2": InputPathType,
    "surface_volume": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "output_params": typing.NotRequired[str | None],
    "node_indices": typing.NotRequired[InputPathType | None],
    "proj_dir": typing.NotRequired[InputPathType | None],
    "data": typing.NotRequired[InputPathType | None],
    "node_debug": typing.NotRequired[float | None],
    "debug_level": typing.NotRequired[float | None],
    "make_consistent": bool,
    "dset": typing.NotRequired[InputPathType | None],
    "mapfile": typing.NotRequired[InputPathType | None],
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
        "SurfToSurf": surf_to_surf_cargs,
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
        "SurfToSurf": surf_to_surf_outputs,
    }.get(t)


class SurfToSurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_to_surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output file in 1D format"""


def surf_to_surf_params(
    input_surface_1: InputPathType,
    input_surface_2: InputPathType,
    surface_volume: InputPathType | None = None,
    prefix: str | None = None,
    output_params: str | None = None,
    node_indices: InputPathType | None = None,
    proj_dir: InputPathType | None = None,
    data: InputPathType | None = None,
    node_debug: float | None = None,
    debug_level: float | None = None,
    make_consistent: bool = False,
    dset: InputPathType | None = None,
    mapfile: InputPathType | None = None,
) -> SurfToSurfParameters:
    """
    Build parameters.
    
    Args:
        input_surface_1: First input surface file (S1).
        input_surface_2: Second input surface file (S2).
        surface_volume: Specify the surface volume (SV1).
        prefix: Specify prefix for the output file.
        output_params: List of mapping parameters to include in output.
        node_indices: 1D file containing node indices of S1 to consider.
        proj_dir: 1D file containing projection directions.
        data: 1D file containing data to be interpolated.
        node_debug: Node index for debugging purposes.
        debug_level: Debugging level.
        make_consistent: Force a consistency check and correct triangle\
            orientation.
        dset: Dataset file for data interpolation; mutually exclusive with\
            -data.
        mapfile: File containing mapping parameters between surfaces S2 and S1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfToSurf",
        "input_surface_1": input_surface_1,
        "input_surface_2": input_surface_2,
        "make_consistent": make_consistent,
    }
    if surface_volume is not None:
        params["surface_volume"] = surface_volume
    if prefix is not None:
        params["prefix"] = prefix
    if output_params is not None:
        params["output_params"] = output_params
    if node_indices is not None:
        params["node_indices"] = node_indices
    if proj_dir is not None:
        params["proj_dir"] = proj_dir
    if data is not None:
        params["data"] = data
    if node_debug is not None:
        params["node_debug"] = node_debug
    if debug_level is not None:
        params["debug_level"] = debug_level
    if dset is not None:
        params["dset"] = dset
    if mapfile is not None:
        params["mapfile"] = mapfile
    return params


def surf_to_surf_cargs(
    params: SurfToSurfParameters,
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
    cargs.append("SurfToSurf")
    cargs.append(execution.input_file(params.get("input_surface_1")))
    cargs.append(execution.input_file(params.get("input_surface_2")))
    if params.get("surface_volume") is not None:
        cargs.extend([
            "-sv",
            execution.input_file(params.get("surface_volume"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("output_params") is not None:
        cargs.extend([
            "-output_params",
            params.get("output_params")
        ])
    if params.get("node_indices") is not None:
        cargs.extend([
            "-node_indices",
            execution.input_file(params.get("node_indices"))
        ])
    if params.get("proj_dir") is not None:
        cargs.extend([
            "-proj_dir",
            execution.input_file(params.get("proj_dir"))
        ])
    if params.get("data") is not None:
        cargs.extend([
            "-data",
            execution.input_file(params.get("data"))
        ])
    if params.get("node_debug") is not None:
        cargs.extend([
            "-node_debug",
            str(params.get("node_debug"))
        ])
    if params.get("debug_level") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug_level"))
        ])
    if params.get("make_consistent"):
        cargs.append("-make_consistent")
    if params.get("dset") is not None:
        cargs.extend([
            "-dset",
            execution.input_file(params.get("dset"))
        ])
    if params.get("mapfile") is not None:
        cargs.extend([
            "-mapfile",
            execution.input_file(params.get("mapfile"))
        ])
    return cargs


def surf_to_surf_outputs(
    params: SurfToSurfParameters,
    execution: Execution,
) -> SurfToSurfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfToSurfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".1D") if (params.get("prefix") is not None) else None,
    )
    return ret


def surf_to_surf_execute(
    params: SurfToSurfParameters,
    execution: Execution,
) -> SurfToSurfOutputs:
    """
    Interpolate data from one surface to another.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfToSurfOutputs`).
    """
    params = execution.params(params)
    cargs = surf_to_surf_cargs(params, execution)
    ret = surf_to_surf_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_to_surf(
    input_surface_1: InputPathType,
    input_surface_2: InputPathType,
    surface_volume: InputPathType | None = None,
    prefix: str | None = None,
    output_params: str | None = None,
    node_indices: InputPathType | None = None,
    proj_dir: InputPathType | None = None,
    data: InputPathType | None = None,
    node_debug: float | None = None,
    debug_level: float | None = None,
    make_consistent: bool = False,
    dset: InputPathType | None = None,
    mapfile: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfToSurfOutputs:
    """
    Interpolate data from one surface to another.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_surface_1: First input surface file (S1).
        input_surface_2: Second input surface file (S2).
        surface_volume: Specify the surface volume (SV1).
        prefix: Specify prefix for the output file.
        output_params: List of mapping parameters to include in output.
        node_indices: 1D file containing node indices of S1 to consider.
        proj_dir: 1D file containing projection directions.
        data: 1D file containing data to be interpolated.
        node_debug: Node index for debugging purposes.
        debug_level: Debugging level.
        make_consistent: Force a consistency check and correct triangle\
            orientation.
        dset: Dataset file for data interpolation; mutually exclusive with\
            -data.
        mapfile: File containing mapping parameters between surfaces S2 and S1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfToSurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_TO_SURF_METADATA)
    params = surf_to_surf_params(
        input_surface_1=input_surface_1,
        input_surface_2=input_surface_2,
        surface_volume=surface_volume,
        prefix=prefix,
        output_params=output_params,
        node_indices=node_indices,
        proj_dir=proj_dir,
        data=data,
        node_debug=node_debug,
        debug_level=debug_level,
        make_consistent=make_consistent,
        dset=dset,
        mapfile=mapfile,
    )
    return surf_to_surf_execute(params, execution)


__all__ = [
    "SURF_TO_SURF_METADATA",
    "SurfToSurfOutputs",
    "SurfToSurfParameters",
    "surf_to_surf",
    "surf_to_surf_params",
]
